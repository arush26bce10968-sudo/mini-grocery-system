# mini-grocery-system
       Simple Grocery Billing System

            Introduction 

This is a simple Python project made for a basic grocery billing system.
The program lets the user enter the items they bought and their
quantities, add or remove items, use coupons, and finally calculate the
total bill.

The project is mainly made for practicing basic Python concepts and
understanding how they can be used in a small real-life type
application.

           [ What the Program Can Do ]

The program has the following main features:

1- Shows the available grocery items and their prices.
2- Takes the purchased items from the user.
3- Takes the quantity of each item.
4- Allows the user to add another item.
5- Allows the user to remove an item.
6- Supports item-specific coupon codes.
7- Generates a coupon code when a valid 10-digit phone number is
    entered.
8- Accepts general discount coupons.
9-  Adds 5% tax to the bill.
10- Shows the final list of purchased items and their quantities.

               Grocery Items and Prices

The current program uses these items:

  No.   Item           Price
    
  1     Bread           20
  2     Butter          50
  3     Cheese          80
  4     Chicken         300
  5     Chips           10
  6     Candy           5
  7     Toothpaste      40
  8     Kurkure         20

                Entering Purchased Items

First, the user enters the names of the items they want to purchase.

For example:

``` text
bread butter cheese
```

These item names are stored in a NumPy array.

After that, the user enters the quantity of each item. For example:

   text

   2 1 3

Here, the quantities match the items entered above.


                      Adding an Item


The program asks whether the user wants to add another item.
                      
                     text

          DO YOU WANT TO ADD ITEM?


If the user enters ' yes ', they are asked for the item name and its
quantity.

For example:
 
ENTER ITEM TO ADD: chips
ENTER QUANTITY: 2

The arrays are converted into normal Python lists temporarily so that
the new item and quantity can be added. After adding them, they are
converted back into NumPy arrays.


                   Removing an item
                   


The user can also remove an item that they have already entered.

The program asks for the item name and checks whether it is present. If
it is found, the program removes both the item and its corresponding
quantity.

The basic steps are:

1-  Enter the item to remove.
2-  Check whether the item is present.
3-  Find its position.
4-  Remove the item.
5-  Remove its quantity from the same position.

If the item is not found, the program displays:

ITEM NOT FOUND


                Item-Specific Coupons


The program also contains some item-specific coupon codes.

  Coupon Code        Intended Use
   
  riseup           Butter
  clockadoodledo   Chicken
  smoothlike       Cheese

These coupons are intended to reduce the price of the related item.


                   Calculating the Item Price


The basic calculation used for an item is:

Item Price × Quantity

For example, if the quantity of bread is 2:

₹20 × 2 = ₹40

The cost of the purchased items is then added together to get the total
amount before the final tax calculation.


                  Phone Number Coupon


The program asks the user for a phone number:

TO GET COUPON ENTER YOUR PHONE NUMBER

If the entered value has exactly 10 characters, the program displays the
coupon:

MONEYHEIST

Otherwise, it displays a message saying that no coupon is available.


                    General Coupon Codes


The program also accepts these general coupon codes:

  Coupon Code      Discount
 
  money               30%
  moneyheist          20%
  father              40%

The user can enter the coupon code at the end of the purchase process.


                       Tax Calculation


After calculating the total, the program adds 5% tax.

The calculation is:

Grand Total = Total Price + 5% Tax

The code used for this is:

a1 = a * 0.05 + a


                          Final Bill


At the end, the program prints the purchased items along with their
quantities.

It then shows:

The Total price before tax
The Grand Total

Finally, it displays a thank-you message for the purchase.


                          Requirements


To run this project, you need:

 1- Python 3.x
 2- NumPy

NumPy can be installed using:

1- pip install numpy


                    How to Run the Program


1- Save the Python code in a file named:

grocery_system.py

2- Open Command Prompt or a terminal in the same folder.

3- Run the program using:
python grocery_system.py

4- Enter the information whenever the program asks for it.

     
                      Example Input


For example, the user can enter:

bread butter cheese

For quantities:
2 1 1
If they want to add another item:

yes

Then:

chips

and:

3


If they do not want to remove an item:

no

                     Project Structure

The project can be kept simple with these two files:

Grocery-Billing-System/
│
├── grocery_system.py
└── README.md


                 Python Concepts Used


This project uses several basic Python concepts.


                 NumPy Arrays


The entered items and quantities are stored in arrays:

l1 = array(p.split(), str)
l2 = array(q.split(), int)


                 Taking Input

The input() function is used to take information from the user:

p = input()

              If-Else Statements


The program uses conditions to make decisions. For example:


if add.lower() == "yes":
    ...


               For Loops


Loops are used to go through the items:

for m in l1:
    ...


           Converting Arrays to Lists 


When an item needs to be added or removed, the arrays are converted to
lists:

l1 = l1.tolist()
l2 = l2.tolist()


             Adding Items


The append() function is used to add new values:

l1.append(add_item)
l2.append(add_quantity)


            Removing Items


The pop() function is used to remove an item at a particular position:

l1.pop(position)
l2.pop(position)


            Important Points About the Current Code


The supplied program has a few coding issues that should be fixed if it
is going to be used as a fully working billing system.

For example, the code currently has:

if m.lower == 'bread':


Here, 'lower'is being referred to without calling it. It should be:

if m.lower() == 'bread':

The same issue occurs in the coupon checks. For example:

if k.lower == 'riseup':

should be:

if k.lower() == 'riseup':

There is also an issue with l3. It is created with only three values:


l3 = array([20, 50, 300], int)

but the program later tries to access indexes such as l3[3] and
l3[6]. The price array needs to be set up correctly before those parts
can work.

Another thing to keep in mind is the use of list as a variable name:

list = (...)

list is already a built-in Python function. It would be better to use
a name such as:

item_list = (...)


This avoids problems when the list() function is needed later. 


                  Ideas for Improving the Project


The project can be developed further by adding features such as:

1- Better input checking.
2- Automatic price selection.
3-  Stock or available-quantity management.
4-  A proper printed receipt.
5-  GST/tax details on the bill.
6-  More coupon options.
7-  Coupon expiry dates.
8-  Different payment methods.
9-  A simple GUI.
10- Saving the bill to a file.
11- Separate functions for adding items, removing items, calculating the
12- bill, and handling coupons.


                       Learning Purpose


This project is useful for beginners who are learning Python, especially
for basic BTech CSE programming practice.

It brings together simple concepts such as arrays, lists, loops,
conditions, strings, user input, and arithmetic calculations in one
small project.

                       License

This project is made for educational and learning purposes.

