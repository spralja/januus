from os import listdir, mkdir
from os.path import isfile, join, split

import shutil

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


def copy_all_files(jan_path=join('.jan', '1'), path=''):
    """
    Copies all files from the repository to '.jan/version'
    """
    file_names = listdir(*((path,) if path else ()))
    for file_name in file_names:
        file_path = join(path, file_name)
        jan_file_path = join(jan_path, file_path)
        if split(file_path)[:2] == split(jan_path):
            continue

        if isfile(file_path):
            shutil.copy(file_path, jan_file_path)
        else:
            mkdir(jan_file_path)
            copy_all_files(jan_path=jan_path, path=file_path)


def initialise():
    """
    Initialises the repository
    """
    mkdir('.jan')
    mkdir(join('.jan', '1'))
    copy_all_files()
