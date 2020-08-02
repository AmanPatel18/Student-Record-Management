import SRM
import sys
import time
from Color_Console import *
from os import system

adm=SRM.Admission()

key='y'
while key=='y' or key=='Y':     
    system('cls')
    color(text="black",bg="light red")
    print("\nMain Menu:")
    print("\n1. Insert Records")
    print("\n2. View Records")
    print("\n3. Delete Records")
    print("\n4. Search Records")
    print("\n5. Update Records")
    print("\n6. Pending Fees")
    print("\n7. Exit")
    ch=int(input("\nEnter your choice:"))
    if ch==1:
        color(text="white",bg="purple")
        adm.storeRec()
    elif ch==2:
        color(text="green",bg="black")
        adm.readRec()
    elif ch==3:
        color(text="red",bg="black")
        adm.deleteRec()
    elif ch==4:
        color(text="black",bg="light green")
        adm.searchRec()
    elif ch==5:
        color(text="black",bg="red")
        adm.updateRec()
    elif ch==6:
        color(text="yellow",bg="black")
        adm.pending_fees()
    elif ch==7:
        ch=input("\nDo you want to exit?(y/n):")
        if ch=='y' or ch=='Y':
            print("\nThankyou for using our application...!\n\nProgrammed By: Aman Patel")
            time.sleep(2)
            sys.exit()
        else:
            input("\nPress Enter to continue....")
    else:
        input("\nInvalid Entry! Press Enter to continue...")