from os import listdir, mkdir
from os.path import isfile, join

def _get_all_files(path=''):
    """
    @return files: [str] returns paths to all files in the repository
    """
    _files = listdir(*((path,) if path else ()))
    files = []
    for file in _files:
        if isfile(join(path, file)):
            files.append(join(path, file))
        else:
            files += _get_all_files(join(path, file))

    return files

def initialise():
    """
    Initialises the repository
    """
    all_files = _get_all_files()
    mkdir('.jan')
    mkdir('.jan/1')
    