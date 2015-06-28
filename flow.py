from string_utils import StringUtils
class Flow:

    def do(self, operations, input_str):
        module = __import__(operations[input_str])            
        class_ = getattr(module, StringUtils.camelize(operations[input_str]))
        action = class_()
        action.step_one()