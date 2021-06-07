# import re
#
# RE_NAME = re.compile(r'^[А-ЯЁ][а-яё]+$')
#
#
# def name_is_valid(name):
#    return RE_NAME.match(name)




import re

RE_DATE = re.compile(r'^(\d{2}.){2}\d{4}$')

re.match(r'^(\d{2}.){2}\d{4}$', '23.01.2021')

for date in ['23.01.2021', '23,01,2021', '23~01~2021', 'sdfsfds']:
    assert RE_DATE.match(date), f'wrong date {date}'
