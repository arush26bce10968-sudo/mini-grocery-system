from numpy import *   
item = ('bread','butter','cheese','chicken','chips','candy','toothpaste','kurkure')   
print(">>>>>>>  ITEM PRICES  <<<<<<<")  
list=('1. bread = 20 RS.','2. butter = 50 RS.','3. cheese = 80 RS.','4. chicken = 300 RS.','5. chips = 10 RS.','6. candy = 5 RS.','7. toothpast = 40 RS.','8. kurkure = 20 RS.')  
for lis in list:      
    print(lis)  

print(">>>>>>>>>>  LIST OF ITEM PURCHASED  <<<<<<<<<<<")  
print()  
p=input()  
l1=array(p.split( ), str)  

print(">>>>>>>>>>  ENTER QUANTITY OF ITEM PURCHASED  <<<<<<<<<<<")  
print()  
q=input()  
l2=array(q.split( ), int)  
print()
print(">>>>>>>>>>  DO YOU WANT TO ADD ITEM?  <<<<<<<<<<<")
add=input()

if add.lower()=="yes":
    add_item=input("ENTER ITEM TO ADD: ")
    add_quantity=int(input("ENTER QUANTITY: "))

    l1=l1.tolist()
    l2=l2.tolist()

    l1.append(add_item)
    l2.append(add_quantity)

    l1=array(l1,str)
    l2=array(l2,int)
print()
print(">>>>>>>>>>  DO YOU WANT TO REMOVE ITEM?  <<<<<<<<<<<")
remove=input()

if remove.lower()=="yes":
    remove_item=input("ENTER ITEM TO REMOVE: ")

    l1=l1.tolist()
    l2=l2.tolist()

    if remove_item in l1:
        position=l1.index(remove_item)
        l1.pop(position)
        l2.pop(position)
        print("ITEM REMOVED SUCCESSFULLY")
    else:
        print("ITEM NOT FOUND")

    l1=array(l1,str)
    l2=array(l2,int)


a=0  
l3=array([20, 50, 300], int)  
l4=array((),str)  

print(">>>>>>>>>  ENTER NUMBER OF ITEM SPECIFIC COUPON CODES  <<<<<<<<")  
d=int(input())  
j=0  

if d!=0:  
    for j in range (0,d+1):  
        print(">>>>>>   ENTER ITEM SPECIFIC COUPON CODE IF ANY   <<<<<<")  
        c=input()  
        l4.append(c)  

for k in l4:  
    if k.lower=='riseup':  
        l3[1]=l3[1]/2  
    elif k.lower=='clockadoodledo':  
        l3[6]=(l3[6]/3)*2  
    elif k.lower=='smoothlike':  
        l3[2]=(l3[2]/3)*2  

i=-1  

for m in l1:  
    i=i+1  
    a= a + l3[i]  

    if m.lower=='bread':  
        a= a + l3[0] * l2[i]  
    elif m.lower=='butter':  
        a= a + l3[1] * l2[i]  
    elif m.lower=='cheese':  
        a= a + 80 * l2[i]  
    elif m.lower=='egg':  
        a= a + 18 * l2[i]  
    elif m.lower=='chips':  
        a= a + 10 * l2[i]  
    elif m.lower=='chicken':  
        a= a + l3[2] * l2[i]  
    elif m.lower=='candy':  
        a= a + 5 * l2[i]  
    elif m.lower=='toothpaste':  
        a= a + 40 * l2[i]  
    elif m.lower=='kurkure':  
         a= a + 20 * l2[i]  


print(">>>>>>>>   TO GET COUPON ENTER YOUR PHONE NUMBER    <<<<<<<< ")  
num=input()  

if len(num)==10:  
    print(">>>>>>>>>   YOUR COUPON CODE   <<<<<<<<<")  
    print("                   🡇")  
    print("               MONEYHEIST")  
else:  
    print("      Invalid Number >>> No Coupon For You        ")  

print()  
print(">>>>>>>>  ENTER COUPON CODE IF ANY  <<<<<<<<")  
print()  
t=input("                     ")  
h=array(t.split( ))  

for g in h:  
    if g.lower=='money':  
        a=a*0.7  
    elif g.lower=='moneyheist':  
        a=a*0.8  
    elif g.lower=='father':  
        a=a*0.6  

a1=a*0.05+a  

for y in range (0,len(l1)):  
    print(l1[y],'➔',l2[y])  

print()  
print()  
print()  

print(f"The Total price before tax = {a} ")  
print("The Grand Total = ",a1)  
print("----------------------- Thank you for purchase -----------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
