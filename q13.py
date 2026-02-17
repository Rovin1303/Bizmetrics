import sys
class ValidationException(Exception):
    pass

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
                analytics = input("Want analytics?(Y/N): ").upper()
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
                raise ValidationException("Subject is not valid")
        else:
            raise ValidationException("Subject must be alphabets")

    def GetHostel(self):
        hostel = input("Want accommodation?? (Y/N): ").upper()
        if hostel.isalpha():
            if hostel == 'Y':
                self.annual_hostel = 200000
            elif hostel == 'N':
                self.annual_hostel = 0
            else:
                raise ValidationException("Please respond in Y or N")
        else:
            raise ValidationException("Non alpha value inserted in hostel")

    def GetFood(self):
        food = input("Want food?? (Y/N): ").upper()
        if food.isalpha():
            if food == 'Y':
                food1 = int(input("Want food how many months?? "))
                if food1 < 0 or food1 > 24:
                    raise ValidationException("Months invalid")
                else:
                    self.annual_food = self.annual_food * food1
            else:
                self.annual_food = 0
        else:
            raise ValidationException("Food should be Y or N")

    def GetTransport(self):
        transport = input("Transport for sem or full year (1/2): ")
        if transport.isdigit():
            transport = int(transport)
            if transport == 1 or transport == 2:
                self.annual_transport = 13000 * transport
            else:
                raise ValidationException("Enter 1 for sem or 2 for full year")
        else:
            raise ValidationException("Digit is required")

    def generate_bill(self):
        total = self.annual_subject_cost+ self.annual_transport+ self.annual_food + self.annual_hostel
        print("\nTotal Bill of student:")
        print("Subject Cost:", self.annual_subject_cost)
        print("Accommodation Cost:", self.annual_hostel)
        print("Transport Cost:", self.annual_transport)
        print("Annual Food:", self.annual_food)
        print("Total Cost:", total)
try:
    student = StudentBilling()
    student.GetSubject()
    student.GetHostel()
    student.GetFood()
    student.GetTransport()
    student.generate_bill()
except ValidationException as e:
    print(e)
except:
    print(sys.exc_info())
