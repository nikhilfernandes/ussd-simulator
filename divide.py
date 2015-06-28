from operation import Operation
class Divide(Operation):

    def __init__(self):
        super(Divide, self).__init__()  

    def do(self):
      try:
        return float(self.first_number) / float(self.second_number)                      
      except ZeroDivisionError:
        print("You cant divide a number by 0: \n")
        self.step_two()