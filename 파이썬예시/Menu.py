class Menu:
    def __init__(self):
        self.name=[]
        self.price=[]
        f=open("d:/temp/menu.txt",mode="r",encoding="utf-8")
        lines=f.readlines()
        for line in lines:
            ar=line.split(',')
            self.name.append(ar[0])
            self.price.append(int(ar[1]))
        f.close()

    def display(self):
        for i in range(len(self.name)):
            print(i+1," ",self.name[i],", ",self.price[i])

    def addnew(self,name,price):
        self.name.append(name)
        self.price.append(price)
        self.save()
    def update(self,ndx, name, price):
        self.name[ndx]=name
        self.price[ndx]=price
        self.save()

    def delete(self,ndx):
        del self.name[ndx]
        del self.price[ndx]
        self.save()

    def save(self):
        f=open("d:/temp/menu.txt",mode="w",encoding="utf-8")
        for i in range(len(self.name)):
            f.write(self.name[i]+","+str(self.price[i])+"\n")
        f.close()