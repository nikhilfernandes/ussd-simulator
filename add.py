from operation import Operation
class Add(Operation):

    def __init__(self):
        super(Add, self).__init__()        

    def step_two(self):
        super(Add, self).step_two()
        print(float(self.first_number) + float(self.second_number))