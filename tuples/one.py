# list is mutable so we need same data structure than can be immutable and work like list

car_types = ("SUV", "Sedan", "Electric")

print(car_types[0])
# car_types[0] = "SUV" #error
print(car_types)

more_car_types = ("Hatchback")

all_car_types = car_types + more_car_types

car_types.count("SUV")

(suv, sedan, ev) = car_types
# first three are variable in which values are assigned from tuple and should have equal variable = len(tuple)