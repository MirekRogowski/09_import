from helper import *

if sys.argv[0] == "magazyn.py":
    accountancy.open_data(sys.argv[1])
    accountancy.transform_data()
    # accountancy.logs.append(sys.argv[2:])
    accountancy.writa_data("magazyn", "01zapis.txt")
    accountancy.stock_status(sys.argv[2:])

