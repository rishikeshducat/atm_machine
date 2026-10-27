class atm:
    def __init__(self):
        self.amount=10000
        self.pin=1234
        print('welcome to atm machine')
    def card_insert(self):
        user_card=input('insert your card')
        if user_card=='card':
            print('card inserted')
            ob.enter_pin()
        else:
            print('invalid card')
    def enter_pin(self):
        user_pin=int(input('enter the pin'))
        if user_pin==self.pin:
            print('pin correct')
            print('1)check balance\n2)withdraw')
            user_selection=int(input('select the option'))
            if user_selection==1:
                ob.check_balance()
            elif user_selection==2:
                ob.withdraw()
            else:
                print('invalid selection')

        else:
            print('invalid pin')
    def check_balance(self):
        print('your balance is  ',self.amount)
    def withdraw(self):
        user_amount=int(input('enter the amount'))
        print('your balance is ',self.amount-user_amount)
ob=atm()
ob.card_insert()

    
