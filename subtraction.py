from operation import Operation
class Subtraction(Operation):

    def __init__(self):
        super(Subtraction, self).__init__()        
    
    def do(self):
      return float(self.first_number) - float(self.second_number)    