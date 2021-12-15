import sys


class Accountant:
    def __init__(self):
        self.balance = 0
        self.warehouse = {}
        self.logs = []
        self.data = []
        self.transformed_data = []

    def open_data(self, filepath):
        with open(filepath) as f:
            for line in f:
                self.data.append(line.strip())

    def writa_data(self, action, filepath):
        with open(filepath, "w") as f:
            for row in self.logs:
                for line in row:
                    f.write(f"{line}\n")
        print(f"--- >>> {action} -->> saldo: {self.balance}. Log operacji w pliku {filepath}")
        return

    def stock_status(self, *args):
        for arg in args:
            for prd_id in arg:
                if prd_id in self.warehouse:
                    print(f"{prd_id} : {accountancy.warehouse[prd_id]} sztuk")
                else:
                    print(f"{prd_id} : brak poyzcji w magazynie")
        return


    def transform_data(self):
        # transformed_data = []
        index = 0
        action_param = {"saldo": 2, "zakup": 3, "sprzedaz": 3}
        while index < len(self.data):
            if self.data[index] in action_param:
                qty_param = action_param[self.data[index]]
                action = self.data[index]
                if action == "saldo":
                    self.logs.append([action, self.data[index + 1], self.data[index + qty_param]])
                    self.balance += int(self.data[index+1])
                elif action == "zakup":
                    self.logs.append([action, self.data[index + 1], self.data[index + 2], self.data[index + qty_param]])
                    self.balance -= int(self.data[index + qty_param]) * int(self.data[index + qty_param])
                    if self.data[index + 1] in self.warehouse:
                        # add quntity to warehouse
                        self.warehouse[self.data[index + 1]] += int(self.data[index + qty_param])
                    else:
                        # add item to warehouse
                        self.warehouse[self.data[index + 1]] = self.data[index + qty_param]

                elif action == "sprzedaz":
                    self.logs.append([action, self.data[index + 1], self.data[index + 2], self.data[index + qty_param]])
                    if (int(self.warehouse[self.data[index + 1]]) - int(self.data[index + qty_param])) < 0:
                        print(f"\nChcesz sprzedać {self.data[index + qty_param]} sztuk {self.data[index + 1]}. "
                              f" W magazynie jest: {self.warehouse[self.data[index + 1]]}\n ")
                        return
                    qty = int(self.warehouse[self.data[index + 1]])
                    qty -= int(self.data[index + qty_param])
                    self.warehouse[self.data[index + 1]] =qty
                    self.balance += int(self.data[index + 2]) * int(self.data[index + qty_param])
                index += 1
                tmp = self.data[index:index+qty_param]
                self.transformed_data.append([action, tmp])
                index += qty_param
            else:
                print("Koniec programu")
                break
        return

    def get_balance(self, action):
        new_balance = int(input("Podaj wartość salda: "))
        self.balance += new_balance
        comments = input("Komentarz: ")
        self.logs.append([action, new_balance, comments])
        return

    def get_buy(self, prd_id, prd_prise, prd_qty):
        if self.balance <= 0:
            print(f"\nSaldo wynosi: {self.balance}. Nie można kupić towaru\n ")
            return
        if prd_prise * prd_qty > self.balance:
            print(f"\nNie mozna dokonac zakupu. Za małe saldo: {self.balance}\n")
            return
        self.balance -= prd_prise * prd_qty
        if prd_id in self.warehouse:
            # add quntity to warehouse
            self.warehouse[prd_id] += prd_qty
        else:
            # add item to warehouse
            self.warehouse[prd_id] = prd_qty
        self.logs.append(["zakup", prd_id, prd_prise, prd_qty])
        return

    def get_sale(self, prd_id, prd_prise, prd_qty):
        if not self.warehouse:
            print("\nMagazyn jest pusty proszeę zakupić towar.\n")
            return
        if not prd_id in self.warehouse:
            print("\nBrak towaru  w magazanie, proszę towar  wybrać z poniższej listy:  ")
            temp_data = []
            index = 0
            while index < len(self.warehouse):
            # for key in self.warehouse:
                temp_data += temp_data.append(f"{key} - {self.warehouse[key]} sztuk")
                # print(f"{key} - {self.warehouse[key]} sztuk")
                continue
            return
        # remove item from warehouse
        if (self.warehouse[prd_id] - prd_qty) < 0:
            print(f"\nChcesz sprzedać {prd_qty} {prd_id} w magazynie {self.warehouse[prd_id]}\n ")
            return
        self.warehouse[prd_id] -= prd_qty
        self.balance += prd_prise * prd_qty
        self.logs.append(["sprzedaz", prd_id, prd_prise, prd_qty])

# availabe_actions = ["saldo", "sprzedaz", "zakup", "stop", "konto", "magazyn", "przeglad"]
accountancy = Accountant()
# accountancy.open_data("file.txt")
# print(accountancy.data)
# accountancy.transform_data()
# print(accountancy.transformed_data)

# while True:
#     action = input("Wybierz akcje: \n")
#     if action == "saldo":
#         accountancy.get_balance("saldo")
#     elif action == "zakup":
#         accountancy.get_buy("zakup")
#     elif action == "sprzedaz":
#         accountancy.get_sale("sprzedaz")
#     elif action == "stop":
#         accountancy.logs.append([action])
#         break
#     else:
#         print(f"\nDostępne akcje: {availabe_actions[:3]}")
#         print("\nNiedozwolna akcja")
#         exit("exit")

# print(accountancy.balance)
# print(accountancy.logs)
# print(accountancy.warehouse)

    # for row in accountancy.logs:
    #     for line in row:
    #         print(line)
    # print("--- >>> saldo")
