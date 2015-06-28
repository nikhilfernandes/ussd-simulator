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
            self.account_number = input("Please choose an account: \n 1. 00031xxxxx1234 \n 2. 00090xxxxx5678\n")
            if (self.account_number == "1"):
                print("Your account balance is: \n Rs.2000.00")
                print("\n")
                bank_flow = BankFlow()
                bank_flow.menu()




