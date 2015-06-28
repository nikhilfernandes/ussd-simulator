

class CalculatorFlow:
      operations = {'1': 'add', '2': "subtract", "3":"multiply", "4": "divide"}

      def menu(self):
        self.input =  input("1. Add \n2. Subtract \n3. Multiply \n4. Divide\n")
        if self.input in self.operations :
            module = __import__(self.operations[self.input])            
            class_ = getattr(module, self.operations[self.input].title())
            action = class_()
            action.step_one()
        else:
            print("Wrong Selection: \n")
            self.menu()


