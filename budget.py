class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        output = str()
        # A title line of 30 characters where the name of the category is centered in a line of * characters.
        for n in range(int((30 - len(self.name))/2)):
            output += '*'
        output += self.name
        for n in range(int((30 - len(self.name))/2)):
            output += '*'
        output += '\n'
        # A list of the items in the ledger. Each line should show the description and amount
        for led in self.ledger:
            # The first 23 characters of the description should be displayed, then the amount
            if len(led['description']) > 23:
                for n in range(23):
                    output += led['description'][n]
            else:
                output += led['description']
                for n in range(23 - len(led['description'])):
                    output += ' '
            # The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
            if len('{:.2f}'.format(led['amount'])) > 7:
                for n in range(7):
                    output += '{:.2f}'.format(led['amount'])[n]
            else:
                for n in range(7 - len('{:.2f}'.format(led['amount']))):
                    output += ' '
                output += '{:.2f}'.format(led['amount'])
            output += '\n'
        # A line displaying the category total.
        output += 'Total '
        output += '{:.2f}'.format(self.get_balance())

        return output

    def deposit(self, amount, description=''):
        self.ledger.append(
            {'amount': float(amount), 'description': description})
        return True

    def withdraw(self, amount, description=''):
        if(self.check_funds(amount)):
            self.ledger.append({'amount': -abs(float(amount)),
                                'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = float(0)
        for led in self.ledger:
            balance += led['amount']
        return balance

    def transfer(self, amount, CategoryObject):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to '+CategoryObject.name)
            CategoryObject.deposit(amount, 'Transfer from '+self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        return False if amount > self.get_balance() else True


def create_spend_chart(categories):
    pass
