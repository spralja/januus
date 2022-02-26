import argparse

from .actions import initialise, resolute, tally

commands = {
    'initialise': initialise,
    'resolute': resolute,
    'tally': tally,
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Jaanus version control system')
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')
    initialise = subparsers.add_parser('initialise', help='Create repository')
    resolute = subparsers.add_parser('resolute', help='Create permanent snapshot of repository')
    tally = subparsers.add_parser('tally', help='Log resolutions')
    resolute.add_argument('-m', help='add a message', dest='message')
    initialise.add_argument('-m', help='add a message', dest='message')
    args = parser.parse_args()
    commands[args.command](**args.__dict__)
    