class Category:
    category_name = str()
    available_budget = float()
    current_draw = float()
    ledger = list()
    
    def __repr__(self) -> str:
        return "Category()"
    
    #create the ledger list when the object is call
    def __str__(self) -> str:
        total = float()
        display = f"{self.category_name}".center(30, "*") + "\n"
        for x in self.ledger:
            desc = "{}".format(x['description']).ljust(23)[:23]
            amnt = "{:.2f}".format(x['amount']).rjust(7)[:7]
            display += desc + amnt + "\n"
            total += x['amount']
        display += "Total: {:.2f}".format(total)
        return display
    
    def __init__(self, category_name=str()):
        self.category_name = category_name
        self.available_budget = float()
        self.ledger = list()

    def deposit(self, amount, description=str()):
        amount = float(amount)
        self.available_budget = amount
        d = dict()
        d['amount'] = amount
        d['description'] = description
        self.ledger.append(d)

    def withdraw(self, amount, description=str()):
        amount = float(amount)
        if Category.check_funds(self, amount) is True:
            self.available_budget -= amount
            self.current_draw += amount
            d = dict()
            d['amount'] = amount*-1
            d['description'] = description
            self.ledger.append(d)
            return True
        return False

    def get_balance(self):
        return self.available_budget

    def transfer(self, amount, budget_category):
        amount = float(amount)
        if Category.check_funds(self, amount) is True:
            desc_to = "Transfer to {}".format(budget_category.category_name)
            Category.withdraw(self, amount, desc_to)

            desc_from = "Transfer from {}".format(self.category_name)
            budget_category.deposit(amount, desc_from)
            return True
        return False

    def check_funds(self, amount):
        if self.available_budget >= amount:
            return True
        return False


def create_spend_chart(categories):
    # count total draw of all category and max len category name
    max_len_categories = int()
    total_draw = float()
    for category in categories:
        total_draw += category.current_draw
        len_category = len(category.category_name)
        if len_category > max_len_categories:
            max_len_categories = len_category
    # create the percentage bar withdraw of all category
    chart = "Percentage spent by category\n"
    percent = 100.0
    while percent >= 0:
        chart += "{}| ".format(int(percent)).rjust(5)
        # condition percentage withdraw
        for category in categories:
            percent_cat = (category.current_draw/total_draw)*100
            if percent <= percent_cat:
                chart += 'o  '
            else:
                chart += '   '
        percent -= 10.0
        chart += '\n'
    # add '-' att the bot of bar
    line_len = len(categories)*3
    chart += '{}\n'.format('-'*(line_len+1)).rjust(line_len+6)
    # make the horizontal category name
    i = 0
    # print(max_len_categories)
    while max_len_categories > i:
        chart += ' ' * 5
        for category in categories:
            # skip if the string is out of range
            try:
                chart += '{}  '.format(category.category_name[i])
            except IndexError:
                chart += '   '
        # no enter in the last category name
        if max_len_categories > i + 1:
            chart += '\n'
        i += 1

    return chart