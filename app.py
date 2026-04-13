
item_bakery = [
    {
    "name": "very good cookies", 
    "price": float("7.50"), 
    "description": "definetly perfect cookies"
    },

    {"name": "fanastic cake", 
    "price": int("50"), 
    "description": "this will end better than cookies"
    },

    {"name": "bread", 
    "price": int("2"), 
    "description": "very good bread"
    },

    {
    "name": "cereal",
    "price": int("1"),
    "description": "very cool"
    }
    ]
receipt = []

price = []

for index, item in enumerate(item_bakery):
    print(index, ":", item["name"])

item = int(input("What would you like? "))

if isinstance(item, int):
    print(item_bakery[item]["name"])
    price.append(item_bakery [item]["price"])
    receipt.append(item_bakery [item]["name"])

else:
    print("We don't have that here")
    
more = input("Would you like to continue purchasing? ")

while more == "yes":

    item = int(input("What would else would you like? "))

    if isinstance(item, int):

        print(item_bakery[item]["name"])
        price.append(item_bakery [item]["price"])
        receipt.append(item_bakery [item]["name"])
        more = input("Would you like to continue purchasing? ")

    elif more == "no":
        break

    else: 

        print("We don't have that here")
        more = input("Would you like to continue purchasing? ")

exit = input("Thank you for purchasing our items. Would you like an receipt ")

if exit == "yes": 
    for index, item in enumerate(receipt):
        print(index, ":", item)
    print(f"Your total is ${sum(price)}0")
