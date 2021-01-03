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
        output += 'Total: '
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
    listCat = list()
    # listCat : list name and persent of each category
    for cat in categories:
        totalDeposit = float(0)
        totalWithdraw = float(0)
        for led in cat.ledger:
            if led['amount'] > 0:
                totalDeposit += led['amount']
            else:
                totalWithdraw += abs(led['amount'])
        persent = totalWithdraw/totalDeposit * 100
        persent = persent - persent % 10
        persent = int(persent)
        listCat.append([cat.name, persent])
    # print(listCat)
    # [['Food', 10], ['Clothing', 30], ['Auto', 0]]

    # y : length height of char
    y = 0
    maxLenOfCatName = 0
    for li in listCat:
        if maxLenOfCatName < len(li[0]):
            maxLenOfCatName = len(li[0])
    # 12: 11 line from 100 to 0 percent, 1 line for '----'
    y = 12 + maxLenOfCatName

    # print barchar
    char = str()
    char += 'Percentage spent by category\n'
    for j in range(y):
        # print 100 to 0 %
        if 0 <= j and j <= 10:
            persent = 100 - 10*j
            space = 3 - len(str(persent))
            for k in range(space):
                char += ' '
            char += str(persent)
            char += '| '
            for i in range(len(listCat)):
                if listCat[i][1] >= persent:
                    char += 'o  '
                else:
                    char += '   '
        # print '-----'
        elif j == 11:
            char += '    -'
            for i in range(len(listCat)):
                char += '---'
        # print cat name
        else:
            char += '     '
            index = j - 12
            for i in range(len(listCat)):
                if index <= len(listCat[i][0]) - 1:
                    char += listCat[i][0][index]
                    char += '  '
                else:
                    char += '   '
        char += '\n'
    return char
