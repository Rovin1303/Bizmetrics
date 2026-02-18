# #q1
name = '''Hi How are you?
Starterd learning python.
It's really interesting.'''

print(name[:])  #Hi How are you?Starterd learning python.It's really interesting.
print(name[-10:-5]) #teres
print(name[3:12]) #How are y
print(name[12:3]) #cannot be bigger[m>n]X
print(name[5:6]) #w
print(name[-4:-12])  #wrong 
print(name[::2]) #H o r o?Satr erigpto.I' elyitrsig
print(name[::-2]) # .nteen larst nhy nnaldert uyeawHi

# #q2
l1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']

print(l1[:])

print(l1[::3])

print(l1[::-2])

print(l1[-2],l1[8])

print(type(l1[3]))


sum = l1[5]+l1[6]+l1[7]
print(sum)

# #q3
l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, 'Success']

print(l2[4])
print(l2[1:5])
print(l2[7])
print(l2[7][2])
print(l2[7][2:])
print(l2[:3])
print(l2[3:])

# #q4

l2[4][1] = 'BEE'
print(l2)

# #q5
del l2[4][1]
print(l2)

# #6.	In l2 add a dictionary at the end {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}
dict = {'insect': ['bee', 'moth'] , 'bird' : ['parrot', 'sparrow']}
l2.append(dict)
print(l2)

# #7.	From l2 extract insect information.

print(l2[8]['insect'])

# #8.	Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2

d1 = {'a':10, 'b':20, 'c' : 30}
l2.insert(2,d1)
print(l2)

# #9.	Based on new l2 created here extract the value 10 from l2 dictionary.

print(l2[2]['a'])

# #10
l2 =[1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, 'Success', (200,300, 'Hundreds')]

print(l2[4][2])   
print(l2[5][:])
print(l2[2])
print(l2[1:5])
print(l2[5])
print(l2[5][3:-1])
print(l2[-1])
print(l2[-4:-3])
print(l2[-4:-10])
print(l2[7][2])
print(l2[-7][2:])
print(l2[:-3])
print(l2[-3:])

#OUTPUT
# '''50
# Python
# 3
# [2, 3, 5, (90, 40, 50, 10)]
# Python
# ho
# (200, 300, 'Hundreds')
# [100]
# []
# work hard
# thon
# [1, 2, 3, 5, (90, 40, 50, 10), 'Python', 400, ['a', 'b', 'work hard'], 100]
# [200, 'Success', (200, 300, 'Hundreds')]'''

# #11
class InvalidMarks(Exception):
    pass
def CheckPassFail(marks):
    try:
        if (not marks.isalnum() and not marks.isalpha()) or marks.isdigit():
            marks = float(marks)
            if marks>100 or marks<0:
                raise InvalidMarks("Marks are invalid")
            elif marks>80.00:
                output = "distinction"
            elif marks>60.00:
                output = "first class"
            elif marks>40.00:
                output = "second class"
            elif marks>=35.00:
                output = "pass"
            else:
                output = "fail"
        else:
            raise ValueError("Alphabets not allowed")
    except InvalidMarks as e:
        print(e)
    except ValueError as e:
        print(e)
    return output


marks = input("Enter marks of student:")
grade = CheckPassFail(marks)
print("Grade for student:",grade)

# #12
class SalaryError(Exception):
    pass
def get_sal_rating(sal,rating):
    if sal.isdigit() and rating.isalpha():
        sal = int(sal)
        if  sal<=0:
            raise SalaryError("Salary cannot be less than zero")
        if sal<=500000:
            if rating == 'A':
                sal = sal +sal*0.16
            elif rating == 'B':
                sal = sal +sal*0.12
            elif rating == 'C':
                sal = sal +sal*0.10
            elif rating == 'D':
                sal = sal +sal*0.06
            else:
               raise ValueError("Rating is not valid")
        elif sal>500000 and sal<=1000000:
            if rating == 'A':
                sal = sal +sal*0.14
            elif rating == 'B':
                sal = sal +sal*0.10
            elif rating == 'C':
                sal = sal +sal*0.08
            elif rating == 'D':
                sal = sal +sal*0.06
            else:
                raise ValueError("Rating is not valid")
        elif sal>1000000 and sal<=1500000:
            if rating == 'A':
                sal = sal +sal*0.08
            elif rating == 'B':
                sal = sal +sal*0.06
            elif rating == 'C':
                sal = sal +sal*0.04
            elif rating == 'D':
                sal = sal*1
            else:
                raise ValueError("Rating is not valid")
        elif sal>1500000 and sal<=2300000:
            if rating == 'A':
                sal = sal +sal*0.07
            elif rating == 'B':
                sal = sal +sal*0.05
            elif rating == 'C':
                sal = sal +sal*0.04
            elif rating == 'D':
                sal = sal*1
            else:
                raise ValueError("Rating is not valid")
        else:
            raise SalaryError("salary amount exceeded")
            
    else:
        raise SalaryError("salary is not is correct format") 
    return sal
   
