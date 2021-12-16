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
        self.transform_data()
        return

    def writa_data(self, action, filepath):
        with open(filepath, "w") as f:
            for row in self.logs:
                for line in row:
                    f.write(f"{line}\n")
        print(f"\n--- >>> {action} -->> saldo: {self.balance}. \nLog operacji w pliku {filepath}\n")
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
        transformed_data = []
        index = 0
        action_param = {"saldo": 2, "zakup": 3, "sprzedaz": 3}
        while index < len(self.data):
            if self.data[index] in action_param:
                qty_param = action_param[self.data[index]]
                action = self.data[index]
                index += 1
                tmp = self.data[index:index+qty_param]
                if action == "saldo":
                    self.get_balance(action, *tmp)
                if action == "zakup":
                    self.get_buy(action, *tmp)
                if action == "sprzedaz":
                    self.get_sale(action, *tmp)
                transformed_data.append([action, tmp])
                index += qty_param
            else:
                break
        return True

    def get_balance(self, action, new_balance, comments):
        self.balance += int(new_balance)
        self.logs.append([action, new_balance, comments])
        return

    def get_buy(self, action, prd_id, prd_prise, prd_qty):
        prise = int(prd_prise)
        qty = int(prd_qty)
        if self.balance <= 0:
            print(f"\nSaldo wynosi: {self.balance}. Nie można kupić towaru\n ")
            return
        if prise * qty > self.balance:
            print(f"\nNie mozna dokonac zakupu. Za małe saldo: {self.balance}\n")
            return
        self.balance -= prise * qty
        if prd_id in self.warehouse:
            # add quntity to warehouse
            self.warehouse[prd_id] += qty
        else:
            # add item to warehouse
            self.warehouse[prd_id] = qty
        self.logs.append([action, prd_id, prd_prise, qty])
        return

    def get_sale(self, action, prd_id, prd_prise, prd_qty):
        prise = int(prd_prise)
        qty = int(prd_qty)
        if not self.warehouse:
            print("\nMagazyn jest pusty proszeę zakupić towar.\n")
            return
        if not prd_id in self.warehouse:
            print("\nBrak towaru  w magazanie, proszę towar  wybrać z poniższej listy:  ")
            temp_data = []
            index = 0
            while index < len(self.warehouse):
            # for key in self.warehouse:
                temp_data += temp_data.append(f"{index} - {self.warehouse[index]} sztuk")
                # print(f"{key} - {self.warehouse[key]} sztuk")
                continue
            return
        # remove item from warehouse
        if (self.warehouse[prd_id] - qty) < 0:
            print(f"\nChcesz sprzedać {qty} {prd_id} w magazynie {self.warehouse[prd_id]}\n ")
            return
        self.warehouse[prd_id] -= qty
        self.balance += prise * qty
        self.logs.append([action, prd_id, prd_prise, prd_qty])

def review(first, last):
    if first < 1:
      first = 1
    if last > len(accountancy.logs) :
      last = len(accountancy.logs)
    while first <= last:
      print(f"Akcja nr {first} - {accountancy.logs[first-1]}")
      first += 1
    print("--- >>> przeglad")


accountancy = Accountant()