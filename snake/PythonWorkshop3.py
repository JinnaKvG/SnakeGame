class Kitten:
    def make_sound(self):
        print (self.name, "says Meow!")
    
spot = Kitten()

spot.name = "spot"
print (spot.name)

new_kitten = Kitten()
new_kitten.name = "Whiskas"
print (new_kitten.name)
print (spot.name)

spot.make_sound()
new_kitten.make_sound()