from helper import *

accountancy.open_data(sys.argv[1])
accountancy.stock_status(sys.argv[2:])
accountancy.writa_data("magazyn", "01zapis.txt")


