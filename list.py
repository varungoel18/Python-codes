my_lst = list()
my_lst = [6,3,1,8]
print(my_lst)
my_lst.pop(2)
print(my_lst)
my_lst.reverse()
print(my_lst)
10 in my_lst
my_lst.remove(3)
print(my_lst)
my_lst.sort()
print(my_lst)

my_lst.append([20,30,40])    # it append whole list on its own
print(my_lst)

my_lst.extend([50,60,70])  # single unit is appended one by one
print(my_lst)

my_lst2 = ["Python",[1,2,3],4.0 , True]       # hetrogeneous list
print(my_lst2)

new_lst = list(range(1,11))
print(new_lst)
new_lst2 = []
for ele in new_lst:
    new_lst2.append(ele**2)
print(new_lst2)

new_lst2  = [ele**2 if ele%2==0 else ele**3 for ele in new_lst]    # list comprehention  (sol, condition, for statement) format of list comprehention
print(new_lst2)
