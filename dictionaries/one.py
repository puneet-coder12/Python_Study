car_variety  = {
    "BMW" : "1cr",
    "AUdi" : "80L",
    "Porche" : "2cr"
}

# print(car_variety["BMW"])
# print(car_variety.get("Porche"))

car_variety["BMW"] = "4cr"

for car in car_variety:
    print(car, end = " : ")
    print(car_variety[car]) 

for key, value in car_variety.items():
    print(key, value)
    
if("BMW" in car_variety):
    print("I have BMW")

print(len(car_variety))