from helper import *

accountancy.open_data(sys.argv[1])
accountancy.get_sale("sprzedaz", *sys.argv[2:])
accountancy.writa_data("sprzedaz", "01zapis.txt")

