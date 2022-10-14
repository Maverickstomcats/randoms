from random import randint
from random import shuffle 
from random import choice
  
  # random
  # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
  #show you two useful functions for now.
print("random")
dice1 = randint(1,7)
dicetwo = randint(1,7)
rolledDoubles = dice1 == dicetwo 
if rolledDoubles: 
  print("it's a double!")
else:
  print("not a double, nerd")

#my_list = range(1,200)
#print(my_list)
#shuffle(my_list)
#print(my_list)
#newlist = randint(1,201)
#print(newlist)

#f newlist % 2 == 0:
  #print(f"{newlist} is even")
#else:
  #print("odd")

color = ["red", "blue", "green", "pink"]
random_color = choice(color)
print(f"choice color is {random_color}")