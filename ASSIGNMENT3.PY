def sorting():
    tuple1 = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
    tuple1.sort(key = lambda a:a[1])
    print(tuple1)

sorting()    

#Q2
def square():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list1 = list(map(lambda x: x**2, list1))
    print(list1)
    
square()    
#q3
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple2 = tuple(map(lambda x: str(x), list2))
print(tuple2)

#Q4
from functools import reduce

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
value = reduce(lambda x, y: x*y, list3)
print(value)

#Q5
list4 = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list5 = list(filter(lambda x: x %2 == 0 and x % 3 == 0, list4))
print(list5)

#Q6
list7 = ['python', 'php', 'aba', 'radar', 'level']

def ispalindrome(str1):
    i = 0
    flag = 0
    n = len(str1)
    while i <= len(str1)/2:
        if(str1[i] != str1[n-i-1]):
            flag = 1
            break
        i += 1
    if flag == 0:
        return str1
    
str10 = ispalindrome('aba')    
print(str10)

list8 = list(filter(ispalindrome, list7))
print(list8)   

list11 = list(filter(lambda x: x == "".join(reversed(x)), list7))
print(list11)

