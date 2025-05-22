class Catregory:
    categories = []
    def __init__(self, name,from_Expences = False):
        self.name = name
        self.ledger = list()
        self.balance = 0
        if not from_Expences:
            Catregory.categories.append(name)
        
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
      
    def transfer(self, amount, category):
        if self.check_funds(amount):
          self.withdraw(amount, "Transfer to " + category.name)
          self.deposit(amount, "Transfer from " + self.name)
          return True
           
class Expences(Catregory):
    def __init__(self,name):
        super().__init__(name ,from_Expences= True)
        self.percentages = []
        self.max_lent = 0
        
    def get_purcentages(self, categories):
        for category in categories:
            if len(category.ledger) > 1:
                category_spent = category.ledger[1]["amount"]
                category_percentage = abs(category_spent)*100 / (category.balance + abs(category_spent))
                self.percentages.append(category_percentage)
            else:
                self.percentages.append(0)
    def print_dush(self):
        for i in range(100,-10,-10):
            print(f"{i:3}|",end='')
            for percentage in self.percentages: 
                if percentage >= i:
                    print("o  ", end="")
                else:
                    print("   ", end="")
            print()
        print("    " + "-"*10) 
           
    # Add spaces to names that have less lent than the gratest 
    def add_apaces(self):
        self.max_lent = max([len(char) for char in Catregory.categories])
        for i,name in enumerate(Catregory.categories):
           if len(name) < self.max_lent:
              Catregory.categories[i] = name + (' '*(self.max_lent-len(name)))
        return Catregory.categories
    @staticmethod    
    def helper(names: list):
        return names[1:] 
    
    def print_names(self):
        for _ in range(self.max_lent):
            print(f"{Catregory.categories[0][0]:>4}{Catregory.categories[1][0]:>4}{Catregory.categories[2][0]:>4}")
            Catregory.categories = list(map(Expences.helper,Catregory.categories))
            
            
food = Catregory("FOOD")
clothing = Catregory("Clothing")
auto = Catregory("Auto")
food.deposit(1000, "restaurant")
clothing.deposit(500, "shopping")
auto.deposit(1000, "gas")
food.withdraw(700, "restaurant")
clothing.withdraw(200, "shopping")
auto.withdraw(100, "gas")
print(Catregory.categories)
print('='*30)
expences = Expences('expences')
categories = [food,clothing,auto]
expences.get_purcentages(categories)
expences.add_apaces()
expences.print_dush()
expences.helper(Catregory.categories)
expences.print_names()

