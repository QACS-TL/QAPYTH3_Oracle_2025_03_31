import animal
import dog

ani1 = animal.Animal("Fido",  8, "Purple")
#ani1.name = "Fido"
#ani1.colour = "Black"
#ani1.limb_count = 3
#ani1._health = 30

ani2 = animal.Animal("Rover")
#ani2.name = "Rover"
#ani2.colour = "White"
ani2.limb_count = -1
# ani2._limb_count = -10

dog1 = dog.Dog("Fifi")
print(dog1.eat("bone"))

animals = []
animals.append(ani1)
animals.append(ani2)
animals.append(dog1)

for ani in animals:
    print(f"Limb count is {ani.limb_count}")
    print(ani.eat("Cheese"))
