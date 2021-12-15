from helper import *

accountancy.open_data(sys.argv[1])
accountancy.transform_data()
accountancy.get_buy(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
accountancy.writa_data("zakup", "01zapis.txt")
