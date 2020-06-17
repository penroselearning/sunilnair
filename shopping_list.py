shopping_list = []

def shopping_cart(item):
    global shopping_list
    
    shopping_list.append(item)
    
    return shopping_list 
    
def shopping_cart_remove(item):
    global shopping_list
    shopping_list.remove(item)
    return shopping_list
