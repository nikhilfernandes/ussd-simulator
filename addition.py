from operation import Operation
class Addition(Operation):

    def __init__(self):
        super(Addition, self).__init__()        
        
    def do(self):
      return float(self.first_number) + float(self.second_number)