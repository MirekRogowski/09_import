from helper import *

if sys.argv[0] == "saldo.py":
    accountancy.open_data(sys.argv[1])
    accountancy.transform_data()
    accountancy.logs.append(["saldo", sys.argv[2], sys.argv[3]])
    accountancy.balance += int(sys.argv[2])
    accountancy.writa_data("saldo","01zapis.txt")

# print(accountancy.balance)
# print(accountancy.logs)
# print(accountancy.warehouse)

#
# if (len(sys.argv) == 4 and sys.argv[1]=="saldo") or (len(sys.argv) == 2 and sys.argv[1]=="saldo"):
#     accountancy.logs.append(sys.argv[1:])
#     accountancy.balance += int(sys.argv[2])
#     accountancy.writa_data("zapis.txt")