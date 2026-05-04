# اسم المشروع  نظام دفاتر العناوين 
#الفكرة الأساسية لهذا المشروع كانت بناء تطبيق لإدارة جهات الاتصال، يتيح للمستخدم القيام بعدة عمليات برمجية ذكية:

""" مع تصنيفها (Family / Personal / Work). : ضافة جهات اتصال جديدة

البحث الذكي: سواء من خلال الاسم أو رقم الهاتف.

التحقق من البيانات: البرنامج كان يتأكد من عدم تكرار رقم الهاتف لمنع الأخطاء.

الحذف والتعديل: إمكانية مسح جهة اتصال معينة باستخدام الاسم أو الرقم.

عرض البيانات: إظهار قائمة كاملة بجميع الأسماء المخزنة."""
contacts = [ ]
while True:
  print("Welcome to our Address book, please to find what you want")
  print("1.Add new contact ")
  print("2.Search by name ")
  print("3.Search by number ")
  print("4.Delete contact by name")
  print("5.Delete contact by number.")
  print("6.Show all contacts.")
  print("7.Exit.")
  choice=int(input("Please to enter your choice: "))
  if choice==1 : 
    name = input("Enter name: ")
    contact_type = input("Family / Personal / Work : ").capitalize()
    if contact_type not in ["Family", "Personal", "Work"]:
     contact_type = "Other"
    number=input("Enter the number : ")
    used = False
    for c in contacts :
       if number == c["number"]:
          used = True
          break
    if  used :
        print(" Error: This number already exists!")
    else:
      contact = {
        "name": name,
        "type": contact_type,
        "number" : number
  }
      contacts.append(contact)
      print("Process Success: Contact added successfully.")

  elif choice == 2:
    search_name=input("Enter name to search : ").lower( )
    found = False
    for c in contacts :
       if search_name in c["name"].lower():
         print("contact found ")
         print("Name: ",c["name"])
         print("Number:",c["number"])
         print("contact type :" , c["type"])
         found = True
    if not found :
        print("contact not found")
  elif choice == 3:
     search_number=input("Enter the number to search : ")
     found = False
     for c in contacts :
        if c["number"]==search_number:
           print(" contact found ")
           print("Name :", c["name"])
           print("Number :" , c["number"])
           found = True
           break
     if not found:
           print("contact not found")
  elif choice == 4 :
    del_name = input (" Enter the name to delete : ")
    found = False 
    for c in contacts :
       if c["name"] == del_name :
          contacts.remove(c)
          found = True 
    if found:
           print("All matching contacts deleted")
    else: 
          print ("contact not found")
          
  elif choice == 5:
     del_number= input (" Enter the number to delete : ")
     found = False
     for c in contacts :
        if c["number"]== del_number:
           contacts.remove(c)
           print("contact was deleted ")
           found = True
           break
     if not found :
           print ("contact not found")
  elif choice == 6:
      if not contacts:
            print("The address book is empty.")
      for c in contacts:
       print(c)

  elif choice == 7 :
     print ( "Goodbye ^-^ ")  
     break
  else :
     print("Error: Invalid choice.") 

     

     
     
     


  



   
     

    

