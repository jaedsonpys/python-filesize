from io import BufferedReader


def get_file_size(
    file: BufferedReader,
    kb: bool = None,
    mb: bool = None,
    gb: bool = None
) -> float:
    print(type(file))
    if not isinstance(file, BufferedReader):
        raise Exception('The file must be opened in binary mode')

    file_content = file.read()
    file_bytes = len(file_content)
