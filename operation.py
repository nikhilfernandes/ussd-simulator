from string_utils import StringUtils
from calculator_flow import CalculatorFlow

class Operation:

    def step_one(self):
      self.first_number =  input("Enter the first number: \n")
      if StringUtils.is_number(self.first_number):
          self.step_two()
      else:
          print("Please enter a valid number: \n")
          self.step_one()




    def step_two(self):
        self.second_number =  input("Enter the second number: \n")              
        if not StringUtils.is_number(self.second_number):          
          print("Please enter a valid number: \n")
          self.step_two()
        else:
          print(self.do())
          print("\n")
          calculator_flow = CalculatorFlow()
          calculator_flow.menu()


      

