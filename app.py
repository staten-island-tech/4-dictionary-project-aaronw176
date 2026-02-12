
item_bakery = [
    {
    "name": "very good cookies", 
    "price": float("7.50"), 
    "description": "definetly perfect cookies"
    },
    {"name": "fanastic cake", 
    "price": int("50"), 
    "description": "this will end better than cookies"},

    {"name": "pboy", 
    "price": int("0"), 
    "description": "he will make very good cookies"
}
{
    "name": "cayley",
    "price": int("1")
    "description": "she is a cereal killer you might not want this..."
    }
]
receipt = [
]
price = []

for index, item in enumerate(item_bakery):
    print(index, ":", item["name"])

item = int(input("What would you like? "))

if item == 0 :
    print(item_bakery [0]["name"])
    receipt.append(item_bakery [0]["name"])
    price.append(item_bakery [0]["price"])
elif item == 1 :
    print(item_bakery [1]["name"] )
    receipt.append(item_bakery [1]["name"])
    price.append(item_bakery [1]["price"])
elif item == 2 :
    print(item_bakery [2] ["name"])
    receipt.append(item_bakery [2]["name"])
    price.append(item_bakery [2]["price"])
else:
    print("We don't have that here")

more = input("Would you like to continue purchasing? ")
while more == "yes":
    item = int(input("What would else would you like? "))
    if item == 0 :
        print(item_bakery [0]["name"])
        receipt.append(item_bakery [0]["name"])
        price.append(item_bakery [0]["price"])
    elif item == 1 :
        print(item_bakery [1]["name"] )
        receipt.append(item_bakery [1]["name"])
        price.append(item_bakery [1]["price"])
    elif item == 2 :
        print(item_bakery [2] ["name"])
        receipt.append(item_bakery [2]["name"])
        price.append(item_bakery [2]["price"])
    else:
        print("We don't have that here")
    more = input("Would you like to continue purchasing? ")
exit = input("Thank you for purchasing our items. Would you like an receipt ")
if exit == "yes": 
    for index, item in enumerate(receipt):
        print(index, ":", item)
    print(f"Your total is ${sum(price)}")
        
