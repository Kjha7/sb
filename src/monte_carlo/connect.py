import settings
import requests


class Connect(object):
    def __init__(self):
        self._url = 'http://ichart.finance.yahoo.com/table.csv?s=' + settings.STOCK + '&g=abo'

    def get_csv(self):

        page = requests.get(self._url)
        content = page.content

        with open(settings.PATH_TO_DATA, 'w') as csv_file:
            content = content.split('\n')
            for line in range(len(content)):
                if line == 0:
                    pass
                else:
                    csv_file.write(content[line] + '\n')
