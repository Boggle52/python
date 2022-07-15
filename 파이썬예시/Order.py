class Order:
    def __init__(self):
        self.cancel()

    def add(self,menu_no,qty,price):
        self.menu_no.append(menu_no)
        self.qty.append(qty)
        self.price.append(price)

    def cancel(self):
        self.menu_no=[]
        self.qty=[]
        self.price=[]

    def display(self,menu):
        print('----------------------------------')
        for i in range(len(self.menu_no)):
            print(menu.name[self.menu_no[i]],", x",self.qty[i],"=",self.price[i])
        print('----------------------------------')

