from bank_flow import BankFlow
class MiniStatement:

  def step_one(self):
        self.password =  input("Enter your login password: \n")
        if (self.password == "password"):
            self.step_two()
        else:
            self.step_one()

  def step_two(self):
      print("You last 3 transactions are: \n CR, Rs 100.00 15-06-2015\n DR, Rs 100.00 16-06-2015\n DR, Rs 100.00 18-06-2015 ")
      print("\n")
      bank_flow = BankFlow()
      bank_flow.menu()