# #List Methods:
#
# #same as string methods
#
# numbers = [ 5,2,1,7,4,5]
# numbers.append(20) #this method inserts 20 at the end of the list
# print(numbers)
#
# numbers.insert(0,10) #this will insert 10 at index 0.
# print(numbers)
#
# numbers.remove(2) #removes items
# print(numbers)
#
# numbers.clear #clears whole list
# print(numbers)
#
# numbers.pop #removes end item
#
# numbers.index(5) #this will return the INDEX of the first occurrence of the item
# print(numbers)
#
# print (5 in numbers) #this "in" method will return a boolean if a value exists.
#
# numbers.count(5) #.count will return the number of times this occurs
# print(numbers)
#
# numbers.sort () #sort doesnt return a value, but it will sort the list
# print(numbers)
#
# numbers.reverse() #reverse will reverse the order of the list
# print(numbers)
#
# numbers2 = numbers.copy() #this will copy the referenced list
# print(numbers2)
#

list_of_numbers = [1, 3, 2, 5, 3, 2, 5, 8, 23, 5, 6, 7, 4, 3, 2, 5, 7, 89, 0, 2, 1, 1, 3, 6, 2, 3, 6, 4, 3, 2, 2, ]
uniques = []
for number in list_of_numbers:
    list_of_numbers.reverse()
    list_of_numbers.sort()
    if number not in uniques:
        uniques.append(number)
print(uniques)