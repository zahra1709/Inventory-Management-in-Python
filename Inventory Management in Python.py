#Zahra Tasnim
#TP064447

import os
import datetime

#login details:

def login():
    while True:
        username = "Zahra_Tasnim"
        password = "ztasnim1709"

        uname = input("Enter your username: ")
        pword = input("Enter your password: ")

        if uname == username and pword == password:
            print ("--------------Entry granted--------------")
            return uname

        else:
            print("Incorrect username or password, try again.\n\n\n")
        
            
        



#writing items into inventory:
def create_inventory():
    while True:
        try:
            with open ("ppe.txt","r") as fh:
                print ("Inventory already exists.")
                file = open("ppe.txt")
                file_contents = file.read()
                print(file_contents)
                break
        except:
            print("Inventory is empty, create it.")
            with open ("ppe.txt","w") as fh:
                while True:
                    item_code = input("Enter item code: ")
                    item_name = input("Enter item name: ").title()
                    supplier_code = input("Enter supplier code: ")
                    item_num = int("100")
                    rec = item_code+" : "+item_name+" : "+supplier_code+" : "+str(item_num)
                    fh.write(rec + "\n")
                    ans = input("Do you want to add another item? Press Enter to continue, and type 'q' to stop.\n")
                    if ans.lower() == "q":
                        break
            
            
        
              

#reading ppe file:
def read_ppe():
    allrec = []
    try:
        with open ("ppe.txt","r") as rfh:
            for line in rfh:
                allrec.append(line.strip().split(" : "))
                length = len(allrec)
                
        for x in range(length-1):
            for y in range(x+1, length):
                if allrec[x][0] > allrec[y][0]:
                    temp = allrec[x]
                    allrec[x] = allrec[y]
                    allrec[y] = temp
        print("-"*95)
        print(" | " + "Item Code".center(20) + " | " + "Item Name".center(20) + " | " + "Supplier Code".center(20) + " | " + "Quantity".center(20) + " | ")
        print("-"*95)
        length = len(allrec)
        for line in range(length):
            print(" | " + allrec[line][0].center(20) + " | " + allrec[line][1].center(20) + " | " + allrec[line][2].center(20) + " | " + allrec[line][3].center(20) + " | ")
            print("-"*95)
            
    except:
        print("Inventory is empty.")
     

def update_ppe():

     import os
     allrec = []
     with open ("ppe.txt","r") as fh:
          for line in fh:
               rec = line.strip().split(" : ")
               allrec.append(rec)
          print(allrec)
     code = input("Enter item code: ")
     flg = -1
     length = len(allrec)
     for cnt in range(0, length):
          while True:
               if code in allrec[cnt][0]:
                    flg = cnt
               break
          else: 
               print("The item code entered does not exist in file.")
    
     while True:
          ans = int(input("Enter '2' for supplier, '3' for quantity."))
          if ans == int("2"):
                    new_v = input("Enter new data: ")
                    allrec[flg][ans] = new_v
                    with open ("ppe.txt","w") as fh:
                       for flg in range(len(allrec)):
                         rec = " : ".join(allrec[flg])+"\n"
                         fh.write(rec)
                         print(rec)
                    break
          
          if ans == int("3"):
                    ques = input("Are you receiving (add) or distributing (sub)?\n")
                    old = allrec[flg][3]
                    if ques == "add":
                         add = int(input("How much are you receiving?\n"))
                         new = int(old) + add
                         allrec[flg][3] = allrec[flg][3].replace(old, str(new))
                         print(allrec[flg])
                         with open("ppe.txt","w") as fh:
                              for flg in range(len(allrec)):
                                   rec = " : ".join(allrec[flg])+"\n"
                                   fh.write(rec)
                                   print(rec)
                    elif ques == "sub":
                         subt = int(input("How much are you distributing?\n"))
                         if subt > int(old):
                              print("Insufficient items in inventory.")
                              break
                         new = int(old) - subt
                         allrec[flg][3] = allrec[flg][3].replace(old, str(new))
                         print(allrec[flg])
                         with open("ppe.txt","w") as fh:
                              for flg in range(len(allrec)):
                                   rec = " : ".join(allrec[flg])+"\n"
                                   fh.write(rec)
                                   print(rec)
                                   lists = []
                                   with open ("distribution.txt","r") as fh:
                                     for line in fh:
                                       rec = line.strip().split(" : ")
                                       lists.append(rec)
        
                          
                         oldquan=int(lists[flg][3])
                         newquan= int(lists[flg][3].replace(lists[flg][3],allrec[flg][3]))
                          
                         with open ("distribution.txt","r") as fh:
                              filedata = fh.read()
                              filedata = filedata.replace(lists[flg][0]+" : "+lists[flg][1]+" : "+lists[flg][2]+" : "+str(oldquan), lists[flg][0]+" : "+lists[flg][1]+" : "+lists[flg][2]+" : "+str(newquan))
                         with open ("distribution.txt","w") as fh:
                              fh.write(filedata)
                    break
        
    
