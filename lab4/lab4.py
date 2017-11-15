class animal(object):
    def __init__(self,sound,name,age,favorite_color):
        self.sound = sound
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
    def eat(self,food):
        print("yummy!!" + self.name + "is eating" + food)
        #Problem 1:
    def description(self,food):
        print(self.name + "is" + self.age + "years old and loves the color" + self.favorite_color)
    def make_sound(self,sound):
        #Problem 2:
        print(sound)
        print(sound)
        print(sound)
#Problem 3:
class person(object):
    def __init__(self,name,age,city,gender):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
    def eat(self,favorite_breakfast):
        print("yummy!!" + self.name + "is eating" + favorite_breakfast)
    def eat(self,favorite_pet):
        print("yummy!!" + self.name + "favorite pet is" + favorite_pet)
#Problem 3 EXTRA:
class song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self,lyrics):
        print(lyrics)
