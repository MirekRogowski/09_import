from helper import *

accountancy.open_data(sys.argv[1])
accountancy.get_balance("saldo", *sys.argv[2:])
accountancy.writa_data("saldo", "01zapis.txt")

