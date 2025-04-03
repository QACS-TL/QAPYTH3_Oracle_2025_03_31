import animal

ani1 = animal.Animal("Fido",  8, "Purple")
#ani1.name = "Fido"
#ani1.colour = "Black"
#ani1.limb_count = 3
#ani1._health = 30

ani2 = animal.Animal("Rover")
#ani2.name = "Rover"
#ani2.colour = "White"
ani2.limb_count = 5

animals = []
animals.append(ani1)
animals.append(ani2)

for ani in animals:
    print(ani)
    print(ani.eat("Cheese"))
