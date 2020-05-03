from logzero import logger

from DateParser import DateParser


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