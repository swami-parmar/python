from assignments.assignment2 import playlist

my_profile =("swami",16,"pizza",True)
print(my_profile)

playlist=('shape of you','blinding lights','believer','senorita','levitating')
print(playlist)

order=('burger','fries','coke')
my_list=list(order)
my_list.append('icecream')
order = tuple(my_list)
print(order)

insta_post = (101 , "swami", 250, ["#love","insta"],True)
print(insta_post)
for item in insta_post:
    print(type(item))

duration=(12,5,0,20,7,3,15)
my_list1 =list(duration)
my_list1= (x for x in my_list1 if x>=5)
print(duration)