#create hospital file
def create_hospital():
    var = 0
    while var < 3:
        var += 1
        with open ("hospital.txt","a+") as fh:
            hospital_code = input("Enter hospital code: ")
            if hospital_code in open("hospital.txt").read():
                    print("Hospital has already been added to list. Add another.")
                    break
            hospital_name = input("Enter hospital name: ")
            hospital_address = input("Enter hospital address: ")
            hos_email = input("Enter email address: ")
            rec = hospital_code+" : "+hospital_name+" : "+hospital_address+" : "+hos_email
            fh.write(rec + "\n")
            ans = input("Do you want to add another hospital? Press Enter to continue, and type 'q' to stop.")
            if ans.lower() == "q":
                break
     
#read hospital
def read_hospital():
    allrec = []
    try:
        with open ("hospital.txt","r") as rfh:
            for line in rfh:
                allrec.append(line.strip().split(":"))
            length = len(allrec)

        for x in range(length-1):
            for y in range(x+1, length):
                if allrec[x][0] > allrec[y][0]:
                    temp = allrec[x]
                    allrec[x] = allrec[y]
                    allrec[y] = temp
        print("-"*145)
        print(" | " + "Hospital Code".center(20) + " | " + "Hospital Name".center(40) + " | " + "Address".center(30) + " | " + "Email".center(30) + " | " )
        print("-"*145)
        length = len(allrec)
        for line in range(length):
            print(" | " + allrec[line][0].center(20) + " | " + allrec[line][1].center(40) + " | " + allrec[line][2].center(30) + " | " + allrec[line][3].center(30) + " | ")
            print("-"*145)
    except:
         print("File is empty.")

#update hospital:
def update_hospital():
     while True:
       
            allrec = []
            with open ("hospital.txt","r") as fh:
                for line in fh:
                    rec = line.strip().split(" : ")
                    allrec.append(rec)
            code = input("Enter hospital code: ")
            flg = -1
            for cnt in range(len(allrec)):
                if code in allrec[cnt][0]:
                    flg = cnt
                    break
                else:
                    print("The hospital code entered does not exist.")
                    break
            if flg != -1:
                ans = int(input("Enter '1' if you want to update name, '2' for address, '3' for email address."))
                allrec[cnt][ans] = input("Enter new data: ")
                with open("hospital.txt","w+") as fh:
                    for cnt in range(len(allrec)):
                        rec = " : ".join(allrec[cnt])+"\n"
                        fh.write(rec)
            break
        
            
#create supplier
def create_supplier():
    var = 0
    while var < 3 :
         with open ("supplier.txt","a+") as fh:
                while True:
                    var += 1
                    supplier_code = input("Enter supplier code: ")
                    if supplier_code in open("supplier.txt").read():
                        print("This supplier is already in list.")
                        break
                    supplier_name = input("Enter supplier name: ")
                    supplier_address = input("Enter supplier address: ")
                    sup_email = input("Enter email address: ")
                    rec = supplier_code+" : "+supplier_name+" : "+supplier_address+ " : " +sup_email
                    fh.write(rec + "\n")
                    ans = input("Do you want to add another supplier? Press Enter to continue, and type 'q' to stop.")
                    if ans.lower() == "q":
                        break
                    break
#read supplier
def read_supplier():
    allrec = []
    try:
        with open ("supplier.txt","r") as rfh:
            for line in rfh:
                allrec.append(line.strip().split(":"))
            length = len(allrec)

        for x in range(length-1):
            for y in range(x+1, length):
                if allrec[x][0] > allrec[y][0]:
                    temp = allrec[x]
                    allrec[x] = allrec[y]
                    allrec[y] = temp
        print("-"*135)
        print(" | " + "Supplier Code".center(20) + " | " + "Supplier Name".center(20) + " | " + "Address".center(30) + " | " + "Email".center(30) + " | ")
        print("-"*135)
        length = len(allrec)
        for line in range(length):
            print(" | " + allrec[line][0].center(20) + " | " + allrec[line][1].center(20) + " | " + allrec[line][2].center(30) + " | " + allrec[line][3].center(30) + " | ")
            print("-"*135)
    except:
        print("File is empty.")

