from helper import *

if sys.argv[0] == "konto.py":
    accountancy.open_data(sys.argv[1])
    accountancy.transform_data()
    accountancy.logs.append(sys.argv[2:])
    accountancy.writa_data("konto", "01zapis.txt")
print(f"\nKonto: {accountancy.balance}")
