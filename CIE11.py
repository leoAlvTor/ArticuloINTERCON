class CIE11:

    diagnosis: str
    error: bool
    error_message: str
    chapters: list

    def __init__(self, error: bool = False, error_message: str = '', chapters=None):
        if chapters is None:
            chapters = []
        self.error = error
        self.error_message = error_message
        self.chapters = list(set(chapters))

    def __str__(self):
        return f'Diagnosis: {self.diagnosis}, Error: {self.error}, Error message: {self.error_message},' \
               f' Chapters: {self.chapters}'
