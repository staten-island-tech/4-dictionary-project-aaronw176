
item_bakery = [
    {
    "name": "very good cookies", 
    "price": "1.50", 
    "description": "definetly perfect cookies"
    },
    {"name": "fanastic cake", 
    "price": "50", 
    "description": "this will end better than cookies"},

    {"name": "pboy", 
    "price": "free", 
    "description": "he will make very good cookies"
}
]


for index, item in enumerate(item_bakery):
    print(index, ":", item["name"])

item = int(input("What would you like? "))

if item == ":
    print(item_bakery [0]["name"])
elif item == "cake":
    print(item_bakery [1]["name"] )
elif item == "devil":
    print(item_bakery [2] ["name"])
else:
    print("We don't have that here")