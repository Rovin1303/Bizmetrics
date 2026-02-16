from functools import reduce
#Write a list comprehension to generate squares of numbers from 1 to 10

l1 = [x**2 for x in range(1,11)]
print(l1)
#2. Create a list of even numbers between 1 and 50 using list comprehension.
l2 = [x for x in range(1,51) if x%2 == 0]
print(l2)

#3. Convert all strings in a list to uppercase using list comprehension.

l3 = ['apple','orange','pineapple']
l3 = [x.upper() for x in l3]
print(l3)

#4. Given a list of integers, create a new list that contains only the positive numbers.

l4 = [23,-4,12,-13,56,33]
l5 = [x for x in l4 if x>0]
print(l5)

#5. Create a list of tuples (num, num^2) for numbers 1 to 5

l5  = [(num,num**2) for num in range(1,6)]
print(l5)

#6. Extract all vowels from a given string using list comprehension.

str1 = 'greenfish'
l6 = [x for x in str1 if x in('aeiou')]
print(l6)

#7.Flatten a 2D list using list comprehension.
lst = [[1,2,3],[4,5,6]]
l2 = []
lst = [l2.extend(x) for x in lst if isinstance(x,list)]
print(l2)

#8. Replace all negative numbers in a list with 0 using list comprehension.
lst = [2,4,3,-2,-4,1]
lst = [x if x>0 else 0 for x in lst]
print(lst)

#9. Given a list of words, create a list of lengths of each word.
lst = ["robert",'banana','grapes']
l9 = [len(x) for x in lst]
print(l9)

#10. Filter out words that start with the letter 'A' or 'a'.

lst = ['Anabella','banana']
l10 = [lst.pop(lst.index(x)) for x in lst if x[0] in('A','a')]
print(lst)
# From a list of numbers, generate a list of “even” or “odd” strings using list comprehension

lst = [1,2,3,4,5,6,7]
l11 = ['even' if x%2 == 0 else 'odd' for x in lst]
print(l11)

# Create a list of numbers divisible by both 3 and 5 in range 1–100.

l12 = [x for x in range(1,101) if x%3 == 0 and x%5 ==0]
print(l12)

#Write a nested list comprehension to generate a multiplication table for 1–5.

l13 = [[(x*i) for i in range(1,11)] for x in range(1,6)]
print(l13)

#Convert a dictionary’s keys into a list using list comprehension.
d = {1:'a',2:'b',3:'c'}
l14 = [k for k in d.keys()]
print(l14)

#Extract numeric digits from a string using list comprehension.
str1 = 'aaacc2343eee'
l15 = [str1[x] for x in range(0,len(str1)) if str1[x].isdigit()]
print(l15)

#16. Use list comprehension to remove all spaces from a string.
s = "str1 str1 str1"
str2 = ''
l1 = ['' if s[x] == ' ' else str2 + s[x] for x in range(0,len(s))]
print(str2.join(l1))
#17. Create a list of characters that appear more than once in a string.

s ='indianhighschool'
l17 = [{x for x in s if s.count(x)>1}]
print(l17)

#18. From a list of sentences, generate a list of all words (split using list comprehension).

l1 = ["hello man","program in python"]
l18 = [word for s in l1 for word in s.split()]
print(l18)

#19. Create a list of unique elements from a list using list comprehension + condition.

l1= [1,2,2,3,4,5,5,5]
l2 = []
l19 = [l2.append(x)  for x in l1 if x not in l2]
print(l2)
#20. Generate all pairs (x, y) where x is from list A and y is from list B (cartesian product).

l1 = [1, 2]
l2 = ['a', 'b']
lst_pair = [(x, y) for x in l1 for y in l2]
print(lst_pair)

#1. Write a lambda to add two numbers.
x = lambda x,y : x+y
print(x(2,3))

#2. Create a lambda to check if a number is even.
xy = lambda x:'even' if x%2 == 0 else 'odd'
print(xy(2))

#3. Write a lambda to get the last character of a string.

str = lambda x:x[-1]
print(str('datae'))

#4. Use lambda with map() to square every number in a list.

nums = [1,2,3,4]
d = list(map(lambda x:x**2,nums))
print(d)

