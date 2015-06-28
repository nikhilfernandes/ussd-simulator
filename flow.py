class Flow:

    def do(self, operations, input_str):
        module = __import__(operations[input_str])            
        class_ = getattr(module, operations[input_str].title())
        action = class_()
        action.step_one()