#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Alvaro Garcia"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse

from logzero import logger

from file_commands import FileCommands
from invoice_wizard import InvoiceWizard


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
