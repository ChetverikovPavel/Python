from requests import get
from decimal import Decimal
import datetime


def currency_rates(val_key):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    cont_list = content.split('Date="')[1:]
    cont_date = cont_list[0][:10]
    cont_date = cont_date.split('.')
    cont_date = datetime.date(int(cont_date[2]), int(cont_date[1]), int(cont_date[0]))
    cont_dict = dict(zip(
        [el.split('<')[0] for el in content.split('<CharCode>')[1:]],
        [Decimal(el.split('<')[0].replace(',', '.')).quantize(Decimal("1.00")) \
         for el in content.split('<Value>')[1:]]))
    if val_key not in cont_dict.keys():
        return 'None'
    else:
        return f'{cont_dict[val_key]}, {cont_date}'


if __name__ == "__main__":
    print('USD', currency_rates('USD'))
    print('EUR', currency_rates('EUR'))
