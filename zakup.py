from helper import *

accountancy.open_data(sys.argv[1])
accountancy.get_buy("zakup", *sys.argv[2:])
accountancy.writa_data("zakup", "01zapis.txt")
