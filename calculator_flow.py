from flow import Flow
class CalculatorFlow:
      operations = {'1': 'add', '2': "subtract", "3":"multiply", "4": "divide"}

      def menu(self):
        self.input =  input("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n9. Exit\n")
        if self.input in self.operations :
            flow = Flow()
            flow.do(self.operations, self.input)
        elif (self.input == "9"):
          exit()          
        else:
            print("Wrong Selection: \n")
            self.menu()


