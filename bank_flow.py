from flow import Flow
class BankFlow:
    operations = {'1': 'balance_inquiry', '2': "mini_statement", "3":"funds_transfer", "4": "bill_payments"}

    def menu(self):
      self.input =  input("1. Balance Inquiry \n2. Mini Statement \n3. Funds Transfer \n4. Bill Payments \n5. Cheque Functions \n6. Other Services\n")
      if self.input in self.operations :
          flow = Flow()
          flow.do(self.operations, self.input)            
          
      else:
          print("Wrong Selection: \n")
          self.menu()
