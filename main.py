immutable_var= 1, 2, 3, 4
print(immutable_var)
#immutable_var[0]=9
# Выдает ошибку, так как кортедж не поддерживает обращение по элементам.
mutable_list=immutable_var + ([1,2],'a','b')
print(mutable_list)
mutable_list= ([1, 2], 3, 4)
print(mutable_list)
mutable_list [0][0]=5
print(mutable_list)
mutable_list = ([1,2],3,4)+(5,6)
print(mutable_list)
mutable_list = (1,2)*4
print(mutable_list)
mutable_list= [1, 2, 3, 4]
mutable_list.append(900)
print(mutable_list)
mutable_list.remove(3)
print(mutable_list)