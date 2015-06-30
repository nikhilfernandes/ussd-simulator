from operation import Operation
class Multiplication(Operation):

    def __init__(self):
        super(Multiplication, self).__init__()        

    def do(self):
      return float(self.first_number) * float(self.second_number)                