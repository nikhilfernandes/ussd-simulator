from operation import Operation
class Divide(Operation):

    def __init__(self):
        super(Divide, self).__init__()        

    def step_two(self):
        super(Divide, self).step_two()
        print(float(self.first_number) / float(self.second_number))