sal = input("Enter salary:")
rating = input("Enter rating.")
try:
    salary_aft_incre = get_sal_rating(sal,rating)
except SalaryError as e:
    print(e)
except ValueError as e:
    print(e)
print("Salary after increment:",salary_aft_incre)


#Q13
class StudentBilling:

    def __init__(self):
        self.subject_list = ['HR', 'Finance', 'Marketing', 'DS']
        self.annual_subject_cost = 200000
        self.annual_hostel = 0
        self.annual_food = 2000
        self.annual_transport = 0

    def GetSubject(self):

        subject = input("Enter your subject: ")

        if subject.isalpha():
            if subject == 'HR':
                analytics = input("Want analytics?? (Y/N): ").upper()
                if analytics == 'Y':
                    self.annual_subject_cost += 200000 * 0.10
                else:
                    self.annual_subject_cost = 200000

            elif subject == 'Finance':
                self.annual_subject_cost = 200000

            elif subject == 'Marketing':
                analytics = input("Want analytics?? (Y/N): ").upper()
                if analytics == 'Y':
                    self.annual_subject_cost += 200000 * 0.10
                else:
                    self.annual_subject_cost = 200000

            elif subject == 'DS':
                self.annual_subject_cost = 200000

            else:
                print("Subject is not valid")

        else:
            print("Subject must be alphabets")

    def GetHostel(self):

        hostel = input("Want accommodation?? (Y/N): ").upper()

        if hostel.isalpha():
            if hostel == 'Y':
                self.annual_hostel = 200000
            elif hostel == 'N':
                self.annual_hostel = 0
            else:
                print("Please respond in Y or N")
        else:
            print("Non alpha value inserted in hostel")

    def GetFood(self):

        food = input("Want food?? (Y/N): ").upper()

        if food.isalpha():
            if food == 'Y':
                food1 = int(input("Want food how many months?? "))
                if food1 < 0 or food1 > 24:
                    print("Months invalid")
                else:
                    self.annual_food = self.annual_food * food1
            else:
                self.annual_food = 0
        else:
            print("Food must be Y or N")

    def GetTransport(self):

        transport = input("Transport for sem or full year (1/2): ")

        if transport.isdigit():
            transport = int(transport)
            if transport == 1 or transport == 2:
                self.annual_transport = 13000 * transport
            else:
                print("Enter 1 for sem or 2 for full year")
        else:
            print("Digit is required")

    def generate_bill(self):

        total = self.annual_subject_cost+ self.annual_transport+ self.annual_food + self.annual_hostel
        print("\nTotal Bill of student:")
        print("Subject Cost:", self.annual_subject_cost)
        print("Accommodation Cost:", self.annual_hostel)
        print("Transport Cost:", self.annual_transport)
        print("Annual Food:", self.annual_food)
        print("Total Cost:", total)

student = StudentBilling()

student.GetSubject()
student.GetHostel()
student.GetFood()
student.GetTransport()
student.generate_bill()

#q14
import sys
class InvalidBooksException(Exception):
    pass
class InvalidSubjectException(Exception):
    pass
