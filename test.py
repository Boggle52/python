"""
i=10
type(i)
<class 'int'>
i=2.14
type(i)
<class 'float'>
i="Hello"
type(i)
<class 'str'>

i=3
a="Hello"*3
print(a)
HelloHelloHello

print("star"*5)
starstarstarstarstar

total=2+\
        3*4
print(total)
14

i="Hello World"
print(i[0:5])
Hello
Hello
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Hello
NameError: name 'Hello' is not defined
i="abcdefg"
print(i[2:4])
cd
cd
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    cd
NameError: name 'cd' is not defined. Did you mean: 'id'?
i="Good Morning Vietnam"
print(i[:6])
Good M
print(i[2:])
od Morning Vietnam

i = 5
if i >= 10:
    print("10보다 큽니다.")
else:
    print("10보다 작습니다.")

s = input('값을 입력하시오\n')
i = int(s)
if i > 0:
    print("i는 양의 정수입니다.")
elif i < 0:
    print("i는 0이거나 음의 정수입니다.")
else:
    print("i는 0입니다.")

x = input('값을 입력하시오.\n')
x = int(x)
i = 0
while i < x:
    print(i)
    i = i+1

x = input('값을 입력하시오.\n')
x = int(x)
i = 2
while i < 10:
    #    print(x, 'x', i, '=', x*i, '\n')
    print(f"{x}x{i}={x * i}")
    i = i + 1

i = 1
while i < 100:
    if i % 2 == 1:
        print(i)
    i = i+1

i = 1
while i < 100:
    print(i)
    i = i+2

x = 2
i = 1
while x < 10:

    while i < 10:
        print(f"{x}x{i}={x * i}")
        i += 1

    x += 1
    i = 1

for i in range(1, 10, 2):
    print(i)

for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print(f"{i}x{j}={i*j}")

i = 1
total = 0
while i < 100:
    if i % 2 != 0 and i % 3 != 0:
        print(i)
        total += i
    i += 1
print("total=", total)

for i in range(0, 10, 1):
    print('$'*i)
for i in range(10, 0, -1):
    print('$'*i)

for i in range(2, 1000):
    if i == 2:
        print(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1 and i % j != 0:
                print(i)

for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

x = int(input('값을 입력하시오.\n'))
y = int(input())
gcd = 1
lcm = 1
if x > y:
    x, y = y, x
for i in range(x, 1, -1):
    if x % i == 0 and y % i == 0:
        x = x//i
        y = y//i
        gcd = i
        break
else:
    print("최대공약수가 없습니다.")
lcm = gcd * x * y
print("최대공약수:", gcd, "최소공배수:", lcm)

a = []
for i in range(0, 10):
    score = input('점수를 입력하시오.\n')
    a.insert(i, score)
for v in a:
    print(v)

score = {'이름': [], '영어': [], '수학': [], '국어': []}
engTotal, mathTotal, korTotal = 0, 0, 0
for i in range(0, 1):
    name = input('이름: ')
    eng = int(input('영어: '))
    math = int(input('수학: '))
    kor = int(input('국어: '))
    score['이름'].append(name)
    score['영어'].append(eng)
    score['수학'].append(math)
    score['국어'].append(kor)
    engTotal += eng
    mathTotal += math
    korTotal += kor
print('영어\n총점:', engTotal, '\n평균:', engTotal/len(score['이름']),
      '\n수학\n총점:', mathTotal, '\n평균:', mathTotal/len(score['이름']),
      '\n국어\n총점:', korTotal, '\n평균:', korTotal/len(score['이름']))
print('영어')
print('총점:', engTotal)
print('평균:', engTotal....)
print(score)

menuList = []
while True:
    name = input('메뉴명: ')
    if name == "":
        break
    price = int(input('가격: '))
    menu = dict(name=name, price=price)
    menuList.append(menu)
#   print(menuList)
for x in menuList:
    print(x['name'], '=', x['price'])



def accum(n):
    if n == 1:
        return 1
    else:
        return n + accum(n-1)



def accum(n):
    return n + accum(n-1) if n > 1 else 1


print(accum(101))

import calendar
print(calendar.firstweekday())
wd = ['월', '화', '수', '목', '금', '토', '일']
print(wd[calendar.weekday(1996, 10, 16)])

import pack.mymod1

pack.mymod1.listhap(1, 2)
pack.mymod1.kbs()

from pack import mymod1
mymod1.mbc()

from pack.mymod1 import *
mbc()
kbs()

import mymod3
print(mymod3.multi(5, 3))

import sys
sys.path.append(r'C:/Users/admin/Desktop/업로드')
import mymod4
print(mymod4.div(6, 3))

from turtle import *
p = Pen()
p.color('red', 'yellow')
p.pendown()
p.begin_fill()

while True:
    p.forward(300)
    p.left(179)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()

f = open('C:/Users/admin/Desktop/ss.txt', mode='r', encoding='utf-8')
lines = f.readlines()
for row in lines:
    ar = row.split(', ')
    print('메뉴명=', ar[0], ',', '가격=', ar[1], end='')
f.close()

f = open('C:/Users/admin/Desktop/ss.txt', mode='a', encoding='utf-8')
f.writelines("어펜드5")
f.writelines("어펜드6")
f.close()
"""

