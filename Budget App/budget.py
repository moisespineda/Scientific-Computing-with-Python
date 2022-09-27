class Category:
    def __init__(self, category):
        self.category=category
        self.ledger=[]

    def __str__(self):
        s = self.category.center(30, "*") + "\n"

        for item in self.ledger:
            temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            s += temp + "\n"
            
        s += "Total: " + str(self.get_balance())
        return s
        
    def check_funds(self, amount):
        if self.get_balance()>=amount:
            return True
        return False

    #method for depositing an amount in the balanced with its descriptions
    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description":description})

    #method for withdreawing an amount in the balanced with its description
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":description})
        return False

    def get_balance(self):
        total=0
        for i in self.ledger:
            total+= i["amount"]
        return total

    def transfer(self, amount, cat_name):
        if self.withdraw(amount, "Transfer to {}".format(cat_name.category)):
            cat_name.deposit(amount, "Transfer from", self.category)
            return True
        return False

def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "
    # Spaces
    s += " "
  s += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].category[i] + " "
      else:
        s += "   "
    # Spaces
    s += " "

  return s