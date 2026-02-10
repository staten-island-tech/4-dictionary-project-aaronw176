
item_bakery = {
    "name": "very good cookies", "price": "1.50", "description": "definetly perfect cookies",

    "name": "fanastic cake", "price": "50", "description": "this will end better than cookies",

    "name": "cayley", "price": "free", "description": "she will make very good cookies"

}
item = input("What would you like? ")

if item == "cookies":
    print(item_bakery[0] ["name"] )
elif item == "cake":
    print(item_bakery[1] ["name"] )
elif item == "devil":
    print(item_bakery[] ["name"] )
else:
    print("We don't have that here")
