import re
def val_price(price):
    v=re.search("^[1-9]",price)
    if v:
        return int(price)
    else:
        print('something went wrong - you enter wrong Name')
        print("Please enter 7 and again fill the data")


def val_name(name):
    val1=re.search('^[A-Za-z]',name)
    if val1:
        return name
    else:
        print('something went wrong - you enter wrong Name')
        print("Please enter 7 and again fill the data")


def val_emailid(emailid):
    val6=re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',emailid)
    if val6:
        return emailid
    else:
        print('something went wrong - you enter wrong emailid')
        print("Please enter 7 and again fill the data")


