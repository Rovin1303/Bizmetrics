import sys
import os
class ValidationException(Exception):
    pass

class StudentBilling:
    def __init__(self):
        '''
        Docstring for __init__
        
        setting instance variables for the student object
        '''
        self.totalsub = 200000
        self.totalhostel = 0
        self.totalfood = 2000
        self.totaltransport = 0

    def GetSubject(self):
        '''
        Docstring for GetSubject
        
        :Course the student wants to register and whether wants analytics or not
        '''
        subject = input("Enter your subject: ")
        if subject.isalpha():
            if subject == 'HR':
                analytics = input("Want analytics?(Y/N): ").upper()
                if analytics == 'Y':
                    self.totalsub+= 200000 * 0.10
                else:
                    self.totalsub = 200000
            elif subject == 'Finance':
                self.totalsub = 200000

            elif subject == 'Marketing':
                analytics = input("Want analytics?? (Y/N): ").upper()
                if analytics == 'Y':
                    self.totalsub += 200000 * 0.10
                else:
                    self.totalsub = 200000
            elif subject == 'DS':
                self.totalsub = 200000
            else:
                raise ValidationException("Subject is not valid")
        else:
            raise ValidationException("Subject must be alphabets")

    def GetHostel(self):
        """
        Docstring for GetHostel
        
        :Ask the student whether wants accomadation 
        """
        hostel = input("Want accommodation?? (Y/N): ").upper()
        if hostel.isalpha():
            if hostel == 'Y':
                self.totalhostel = 200000
            elif hostel == 'N':
                self.totalhostel = 0
            else:
                raise ValidationException("answer in Y or N")
        else:
            raise ValidationException("Non alpha value inserted in hostel")

    def GetFood(self):
        '''
        Docstring for GetFood
        
        :This function checks whether student wants food and how many months
        '''
        food = input("Want food?? (Y/N): ").upper()
        if food.isalpha():
            if food == 'Y':
                food1 = int(input("Want food how many months?? "))
                if food1 < 0 or food1 > 24:
                    raise ValidationException("Months invalid")
                else:
                    self.totalfood = self.totalfood * food1
            else:
                self.totalfood = 0
        else:
            raise ValidationException("Food should be Y or N")

    def GetTransport(self):
        '''
        Docstring for GetTransport
        
        This function checks whether student wants Transport for sem or full year
        '''
        transport = input("Transport for sem or full year (1/2): ")
        if transport.isdigit():
            transport = int(transport)
            if transport == 1 or transport == 2:
                self.totaltransport = 13000 * transport
            else:
                raise ValidationException("Enter 1 for sem or 2 for full year")
        else:
            raise ValidationException("Digit is required")

    def generate_bill(self):
        """
        Docstring for generate_bill
        
        Bill is created with the details collected from above functions
        """
        try:
            total = self.totalsub+ self.totaltransport+ self.totalfood + self.totalhostel
            print("\nTotal Bill of student:")
            print("Subject Cost:", self.totalsub)
            print("Accommodation Cost:", self.totalhostel)
            print("Transport Cost:", self.totaltransport)
            print("Annual Food:", self.totalfood)
            print("Total Cost:", total)
            doyou = input("Do you want to print the bill")
            if doyou == 'Y':
                nm = input("Enter name:")
                dpath = r"C:/Users/Rovin/OneDrive/Desktop/MCA/student_bills"
                filen = f"Bill_{nm}.txt"
                filename = os.path.join(dpath,filen)
                with open(filename,'w') as f:
                    f.write("{0:<20}{1:10}\n".format("Subject Cost:",self.totalsub))
                    f.write("{0:<15}{1:15}\n".format("Accommodation Cost:", self.totalhostel))
                    f.write("{0:<15}{1:15}\n".format("Transport Cost:", self.totaltransport))
                    f.write("{0:<15}{1:15}\n".format("Annual Food:", self.totalfood))
                    f.write("{0:<15}{1:15}\n".format("Total Cost:", total))
        except:
            print(sys.exc_info())
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
