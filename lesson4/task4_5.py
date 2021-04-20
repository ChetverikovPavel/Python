import utils
from sys import argv

if len(argv) > 1:  # Выполняется через терминал
    print(utils.currency_rates(argv[1]))
