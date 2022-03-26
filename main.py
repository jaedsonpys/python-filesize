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

    if not any([kb, mb, gb]):
        raise Exception('You must choose a storage unit of measurement')

    if kb:
        result = ((file_bytes / 1000), 'kb')
    elif mb:
        result = ((file_bytes / 1e+6), 'mb')
    elif gb:
        result = ((file_bytes / 1e+9), 'gb')

    return result
