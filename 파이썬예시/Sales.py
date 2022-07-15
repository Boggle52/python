import Order

from datetime import datetime

class Sales:
    def __init__(self):
        self.mobile=[]
        self.total=[]
        self.created=[]

    def add(self,mobile,order):
        today=datetime.today()
        now=today.strftime("%Y-%m-%d %H:%M")
        self.created.append(now)
        self.mobile.append(mobile)
        total=0
        for price in order.price:
            total+=price
        self.total.append(total)

    def getSum(self):
        # 매출목록 보여주고
        # 매출총액계산/출력
        pass
    def display(self):
        sales_total=0
        for i in range(len(self.mobile)):
            print(self.mobile[i],", ",self.total[i],", ",self.created[i])
            sales_total+=self.total[i]
        print("총매출합계:"+str(sales_total))