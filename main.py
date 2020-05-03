#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Alvaro Garcia"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse

from logzero import logger

from DateParser import DateParser


def main(args):
    """ Main entry point of the app """
    logger.info(args)

    wizard = InvoiceWizard()
    date = wizard.parse_date(int(args.default_year))
    company_name = wizard.parse_company_name()

    file_commands = FileCommands()
    command = file_commands.compose_move_command(args, company_name, date)
    file_commands.write_if(command, file=args.execution_pipe)
    logger.info(f"Command ={command}")
    return 0


class FileCommands:
    @staticmethod
    def compose_move_command(args, company_name, date):
        new_filename = " - ".join([date, company_name, args.file])
        new_filename = f'"{new_filename}"'
        command = f'mv "{args.file}" {new_filename}'
        return command

    @staticmethod
    def write_if(command, file):
        if file is not None:
            with open(file, 'w') as file:
                file.write(command + '\n')


class InvoiceWizard:
    def parse_date(self, default_year):
        while True:
            raw_input = self.read_from_user('Enter the date (%d %m, %d/%m, also with %y): ')
            parsed_date = DateParser(default_year=default_year).reformat(raw_input)
            if parsed_date is None:
                continue
            if self.is_validated_by_user(parsed_date):
                return parsed_date

    def parse_company_name(self):
        while True:
            raw_input = self.read_from_user('Enter the company name: ')
            if raw_input is None:
                continue
            if self.is_validated_by_user(raw_input):
                return raw_input

    @staticmethod
    def is_validated_by_user(value):
        try:
            raw_input = input(f'Is it valid "{value}"? [Y/n]')
            clean_input = raw_input.strip()
            if clean_input.upper() == "Y" or clean_input == "":
                return value
        except ValueError as e:
            logger.info(e)
            logger.error(f"Did not understand '${raw_input}'")
        return None

    @staticmethod
    def read_from_user(prompt):
        try:
            raw_input = input(prompt)
            return raw_input
        except ValueError as e:
            logger.info(e)
            logger.error(f"Did not understand '${raw_input}'")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("file", help="Which file to rename")

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("--year", action="store", dest="default_year", default=None)

    parser.add_argument("--pipe", action="store", dest="execution_pipe", default=None)

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
