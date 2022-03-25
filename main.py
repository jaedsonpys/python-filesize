from typing import BinaryIO


def get_file_size(file: BinaryIO) -> tuple:
    if not isinstance(file, BinaryIO):
        raise Exception('The file must be opened in binary mode')

    file_content = file.read()
    file_bytes = len(file_content)
