from string_utils import StringUtils
from flow import Flow
class Simulator:


    def __init__(self, flows):
        self.flows = flows

    def run(self):
        msisdn = input("Enter your MSISDN: \n #123# for Banking \n #234# for Calculator \n") 
        if msisdn in self.flows:            
            Flow.create_flow(self.flows[msisdn], StringUtils.camelize(self.flows[msisdn])).menu()         
        else:
            self.run()

simulator=Simulator({'#123#': 'bank_flow', '#234#': "calculator_flow"})
Simulator.run(simulator)