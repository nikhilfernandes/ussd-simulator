from flow import Flow
class BankFlow:
    operations = {'1': 'balance_inquiry', '2': "mini_statement", "3":"funds_transfer"}

    def menu(self):
      self.input =  input("1. Balance Inquiry \n2. Mini Statement \n3. Funds Transfer \n9. Exit \n")
      flow = Flow()
      flow.do(self.operations, self.input, "bank_flow")
