fridge = {
    "name": "fridge",
    "brand": "Unknow",
    "foods": ["cheese", "bread", "meat"],
    "2_type": ["freezer", "firdge"],
    "freezer": {
        "foods": ["ice_cream", "ice"]
    }
}


for i in fridge:
    print(i)

for i in fridge.values():
    print(i)

for i, j in fridge.items():
    print(f"{i} : {j}")
