import string
import random
#how much genreat from object count
characters_number = float(7)

#import libraries
# the range of Objects will be in the generate 
s1 = ["Paris", "Egypt", "Hero", "Oni-Chan", "Brother",
      "Vgr", "vgr", "Void", "volo", "Voidlas", ]
s2 = ["javav2", "Hello_World", "C9", "Light", ]
s3 = ["Maged", "Mohamed", "Ahmed", "Meliodas", "SEN", "Darkness"]
s4 = ["1001", "001", "0005"]
# from random library make all objects s1 , s2 , s3 ,s4 random generation
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
generate = [] #make a empty list
part1 = round(characters_number * (30/100))# This will make chance random diffrent here its 30%
part2 = round(characters_number * (20/100))# here its part1 20 / 100 20% from the from the first ratio
for i in range(part1):#This the first part from the password represent 30 from the generate
    generate.append(s1[i])
    generate .append(s2[i])
for i in range(part2):#this the same method up there  represent  20 % from 100% in part 2
    generate.append(s3[i])
    generate.append(s4[i])

generate = "".join(generate[0:]) #this will make the generate with out type = list 

print(generate)#this will print the generate result
