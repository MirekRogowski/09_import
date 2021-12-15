from helper import *

accountancy.open_data(sys.argv[1])
accountancy.transform_data()
accountancy.writa_data("przeglad", "01zapis.txt")
review(int(sys.argv[2]), int(sys.argv[3]) )
