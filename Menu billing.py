print("Welcome to Master Cafe 🥘")
name = input("Please Enter Your Name:")
menu = {"Burger": 60,
        "Pizza": 120,
        "Fries": 50
  }
  
print(f"""Hello {name.capitalize()}, please choose your order
Here is our menu:
A. Burger 🍔 
B. Pizza 🍕 
C. Fries 🍟""")
item1 = input("Choose your first order:")
item2 = input("Choose your second order:")

odr1 = item1.capitalize()
odr2 = item2.capitalize()

if odr1 in menu and odr2 in menu:
  if odr1 != odr2:
    print(f"Good choice, you have ordered a {odr1} and a {odr2}")
    bill =(
      f"Here is your bill:\n"
      f"{odr1} is just ₹{menu[odr1]}\n"
      f"{odr2} is just ₹{menu[odr2]}\n\n"
      f"Total ={menu[odr1]+menu[odr2]}\n"
      
      )
    print(bill)
    if (menu[odr1]+menu[odr2]) > 150:
      print(f"Congratulations 👏 You just win a free Icecream 🍦 ")
  if odr1 == odr2:
    print(f"Good choice, you have ordered two {odr1}")
    bill =(
      f"Here is your bill:\n"
      f"Two {odr1} is just ₹{menu[odr1]} x 2\n\n"
      f"Total ={(menu[odr1]+menu[odr2])*0.9} (Special discount for you 😉)\n"
      )
    print(bill)
    if (menu[odr1]+menu[odr2])*0.9 > 150:
      print(f"Congratulations 👏 You just win a free Icecream 🍦 ")

if odr1 in menu and odr2 not in menu:
    print(f"sorry, {odr1} is available, but {odr2} is not available here.")
if odr2 in menu and odr1 not in menu:
    print(f"sorry, {odr2} is available, but {odr1} is not available here.")
if odr1 not in menu and odr2 not in menu:
    print(f"sorry, {odr1} and {odr2} both are not available here.")

print(f"Thank you, {name} 🙃" )