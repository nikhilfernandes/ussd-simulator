from operation import Operation
class Subtract(Operation):

    def __init__(self):
        super(Subtract, self).__init__()        
    
    def do(self):
      return float(self.first_number) - float(self.second_number)    