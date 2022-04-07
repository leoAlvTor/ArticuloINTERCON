import timeit

import pandas as pd
import api_CIE11
import warnings
from tqdm import tqdm
import db_script
from CIE11 import CIE11

warnings.filterwarnings("default")


def read_file(file_name: str, sheet: str) -> pd.DataFrame:
    return pd.read_excel(file_name, sheet_name=sheet)


def get_column_values(dataframe: pd.DataFrame, col_name: str) -> list:
    return dataframe[col_name].tolist()


def get_unique_values(dataframe: pd.DataFrame, col_name: str) -> list:
    return sorted(dataframe[col_name].unique().tolist())


def separate_string_values(string_list: list[str], separator: str) -> list:
    separated_values = []
    [separated_values.extend(x.split(separator)) for x in string_list if separator in x]
    separated_values = map(lambda value: value.strip(), separated_values)
    return list(set(separated_values))


def delete_values_by_condition(values: list[str], condition: str) -> list:
    return [element for element in values if condition not in element]


def join_lists_as_set(*args) -> set[str]:
    final_list = []
    [final_list.extend(element) for element in args]
    return set(final_list)


def get_CIE11_diagnosis(diagnosis_list: set):
    found_diagnosis = []
    not_found_diagnosis = []

    headers = api_CIE11.generate_headers()
    for element in tqdm(diagnosis_list):
        cie11_object = api_CIE11.search_diagnosis(api_CIE11.generate_body(element), headers)
        cie11_object.diagnosis = element
        found_diagnosis.append(cie11_object) if not cie11_object.error else not_found_diagnosis.append(cie11_object)
    return found_diagnosis, not_found_diagnosis


def print_diagnosis(found, not_found: list[CIE11]):
    print('Not found diagnosis:', len(not_found))
    if str.upper(input('Print not found diagnosis? Y/N: ')) == 'Y':
        for x in not_found:
            print(x.diagnosis)
    print('****' * 30)
    print('Correct diagnosis:', len(found))
    if str.upper(input('Print diagnosis? Y/N: ')) == 'Y':
        [print(x) for x in found]


def save_statements(statement1: list[str], statement2: list[str]):
    with open('diagnostico.sql', 'w') as f:
        for line in statement1:
            f.write(f"{line}\n")

    with open('diagnostico_cie11.sql', 'w') as f:
        for line in statement2:
            f.write(f"{line}\n")


file = read_file(file_name="Datos pre-procesados 1196-2022.xlsx", sheet="Sheet1")
unique_simple_values = get_unique_values(file, 'Diagnóstico')
unique_separated_values = separate_string_values(unique_simple_values, separator='/')
unique_simple_values = delete_values_by_condition(unique_simple_values, condition='/')

final_diagnosis_set = join_lists_as_set(unique_simple_values, unique_separated_values)
found_diagnosis, not_found_diagnosis = get_CIE11_diagnosis(final_diagnosis_set)
print_diagnosis(found_diagnosis, not_found_diagnosis)

diagnostico_statements = list(db_script.generate_diagnostico_statements(found_diagnosis))
diagnostico_cie11_statements = list(db_script.generate_diagnostico_cie11_statements(found_diagnosis))
save_statements(diagnostico_statements, diagnostico_cie11_statements)

