#Food counter program
menu={ 'Popcorn':180,
       "Coke":60,
       "Samosa":45,
       "Ice cream":70,
       "Pizza":300
       }
cart=[]
total=0
print("-----------------MENU-------------")
for key,value in menu.items():
    print(f'{key:10}: ₹{value}')
print("----------------------------------")
while True:
    food =input("Select an item (Type 'Exit' To Quit):").capitalize()
    if food=='Exit':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------YOUR ORDER-----------")

for food in cart:
    total+=menu.get(food)
    print(food,end=' ')
print()
print(f"Total: {total}")

print("-------------------------------")
