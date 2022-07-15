# 샘플 Python 스크립트입니다.

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
import Menu
import Order
import Sales

if __name__ == '__main__':
    menu = Menu.Menu()
    sale = Sales.Sales()
    sch=input('작업을 선택하시오 [m:메뉴목록, o:주문입력, s:매출조회, x:프로그램종료]\n')
    while sch!='x':
        if sch=='m':
            menu.display()
        elif sch=='o':
            order = Order.Order()
            menu.display()
            m_no=int(input('메뉴번호를 입력하시오 [0:주문완료]'))
            while m_no!=0:
                m_no-=1  # menu_no -> index로 변환
                qty=int(input('수량을 입력하시오'))
                price=menu.price[m_no]*qty
                order.add(m_no,qty,price)
                #print(menu.name[m_no]," x",str(qty),"=",price)
                menu.display()
                m_no = int(input('메뉴번호를 입력하시오 [0:주문완료]'))
            if len(order.menu_no)!=0:
                mobile=input('모바일번호를 입력하시오.')
                if mobile=="-1":
                    order.cancel()
                if len(order.menu_no)!=0:
                    order.display(menu)
                    sale.add(mobile,order)
        elif sch=='s':
            sale.display()
        sch = input('작업을 선택하시오 [m:메뉴목록, o:주문입력, s:매출조회, x:프로그램종료]\n')
    # 작업선택 안내
    # 'x'가 아닌 동안
    # 'm': 메뉴목록 보여주기
    #    - menu.display()
    # 'o': 주문입력
    #    - 메뉴번호 입력
    #    - 메뉴번호가 0이 아닌 동안 반복
    #    -    수량
    #    -     새메뉴번호 입력
    #    - 주문내역 보여주고, 모바일번호 입력대기
    #    - 모바일번호가 -1이면, 주문 취소
    #    - 그렇지않으면, 매출에 추가.
    # 's': 매출목록 & 매출총액 보여주기


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
    # print_hi('PyCharm')

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
