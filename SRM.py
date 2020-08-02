import sqlite3 as db
from os import system
from prettytable import PrettyTable

class Admission:

    def getRec(self):
        print("Kindly provide the following information regarding student:-")
        self.name=input("\nName:")
        self.age=int(input("\nAge:"))
        self.gender=input("\nGender:")
        print("\nChoose subject from the following options:-")
        print("\n1.C++\n2.Java\n3.Python\n4.PHP\n5.Javascript")
        self.ch=int(input("\n>"))
        
        if self.ch==1:
            self.subject="C++"
        elif self.ch==2:
            self.subject="Java"
        elif self.ch==3:
            self.subject="Python"
        elif self.ch==4:
            self.subject="PHP"
        elif self.ch==5:
            self.subject="Javascript"
        else:
            self.subject=None

        self.total_fees=self.set_total_fees()

        print("\nTotal Fees: "+str(self.total_fees))
        self.amt_paid=int(input("\nAmount Paid:"))
        
        self.batch=self.set_batch()
 
    def set_total_fees(self):
        if self.ch==1:
            fees=1000;
        elif self.ch==2:
            fees=4000;
        elif self.ch==3:
            fees=5000;
        elif self.ch==4:
            fees=3000;
        elif self.ch==5:
            fees=2000;
        else:
            print("\nInvalid Entry!")
        return fees

    def set_batch(self):
        if self.subject=="C++":
            self.bat="1st"
        elif self.subject=="Java":
            self.bat="1st"
        elif self.subject=="Python":
            self.bat="2nd"
        elif self.subject=="PHP":
            self.bat="3rd"
        elif self.subject=="Javascript":
            self.bat="3rd"
        else:
            self.bat=None
        return self.bat
    
    def printRec(self):
        system('cls')
        print("\nYou have entered the following Details:")
        print("\nName: "+self.name)
        print("\nAge: "+str(self.age))
        print("\nGender: "+self.gender)
        print("\nSubject: "+self.subject)
        print("\nBatch: "+self.batch)
        print("\nTotal Fees: "+str(self.total_fees))
        print("\nAmount Paid :"+str(self.amt_paid))
    
    def set_fee_status(self):
        self.fee_status="Paid!"
        if self.amt_paid==1000 and self.subject=="C++":
            self.pend_amt = self.total_fees-self.amt_paid
        elif self.amt_paid==2000 and self.subject=="Javascript":
            self.pend_amt = self.total_fees-self.amt_paid
        elif self.amt_paid==3000 and self.subject=="PHP":
            self.pend_amt = self.total_fees-self.amt_paid
        elif self.amt_paid==4000 and self.subject=="Java":
            self.pend_amt = self.total_fees-self.amt_paid
        elif self.amt_paid==5000 and self.subject=="Python":
            self.pend_amt = self.total_fees-self.amt_paid
        else:
            self.pend_amt = self.total_fees-self.amt_paid
            self.fee_status="Due!"

    def disp_fee_status(self):
        self.set_fee_status()
        print("\nAmount Paid: "+str(self.amt_paid))
        print("\nTotal Fees: "+str(self.total_fees))
        print("\nPending Amount: "+str(self.pend_amt))
        print("\nFee Status: "+str(self.fee_status))

    def  storeRec(self):
        ch='y'
        while ch=='Y' or ch=='y':
            con=db.connect('student.db')
            cur=con.cursor()
            system('cls')
            self.getRec()
            self.printRec()
            self.set_fee_status()
            
            query="INSERT INTO student (Name,Batch,Subject,Age,Gender,Total_Fees,Amount_Paid,Pending_Amount,Fee_Status) VALUES(:name, :batch, :sub, :age, :gen, :tf, :ap, :pa, :fs)"
            
            insert_data={
                'name':str(self.name),'batch':str(self.batch),'sub':str(self.subject),'age':self.age,'gen':str(self.gender),'tf':self.total_fees,'ap':self.amt_paid,'pa':self.pend_amt,'fs':str(self.fee_status)
                }
            cur.execute(query,insert_data)
            con.commit()
            if query:
                print("\nRecord Inserted Successfully...!")
            else:
                system('cls')
                print("\nOperation Failed...!")
            ch=input("\n\nDo you want to insert more records?(y/n):")
            if ch=='N' or ch=='n':
                input("\n\nPress Enter to go back to the main menu...!")
            con.close()
    
    def readRec(self):
        system('cls')
        con=db.connect('student.db')
        cur=con.cursor()
        query="select * from student"
        cur.execute(query)
        result=cur.fetchall()
        table=PrettyTable()
        table.field_names=["Roll Number","Name","Batch","Subject","Age","Gender","Total Fees","Amount Paid","Pending Amount","Fee Status"]
        for rec in result:
            table.add_row(rec)
        print(table)
        input("\n\nPress Enter to go back to the main menu...!")
        con.commit()
        con.close()
    
    def searchRec(self):
        ch='y'
        while ch=='y' or ch=='Y':
            system('cls')
            con=db.connect('student.db')
            cur=con.cursor()
            rno=input("Enter the Roll Number:")
            query="select * from student where Roll_Number="+rno
            cur.execute(query)
            rec=cur.fetchone()
            table=PrettyTable()
            table.field_names=["Roll Number","Name","Branch","Subject","Age","Gender","Total Fees","Amount Paid","Pending Amount","Fee Status"]
            if rec:
                table.add_row(rec)
                print(table)
            else:
                print("\nRoll Number does not exist...!")
            ch=input("\n\nDo you want to search more records?(y/n):")
            if ch=='n' or ch=='N':
                input("\nPress Enter to go back to main menu...")
            con.commit()
            con.close()
    
    def updateRec(self):
        ch='y'
        while ch=="Y" or ch=='y':
            system('cls')
            con=db.connect('student.db')
            cur=con.cursor()
           
            rno=input("Enter the Roll Number:")
            query="select * from student where Roll_Number="+rno
            cur.execute(query)
            rec=cur.fetchone()
            table=PrettyTable()
            table.field_names=["Roll Number","Name","Batch","Subject","Age","Gender","Total Fees","Amount Paid","Pending Amount","Fee Status"]
           
            if rec:
                table.add_row(rec)
                print(table)
                input("\n\nPress Enter to update the record...")
                self.getRec()
                self.printRec()
                self.set_fee_status()
                
                query="update student set Name=:name,Batch=:batch,Subject=:sub,Age=:age,Gender=:gen,Total_fees=:tf,Amount_Paid=:ap,Pending_Amount=:pa,Fee_Status=:fs where Roll_number="+rno

                insert_data={
                'name':str(self.name),'batch':str(self.batch),'sub':str(self.subject),'age':self.age,'gen':str(self.gender),'tf':self.total_fees,'ap':self.amt_paid,'pa':self.pend_amt,'fs':str(self.fee_status)
                }
                
                cur.execute(query,insert_data)
                con.commit()
                con.close()
                if query:
                    print("\nRecord Updated Successfully...!")
                else:
                    system('cls')
                    print("\nOperation Failed...!")
            else:
                print("\nRoll Number does not exist...!")
            ch=input("\n\nDo you want to update more records?(y/n):")
            if ch=='n' or ch=='N':
                input("\nPress Enter to go back to main menu...")

    def deleteRec(self):
        ch='y'
        while ch=="Y" or ch=='y':
            system('cls')
            con=db.connect('student.db')
            cur=con.cursor()
            rno=input("Enter the Roll Number:")
            
            query="select * from student where Roll_Number="+rno
            cur.execute(query)
            rec=cur.fetchone()
            table=PrettyTable()
            table.field_names=["Roll Number","Name","Batch","Subject","Age","Gender","Total Fees","Amount Paid","Pending Amount","Fee Status"]
            if rec:
                table.add_row(rec)
                print(table)
                delete=input("\nAre you sure you want to delete this record?(y/n):")
                if delete=='y' or delete=='Y':
                    query="delete from student where Roll_Number="+rno
                    cur.execute(query)
                    print("\nRecord Deleted...")
                    ch=input("\nDo you want to delete more records?(y/n):")
                    if ch=='n' or ch=='N':
                        input("\nPress Enter to go back to main menu...")

                else:
                    ch=input("\nDo you want to delete more records?(y/n):")
                    if ch=='n' or ch=='N':
                        input("\nPress Enter to go back to main menu...")
            else:
                print("\nRoll Number does not exist...!")
                ch=input("\nDo you want to delete more records?(y/n):")
                if ch=='n' or ch=='N':
                    input("\nPress Enter to go back to main menu...")
            con.commit()
            con.close()

    def pending_fees(self):
        system('cls')
        print("List of the Students with pending fees:-")
        con=db.connect('student.db')
        cur=con.cursor()
        query="select * from student where Fee_Status='Due!'"
        cur.execute(query)
        result=cur.fetchall()
        table=PrettyTable()
        table.field_names=["Roll Number","Name","Batch","Subject","Age","Gender","Total Fees","Amount Paid","Pending Amount","Fee Status"]
        for rec in result:
            table.add_row(rec)
        print(table)
        input("\n\nPress Enter to go back to the main menu...!")
        con.commit()
        con.close()