def ask_for_books(books, notebooks):

    d1 = {}
    for a in books:
        for b in books[a]:
            print(a, '-->', b, '-->', books[a][b])

    for a in notebooks:
        for b in notebooks[a]:
            print(a, '-->', notebooks[a][b], '-->', b)

    do_you_books = input("Do you want textbooks: ")

    if do_you_books == 'Y':
        std = int(input("Enter the standard: "))
        if 1 <= std <= 4:
            grade = '1st-4th'
        elif 5 <= std <= 8:
            grade = '5th-8th'
        elif 9 <= std <= 10:
            grade = '9th-10th'
        else:
            raise InvalidBooksException("Invalid standard")
        print("\nAvailable textbooks for this standard:")

        for sub in books:
            print(sub, "-->", books[sub][grade])
        dou = 'True'
        while dou == 'True':
            subject = input("Enter subject name: ")
            if subject in books:
                count_books = int(input("Enter quantity: "))
                price = books[subject][grade]
                print(subject, "-->", price * count_books)
                d1[subject] = price * count_books
            else:
                raise InvalidSubjectException("Subject not available")

            dou = input("More books:(True/False)")

    dou1 = 'True'
    wnt_ntb = input("\nDo you want notebooks (Y/N): ").upper()

    if wnt_ntb == 'Y':

        while dou1 == 'True':

            ntb = input("Notebook type: ")
            pages = int(input("Pages (100/200): "))

            if ntb in notebooks and pages in notebooks[ntb]:
                n = int(input("How many notebooks do you want? "))
                total_price = notebooks[ntb][pages] * n
                print(ntb, "-->", total_price)
                d1[ntb] = total_price
            else:
                raise InvalidSubjectException("Notebook not available")

            dou1 = input("More notebooks:(True/False)")
    else:
        print("Done")
    return d1

def total_price(total_books):
    grand_total = 0
    if total_books is None:
        print("Thank you for your time.")
        return 0
    for val in total_books:
        grand_total += total_books[val]

    return grand_total

def print_bill(total_books, grand_total):

    print('-' * 60)
    print("|{:^58}|".format("Welcome to BOOK STORE"))
    print("|{:^58}|".format("RECEIPT"))
    print("|" + "-" * 58 + "|")
    print("|{:<5s} {:30s} {:>20s}|".format("Sr", "Item", "Amount"))
    print("|" + "-" * 58 + "|")

    for idx, item in enumerate(total_books, start=1):
        print("|{:<5d} {:30s} {:>20.2f}|".format(idx, item, total_books[item]))

    print("|" + "-" * 58 + "|")
    print("|{:>36s} {:>20.2f}|".format("Total Cost:", grand_total))
    print("-" * 60)

notebooks = {
    'square': {100: 40, 200: 70},
    '4lines': {100: 30, 200: 50},
    '2lines': {100: 30, 200: 50},
    'single lines': {100: 60, 200: 100},
    'A4 notebook': {100: 100, 200: 180}
}

books = {
    'Hindi': {'1st-4th': 60, '5th-8th': 100, '9th-10th': 150},
    'Marathi': {'1st-4th': 60, '5th-8th': 100, '9th-10th': 150},
    'English': {'1st-4th': 80, '5th-8th': 100, '9th-10th': 150},
    'Science': {'1st-4th': 90, '5th-8th': 120, '9th-10th': 200},
    'Maths': {'1st-4th': 100, '5th-8th': 140, '9th-10th': 250}
}

print("Welcome to Book Store:")
total_books = {}
doyou = input("Do you want to buy something: ").upper()

try:
    if doyou == 'Y':
        total_books.update(ask_for_books(books, notebooks))
        grand_total = total_price(total_books)
        print(grand_total)
        print_bill(total_books, grand_total)

except InvalidBooksException as e:
    print(e)

except InvalidSubjectException as e:
    print(e)

except:
    print(sys.exc_info())

#q15

