from bank_flow import BankFlow
class BalanceInquiry:

    def step_one(self):
        self.password =  input("Enter your login password: \n")
        if (self.password == "password"):
            self.step_two()
        else:
            self.step_one()

    def step_two(self):
        self.balance_for =  input("Fetch Balance for: \n 1. Single Account \n 2. Multiple Accounts\n")
        self.step_three()


    def step_three(self):
        if (self.balance_for == "1"):
            self.single_account_balance()
        elif (self.balance_for == "2"):
            self.show_account_balance("Your account balance for 00031xxxxx1234 is: \n Rs.2000.00\n Your account balance for 00090xxxxx5678 is: \n Rs.1000.00")
        else:
            self.show_account_balance("Wrong Selection")


                

    def show_account_balance(self, message):
        print(message)
        print("\n")
        bank_flow = BankFlow()
        bank_flow.menu()


    def single_account_balance(self):
        self.account_number = input("Please choose an account: \n 1. 00031xxxxx1234 \n 2. 00090xxxxx5678\n")            
        if (self.account_number == "1"):
            self.show_account_balance("Your account balance is: \n Rs.2000.00")               
        elif (self.account_number == "2"):
            self.show_account_balance("Your account balance is: \n Rs.1000.00")                
        else:
            self.show_account_balance("Wrong Selection")                                



