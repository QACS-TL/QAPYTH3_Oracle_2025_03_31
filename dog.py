from animal import Animal
class Dog(Animal):
     def __init__(self, name, limb_count=4, tail_length=30):
         super().__init__(name, limb_count)
         self.tail_length = tail_length

     def wagtail(self, number_of_wags):
         return f"I'm a dog waging my {self.tail_length}cm long tail {number_of_wags} times"

     def eat(self, food):
         return f"I'm a DOG droolingover a {food}. {super().eat(food)}"