from datetime import datetime, timedelta
tendors = {
    1: {"range": (7, 45), "public": {1:5.75, 2:5.75}, "senior": {1:6.25, 2:6.25}},
    2: {"range": (46, 179), "public": {1:6.25, 2:6.25}, "senior": {1:6.75, 2:6.75}},
    3: {"range": (180, 365), "public": {1:6.40, 2:6.40}, "senior": {1:6.90, 2:6.90}},
    4: {"range": (366, 730), "public": {1:7.00, 2:6.75}, "senior": {1:7.50, 2:7.25}},
    5: {"range": (731, 1825), "public": {1:6.70, 2:6.60}, "senior": {1:7.20, 2:7.10}}
}
def calc():

    principal = float(input("Enter principal amount: "))
    days = int(input("Enter number of days for FD: "))

    slab = None
    for key in tendors:
        start, end = tendors[key]["range"]
        if start <= days <= end:
            slab = key
            break

    if not slab:
        print("Invalid tenure")
        return
    
    category = input("Enter category (public/senior): ")

    if category not in ["public", "senior"]:
        print("Invalid category")
        return

    print("Select type: 1 or 2")
    rate_type = int(input("Enter type number: "))

    if rate_type not in tendors[slab][category]:
        print("Invalid type")
        return
    rate = tendors[slab][category][rate_type]

    today = datetime.today()
    maturity_date = today + timedelta(days=days)

    time_years = days / 365
    maturity_amount = principal + (principal * rate * time_years / 100)

    print("Principal:", principal)
    print("Interest Rate:", rate, "%")
    print("Start Date:", today.date())
    print("Maturity Date:", maturity_date.date())
    print("Maturity Amount:", round(maturity_amount, 2))

print("FD Calculator")
calc()

#q16 
string = "In most organized forms of writing, such as essays, paragraphs contain a topic sentence. This topic sentence of the paragraph tells the reader what the paragraph will be about. Essays usually have multiple paragraphs that make claims to support a thesis statement, which is the central idea of the essay."
string  = '''In most organized forms of writing, such as essays,
paragraphs contain a topic sentence. This topic sentence of the paragraph tells 
the reader what the paragraph will be about. Essays usually have multiple paragraphs
that make claims to support a thesis statement, which is the central idea of the essay.'''
print(string)

# #q17
a = 100
e = str(a)
print(e)
b = list(a) #a is not iterable
#print(b)
c = tuple(a) #'int' object is not iterable
#print(c)
d = dict(a) #'dict' object is not callable
#print(d)
m=  set(a) #'int' object is not iterable
#print(m)
h = float(a)
print(h)

# #Q8
city = 'Pune' 
#print(int(city)) invalid literal for int() with base 10: 'Pune'
#print(float(city)) ValueError: could not convert string to float: 'Pune'
print(list(city)) #['P', 'u', 'n', 'e']
print(tuple(city)) #('P', 'u', 'n', 'e')
#print(dict(city))  TypeError: 'dict' object is not callable 
print(set(city)) #{'P', 'e', 'u', 'n'}

# #Q9
l1 = [20,18,15,17,18]
#l2 = int(l1) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#print(l2)
#print(float(l1)) #TypeError: float() argument must be a string or a real number, not 'list'
print(list(l1)) #[20, 18, 15, 17, 18]
print(tuple(l1)) #(20, 18, 15, 17, 18)
#print(dict(l1))  TypeError: 'dict' object is not callable
print(set(l1)) #{17, 18, 20, 15}
#l2 = float(l1) 

# #Q10
snames = []
snames.append(20)
snames.extend(str(30))
snames.append([34,56])
snames.extend('work')
combo = [1,'a','b',2,3]
combo = combo+ snames
print(combo)
snames.append(combo)
combo.extend(snames)

# #11.	Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1 

l1 = [2,3]
l3 = [1,3,4,5,6,7,8]
l3.insert(4,l1)
print(l3)


# Q12
l4 = [1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10]
l5 = []

for val in l4:
    if isinstance(val,int) or isinstance(val,float):
        val = val*5
        l5.append(val)
l4.remove('Nisha')
l4.index(20.50)    
print(l5)

# Q13
l6 = [x**2 for x in range(1,11)]
print(l6)

# Q14
l7 = [x for x in range(1,201) if x%13==0]
print(l7)

# Q15
l8 = [x for x in range(300,401) if x%4==0]
print(l8)

# Q16
x, y = 2, 2
combinations = [[i, j] for i in range(x) for j in range(y)]
print(combinations)
# #27


# Q24
# '''
name = input("Enter username:")
day = input("Enter dob day:")
month = input("Enter dob month:")
year = input("Enter dob year:")
if name.isalpha() and day.isdigit() and month.isdigit() and year.isdigit() :
    password = name[:4]+'@'+day + month
else:
    print("some value is not defined")
print(password)

# Q25
name = input("Enter username:")
day = input("Enter dob day:")
month = input("Enter dob month:")
year = input("Enter dob year:")
dob = day+month+year
if name.isalpha() and day.isdigit() and month.isdigit() and year.isdigit() :
    if name is not "" and len(dob) == 8:
        password = name[:4]+'@'+year
        print(password)
