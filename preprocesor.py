import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_file(file_name: str, sheet: str) -> pd.DataFrame:
    return pd.read_excel(file_name, sheet_name=sheet)


def capitalize_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.applymap(lambda s: s.upper() if type(s) == str else s)


def get_nan_count_column(dataframe: pd.DataFrame) -> numpy.ndarray:
    return dataframe.isna().sum()


def get_nan_count_by_row(dataframe: pd.DataFrame) -> numpy.ndarray:
    return dataframe.isnull().sum(axis=1)


def plot_correlation_matrix(dataframe: pd.DataFrame):
    print('*'*20)
    print(dataframe.corr())
    print('*'*20)


file = read_file(file_name="/home/leo/Documentos/Datos 1996-2022.xlsx", sheet="Hoja1")
plot_correlation_matrix(file)
file = capitalize_dataframe(dataframe=file)
nan_count_columns = get_nan_count_column(dataframe=file)
nan_count_rows = get_nan_count_by_row(dataframe=file)

print("Dataframe head:\n", file.head())
print("File shape:\n", file.shape)
print("NAN count per column:\n", nan_count_columns)
print("NAN count per row:\n", nan_count_rows)


print('*'*100)
print(file.dtypes)