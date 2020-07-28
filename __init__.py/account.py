from datetime import datetime
class BankAccount:
    bank="KCB"
    deposit_history = []
    loan = {}
    loan_balance = 0
    applied_for_loan = False
    # Play around with
    _MAXIMUM_LOAN_BORROWABLE = 350000
    _LOAN_INTEREST_RATE = .12

    #Constructor
    def __init__(self, first_name, second_name):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0

    #Returns the current time in string form
    def _getCurrentTime(self):
        now = datetime.now()
        now_formatted = now.strftime("%b %d %Y, %H:%M:%S")
        return now_formatted

    def account_name(self):
        name= "{} account for {} {} ".format(self.bank, self.first_name,self.second_name)
        return name
    def deposit(self,amount):
        if amount >0:
            self.balance+=amount
            timeDate = self._getCurrentTime()
            transaction_details = {"amount": amount, "date":timeDate}
            self.deposit_history.append(transaction_details)
            print("You have deposited {} to your account at {}".format(amount, timeDate))
        else:
            print("Too low ")
  
  
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            print("You have withdrawed {} from your account".format(amount))
        else:
            print("Amount too low")
    def get_balance(self):
        return "The balance of {} is {} ".format(self.account_name(),self.balance)
    
    def get_statement(self):
        for statement_item in self.deposit_history:
            print("On",statement_item['date'], ", you deposited KES", statement_item['amount'])
    
    def getLoanBalance(self):
        print("Your balance is KES",self.loan_balance,"for loan KES", self.loan["amount_borrowed"],"Borrowed on", self.loan["date"])
    def requestLoan(self, amount):
        # When customer has no Loan balance Give a loan
        if not self.loan_balance > 0:
            timeDate = self._getCurrentTime()
            self.loan["date"] = timeDate
            self.loan["amount_borrowed"] = amount
            self.loan_balance += amount
        #Else Deny loan
        else:
            print("Err:Loan Request Failed Reason:", end="")
            print(self.getLoanBalance())
            
    def payLoan(self,amount):
        if self.loan_balance == 0:
            print("You have no loan balance")
        elif amount > self.loan_balance:
            self.loan_balance = 0
        elif amount <= self.loan_balance:
            self.loan_balance -= amount

        return

    
acc1=BankAccount("Talaso","Susan")
acc2=BankAccount("Eyan", "Achwa")

acc1.deposit(-1000)
acc2.deposit(50)
acc1.deposit(100)
acc2.deposit(30)
acc1.withdraw(10)
acc2.withdraw(30)
acc1.withdraw(20)
acc2.withdraw(10)

acc2.get_statement()
acc1.requestLoan(3000)
acc1.requestLoan(777)
acc1.payLoan(250)
acc1.getLoanBalance()
print(acc1.get_balance())
print(acc2.get_balance())

print(acc1.account_name())
print(acc2.account_name())

File "<stdin>", line 1
    while True print("Hello Akirachix")
                   ^
SyntaxError: invalid syntax

while True:
    x = 10/0
    Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
echo("Hello Akirachix")Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'echo' is not defined
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
try:
    do_something
except:
    handle_exception

    try:
    1 + '1'
except:
    print('there was an error')

    try:
    1 +  '1'
except TypeError:
    print('TypeError exception raised')

    def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            self.deposits.append(amount)
            print("You have deposited {} to {}".format(amount, self.account_name()))

            time = datetime.now()

print(time)

print(time.year)

print(time.month)

print(time.day)

print(time.hour)

print(time.minute)

print(time.second)

print(time.microsecond)

from datetime import datetime

now = datetime.now()

year = now.strftime("%Y")
print("The year is {}".format(year))

month = now.strftime("%m")
print("The month is {}".format(month))

time = now.strftime("%H:%M:%S")
print("The time is {}".format(time))

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("The date and time is {}".format(date_time))

