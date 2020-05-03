from datetime import datetime

from logzero import logger


class DateParser:
    def __init__(self, **kwargs):
        self.default_year = kwargs.get('default_year')

    def reformat(self, string):
        date_time = None
        formats = ['%d/%m/%Y', '%d %m %Y', '%d/%m', '%d %m']
        for date_formats in formats:
            try:
                date_time = datetime.strptime(string, date_formats)
            except ValueError:
                pass

        if date_time is None:
            logger.error(f'Cannot parse "{string}"')
            return date_time

        if self.default_year is not None:
            date_time = date_time.replace(year=self.default_year)

        date = date_time.date()

        return date.isoformat()
