#!/usr/bin/python
from __future__ import print_function
import sys
import argparse
from argparse import RawTextHelpFormatter
import re


def process():
    prev_word_was_from = False
    prev_word_was_join = False

    output = []
    for line in sys.stdin:
        line = line.rstrip().lower()
        line = re.sub(r"\s+", ' ', line)
        line = re.sub(r"[;)]", ' ', line)

        tokens = line.split(" ")
        for token in tokens:
            if token == "from":
                prev_word_was_from = True

            elif token == "join":
                prev_word_was_join = True

            elif prev_word_was_from or prev_word_was_join:
                if re.search("[a-z0-9]", token) and token != "(select":
                    output.append(token)
                prev_word_was_from = False
                prev_word_was_join = False

    dedupe_output = list(set(output))
    dedupe_output.sort()
    for item in dedupe_output:
        print (item)

def process_command_line_args():
    global args

    epilog = """
This script reads text containing ANSI sql queries from <STDIN> and extracts
the table names and output them to <STDOUT>. It sorts and dedupes the table
names before outputing them.
It detects table names by searching for the text that appears after sql
keywords 'FROM' and 'JOIN'.
    """

    parser = argparse.ArgumentParser(description='This script reads text '
                                                 'containing SQL statements '
                                                 'from <STDIN> and writes to '
                                                 '<STDOUT>.',
                                     formatter_class=RawTextHelpFormatter,
                                     epilog=epilog)

    #parser.add_argument('table',help='Enter the table name')

    #parser.add_argument('cols',
    #                    help='Comma delimited column list')

    args = parser.parse_args()


if __name__ == '__main__':
    process_command_line_args()
    process()