car = {
    101: {
        "brand": "Toyota",
        "model": ["mod1", "mod2", "mod3"],
        "price": [10000, 20000, 30000]
    }
}

for key, value in car.items():
    for i in range(len(value["model"])):
        if i ==1:
         print(value["model"][i], value["price"][i])