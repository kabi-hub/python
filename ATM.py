class ATM:
    def __init__(self):
        self.balance=0
        self.pin=1234
        self.attemp=3
    def check_pin(self):
        while self.attemp>0:
          self.temp=int(input("Enter the pin\n"))
          if self.pin==self.temp:
            print("Correct pin")
            return 1
          else:
            self.attemp -=1
            print(f"incorrect you have {self.attemp} attemp left ")
        
        print("too many attemp pin.please contact your bank")
        return 
    def deposite(self):
        amount=int(input("enter the amount\n"))
        self.balance=self.balance+amount
        print(f"Your deposite successful")
        self.atm_menu()
    def withdraw(self):
       amount=int(input("Enter the amount\n"))
       if self.balance<amount:
          print("insufficient balance")
       else:
          self.balance=self.balance-amount
          print("Your withdraw successful")
          self.atm_menu()
    def check_balance(self):
       print(f'your current total balance:{self.balance}')
       self.atm_menu()
    def atm_menu(self):
       print("....Welcome to your service....")
       print("1.deposite balance")
       print("2.withdraw balance")
       print("3.check the balance")
       print("4.exits") 
       choice=int(input("Enter number your want\n"))
       match choice:
          case 1:
             self.deposite()
          case 2:
             self.withdraw()
          case 3:
             self.check_balance()
          case 4:
             print("Thank you using our servise.")
          case _:
             print("invalid number")
obj=ATM()
if obj.check_pin():
   obj.atm_menu()