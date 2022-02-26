import argparse

from .initialise import initialise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Jaanus version control system')
    parser.add_argument('initialise', help='= initialise repository')
    args = parser.parse_args()
    initialise()
    