else:
    print("some value is not defined")

# Q26

for i in range(1,5):
    print("*"*i)

#27
n = int(input("Enter rows:"))
for i in range(n,0,-1):
    if i ==0:
        break
    print("*"*i)

# Q28
str1 = "ABCD"
for i in range(0,len(str1)):
    print(str1[:i+1])
    print()

# Q29
str1 = "ABCD"
for i in range(0,len(str1)):
    print(str1[i]*(i+1))

# Q30
c = 1
for i in range(0,len(str1)):
    print((str(i+1)*(i+1)))

# Q31
str1 = "ABCD"
for i in range(len(str1),-1,-1):
    print(str1[i:][::-1])

# Q32
str1 = input("Enter a string:")
for i in range(len(str1),-1,-1):
    print(str1[i:][::-1])

# Q33
l1 = []
for i in range(1,11):
    if i%2 != 0:
        l1.append(i)
print(l1)

l2 = [x for x in range(1,11) if x%2 !=0]
print(l2)

# Q34
l3 = []
for i in range(200,251):
    if i%2 == 0:
       l3.append(i)
print(l3) 

# Q35 and Q36
l5 = [2,70,'work', 'para', 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
l6 = []
for i in l5:
    if isinstance(i,int) or isinstance(i,float) or isinstance(i,str):
        l6.append(i*2)
    elif isinstance(i,(list,tuple)):
        l6.append(i*2)
    elif isinstance(i, set):
        d = set()
        for x in i:
            d.add(x*2)
        l6.append(d)
    else:
        new_dict = {}
        for k,v in i.items():
            new_dict.update({k:v*2})
        l6.append(new_dict)
print(l6)

#Q37

def ValidateMarks(marks):
    try:
        marks = int(marks)
        if marks>0 and marks<=100:
            return "Marks are valid"
        else:
            return "Marks should be more than 0 and upto 100"
    except ValueError as t:
        return "value error is there"
marks = input("Enter marks of student:")
stmt = ValidateMarks(marks)
print(stmt)

#Q38

def ValidateName(name):
    c = 1
    if name == ' ':
        print("Name is empty:")
        return 0 
    if name.isalpha():
        return 1
    else:
        if ' ' in name:
            print("Space IS PRESENT")
        elif name.isdigit():
            print("IT contains digit")
        elif not name.isalnum() and not name.isspace():
            print("contains special character")
        return 0
    
first_name = input("Enter first name:")
last_name = input("Enter last name:")
print("For First name:\n")
if ValidateName(first_name):
    print("First Name is valid",first_name)
else:
    print("First Name is not valid")
print("\nFor Last name:")
if ValidateName(last_name):
    print("Last Name is valid",last_name)
else:
    print("last Name is not valid")

#Q39
class MobException(Exception):
    pass

def CheckMobileNum(mob_num):
    try:
        if mob_num == ' ':
            print("Mobile Number empty")
            return 0
        if mob_num.isdigit() and len(mob_num) == 10:
            return 1
        else:
            if mob_num.isalpha():
                raise MobException("Contains alphabets")
            elif len(mob_num) !=10:
                raise MobException("Not 10 numbers")
            elif ' ' in mob_num:
                raise MobException("Space detected")
            elif not mob_num.isalnum() and not mob_num.isspace():
                raise MobException("Special Characters present")
            return 0
    except MobException as e:
        print(e)
        
mob_num = input("Enter Mobile Number:")
if(CheckMobileNum(mob_num)):
    print("Mobile number is valid")
else:
    print("Invalid number")

#Q40
name = input("Enter username:")
day = input("Enter dob day:")
month = input("Enter dob month:")
year = input("Enter dob year:")
dob = day+month+year
if name.isalpha() and day.isdigit() and month.isdigit() and year.isdigit() :
    if name is not "" and len(dob) == 8:
        password = name[:4]+'@'+year
        print(password)
else:
    print("some value is not defined")

#Q41
import sys
class DataFeedingException(Exception):
    pass
def DictData():
    dict1 = {}
    val = 1
    while val == 1:
        name = input("Enter name:")
        dob = input("Enter dob:")
        mobile = input("Enter mobile:")
        count = 1
        if name == ' ' or dob == ' ' or mobile == ' ':
            raise DataFeedingException("Data is missing")
        if name.isalpha() and dob.isdigit() and mobile.isdigit():
            if len(dict1.keys()) == 0:
                dict1[count] = {'name':name,'dob':dob,'mobile':mobile}
                val = int(input("enter one more data press 1 else 0"))
            else:
                dict1[count+1] = {'name':name,'dob':dob,'mobile':mobile}
                val = int(input("enter one more data press 1 else 0"))
        else:
            raise DataFeedingException("Format error")
    return dict1
try:
    d1 = {}
    d1 = DictData()
    print(d1)
except DataFeedingException as e:
    print(e)
except:
    print(sys.exc_info())

#Q42
import re
import sys
class ValidityCheck(Exception):
    pass
class AddRecord:
    def __init__(self):
        self.filename = "C:/Users/Rovin/OneDrive/Desktop/MCA/newone/file2.txt"
    def countlines(s,filename):
        s.val= 0
        s.f =open(filename,'r')
        for line in s.f.readlines():
            s.val+=1
        return s.val
    def addtofile(s,c,filedict):
        count = s.countlines(s.filename)
        with open(s.filename,'a') as f:
            f.write(str(count+1)+":"+str(filedict[c])+"\n")
class Validity:
        def valid_name(s,name):
            if name.isalpha():
                if re.match('^[A-Z][a-z]+',name):
                    print("Name is valid")
                    return 1
                else:
                    raise ValidityCheck("Name is not in valid format")
            else:
                raise ValidityCheck("name is in numeric or alphanum or specialchars")

        def valid_mobile(s,mobile):
            if mobile.isdigit():
                if re.match('[6-9]{1}[0-9]{9}',mobile):
                    print("Mobile is valid")
                    return 1
                else:
                    raise ValidityCheck("Mobile is not valid")
            else:
                raise ValidityCheck("Mobile num should be digits")
            
        def valid_pan(s,panid):
            if panid.isalnum() and len(panid) == 10:
                if re.match('[A-Z]{5}[0-9]{4}[A-Z]$',panid):
                    print("Valid pan id")
                    return 1
                else:
                    raise ValidityCheck("pan id is not valid")
            else:
                raise ValidityCheck("pan id should contain alphabets and numbers.")
            
        def valid_marks(s,marks):
                if marks.isdigit():
                    marks= int(marks)
                    if marks>=0 and marks<=100:
                        print("Tenth marks are correct.")
                        return 1
                    else:
                        raise ValidityCheck("Tenth marks are not between 0 and 100.")
                else:
                    raise ValidityCheck("either 10th or 12th marks are as a string.")

        def valid_grade(s,grade):
            if grade.isalpha():
                if re.match('[A,B,C,D,F]',grade):
                    print("Grade is valid")
                    return 1
                else:
                    raise ValidityCheck("grade should be between [A,B,C,D,F]")
            else:
                raise ValidityCheck("Grade should be alphabet")    

class GetStudentInfo(AddRecord,Validity):
    def check_validate(s,n,m,pn,ten_mks,twel_mks,grade):
        if n and m and pn and ten_mks and twel_mks and grade:
            print("All info is valid")
            return 1
        else:
            return 0
                
    def addtodict(s,n,m,pn,ten_mks,twel_mks,grade,filedict):
        count = 0    
        filedict[count] = {'name':n,'mobile':m,'pan':pn,'10th':ten_mks,'12th':twel_mks,'grade':grade}
        s.addtofile(count,filedict)

    def getinfo(s):
        try:
            s.val = 1
            s.filedict = {}
            while s.val == 1:
                n = input("Enter a name of user:")
                name = s.valid_name(n)
                mbl = input("Enter mobile num:")
                mobile = s.valid_mobile(mbl) 
                pan = input("Enter Pan Number:")
                pan_flag = s.valid_pan(pan)
                mks = input("Enter marks:")
                tenth_marks = s.valid_marks(mks)
                twelth = input("Enter 12th marks:")
                twelth_mks = s.valid_marks(twelth)
                grade_marks = input("Enter grade marks:")
                grade = s.valid_grade(grade_marks)
                validcheck = s.check_validate(name,mobile,pan_flag,tenth_marks,twelth_mks,grade)
                if validcheck:
                    s.addtodict(n,mbl,pan,mks,twelth,grade_marks,s.filedict)
                else:
                    print("Invalid info")
                s.val = int(input("Do you want to add another record(0/1):"))
        except ValidityCheck as e:
            print(e)
        except:
            print(sys.exc_info())

doyou = input("Do you want to add record:")
if doyou == 'Y':
     s1 = GetStudentInfo()
     s1.getinfo()

else:
    print("Bye")


#Q45
dict1= {'key1': {'subkey':20} ,'Key2': {'subkey':5},'Key3': {'subkey':16},'Key4': {'subkey':6}}
print(dict1)
l1= list(dict1.keys())
n = len(l1)
for i in range(0,n):
    for j in range(0,n-i-1):
        current_key = l1[j]
        next_key = l1[j+1]
        if dict1[current_key]['subkey'] > dict1[next_key]['subkey']:
            l1[j], l1[j+1] =  l1[j+1],l1[j] #change the key
d1 = {}
for k in l1:
    d1[k] = dict1[k]
print(d1)

#Q46
class NewException(Exception):
    pass
def takeInput():
    dob = input("Enter Birth date")
    if dob.isdigit():
        dob_format = datetime.strptime(dob,"%d-%m-%Y")
        date_today = datetime.now()
        diff = date_today.year - dob_format.year
    else:
        raise NewException("Value should be integer")
    return diff
try:
    d = input("want license?")
    if d == 'Y':
        difference = takeInput()
        print("Age:",difference)
    else:
        print("Thank you")
except NewException as e:
    print(e)

#Q47
import sys
class NewException(Exception):
    pass
eligble_age = 18
def checkEligible(age):
    if age >=eligble_age:
        print("Eligible for license")
    else:
        print("Not eligible for license")

def takeInput():
    dob = input("Enter Birth date")
    if dob.isdigit():
        dob_format = datetime.strptime(dob,"%d-%m-%Y")
        date_today = datetime.now()
        diff = date_today.year - dob_format.year
    else:
        raise NewException("Value should be integer")
    return diff
try:
    d = input("want license?")
    if d == 'Y':
        difference = takeInput()
        checkEligible(difference)
    else:
        print("Thank you")
except NewException as e:
    print(e)

#Q48
def check_palidrome(str1):
    if str1 == str1[::-1]:
        print("palindrome")
    else:
        print("Not Palindrome")
str1 = input("Enter name")
check_palidrome(str1)

#Q49
def fibonacci():
    a = 0
    b = 1
    print(a, b, end=" ")
    while True:
        c = a + b
        if c > 100:
            break
        print(c, end=" ")
        a = b
        b = c
fibonacci()

#Q50
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact* i
    return fact
num = int(input("Enter num:"))
print("Factorial =", factorial(num))

#Q51
def findLargest(l1):
    '''
    Docstring for findLargest
    
    :param l1: list from which largest element is fetched
    '''
    max_element = 0
    for val in l1:
        if val>max_element:
            max_element = val
    return max_element

val = findLargest(l1)
print(val)

#Q52

def freq(lst):
    d1 = {}
    for val in lst:
        if val in d1:
            d1[val] += 1
        else:
            d1[val] = 1
    return d1

l = [1, 2, 3, 2, 1, 4, 3, 2]
print(freq(l))

#Q53

def common(l1, l2):
    l3 = []
    for item in l1:
        if item in l2:
            l3.append(item)
    return l3

l1 = [1, 2, 3, 4, 5]
l2 = [3, 2, 8, 7, 9]
print("Common elements:",common(l1, l2))

#Q55

def print_bill():
    snack = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    print("-" * 50)
    print("|{:^48}|".format("Welcome Hotel Rovin"))
    print("-" * 50)
    total = quantity * price
    print("|{:<7} {:<15} {:<18} {:<5}|".format("sr", "Menu", "quant", "price"))
    print("-" * 50)
    print("|{:<7} {:<15} {:<18} {:<5}|".format(1, snack, quantity, total))
    print("-" * 50)
    print("|{:>30} {:>17}|".format("Total", total))
    print("-" * 50)

print_bill()





