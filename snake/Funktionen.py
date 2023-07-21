length = len ("Katharina")
print (length)

def greet (name):
    print ("Hello", name)
    print ("How are you")
   
greet ("Katharina")
# name = "Katharina"
# print ("Hello", name)
# print ("How are you")

greet ("Toumas")
greet ("Jana")

length = len ("Katharina")
print (length)

result = greet ("Katharina")
print ("The result of greet () is", result) 
 
def double (x):
    result= x * 2
    return result
    
result = double (7)
print ("The result of double () is" , result)


names = ["Stefan", "Katharina", "Petr", "Karolina"]

for name in names:
    greet (name)
    
for i in range (20):
    print ("Hello!")
    print (i)
   
# i = 0
# print ("Hello")
# print (i)

# i = 1
#print ("Hello")
#print (i)

