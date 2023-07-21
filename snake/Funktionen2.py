def double (x):
    return x * 2
    
print (double (4))
print(double("four"))

print (double(4) + 2)

def qoutient_and_remainder (a, b):
    qoutient = a // b
    remainder = a % b
    return qoutient, remainder
    
result = (qoutient_and_remainder(5, 2))
print (result)
q,r = result
print ("The qoutient is" , q)
print ("The remainderis ", r)

hand = [(2, "spades"), (10, "clubs"), (8, "diamonds")]

for value, suit in hand:
    print ("A", value , "of", suit)
# value, suit = (2, "spades")
# print ("A2, value, "of", suit)

#value, suit = (10,"clubs")
#print ("A", value, "of", suit)

things = ["grass", "sun", "carrot", "river"]
colours = ["green", "yellow", "orange", "blue"]

for pair in zip (things, colours):
    print (pair)
    
for thing, colour in zip(things, colours):
    print ("The" , thing, "is", colour)
    
#thing, colour = ("grass", "green")
# print ("The", thing, "is", colour)

#thing, colour = ("sun", "yellow")
# print ("The", thing, "is", colour)

