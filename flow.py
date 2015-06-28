from string_utils import StringUtils
class Flow:

    def do(self, operations, input_str, flow_name):
        if input_str in operations :            
            self.create_flow(operations[input_str], StringUtils.camelize(operations[input_str])).step_one()
        elif (input_str == "9"):
          exit()          
        else:
            print("Wrong Selection: \n")
            self.create_flow(flow_name, StringUtils.camelize(flow_name)).menu()
            

    def create_flow(self, module_name, class_name):
        module = __import__(module_name)            
        class_ = getattr(module, class_name)
        return class_()

        