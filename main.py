names=['grace','alice','day','irene','coop']
print(names)
print(names[0])
print(names[4])
names.append('raph')
print(names)
names.insert(2,'belta')
print(names)
print(names[3:5])
print(names[-1])
print(names[-6])
names.remove('coop')
print(names)

d=[1,2,5,6,7,8,4,2,1,2,1,8,2]
print(d.count(2))
print(d.count(1))
names=["a","b","A","B","a","b","e","f","a","b"] #Items in a list
print(names)
print(names.count("b"))
print(names.count("a"))

newNames=["Grace","Day","Irene","Grace","Grace"]
print(newNames.count("Grace"))


fruits=["Apple","Bananas","Mango","Orange","Straw berry"]
print(fruits)
fruits.insert(0,"water mellon") #insert at acertain position
print(fruits)
fruits.append("Lemon")
print(fruits)
print(fruits.index("Lemon"))
print(fruits.index("water mellon"))
print(fruits[4])
#Reverse
num=[1,56,90,57,2,4,3,5,7,8,90]
print(num)
num.reverse()
print(num)
num.reverse()
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
#Letters

letter=["a","b","e","z","m","n","c","d","e"]
print(letter)
letter.reverse()
print(letter)
letter.sort()
print(letter)
letter.sort(reverse=True)
print(letter)
#Extends

myList=[1,2,3,4,5,6]
nList=["a","b","c","d","e"]
print(myList)
print(nList)
myList.extend(nList)

print(myList)
#Concatination (Adding Lists)
myList=[1,2,3,4,5]
nList=["Mango","Oranges","Pine apple","Banana"]
print(nList+myList)
# def append(name):
#     pass
#
# def insert(index,name):
#     pass


def myfunction(parameter,argument="Grace"):
    pass
myfunction("New Param")
myDict={
    "Key":"Value"
}