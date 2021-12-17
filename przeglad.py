from helper import *

accountancy.open_data(sys.argv[1])
review(int(sys.argv[2]), int(sys.argv[3]) )
accountancy.writa_data("przeglad", "01zapis.txt")

