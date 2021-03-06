#!/usr/bin/python
__author__ = 'singhaman'

import sys
import argparse
from argparse import RawTextHelpFormatter
import re


def process(field_delimiter, num_occurrences_to_replace):

    for line in sys.stdin:
        if field_delimiter == '|':
            field_delimiter = "["+field_delimiter+"]"

        print re.sub(field_delimiter,
                     '\n',
                     line.rstrip('\n'),
                     num_occurrences_to_replace)


def process_command_line_args():
    global args

    epilog = """
Notes:
- Control-A (^A) can specified as string $'\\x01'
- Control-B (^B) can be specified as string $'\\x02'

Examples:
- Replace tabs(\\t) with newline (\\n)
    echo -e "test\\t1" | bl.py

- Replace tabs(\\t) and pipes(|) with newline (\\n)
    echo -e "test\\t1|orange|lemon" | bl.py "\\t" | bl.py "|"

- Replace first two occurrences of tabs(\\t) with newline (\\n)
    echo -e "test\\t1\\torange\\tlemon" | bl.py "\\t" 2
"""

    parser = argparse.ArgumentParser(description='This script replaces the '
                                                 'field_delimiter with new line '
                                                 'character',
                                     formatter_class=RawTextHelpFormatter,
                                     epilog=epilog)

    parser.add_argument('field_delimiter', nargs='?', default='\t',
                        help='Enter delimiter (default is \\t)')

    parser.add_argument('num_occurrences_to_replace', nargs="?", default=0,
                        type=int, help='Number of occurrences of '
                                       'field_delimiter to replace. 0 is '
                                       'default and it means all occurrences '
                                       'will be replaced by new line.')

    args = parser.parse_args()


if __name__ == '__main__':
    process_command_line_args()
    process(args.field_delimiter, args.num_occurrences_to_replace)


