orders={}
bill = 0
def update_order(menu,cookie,qty):
    global orders,bill
    
    orders[cookie] = qty * [price for (c,price) in menu.items() if c==cookie][0]
    bill += orders[cookie]
    return orders,bill

def remove_order(cookie):
    global orders
    orders.pop(cookie)
    return orders