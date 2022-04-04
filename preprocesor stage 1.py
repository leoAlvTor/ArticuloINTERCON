import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_file(file_name: str, sheet: str) -> pd.DataFrame:
    return pd.read_excel(file_name, sheet_name=sheet)


def delete_empty_rows(dataframe: pd.DataFrame, col_name: str) -> pd.DataFrame:
    return dataframe.dropna(subset=[col_name], inplace=False)


def delete_duplicates(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.drop_duplicates()


def get_unique_values(dataframe: pd.DataFrame, col_name: str) -> list:
    return dataframe[col_name].unique().tolist()


def preprocess_string(strings: list[str]) -> list:
    return [' '.join(string.strip().lower().split()) for string in strings]


def update_column_values(dataframe: pd.DataFrame, col_name: str, new_values: dict) -> pd.DataFrame:
    for key, value in new_values.items():
        dataframe.loc[dataframe[col_name] == key, col_name] = value
    return dataframe


file = read_file(file_name="/home/leo/Documentos/Datos 1996-2022.xlsx", sheet="Hoja1")
print('Shape BEFORE deleting empty diagnosis rows:\t', file.shape)
file = delete_empty_rows(dataframe=file, col_name='Diagnóstico')
print('Shape AFTER deleting empty diagnosis rows:\t', file.shape)
file = delete_duplicates(file)
print('Shape AFTER deleting duplicate rows:\t\t', file.shape)
unique_diagnosis = get_unique_values(file, 'Diagnóstico')
print('Unique row count in column {Diagnóstico}:\t', len(unique_diagnosis))
preprocessed_strings = preprocess_string(unique_diagnosis)
file = update_column_values(file, 'Diagnóstico', dict(zip(unique_diagnosis, preprocessed_strings)))
file.to_excel('Datos pre-procesados 1196-2022.xlsx')
print(file.head())
