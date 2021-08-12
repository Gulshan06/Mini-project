import csv,smtplib,time,logging,pymongo
import validation as v
# try:
client = pymongo.MongoClient("mongodb+srv://Gulshan06:Gullu2132@cluster0.8ikox.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydatabase= client['miniprojectDb']
Collection_name =mydatabase['products']
Collection_name1=mydatabase['Bill']   
header = ["_id","productname","discription","price","manufacturer","manufacturingdate","expirydate","AddOn"]
productlist=[]
class ProductDetails:
    def addproductdetails(self,productname,discription,price,manufacturer,manufacturingdate,expirydate):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"productname":productname,"discription":discription,"price":price,"manufacturer":manufacturer,"manufacturingdate":manufacturingdate,"expirydate":expirydate,'AddOn':current_time}
        productlist.append(dict1)
obj1=ProductDetails()
while(True):
    print("1.Add Products")
    print("2.View all products details")
    print("3.Customer service")
    print("4.List all the products that expired")
    print("5.Search the item by name")
    print("6.For CSV file")
    print("7.For Delete the data ")
    print("8.For update the data ")
    print("9.For All customer bill  ")
    print("10.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        productname=input("enter the product name - ")
        discription=input("enter the description of product - ")
        price=input("enter the price of product  - ")
        manufacturer=input("enter the manufacturer company name - ")
        manufacturingdate=input("enter product manufacturing date in mm-dd-yyyy format - ")
        expirydate=input("enter the expiry date in mm-dd-yyyy format - ")
        obj1.addproductdetails(productname,discription,v.val_price(price),manufacturer,manufacturingdate,expirydate)
        result = Collection_name.insert_many(productlist)
        print(result.inserted_ids)
    elif(choice==2):
        # print(productlist)
        result = Collection_name.find()
        l=[]
        for i in result:
            l.append(i)
        print(l)
    elif(choice==3):
        name= input("enter your name")
        emailid = input('enter your emailid')
        result = Collection_name.find()
        total_product = []
        final_total=0
        bill ={}
        for i in result:
            print('product name - ',i['productname'] ,' price of product - ',i['price'])
            a = int(input('if you want enter the number of Quntity (0 if you don\'t want)  -  '))
            bill["productname"]= i['productname']
            bill["price"]= i['price']
            bill["no_of_product"]= a
            total = i['price']*a
            final_total += total 
            print(bill)
            total_product.append(bill)
        print('customer name - ',v.val_name(name))
        print('customer emailid - ',v.val_emailid(emailid))
        print('your toatal amount is - ', final_total)
        def dis(final_total):
            discount = 0
            if (final_total<500):
                discount=final_total
                return discount
            else:
                if (final_total > 500 and final_total <=1000):
                    f = (final_total/100)*10
                    discount = final_total - f
                    return discount
                elif (final_total >1000 and final_total <=2000):
                    f = (final_total/100)*20
                    discount = final_total - f
                    return discount
                elif (final_total >2000 and final_total <=3000):
                    f = (final_total/100)*30
                    discount = final_total - f
                    return discount
                elif (final_total >3000 and final_total <=4000):
                    f = (final_total/100)*40
                    discount = final_total - f
                    return discount
                elif (final_total >4000):
                    f = (final_total/100)*50
                    discount = final_total - f
                    return discount
        print('your total amount after discount is - ',dis(final_total))
        print(total_product)
        result1 = Collection_name1.insert_many(total_product)
        print(result1.inserted_ids)
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("gulshan062132@gmail.com","Gullu@2132")
        message='your total amount is - '+str(dis(final_total))
        connection.sendmail("gulshan062132@gmail.com",emailid, message)
        print("Message sended successful")
        connection.quit()
    elif(choice == 4):
        print("list all the products that expire  - ")
        result = Collection_name.find()
        current_date=time.strftime("%m-%d-%Y-",time.localtime())
        expired=(list(filter(lambda i:i["expirydate"]<str(current_date),result)))    
        if len(expired)>0:
            print(expired)
        else:
            print("No Expired product found")
    elif(choice == 5):
        a = input('enter the product name')
        result = Collection_name.find({"productname":a})
        l = []
        for i in result:
            l.append(i)
        print(l)
    elif(choice == 6):
        result=Collection_name.find()
        with open('Mongo_Product.csv','w+',encoding='UTF8',newline='') as s:
                writer = csv.DictWriter(s,fieldnames=header)
                writer.writeheader()
                writer.writerows(result) 
                print("file created successfuly") 
    elif(choice==7):
        b = input('enter the product name')
        result=Collection_name.delete_one({'productname':b})
        # print(result.deleted_count)
        if result==0:
            print("Nothing deleted")
        else:
            print(result.deleted_count," item deleted")
    elif(choice==8):
        updatename=input("enter product name that you want to update")
        updateprice= int(input('enter the updated price'))
        result=Collection_name.update_one({'productname':updatename},{"$set":{"price":updateprice}})
        print("your data is updated")
    elif(choice==9):
        result1=Collection_name1.find()
        for i in result1:
            print(i)
    elif(choice==10):
        break
# except Exception:
#     logging.error("Something went wrong")
# else:
#     print("Your program completed Successfully")
# finally:
#     print("Thank You!!")

