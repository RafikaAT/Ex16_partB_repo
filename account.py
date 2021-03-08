from datetime import date

class Account:
    numCreated = 0
    def __init__(self, current):
        self.balance = current
        Account.numCreated +=1

    def deposit(self, amount):
        self.balance += amount
        return

    def withdraw(self, amount):
        self.balance -= amount
        return

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    withdrawal_charge = 0.7
    interest_1 = 0.5

# The below constructor is not needed as we do not
# have any additional attributes - all is inherited
    # def __init__(self, current):
    #     pass

# Adding Methods
# This method adds interest with each deposit
    def add_interest(self, amount):
        return Account.deposit(self, amount*self.interest_1)

    # This method fines the user for withdrawals by deducting 70% of the withdrawal amount
    # each time the user withdraws
    def deduct_withdrawal(self, amount):
        return Account.withdraw(self, amount+(amount*self.withdrawal_charge))

# class StudentAccount(Account):
#     def __init__(self, current, overdraft_amount=0):
#         super().__init__(current)
#         self.overdraft_amount = overdraft_amount
#     def set_student_overdraft(self, amount, overdraft=0):
#         self.withdraw(amount)
#         if self.balance < 0:
#             overdraft = (self.balance-amount)*(-1)
#
#             if overdraft >= 2000:
#                 print("you have reached your limit", overdraft)
#             else:
#                 print ('hello')
#
#         else:
#             overdraft==0


class ChildBankAccount(Account):
    def __init__(self, current, restricted=True):
        super().__init__(current)
        self.balance = current
        self.restricted = restricted

    def calculate_age(self, dtob):
        today = date.today()
        return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))


    def isRestricted(self, dtob):
        # today = date.today()
        # born_year = print((input("Please enter your birth year"))
        # birth_year = int(born_year)
        # age = today.year - birth_year

        if self.calculate_age(dtob) < 18:
            print("Welcome to your account")
        else:
            raise Exception('This account is for persons under the age of 18. Please create an adult account.')
    # def restrict_withdraw(self):
    #     if self.balance < 0:
    #         def
