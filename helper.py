import sys


class Accountant:
    def __init__(self):
        self.balance = 0
        self.warehouse = {}
        self.logs = []
        self.data = []

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
        print(f"--- >>> {action} -->> saldo: {self.balance}. \n\nLog operacji w pliku {filepath}\n")
        return

    def stock_status(self, *args):
        for arg in args:
            print(f"Stan magazynu: ")
            for prd_id in arg:
                if prd_id in self.warehouse:
                    print(f" - {prd_id} : {accountancy.warehouse[prd_id]} sztuk")
                else:
                    print(f" - {prd_id} : brak poyzcji w magazynie")
        print("\n")
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
        if self.balance + int(new_balance) < 0:
            print(f"\nBrak środków na koncie.\n"
                  f"Obecny stan konta -->> {self.balance}\n"
                  f"Potrzebujesz jeszcze-->> {self.balance + int(new_balance)}\n"
                  f"Do zapłaty -->> {new_balance}")
            return
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
            print(f"\nNie mozna dokonac zakupu - {prd_id}. Za małe saldo - {self.balance}\n"
                  f"Koszt zakupu - {prise * qty}. Brakuje - {prise * qty - self.balance}\n")
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
            print(f"\nBrak {prd_id} w magazynie.")
            self.stock_status()
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
    print("\nHitoria akcji:")
    while first <= last:
      print(f"Akcja nr {first} - {accountancy.logs[first-1]}")
      first += 1
    print("\n")

def action(file, action, *data):
    accountancy.open_data(file)
    accountancy.get_balance(action, *data)
    accountancy.writa_data(action, "01zapis.txt")



accountancy = Accountant()