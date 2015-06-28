from string_utils import StringUtils
class Simulator:


    def __init__(self, flows):
        self.flows = flows

    def run(self):
        msisdn = input("Enter your MSISDN: \n #123# for Banking \n #234# for Calculator \n") 
        if msisdn in self.flows:                     
            module = __import__(self.flows[msisdn])            
            class_ = getattr(module, StringUtils.camelize(self.flows[msisdn]))
            flow = class_()
            flow.menu()            
        else:
            self.run()

    
    
      




simulator=Simulator({'#123#': 'bank_flow', '#234#': "calculator_flow"})
Simulator.run(simulator)