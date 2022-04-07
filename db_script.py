from CIE11 import CIE11
from tqdm import tqdm


def generate_diagnostico_statements(instance_list: list[CIE11]):
    for instance in instance_list:
        yield f"INSERT INTO Diagnostico(Diagnosticocol) values('{instance.diagnosis}');"


def generate_diagnostico_cie11_statements(instance_list: list[CIE11]):
    for instance in instance_list:
        for chapter in instance.chapters:
            chapter = -5 if chapter == 'V' else chapter
            chapter = -10 if chapter == 'X' else chapter
            yield f"INSERT INTO Diagnostico_has_CIE11(Diagnostico_idDiagnostico, CIE11_idCIE11) " \
                  f"values ((SELECT idDiagnostico FROM Diagnostico WHERE Diagnosticocol = '{instance.diagnosis}')," \
                  f" {int(chapter)});"
