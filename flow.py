from string_utils import StringUtils
class Flow:

    def do(self, operations, input_str):
        if input_str in operations :
            module = __import__(operations[input_str])            
            class_ = getattr(module, StringUtils.camelize(operations[input_str]))
            action = class_()
            action.step_one()
        elif (input_str == "9"):
          exit()          
        else:
            print("Wrong Selection: \n")
            self.menu()

        