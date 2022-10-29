# Name: - Neeraj Kumar
# ID: - 2047559

mydict = {}
my_list = input().split()



for item in my_list:
   if item in mydict:
      mydict[item] += 1
   else:
      mydict[item] = 1

for val in my_list:
   print(f'{val} {mydict[val]}')

#print(mydict)