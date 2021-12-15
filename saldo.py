from helper import *

accountancy.open_data(sys.argv[1])
accountancy.transform_data()
accountancy.logs.append(["saldo", sys.argv[2], sys.argv[3]])
accountancy.balance += int(sys.argv[2])
accountancy.writa_data("saldo","01zapis.txt")
