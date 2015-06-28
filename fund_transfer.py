from bank_flow import BankFlow
class FundTransfer:

  def step_one(self):
        self.password =  input("Enter your login password: \n")
        if (self.password == "password"):
            self.step_two()
        else:
            self.step_one()

  def step_two(self):
      self.payee = input("Please choose a Payee:\n 1. Mom\n 2. Dad\n 3. Rajesh\n ")      
      if (self.payee not in ["1", "2", "3"]):
            print("Please select the correct payee: \n ")
            self.step_two()
      else:
            self.step_three()


  def step_three(self):
      self.account_number = input("Please choose an account to transfer from: \n 1. 00031xxxxx1234 \n 2. 00090xxxxx5678\n")            
      if (self.account_number not in ["1", "2"]):
        print("Please select the correct account: \n ")
        self.step_three()  
      else:
        self.step_four()
  
  def step_four(self):
      self.transfer_amount = input("Please choose the transfer amount: \n")            
      if(self.transfer_amount.isdigit()):
        print("Amount has been transferred")
        bank_flow = BankFlow()
        bank_flow.menu()
      else:
        print("Invalid transfer Amount: \n")
        self.step_four();

      
      