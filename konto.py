from helper import *

accountancy.open_data(sys.argv[1])
accountancy.get_balance("konto", *sys.argv[2:])
accountancy.writa_data("konto", "01zapis.txt")
print(f"\nKonto: {accountancy.balance}")
