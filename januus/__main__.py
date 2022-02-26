import argparse

from .actions import initialise, resolute

commands = {
    'initialise': initialise,
    'resolute': resolute,
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Jaanus version control system')
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')
    initialise = subparsers.add_parser('initialise', help='Create repository')
    resolute = subparsers.add_parser('resolute', help='Create permanent snapshot of repository')
    args = parser.parse_args()
    commands[args.command]()
    