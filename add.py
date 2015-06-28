from operation import Operation
class Add(Operation):

    def __init__(self):
        super(Add, self).__init__()        
        
    def do(self):
      return float(self.first_number) + float(self.second_number)