#update supplier:
def update_supplier():
     while True:
        allrec = []
        with open ("supplier.txt","r") as fh:
            for line in fh:
                rec = line.strip().split(" : ")
                allrec.append(rec)
        code = input("Enter supplier code: ")
        flg = -1
        for cnt in range(len(allrec)):
            if code in allrec[cnt][0]:
                flg = cnt
                break
            else:
                print("The supplier code entered does not exist.")
                break
        if flg != -1:
            ans = int(input("Enter '1' if you want to update name, '2' for address, '3' for email address."))
            allrec[cnt][ans] = input("Enter new data: ")
            with open("ppe.txt","w+") as fh:
                for cnt in range(len(allrec)):
                    rec = " : ".join(allrec[cnt])+"\n"
                    fh.write(rec)
        break

#create distribution file
def create_distribution():
    while True:
        with  open("distribution.txt", "a+") as fh:
            item_code = input("Enter item code: ")
            sup_code = input("Enter supplier code: ")
            hos_code = input("Enter code of hospital where the item is sent: ")
            quantity = int(input("Enter amount of items distributed: "))
            date = datetime.date.today()
            rec = item_code+" : "+sup_code+" : "+hos_code+" : "+str(quantity)+" : "+str(date)
            fh.write(rec+"\n")
            ans = input("Do you want to add more items? Press Enter to continue, and type 'q' to stop.")
            if ans.lower() == "q":
                    break
            

#read distribution:
def read_distribution():
    allrec = []

    with open ("distribution.txt","r+") as rfh:
        for line in rfh:
            allrec.append(line.strip().split(":"))
        length = len(allrec)

    for x in range(length-1):
        for y in range(x+1, length):
            if allrec[x][0] > allrec[y][0]:
                temp = allrec[x]
                allrec[x] = allrec[y]
                allrec[y] = temp
    print("-"*120)
    print(" | " + "Item Code".center(20) + " | " + "Supplier Code".center(20) + " | " + "Hospital Code".center(20) + " | " + "Quantity".center(20) + " | " + "Date".center(15) + " | " )
    print("-"*120)
    length = len(allrec)
    for line in range(length):
        print(" | " + allrec[line][0].center(20) + " | " + allrec[line][1].center(20) + " | " + allrec[line][2].center(20) + " | " + allrec[line][3].center(20) + " | " + allrec[line][4].center(15) + " | ")
        print("-"*120)

#Update distribution:
def update_distribution():
     import os
     allrec = []
     with open ("distribution.txt","r") as fh:
          for line in fh:
               rec = line.strip().split(" : ")
               allrec.append(rec)
          print(allrec)
     code = input("Enter item code: ")
     flg = -1
     length = len(allrec)
     for cnt in range(0, length):
          while True:
               if code in allrec[cnt][0]:
                    flg = cnt
               break
          else: 
               print("The item code entered does not exist in file.")
               
     while True:
          ans = int(input("Enter '1' if you want to update supplier code, '2' for hospital code, '3' for quantity."))
          if ans == int("1") or ans == int("2"):
                    new_v= input("Enter new data: ")
                    allrec[flg][ans] = new_v
                    with open ("distribution.txt","w") as fh:
                       for flg in range(len(allrec)):
                         rec = " : ".join(allrec[flg])+"\n"
                         fh.write(rec)
                         print(rec)
                    break
          
          if ans == int("3"):
                    dist = int(input("How much do you want to distribute?"))
                    temp = int(allrec[flg][ans])
                    new= str(int(temp+dist))
                    allrec[flg][ans] = allrec[flg][ans].replace(str(temp),new)
                    with open ("distribution.txt","w") as fh:
                         for flg in range(length):
                           rec = " : ".join(allrec[flg])+"\n"
                           fh.write(rec)
                           print(rec)
                           lists = []
                           with open ("ppe.txt","r") as fh:
                                 for line in fh:
                                   rec = line.strip().split(" : ")
                                   lists.append(rec)
        
                          
                           oldquan=int(lists[flg][3])
                           newquan= int(lists[flg][3].replace(lists[flg][3],allrec[flg][3]))
                          
                           with open ("ppe.txt","r") as fh:
                              filedata = fh.read()
                              filedata = filedata.replace(lists[flg][0]+" : "+lists[flg][1]+" : "+lists[flg][2]+" : "+str(oldquan), lists[flg][0]+" : "+lists[flg][1]+" : "+lists[flg][2]+" : "+str(newquan))
                           with open ("ppe.txt","w") as fh:
                              fh.write(filedata)
                              
                             
                    break
        
