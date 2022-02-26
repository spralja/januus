from os import listdir, mkdir, remove
from os.path import isfile, join, split

import shutil
from datetime import datetime
import calendar

janunassign_file = open('.janunassign', 'r')
janunassign = janunassign_file.read().split('\n')
janunassign = [unasignee for unasignee in janunassign if unasignee]
janunassign_file.close()

exclude = ['.jan'] + janunassign



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


def copy_all_files(jan_path=join('.jan', '0'), path=''):
    """
    Copies all files from the repository to '.jan/version'
    """
    file_names = listdir(*((path,) if path else ()))
    for file_name in file_names:
        file_path = join(path, file_name)
        jan_file_path = join(jan_path, file_path)
        if split(file_path)[0] in exclude:
            print(split(file_path)[0])
            print(exclude)
            continue

        if isfile(file_path):
            shutil.copy(file_path, jan_file_path)
        else:
            mkdir(jan_file_path)
            copy_all_files(jan_path=jan_path, path=file_path)    


def what_version():
    """
    Figure out current version
    """
    dirs = listdir('.jan')
    versions = [int(v) for v in dirs if not isfile(join('.jan', v))]
    return max(versions) + 1


def resolute(version=None, **kwargs):
    """
    Create snapshot of repository
    """
    if not version:
        version = what_version()

    jan_path = join('.jan', str(version))
    mkdir(jan_path)
    message_file = open(jan_path + '.message', 'w')
    message_file.write(kwargs['message'])
    message_file.close()
    datetime_file = open(jan_path + '.datetime', 'w')
    datetime_file.write(str(calendar.timegm(datetime.utcnow().utctimetuple())))
    datetime_file.close()
    copy_all_files(jan_path=jan_path)


def initialise(**kwargs):
    """
    Initialises the repository
    """
    mkdir('.jan')
    resolute(kwargs['message'], 0)


def tally(**kwargs):
    resolutions = [i for i in range(what_version())]
    resolutions.reverse()
    for resolution in resolutions:
        message_file = open(join('.jan', str(resolution) + '.message'), 'r')
        datetime_file = open(join('.jan', str(resolution) + '.datetime'), 'r')
        message = message_file.read()
        _datetime = datetime.fromtimestamp(int(datetime_file.read()))
        datetime_file.close()
        message_file.close()
        print(f'{resolution} : {message} < {_datetime.strftime("%d %B %Y, %H:%M:%S")} >')

def checkout(**kwargs):
    resolution = int(kwargs['resolution'])
    if resolution > what_version():
        raise SyntaxError('hmmm')

    resolute(message=f'checkout resolution <-{resolution}')

    jan_path = join('.jan', str(resolution))
    print('in progress...')