import os
import pyodbc
import datetime
import sys
server = 'DESKTOP-F4N5O36\SQLEXPRESS' 
database = 'hotel_bill'
driver = '{ODBC Driver 17 for SQL Server}'
class OrderException(Exception):
    pass 
class Admin:
    @staticmethod
    def connect_db():
        try:
            conn = pyodbc.connect(f'DRIVER={driver};'
                                f'SERVER={server};'
                                f'DATABASE={database};'
                                f'Trusted_Connection=yes;')
            return conn
        except:
            print(sys.exc_info())

class Order:
    def generate_bill(s,cursor,cusid):
        try:
            s.i = 1
            final_amt = 0
            query = "SELECT m.menu_name,o.quantity,m.menu_price from Orders o Join menu m on o.menu_id = m.menu_id where o.customer_id = ?"
            d = cursor.execute(query,cusid)
            print(f"{'-'*45}")
            print("{0:<30}{1:<5}".format("Bill for user id: ",cusid))
            print(f"{'-'*45}")
            print("{0:<5}{1:<20}{2:<10}{3:<10}".format("sr","item","quantity","price"))
            print(f"{'-'*45}")
            for row in d:
                total = row[1]*row[2]
                print("{0:<5}{1:<20}{2:<10}{3:<10}".format(s.i,row[0],row[1],total))
                s.i = s.i + 1
                final_amt = final_amt + total
            print(f"{'-'*45}")
            print("{0:<35}{1:<5}".format("Total Bill Amt:",final_amt))
            print(f"{'-'*45}")
        except:
            print(sys.exc_info())

    def print_bill(s,cursor,cusid,phno):
        try:
            dpath = "C:/Users/Rovin/OneDrive/Desktop/MCA/newone"
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
            file = f'Bill_{phno}.txt'
            file_name = os.path.join(dpath,file)
            with open(file_name, 'w') as f:
                f.write(timestamp+'\n')
                f.write(f'{'-'*45}'+'\n')
                f.write(f"Bill for user id: {cusid}\n")
                query = "SELECT m.menu_name,o.quantity,m.menu_price from Orders o Join menu m on o.menu_id = m.menu_id where o.customer_id = ?"
                d = cursor.execute(query,cusid)
                f.write(f'{'-'*45}'+'\n')
                f.write("{0:<5}{1:<20}{2:<10}{3:<10}\n".format("sr","item","quantity","price"))
                f.write(f'{'-'*45}'+'\n')
                final_amt = 0
                s.i = 1
                for row in d:
                    total = row[1]*row[2]
                    f.write("{0:<5}{1:<20}{2:<10}{3:<10}\n".format(s.i,row[0],row[1],total))
                    s.i = s.i + 1
                    final_amt = final_amt + total
                f.write(f'{'-'*45}'+'\n')
                f.write("{0:<30}{1:<10}\n".format("Total Bill Amt:",final_amt))
                f.write(f'{'-'*45}'+'\n')
            print("Saved file as:",file_name)
            os.startfile(file_name)
        except:
            print(sys.exc_info())

    def create_id(self,cursor,cusid):
        cursor.execute("INSERT INTO Customers(customer_id) Values(?)",(cusid,))

    def insert_order(self,cursor,menu_id,customer_id,quantity,timestamp):
        cursor.execute("INSERT INTO Orders(quantity,menu_id,timestamp,customer_id) Values(?,?,?,?)",(quantity,menu_id,timestamp,customer_id))

    def display_bill(self,cursor,cusid):
        doyou = input("Do you want to print the bill(1) or display the bill(0)?:")
        phno = input("Please Provide phone number:")
        if doyou == '0':
            self.generate_bill(cursor,cusid)
        else:
            self.print_bill(cursor,cusid,phno)

    def validname(s):
        od1 = input("Enter menu item:")
        if od1.isalpha():
            return od1
        else:
            raise OrderException("Value is not in valid format")

    def get_order_info(self):
        try:
            conn = Admin.connect_db()
            cursor = conn.cursor()
            c = cursor.execute("Select count(*) from Customers").fetchone()[0]
            cusid = c + 1
            self.create_id(cursor,cusid)
            conn.commit()
            val = 1
            while val == 1:
                query = "SELECT * from hotel_bill.dbo.menu"
                cursor.execute(query)
                d = cursor.fetchall()
                for row in d:
                    print(row[1],row[2])
                od1 = self.validname()
                for row in d:
                    if row[1] == od1:
                        quantity = int(input("Enter quantity:"))
                        timestamp = datetime.datetime.now()
                        menu_id = row[0]
                        customer_id = cusid
                        self.insert_order(cursor,menu_id,customer_id,quantity,timestamp)
                        conn.commit()
                val = int(input("Want to order more? 1 for yes and 0 for no:"))
            self.display_bill(cursor,cusid)
        except:
            print(sys.exc_info())
        finally:
            conn.close()

od = input("Do you want to order something:(Y/N):")
if od == "Y":
    storder = Order()
    storder.get_order_info()
else:
    print("Thank you for visiting")