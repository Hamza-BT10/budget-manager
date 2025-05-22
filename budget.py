class Catregory:
    names = []
    def __init__(self, name, from_dashboard= False):
        self.name = name
        self.ledger = list()
        self.balance = 0
        if not from_dashboard:
            Catregory.names.append(name)
        
    def check_funds(self, amount):
        if amount > self.balance:
          return False
        return True
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
          items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
          total += item["amount"]
        output = title + items + "Total: " + str(total)
        return output
      
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        print(f"Deposit {amount} to {self.name}")

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
          self.ledger.append({"amount": -amount, "description": description})
          self.balance -= amount
          print(f"Withdraw {amount} from {self.name}")
          return True
        else:
          print("Insufficient funds")

    def get_balance(self):
        total = 0
        for item in self.ledger:
          total += item["amount"]
        self.balance = total
        return self.balance
      
    def transfer(self, amount, name):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + name.name)
            self.deposit(amount, "Transfer from " + self.name)
            return True

class DashBoard(Catregory):
    def __init__(self,name):
        super().__init__(name,from_dashboard = True)
        self.percentages = []
        self.max_lent = 0

    def get_purcentages(self,names: list):
        for name in names:
            if len(name.ledger) > 1:
                category_spent = name.ledger[1]["amount"]
                category_percentage = abs(category_spent)*100 / (name.balance + abs(category_spent))
                self.percentages.append(category_percentage)
            else:
                self.percentages.append(0)
           
    # Add spaces to names that have less lenth than the gratest  
    def add_apaces(self):
        self.max_lent = max([len(char) for char in Catregory.names])
        for i,name in enumerate(Catregory.names):
           if len(name) < self.max_lent:
                Catregory.names[i] = name.ljust(self.max_lent)
    
    def dush(self):
        for i in range(100,-10,-10):
            print(f"{i:3}|",end='')
            for percentage in self.percentages: 
                if percentage >= i:
                    print("o   ", end="")
                else:
                    print("   ", end="")
            print()
        print("   " + "-"*10) 

    def names(self):
        for i in range(self.max_lent):
            space=5
            for name in Catregory.names:
                if name[i]:
                    print(f"{name[i].rjust(space)}",end='')
                    space = 4
                else:
                    print(f"{" ".rjust(space)}",end='')
                    space = 4      
            print()  
    def print_dush_board(self,names:list):
        self.get_purcentages(names)
        self.add_apaces()
        self.dush()
        self.names()

            
food = Catregory("Food")
clothing = Catregory("Clothing")
auto = Catregory("Auto")
food.deposit(1000, "Restaurant")
clothing.deposit(500, "Shopping")
auto.deposit(1000, "Gas")
food.withdraw(700, "Restaurant")
clothing.withdraw(200, "Shopping")
auto.withdraw(100, "Gas")
dashboard = DashBoard("Dashboard")
all_category = [food, clothing, auto]
dashboard.print_dush_board(all_category)

            