#search:

def SearchItems(file_list, skey):
    result = -1
    for cnt in range(len(file_list)):
        if skey == file_list[cnt][0]:
            result = cnt
            break
    return result


#ppe less than 25:

def ppe_less_than_25():
    try:
        allrec = []
        with open ("ppe.txt","r") as fh:
            for line in fh:
                rec = line.strip().split(" : ")
                allrec.append(rec)

        while True:
            print("Quantity of this item is less than 25: "+"\n")
            print(" | " + "Item Code".center(20) + " | " + "Supplier Code".center(20) + " | " + "Hospital Code".center(20) + " | " + "Quantity".center(20) + " | " )
            print("-"*95)
            for cnt in range(len(allrec)):
                if allrec[cnt][3] < "25":
                    print(" | " + allrec[cnt][0].center(20) + " | " + allrec[cnt][1].center(20) + " | " + allrec[cnt][2].center(20) + " | " + str(allrec[cnt][3].center(20)) + " | ")
            break
    except:
        print("Inventory is empty.")
       

        

                
                    
        





#main function:
        
while True:
    print ("\n")
    print ("\n")
    print ("\n")
    print ("__________ Welcome__________")
    print ("\n")
    print ("\n")
    login()
    print ("\n")
    print ("\n")
    print ("--------------MAIN MENU--------------")
    print ("\n")
    while True:
    
        print ("\n")
        print ("1. Create Files")
        print ("2. Read Files")
        print ("3. Update Files")
        print ("4. Search Distributon File")
        print ("5. Track Inventory")
        print ("6. Exit")
        
        Ans = input("Please choose an option: ")
        if Ans == "1":
            print("1. Create Inventory\n2. Create Hospital file\n3. Create Supplier file\n4. Create Distribution file\n5. Exit\n"+"\n")
            res = input("Please select which file you want to create: ")
            if res == "1":
                create_inventory()
            elif res == "2":
                create_hospital()
            elif res == "3":
                create_supplier()
            elif res == "4":
                create_distribution()
            elif res == "5":
                break
            else:
                print("please pick a correct number.")
        elif Ans == "2":
            print("1. Read Inventory\n2. Read Hospital details\n3. Read Supplier Details\n4. Read Distribution file\n5. Exit\n"+"\n")
            res = input("Please select which file you want to read: ")
            if res == "1":
                read_ppe()
            elif res == "2":
                read_hospital()
            elif res == "3":
                read_supplier()
            elif res == "4":
                read_distribution()
            elif res == "5":
                break
            else:
                print("please pick a correct number.")
        elif Ans == "3":
            print("1. Update Inventory\n2. Update Hospital details\n3. Update Supplier Details\n4. Update Distribution file\n5. Exit\n"+"\n")
            res = input("Please select which file you want to update: ")
            if res == "1":
                update_ppe()
            elif res == "2":
                update_hospital()
            elif res == "3":
                update_supplier()
            elif res == "4":
                update_distribution()
            elif res == "5":
                break
            else:
                print("please pick a correct number.")
        elif Ans == "4":
            file_list= []
            while True:
                try:
                    with open ("distribution.txt","r") as fh:
                        for line in fh:
                            rec = line.strip().split(" : ")
                            file_list.append(rec)
                except:
                    print("The file is empty.")

                print(file_list)
                skey = input("Enter the item code you want to search: ")
                index = SearchItems(file_list, skey)
                if index >= 0:
                    print(" | " + "Item Code".center(20) + " | " + "Supplier Code".center(20) + " | " + "Hospital Code".center(20) + " | " + "Quantity".center(20) + " | " )
                    print("-"*95)
                    print(" | " + file_list[index][0].center(20) + " | " + file_list[index][1].center(20) + " | " + file_list[index][2].center(20) + " | " + str(file_list[index][3].center(20)) + " | ")
                else:
                    print("Item not found.")
                break
        elif Ans == "5":
            print("1. Print inventory\n2. Check inventory for dwindling supplies\n3. Exit\n"+"\n")
            res = input("Please select an option: ")
            if res == "1":
                read_ppe()
            elif res == "2":
                ppe_less_than_25()
            elif res == "3":
                break
            else:
                print("please pick a correct number.")
        elif Ans == "6":
            print("Thank you.")
            break

        else:
            print("please pick a correct number.")
                    
        
            

        
        
          

