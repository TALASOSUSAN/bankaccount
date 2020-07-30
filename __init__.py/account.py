class BankAccount:
    bank ="KCB"
    
    def _init_(self,first_name,last_name,phone_number,bank):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.phone_number=phone_number
        self.bank=bank
        self.deposit=deposit[]
        self.withdraw=withdraw[]

        def get_currentTime(self);
        now=datetime.now()
        time_formatted=now.strftime("%b %d %Y,%H %M %S")
        return time_formatteds

    def get_loan(self,amount):
         try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

        if amount<=0:
            print("A loan cannot be offered at the moment")
            else:
                if self.loan=amount
                print("You have sucessfully recieved a loan of {}".format(amount))
    
    def account_name(self):
        name ="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
        return name
    
    def  deposit(self,amount):
        try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

        if amount =0:
            print("You cannot deposit a negative amount")
        else:
            self.balance +=amount
            self.deposit.append(deposit)  
            time=date.time()
            formated_time=time.strftime{"%m %drd %Y, %H;%M:%S" }
            print("You have deposited {} on {} ".format(amount,self.account,formated_time))
      

    def get_balance(self):
        return "{} balance is {} ".format(self.account_name(),self.balance)

    def withdraw(self,amount):
         try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

      if amount=0:
      print("You cannot withdraw zero amount")
      elif amount >self.balance:
          print("You dont have enough balance to make this request")
      else:
          self.balance>=amount
          self.withdraw.append(amount)   
           formated_time=stime.strftime{"%m %drd %Y, %H;%M:%S"}
          print("You have withdrawn {} from {}".format (self.account_name,self.amount,formated_time))

    def deposit_statement(self):
      for deposit in self.deposit:
          time=diposit['time']
          formated_time=time.strftime{"%m %drd %Y, %H;%M:%S"}
          amount=deposit["amount"]
          statement="You have deposited {} on {}. Your new balance is {}".format(self.amount,formated_time,self.balance)
          print(statement)
     


def  withdraw _ statement(self,amount):
   for withdraw in self.withdrawa:
       time=deposit["time"]
       formated_time=time.strftime{"%m %drd %Y, %H:%M:%S"}
       amount withdraw=["amount"]
       statement="You have sucessfully withdrawn {} on {}".format(amount,formated_time)
       print (statement)

def pay_loan(self,amount):
     try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

    if amount<=0:
    print(" You have insufficient balance to repay the loan")
    else:
        if self.loan==0:
            print("You don't have a loan at the moment")
     else:
         if amount> self.loan:
             print("Your loan is {}, an amount less or equal is required".format(self.loan))

             def __init__self(self,first_name, second_name, phone_number, service_provider);
             self.service_provider=service_provider
             self.airtime=[]
             self.bills=[]
             self.money=[]
             self.recieved=[]
             super().__init__(first_name, second_name, phone_number)

             transaction_details={"amount" amount,"date":timeDate}
             self.airtime.append(transaction_details)
             print("you have bought airtime worth {} on {}", format(amout,timeDate))

             def paybills(self,amount):
        try: 
            amount-1
        except TypeError:
            print("please enter amount in figures")
            return
        if amount>self.balance:
            print("You have insufficient balance.Your balance is {}".format(self.balance))

        else:
            self.balance-=amount
            time=datetime.now()
            paybills={
                "time":time
                "paybills":amount
            }
            self.paybills.append(paybills)
            print("you have paid bills worth {}.your balance is {}".format(amount,self.get_formatted_time(time)))
    def send_money(self,amount):
        try:
            amount-1
        except TypeError:
            print("please enter amount in figures") 
            return
            if amount>self.balance:
                print("failed.insuffcient fundsin your account.your balance is {}".format(self.balance))
                else:
            self.balance-=amount
            time=datetime.now()
            money={
                "time":time
                "money":amount
            }
            self.money.append(money)
            print(" confirmed  you have sent {} .your balance is {}".format(amount,self.get_formatted_time(time)))
    def receive_money(self):
        time=datetime.now()
        money_received={
            "time":time
            return  "You have received {}.your balane is {}".format(self.get_formatted_time)
            
        }