#5. Use lambda with filter() to get only odd numbers from a list.
nums = [1,2,3,4,5,6]
odd_d = list(filter(lambda x:x%2!=0,nums))
print(odd_d)

#6. Use sorted() + lambda to sort a list of tuples by second value.

pairs = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
s = sorted(pairs,key = lambda x:x[1])
print(s)
#7. Create a lambda to check if a string is a palindrome.

str1 = "madam"
palin = lambda s:"palindrome" if s == s[::-1] else "not palinrdrome"
print(palin(str1)) 

#8. Use lambda to find maximum of three numbers.

m = lambda a,b,c : max(a,b,c)
print(m(2,3,4))

#9. Write a lambda to reverse a string.

str1 = lambda s: s[::-1]
print(str1("dtat"))

#10. Use lambda with map() to convert a list of strings to integers.

lst = ["str","data","lsls"]
str_to_int = list(map(lambda x:int(x),l1))
print(str_to_int) 

#11. Use lambda with filter() to remove empty strings from a list.

lst = ["apple",'','','banana']
rem_emt = list(filter(lambda x:x!='',lst))
print(rem_emt)

#12
n = 5
val= reduce(lambda x,y: (x*y),range(1,n+1))
print(val)

#13 Write a lambda that returns the larger of two numbers.

larger = lambda a,b:a if a>b else b
print(larger(3,4))

#14. Use lambda to check if number is divisible by 5

div = lambda x: "divisible" if x%5 == 0 else "not divisible"
print(div(11))

#15. Use lambda + map() to add 10 to each element of a list.

l1 = [2,3,4,5]
add_10 = list(map(lambda x: x+10,l1))
print(add_10)

#16. Use lambda to sort a list of dictionaries by a key (like "age").

names = [{"name": "lokesh", "age": 26}, {"name": "morris", "age": 39}, {"name": "Aditya", "age": 29}]
sor_peop = sorted(names, key=lambda x: x["age"])
print(sor_peop)

#17  Write a lambda that returns True if a character is a vowel.

vowel = lambda x:x in('aeiouAEIOU')
print(vowel('E')) 

#18. Use lambda + filter to extract words of length > 5 from a list.

lst = ['ssss','banana','checcke']
big_words = list(filter(lambda x: len(x)>5,lst))
print(big_words)

#19. Use lambda to calculate the area of a circle (πr²).

area = lambda rad : 3.14*(rad**2)
print(area(2)) 

#20. Write a lambda to remove duplicates from a list using filter + set.

lst = [1,2,3,4,2,3,4,2,1,5]
dup = set(filter(lambda x: x,lst))
print(dup)

#21. Use lambda with reduce() to find the product of all numbers in a list.

lst = [1,2,3,4]
mul = reduce(lambda x,y:x*y,lst)
print(mul)

#22. Write a lambda that returns absolute value of a number.

get_abs = lambda x: abs(x)
print(get_abs(-50))

#23. Use lambda to sort a list of strings by their length.
words = ["apple", "grapes", "banana", "pear"]
sorted_words = sorted(words, key=lambda s: len(s))
print(sorted_words)

#24. Use lambda to get only uppercase characters from a string
str1 = "sTSYsteM"
str2 = ''
upp = str2.join(filter(lambda x:x.isupper(),str1))
print(upp)

#25. Write a lambda that returns the square if number is even, cube if odd.

lst = [1,2,3,4,5,6]
sqr = list(map(lambda x: x**2 if x%2==0 else x**3,lst))
print(sqr)

#26. Use lambda with map to convert Celsius to Fahrenheit.
temp = [0, 20, 30, 100]
ftemp = list(map(lambda x: (x * 9/5) + 32, temp))
print(ftemp)

#27
abc = lambda a,b: sorted(a.lower()) == sorted(b.lower())
print(abc("listen", "silent"))

#28
mixed = [1, "a", 2.5, "apple", 10, True]
nums_only = list(filter(lambda x: isinstance(x, (int, float)) and type(x) != bool, mixed))
print(nums_only)

#29
nums = [1, 5, -3, 10]
neg = any(map(lambda x: x < 0, nums))
print(neg)

#30
multiplier = lambda n: (lambda x: x * n)
double = multiplier(2)
triple = multiplier(3)
print(double(10))
print(triple(10))
