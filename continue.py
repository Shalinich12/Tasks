s1 = {1, 2, 4, 3}
s2 = {3, 4, 9, 8}

s1.add(10)                   
print(s1.union(s2))         
print(s1.intersection(s2))   
print(s1.difference(s2))   
print(s1.symmetric_difference(s2))  
print(s1 & s2)
print(s1 - s2)

List = [10,20,5,30,3,40]
print(sorted(List))
List.sort()
print(List)
List.sort(reverse=True)
print(List)
Tuple = (20,30,10,40,80,15)
print(sorted(Tuple))
print(sorted(Tuple,reverse=True)) 
# for index,item in enumerate(Tuple, start=1):
#     print(f"Index: {index}, Item: {item}") 
# y= enumerate(Tuple)
# print(list(y))


dictionary = {"name":"shalini", "class":"btech"}
print(dictionary["name"])
dictionary["address"]="hyd"
print(dictionary)

dictionary.update({"color":"green"})
print(dictionary)
dictionary.pop("color")
print(dictionary)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.symmetric_difference(set2)  
set4 = set2.difference(set1) # 8 6 7
print(set3)
print(set4)


# set methods examples:
set1={5,8,6,10,20}
set2= {5,10,30,40,60}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.symmetric_difference(set2)  
set4 = set2.difference(set1) 
print(set3)
print(set4)

