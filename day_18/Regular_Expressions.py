import re

##########

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
spliting = paragraph.split()
result = list((i, spliting.count(i)) for i in spliting)
print(result)

############

# p = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

# number = re.findall(r'-?\d+', p)
# res = [eval(i) for i in number]
# res.sort()
# length = len(res)
# print(res[length-1] - res[0])

##########

# i = 'first_name'
# print(i.isidentifier())

###########

# r = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
# r1 = re.sub("@", "", r)
# r2 = re.sub("%", "", r1)
# r3 = re.sub("#", "", r2)
# r4 = re.sub("\$", "", r3)
# r5 = re.sub("&", "", r4)
# print(r5)