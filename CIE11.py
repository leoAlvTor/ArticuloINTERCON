class CIE11:

    error: bool
    error_message: str
    chapters: list

    def __init__(self, error: bool = False, error_message: str = '', chapters: list = []):
        self.error = error
        self.error_message = error_message
        self.chapters = list(set(chapters))
