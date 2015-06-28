from operation import Operation
class Multiply(Operation):

    def __init__(self):
        super(Multiply, self).__init__()        

    def do(self):
      return float(self.first_number) * float(self.second_number)                