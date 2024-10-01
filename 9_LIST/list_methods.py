mylist= [ 1,33,6,7,6,45,6,7]
print("Original List:",mylist)
# # print("Sorted List:",sorted(mylist))
# mylist[1]= 12
# print("Updated List:",mylist)
# mylist.remove(1)
# mylist.pop()
# mylist.append(123)
# mylist.insert(3,99)
# mylist.remove(33)
# index = mylist.index(7)
# print("Index of 7:",index)
# mylist.sort(reverse=True)
# mylist.sort(reverse=True)
# print(" descending  Sorted List:",mylist)
# mylist.sort(reverse=False)
# print("ascending Sorted List:",mylist)
# int_list=1,2,3
# mylist.extend(int_list)
# mytup = ( 1,2,3,4,2)
# print("length of Tuple:",len(mytup))
# print("Tuple:",type(mytup))
# print("Updated List:",mylist)
x = mylist.copy()
print("Copied List:",x)
# mylist.reverse() 
# print("Reversed List:",mylist)
# print("Count of 6:",mylist.count(6))
# mylist.append("hellow")
# print("Updated List:",mylist)
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
print(type(zipped))

list1 = [1, 2, 3]
list2 = ['a', 'b']

zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b')]



