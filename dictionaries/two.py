car_variety  = {
    "BMW" : "1cr",
    "Audi" : "80L",
    "Porche" : "2cr"
}

car_variety["Ferrari"] = "50L"

car_variety.pop("Ferrari")

# car_variety.popitem() # remove the last(by time) added item

# del car_variety["Audi"] # del the reference from memory

# car_variety_copy = car_variety.copy()


squared_nums = {
    x : x**2 for x in range(1, 10)
}

# squared_nums.clear() # clear the dictionary

keys = ["Dubai", "Singapore", "Switzerland"]

default_value = "Best"

new_dict = dict.fromkeys(keys, default_value)