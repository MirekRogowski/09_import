from helper import *

if sys.argv[0] == "sprzedaz.py":
    accountancy.open_data(sys.argv[1])
    accountancy.transform_data()
    accountancy.get_sale(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    accountancy.writa_data("sprzedaz", "01zapis.txt")
