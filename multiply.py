from operation import Operation
class Multiply(Operation):

    def __init__(self):
        super(Multiply, self).__init__()        

    def step_two(self):
        super(Multiply, self).step_two()
        print(float(self.first_number) * float(self.second_number))