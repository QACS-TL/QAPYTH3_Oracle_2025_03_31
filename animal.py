class Animal:
    #name = ""
    #limb_count = 0
    #colour = ""
    #_health = 0

    def __init__(self, name, limb_count=4, colour="Brown"):
        self.name = name
        self.limb_count = limb_count
        self.colour = colour
        self._health = 100

    def eat(self, food):
        # work out calorific value of food
        self._health += 5
        return f"{self.name} is eating {food}. MMMMMM!"

    def __str__(self):
        return f"I'm an {self.colour} animal called {self.name}, I have {self.limb_count} limbs. My health rating is {self._health}"
