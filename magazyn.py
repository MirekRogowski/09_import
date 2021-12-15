from helper import *

accountancy.open_data(sys.argv[1])
accountancy.transform_data()
accountancy.writa_data("magazyn", "01zapis.txt")
accountancy.stock_status(sys.argv[2:])

