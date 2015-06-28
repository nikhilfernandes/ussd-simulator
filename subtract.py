from operation import Operation
class Subtract(Operation):

    def __init__(self):
        super(Subtract, self).__init__()        

    def step_two(self):
        super(Subtract, self).step_two()
        print(float(self.first_number) - float(self.second_number))