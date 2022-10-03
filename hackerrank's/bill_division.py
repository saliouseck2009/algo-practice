def bon_appetit(bill, k, b):
    shared_item=sum(bill)-bill[k]
    item_to_pay = shared_item//2
    if item_to_pay == b :
        print ("Bon Appetit")
    else: 
        print (b-item_to_pay)