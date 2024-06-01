class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def feed_cat(self, cat):
        print(f"{self.name} feeds {cat.name} the cat.")

    def play_with_cat(self, cat):
        print(f"{self.name} plays with {cat.name} the cat.")

class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print(f"{self.name} the cat says Meow!")

    def purr(self):
        print(f"{self.name} the cat purrs contentedly.")


        Vasya = Human("Vasya", 26, "Male")
        Begula = Cat("Fluffy", 2, "British")

        Vasya.feed_cat(Begula)
        Begula.meow()
        Vasya.play_with_cat(Begula)

