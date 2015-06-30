from flow import Flow
class CalculatorFlow:
      operations = {'1': 'addition', '2': "subtraction", "3":"multiplication", "4": "division"}

      def menu(self):
        self.input =  input("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n9. Exit\n")
        flow = Flow()
        flow.do(self.operations, self.input, "calculator_flow")

