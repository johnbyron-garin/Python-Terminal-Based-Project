# John Byron C. Garin
# Final Project

eventscheduler = {}
event_initializer = 0

supplierrecords = {}
supplier_initializer = 0

todolist = {}
todolist_initializer = 0

months_of_the_year = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December',
}

eventscheduler_filename = "eventscheduler.csv"
supplierrecords_filename = "supplierrecords.csv"
todolist_filename = "todolist.csv"
key_filename = "key.csv"

filehandle = open(eventscheduler_filename,'a+')
filehandle.close()

filehandle = open(supplierrecords_filename,'a+')
filehandle.close()

filehandle = open(todolist_filename,'a+')
filehandle.close()

filehandle = open(key_filename,'a+')
filehandle.close()

def section_menu():
    print("""
       _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._
    .-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.
    (                                                                             )
     )    Sections:                                                              (
    (                                                                             )
     )    [1] Event Scheduler                                                    (
    (                                                                             )
     )    [2] Supplier Records Section                                           (
    (                                                                             )
     )    [3] TODO list Section                                                  ( 
    (                                    /^-----^\                                ) 
     )    [4] Overview                   V  o o  V             /\_____/\         (
    (                                     |  Y  |             /  o   o  \         )
     )    [5] Save                         \ Q /             ( ==  ^  == )       (
    (                                      / - \              )         (         )
     )    [6] Load                         |    \            (           )       (
    (                                      |     \     )    ( (  )   (  ) )       )
     )    [0] Exit                         || (___\====    (__(__)___(__)__)     (
    (                                                                             )
     )                                                                           (
    (___       _       _       _       _       _       _       _       _       ___)
        (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)
        ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )
        (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)
        (_ ___) `-._.-'                                         `-._.-' (___ _)
        `-._.-'                                                         `-._.-'
    """)

    section = int(input("Choice: "))
    return section

def menu_event():
    print("""

       _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._
    .-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.
     )                                                                           (
    (                                Options:                                     )
     )                                                                           (
    (        [1] Add event                       [4] View Event                   )
     )                                                                           (
    (                                                                             )
     )       [2] Delete event                    [5] View All Events             (
    (                                                                             )
     )                                                                           (
    (        [3] Delete all events               [0] Return                       )
     )                                                                           (
    (                                                                             )
     )                                                                           (
    (___       _       _       _       _       _       _       _       _       ___)
        `-._.-' (___ _) (__ _ ) (_   _) (__  _) ( __ _) (__  _) (__ _ ) `-._.-'
                `-._.-' (  ___) ( _  _) ( _ __) (_  __) (__ __) `-._.-'
                        `-._.-' (__  _) (__  _) (_ _ _) `-._.-'
                                `-._.-' (_ ___) `-._.-'
                                        `-._.-'
    """)
    choice = int(input("Choice: "))
    return choice

def menu_supplier():
    print("""

    .-=~=-.                                                                 .-=~=-.
    (__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)
    ( _ __)                                                                 ( _ __)
    (__  _)                             Options:                            (__  _)
    (_ ___)                                                                 (_ ___)
    (__  _)                         [1] Add Record                          (__  _)
    ( _ __)                                                                 ( _ __)
    (__  _)                                                                 (__  _)
    (_ ___)                        [2] Delete Record                        (_ ___)
    (__  _)                                                                 (__  _)
    ( _ __)                                                                 ( _ __)
    (__  _)                      [3] Delete all Records                     (__  _)
    (_ ___)                                                                 (_ ___)
    (__  _)                                                                 (__  _)
    ( _ __)                         [4] View Record                         ( _ __)
    (__  _)                                                                 (__  _)
    (_ ___)                                                                 (_ ___)
    (__  _)                       [5] View All Records                      (__  _)
    ( _ __)                                                                 ( _ __)
    (__  _)                                                                 (__  _)
    ( _ __)                           [0] Return                            ( _ __)
    (__  _)                                                                 (__  _)
    (_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)
    `-._.-'                                                                 `-._.-'
    """)

    choice = int(input("Choice: "))
    return choice

def menu_todolist():
    print("""
                .-"-,-"-.          .-"-,-"-.          .-"-,-"-.
          _.-._(         ).-._.-._(         ).-._.-._(         ).-._
        .'_.-._.`.     .'_.-._.-._.`.     .'_.-._.-._.`.     .'_.-._`.
       ( (        `._.'              `._.'              `._.'       ) )
        ) )                                                        ( (
    .-"-,-"-.                    Options:                       .-"-,-"-.
    (         )                                                (         )
    `.     .'                                                   `.     .'
    `._.'                      [1] Add Item                       `._.'
        ) )                                                        ( (
       ( (                                                          ) )
        ) )                                                        ( (
    .-"-,-"-.                [2] Mark as Done                    .-"-,-"-.
    (         )                                                 (         )
    `.     .'                                                   `.     .'
    `._.'                                                       `._.'
        ) )                   [3] View Item                        ( (
       ( (                                                          ) )
        ) )                                                        ( (
    .-"-,-"-.                                                    .-"-,-"-.
    (         )             [4] View All Items                  (         )
    `.     .'                                                    `.     .'
    `._.'                                                          `._.'
        ) )                                                         ( (
       ( (                      [0] Return                           ) )
        ) )                                                         ( (
    .-"-,-"-.                                                   .-"-,-"-.
    (         )                                                 (         )
    `.     .'                                                   `.     .'
    `._.'                                                       `._.'
        ( (                                                          ) )
         ) )     .-"-,-"-.          .-"-,-"-.          .-"-,-"-.    ( (
        ( (_.-._(         ).-._.-._(         ).-._.-._(         ).-._) )
         `._.-._.`.     .'_.-._.-._.`.     .'_.-._.-._.`.     .'_.-._,'
                   `._.'              `._.'              `._.'
    """)
    choice = int(input("Choice: "))
    return choice

def divider():
    print("\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.")

def overview(event_date):
    q = 0
    for eventID in eventscheduler.keys():
        if eventscheduler[eventID]['Date'] == event_date:
            eventscheduler_start_time = eventscheduler[eventID]['Start Time']
            eventscheduler_end_time = eventscheduler[eventID]['End Time']
            eventscheduler_title = eventscheduler[eventID]['Title']
            eventscheduler_supplier_list = eventscheduler[eventID]['Supplier List']
            eventscheduler_description = eventscheduler[eventID]['Description']
            eventscheduler_suppliers = ""
            for elements in eventscheduler_supplier_list:
                if elements != eventscheduler_supplier_list[-1]:
                    eventscheduler_suppliers += elements + ", "
                elif elements == eventscheduler_supplier_list[-1]:
                    eventscheduler_suppliers += elements
            print("\n(" + event_date + ")")
            print("\nAt " + eventscheduler_start_time + " - " + eventscheduler_end_time + ", this event (" + eventID + "), entitled, " + "'" + eventscheduler_title + "', will be about '" + eventscheduler_description + "'\nThe supplier/s, particularly, " + eventscheduler_suppliers + " is/are the one that will be involved in the event")
        
            for todolistID in todolist.keys():
                todolist_associated_event = todolist[todolistID]['Associated Event']
                if todolist_associated_event == eventscheduler_title:
                    todolist_title = todolist[todolistID]['Title']
                    todolist_content = todolist[todolistID]['Content']
                    todolist_associated_supplier = todolist[todolistID]['Associated Supplier']
                    print("\nThe associated event, '" + eventscheduler_title +  "', together with the associated supplier '" + todolist_associated_supplier + "', is also associated to the To Do list (" + todolistID + "), entitled, '" + todolist_title + "', in which its content will be about '" + todolist_content + "'")
            q += 1
        divider()
    if q == 0:
        print("\nNo current plans for this date")
        divider()
    elif q > 0:
        print("\n------------There is/are already " + str(q) + " event/s that will be happening in this date------------")
        divider()

def add_event():                         
    global event_initializer
    event_initializer += 1
    if event_initializer < 10:
        ID = ("E00" + str(event_initializer))
    elif event_initializer >= 10 and event_initializer < 100:
        ID = ("E0" + str(event_initializer))
    elif event_initializer >= 100 and event_initializer < 1000:
        ID = ("E" + str(event_initializer))
    
    divider()
    year = int(input("\nInput year: "))
    divider()

    print("\n< < < Input only the numbers that corresponds to the month of your choice > > >")

    month_validator = False
    while month_validator == False:
        month = int(input("\nInput month: "))
        divider()
        if month < 1 or month > 12:
            month_validator = False
            print("\n! ! ! Invalid Month ! ! ! ")
        else:
            month_validator = True

    if year%4 == 0:
        if month == 2:
            day_validator = False
            while day_validator == False:
                day = int(input("\nInput day: "))
                divider()
                if day < 1 or day > 29:
                    day_validator = False
                    print("\n! ! ! Invalid Day ! ! ! ")
                else:
                    day_validator = True
        
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day_validator = False
            while day_validator == False:
                day = int(input("\nInput day: "))
                divider()
                if day < 1 or day > 31:
                    day_validator = False
                    print("\n! ! ! Invalid Day ! ! ! ")
                else:
                    day_validator = True
        
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day_validator = False
            while day_validator == False:
                day = int(input("\nInput day: "))
                divider()
                if day < 1 or day > 30:
                    day_validator = False
                    print("\n! ! ! Invalid Day ! ! ! ")
                else:
                    day_validator = True

    else:
        if month == 2:
            day_validator = False
            while day_validator == False:
                day = int(input("\nInput day: "))
                divider()
                if day < 1 or day > 28:
                    day_validator = False
                    print("\n! ! ! Invalid Day ! ! ! ")
                else:
                    day_validator = True
        
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day_validator = False
            while day_validator == False:
                day = int(input("\nInput day: "))
                divider()
                if day < 1 or day > 31:
                    day_validator = False
                    print("\n! ! ! Invalid Day ! ! ! ")
                else:
                    day_validator = True
        
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day_validator = False
            while day_validator == False:
                day = int(input("\nInput day: "))
                divider()
                if day < 1 or day > 30:
                    day_validator = False
                    print("\n! ! ! Invalid Day ! ! ! ")
                else:
                    day_validator = True

    event_date = months_of_the_year[month] + " " + str(day) + " " + str(year)

    am_pm_list = ["am", "pm"]

    print("\n< < < Input the time that the event will start > > >")
    hour_start_validator = False
    while hour_start_validator == False:
        hour_start = int(input("\nInput hour: "))
        divider()
        if hour_start < 1 or hour_start > 12:
            hour_start_validator = False
            print("\n! ! ! Invalid Hour ! ! ! ")
        else:
            hour_start_validator = True

    minutes_start_validator = False
    while minutes_start_validator == False:
        minutes_start = int(input("\nInput minutes: "))
        divider()
        if minutes_start < 0 or minutes_start > 59:
            minutes_start_validator = False
            print("\n! ! ! Invalid Minutes ! ! ! ")
        else:
            minutes_start_validator = True

    am_pm_start = input("\nInput AM or PM: ")
    divider()
    while am_pm_start.lower() not in am_pm_list:
        print("\n! ! ! Invalid Input ! ! ! ")
        am_pm_start = input("\nInput AM or PM: ")
        divider()
    
    if minutes_start < 10:
        event_start_time = str(hour_start) + ":0" + str(minutes_start) + " " + am_pm_start
    elif minutes_start >= 10:
        event_start_time = str(hour_start) + ":" + str(minutes_start) + " " + am_pm_start

    print("\n< < < Input the time that the event will end > > >")
    hour_end_validator = False
    while hour_end_validator == False:
        hour_end = int(input("\nInput hour: "))
        divider()
        if hour_end < 1 or hour_end > 12:
            hour_end_validator = False
            print("\n! ! ! Invalid Hour ! ! ! ")
        else:
            hour_end_validator = True

    minutes_end_validator = False
    while minutes_end_validator == False:
        minutes_end = int(input("\nInput minutes: "))
        divider()
        if minutes_end < 0 or minutes_end > 59:
            minutes_end_validator = False
            print("\n! ! ! Invalid Minutes ! ! !")
        else:
            minutes_end_validator = True
    
    am_pm_end = input("\nInput AM or PM: ")
    divider()
    while am_pm_end.lower() not in am_pm_list:
        print("\n! ! ! Invalid Input ! ! ! ")
        am_pm_end = input("\nInput AM or PM: ")
        divider()

    if minutes_end < 10:
        event_end_time = str(hour_end) + ":0" + str(minutes_end) + " " + am_pm_end
    elif minutes_end >= 10:
        event_end_time = str(hour_end) + ":" + str(minutes_end) + " " + am_pm_end

    title = input("\nInput the event title: ")
    divider()

    supplier_list = []
    print("\n< < < So far, these are the existing records in the supplier records section > > >")
    viewall_supplier()
    
    supplier_count_validator = False
    while supplier_count_validator == False:
        supplier_count = int(input("\nInput the number of supplier you wanted to include in the list: "))
        divider()
        if supplier_count > len(supplierrecords):
            supplier_count_validator = False
            print("\n! ! ! The number of supplier you wanted to include in the list exceeds the number of available supplier records ! ! !")
        elif supplier_count == 0:
            supplier_count_validator = False
            print("\n! ! ! The number of supplier can't be 0 ! ! !")
        else:
            supplier_count_validator = True

    count = 0
    supplier_name_list = []
    while count < supplier_count:
        supplier = input("\nInput the supplier record's name you want to add: ")
        divider()
        for keys in supplierrecords.keys():
            supplier_name = supplierrecords[keys]['Name']
            supplier_name_list.append(supplier_name)

        while supplier not in supplier_name_list:
            print("\n! ! ! The record name does not exist in the supplier records section ! ! !")
            supplier = input("\nInput the supplier record's name you want to add: ")
            divider()
        
        if supplier not in supplier_list:
            supplier_list.append(supplier)
            count += 1
        else:
            print("\nYour input is already part of the supplier list, please input a different supplier")
    
    description = input("\n(Description) The event will be about: ")
    divider()
    nested_addevent = {'Date' : event_date, 'Start Time' : event_start_time, 'End Time' : event_end_time, 'Title' : title, 'Supplier List' : supplier_list, 'Description' : description}
    eventscheduler[ID] = nested_addevent

def add_supplier():                         
    global supplier_initializer
    supplier_initializer += 1
    if supplier_initializer < 10:
        ID = ("S00" + str(supplier_initializer))
    elif supplier_initializer >= 10 and supplier_initializer < 100:
        ID = ("S0" + str(supplier_initializer))
    elif supplier_initializer >= 100 and supplier_initializer < 1000:
        ID = ("S" + str(supplier_initializer))
    
    divider()
    name = input("\nInput name: ")
    divider()

    supplier_type = ["food", "sounds", "manpower", "management"]

    print("\nChoose among these supplier types: \n - Food \n - Sounds \n - Manpower \n - Management")
    supplier = input("\nInput supplier type: ")
    divider()

    while supplier.lower() not in supplier_type:
        print("\n! ! ! Invalid input ! ! ! ")
        supplier = input("\nInput supplier type: ")
        divider()

    address = input("\nInput the address: ")
    divider()

    description = input("\nInput the supplier description: ")
    divider()

    nested_addsupplier = {'Name' : name, 'Supplier' : supplier, 'Address' : address, 'Description' : description}
    supplierrecords[ID] = nested_addsupplier

def add_todo():                         
    global todolist_initializer
    todolist_initializer += 1
    if todolist_initializer < 10:
        ID = ("T00" + str(todolist_initializer))
    elif todolist_initializer >= 10 and todolist_initializer < 100:
        ID = ("T0" + str(todolist_initializer))
    elif todolist_initializer >= 100 and todolist_initializer < 1000:
        ID = ("T" + str(todolist_initializer))
    
    divider()
    title = input("\nInput title: ")
    divider()
    content = input("\n(Content) The To Do List item will be about: ")
    divider()

    print("\n< < < So far, these are the existing events in the event scheduler > > >")
    viewall_event()

    associated_event = input("\nInput associated event's title: ")
    divider()
    eventscheduler_title_list = []
    for events in eventscheduler.keys():
        eventscheduler_title = eventscheduler[events]['Title']
        eventscheduler_title_list.append(eventscheduler_title)
    while associated_event not in eventscheduler_title_list:
        print("\n! ! ! Associated event does not exist in the event scheduler ! ! !")
        associated_event = input("\nInput associated event's title: ")
        divider()
    
    print("\n< < < So far, these are the existing records in the supplier records section > > >")
    viewall_supplier()

    associated_supplier = input("\nInput associated supplier record's name: ")
    divider()
    supplierrecords_name_list = []
    for suppliers in supplierrecords.keys():
        supplierrecords_name = supplierrecords[suppliers]['Name']
        supplierrecords_name_list.append(supplierrecords_name)
    while associated_supplier not in supplierrecords_name_list:
        print("\n! ! ! Associated supplier record does not exist in the supplier records section ! ! !")
        associated_supplier = input("\nInput associated supplier record's name: ")
        divider()

    nested_addtodo = {'Title' : title, 'Content' : content, 'Associated Event' : associated_event, 'Associated Supplier' : associated_supplier}
    todolist[ID] = nested_addtodo

def delete_eventschedule(eventscheduler, todolist):
    divider()
    print("\n< < < If you wish to delete a record that is present in a To Do List's Associated Supplier, the To Do List Item itself will also be deleted > > >")
    delete = (input("\nInput the ID you wish to delete: "))
    divider()
    to_be_deleted = []
    if delete in eventscheduler.keys():
        event_title = eventscheduler[delete]['Title']
        for keys in todolist.keys():
            associated_event = todolist[keys]['Associated Event']
            if event_title == associated_event:
                to_be_deleted.append(keys)
                print("\n(" + keys + ") has been removed due to having '" + associated_event + "' as its associated event")
        for items in to_be_deleted:
            del todolist[items]
        del eventscheduler[delete]
        print("\n(" + delete + ") successfully deleted.")
        divider()
    else:
        print("\n! ! ! Sorry, the record does not exist ! ! !")
        divider()

def deleteall_eventschedule(eventscheduler, todolist):
    divider()
    eventscheduler.clear()
    todolist.clear()
    global event_initializer
    event_initializer = 0
    global todolist_initializer
    todolist_initializer = 0
    divider()
    print("\nAll entries were successfully deleted!")
    print("\nAll To Do list items were also deleted since Associated Event Schedules are now non-existent")

def delete_supplierrecord(supplierrecords, eventscheduler, todolist):
    divider()
    print("\n< < < If you wish to delete a record that is present in the Supplier List inside an Event Schedule, the supplier will be removed from the list > > >")
    print("< < < If you wish to delete a record that is present in a To Do List's Associated Supplier, the To Do List Item itself will also be deleted > > >")
    delete = (input("\nInput the ID you wish to delete: "))
    divider()
    if delete in supplierrecords.keys(): 
        supplier_name = supplierrecords[delete]['Name']
        for keys in eventscheduler.keys():
            eventscheduler_supplierlist = eventscheduler[keys]['Supplier List']
            for elements in eventscheduler_supplierlist:
                if supplier_name == elements:
                    eventscheduler_supplierlist.remove(elements)
                    print("\n'" + elements + "' has been removed from (" + keys + ")'s supplier list")

        to_be_deleted = []
        for items in todolist.keys():
            associated_supplier = todolist[items]['Associated Supplier']
            if supplier_name == associated_supplier:
                to_be_deleted.append(items)
                print("\n(" + items + ") has been removed due to having '" + associated_supplier + "' as its associated supplier")
        for items in to_be_deleted:
            del todolist[items]

        del supplierrecords[delete]
        print("\n(" + delete + ") successfully deleted.")
        divider()

        delete_event = []
        for k in eventscheduler.keys():
            supplier_list = eventscheduler[k]['Supplier List']
            if len(supplier_list) == 0:
                delete_event.append(k)
                print("\nBecause the supplier list of (" + k + ") is already empty, the event will be deleted.")

                delete_todolist = []
                for q in delete_event:
                    event_title = eventscheduler[q]['Title']
                    for j in todolist.keys():
                        associated_event = todolist[j]['Associated Event']
                        if event_title == associated_event:
                            delete_todolist.append(j)
                            print("\nTo Do List (" + j + ") that uses (" + k + ") as its Associated Event will also be deleted") 
                for d in delete_todolist:
                    del todolist[d]
        for e in delete_event:
            del eventscheduler[e]
    else:
        print("\n! ! ! Sorry, the record does not exist ! ! !")
        divider()

def deleteall_supplierrecord(supplierrecords, eventscheduler, todolist):
    divider()
    supplierrecords.clear()
    eventscheduler.clear()
    todolist.clear()
    global event_initializer
    event_initializer = 0
    global supplier_initializer
    supplier_initializer = 0
    global todolist_initializer
    todolist_initializer = 0
    divider()                 
    print("\nAll entries were successfully deleted!")
    print("\nBecause all Supplier Records are deleted, all of the Event Schedules were also deleted since the suppliers in their list are now non-existent")
    print("\nAll To Do list items were also deleted since both Associated Event Schedules and Associated Event Suppliers are now non-existent")

def markasdone():
    divider()
    done = (input("\nInput the ID you wish to mark as done: "))
    divider()
    if done in todolist.keys(): 
        del todolist[done]
        print("\n(" + done + ") successfully marked as done.")
        divider()
    else:
        print("\n! ! ! Sorry, the item does not exist ! ! !")
        divider()

def view_event():   
    divider()             
    view = input("\nInput the event ID you wish to view: ")
    divider()
    if view in eventscheduler.keys():   
        eventscheduler_date = eventscheduler[view]['Date']
        eventscheduler_start_time = eventscheduler[view]['Start Time']
        eventscheduler_end_time = eventscheduler[view]['End Time']
        eventscheduler_title = eventscheduler[view]['Title']
        eventscheduler_supplier_list = eventscheduler[view]['Supplier List']
        eventscheduler_description = eventscheduler[view]['Description']
        print("\n===================== E v e n t  I n f o r m a t i o n =====================\n")
        print("Date: " + eventscheduler_date)
        print("Time: " + eventscheduler_start_time + " - " + eventscheduler_end_time)
        print("Title: " + eventscheduler_title)
        supplier_names = ""
        for elements in eventscheduler_supplier_list:
            if elements != eventscheduler_supplier_list[-1]:
                supplier_names += elements + ", "
            elif elements == eventscheduler_supplier_list[-1]:
                supplier_names += elements
        print("Supplier List: " + supplier_names)
        print("Description: " + eventscheduler_description)
        divider()
    else:
        print("\n! ! ! Sorry, the event does not exist ! ! !")
        divider()

def viewall_event():  
    if len(eventscheduler) > 0:  
        print("\n========================== E v e n t  S c h e d u l e s ==========================")                                       
        for k in eventscheduler: 
            eventscheduler_date = eventscheduler[k]['Date']
            eventscheduler_start_time = eventscheduler[k]['Start Time']
            eventscheduler_end_time = eventscheduler[k]['End Time']
            eventscheduler_title = eventscheduler[k]['Title']
            eventscheduler_supplier_list = eventscheduler[k]['Supplier List']
            eventscheduler_description = eventscheduler[k]['Description']
            print("\n(" + k + ")")
            print("Date: " + eventscheduler_date)
            print("Time: " + eventscheduler_start_time + " - " + eventscheduler_end_time)
            print("Title: " + eventscheduler_title)
            supplier_names = ""
            for elements in eventscheduler_supplier_list:
                if elements != eventscheduler_supplier_list[-1]:
                    supplier_names += elements + ", "
                elif elements == eventscheduler_supplier_list[-1]:
                    supplier_names += elements
            print("Supplier List: " + supplier_names)
            print("Description: " + eventscheduler_description)
            divider()
    elif len(eventscheduler) == 0: 
        print("\nThere are no entries yet")

def view_supplier():  
    divider()              
    view = input("\nInput the supplier ID you wish to view: ")
    divider()
    if view in supplierrecords.keys():   
        supplierrecords_name = supplierrecords[view]['Name']
        supplierrecords_supplier = supplierrecords[view]['Supplier']
        supplierrecords_address = supplierrecords[view]['Address']
        supplierrecords_description = supplierrecords[view]['Description']
        print("\n===================== S u p p l i e r  R e c o r d  I n f o r m a t i o n =====================\n")
        print("Name: " + supplierrecords_name)
        print("Supplier: " + supplierrecords_supplier)
        print("Address: " + supplierrecords_address)
        print("Description: " + supplierrecords_description)
        divider()
    else:
        print("\n! ! ! Sorry, the supplier does not exist ! ! !")
        divider()
    
def viewall_supplier():  
    if len(supplierrecords) > 0:    
        print("\n=========================== S u p p l i e r  R e c o r d s ===========================")                                     
        for k in supplierrecords: 
            supplierrecords_name = supplierrecords[k]['Name']
            supplierrecords_supplier = supplierrecords[k]['Supplier']
            supplierrecords_address = supplierrecords[k]['Address']
            supplierrecords_description = supplierrecords[k]['Description']
            print("\n(" + k + ")")
            print("Name: " + supplierrecords_name)
            print("Supplier: " + supplierrecords_supplier)
            print("Address: " + supplierrecords_address)
            print("Description: " + supplierrecords_description)
            divider()
    elif len(supplierrecords) == 0: 
        print("\nThere are no entries yet")

def view_todo():
    divider()         
    view = input("\nInput the to do list ID you wish to view: ")
    divider()
    if view in todolist.keys():   
        todolist_title = todolist[view]['Title']
        todolist_content = todolist[view]['Content']
        todolist_associated_event = todolist[view]['Associated Event']
        todolist_associated_supplier = todolist[view]['Associated Supplier']
        print("\n======================= T o  D o  L i s t  I n f o r m a t i o n =======================\n")
        print("Title: " + todolist_title)
        print("Content: " + todolist_content)
        print("Associated Event: " + todolist_associated_event)
        print("Associated Supplier: " + todolist_associated_supplier)
        divider()
    else:
        print("\n! ! ! Sorry, either the item does not exist or the item was already marked as done ! ! !")
        divider()
    
def viewall_todo():    
    if len(todolist) > 0:
        print("\n============================= T o  D o  L i s t  I t e m s =============================")
        for k in todolist: 
            todolist_title = todolist[k]['Title']
            todolist_content = todolist[k]['Content']
            todolist_associated_event = todolist[k]['Associated Event']
            todolist_associated_supplier = todolist[k]['Associated Supplier']
            print("\n(" + k + ")")
            print("Title: " + todolist_title)
            print("Content: " + todolist_content)
            print("Associated Event: " + todolist_associated_event)
            print("Associated Supplier: " +  todolist_associated_supplier)
            divider()
    elif len(todolist) == 0: 
        print("\nThere are no entries yet")
    
def save_eventscheduler():
    fileHandle = open(eventscheduler_filename,"w")
    for k in eventscheduler:
        eventscheduler_date = eventscheduler[k]['Date']
        eventscheduler_start_time = eventscheduler[k]['Start Time']
        eventscheduler_end_time = eventscheduler[k]['End Time']
        eventscheduler_title = eventscheduler[k]['Title']
        eventscheduler_supplier_list = eventscheduler[k]['Supplier List']
        eventscheduler_description = eventscheduler[k]['Description']
        for element in eventscheduler_supplier_list:
            fileHandle.write(element + "\n")
        fileHandle.write(k + "," + eventscheduler_date + "," + eventscheduler_start_time + "," + eventscheduler_end_time + "," + eventscheduler_title + "," + eventscheduler_description + "\n")
    fileHandle.close()

def load_eventscheduler():
    fileHandle = open(eventscheduler_filename,"r")
    eventscheduler.clear()
    supplier = []
    for line in fileHandle:
        event_data = line[:-1].split(",")
        x = len(event_data)
        if x > 1:
            eventID = event_data[0]
            eventscheduler_date = event_data[1]
            eventscheduler_start_time = event_data[2]
            eventscheduler_end_time = event_data[3]
            eventscheduler_title = event_data[4]
            eventscheduler_description = event_data[5]
            nested_eventscheduler = {}
            nested_eventscheduler['Date'] = eventscheduler_date
            nested_eventscheduler['Start Time'] = eventscheduler_start_time
            nested_eventscheduler['End Time'] = eventscheduler_end_time
            nested_eventscheduler['Title'] = eventscheduler_title
            nested_eventscheduler['Supplier List'] = supplier
            nested_eventscheduler['Description'] = eventscheduler_description
            eventscheduler[eventID] = nested_eventscheduler
            supplier = []
        elif x == 1:
            eventscheduler_supplier_list = event_data[0]
            supplier.append(eventscheduler_supplier_list)
    fileHandle.close()

def save_supplierrecords():
    fileHandle = open(supplierrecords_filename,"w")
    for k in supplierrecords:
        supplierrecords_name = supplierrecords[k]['Name']
        supplierrecords_supplier = supplierrecords[k]['Supplier']
        supplierrecords_address = supplierrecords[k]['Address']
        supplierrecords_description = supplierrecords[k]['Description']
        fileHandle.write(k + "," + supplierrecords_name + "," + supplierrecords_supplier + "," + supplierrecords_address + "," + supplierrecords_description + "\n")
    fileHandle.close()

def load_supplierrecords():
    fileHandle = open(supplierrecords_filename,"r")
    supplierrecords.clear()
    for line in fileHandle:
        supplier_data = line[:-1].split(",")
        supplierID = supplier_data[0]
        supplierrecords_name = supplier_data[1]
        supplierrecords_supplier = supplier_data[2]
        supplierrecords_address = supplier_data[3]
        supplierrecords_description = supplier_data[4]
        nested_supplierrecords = {}
        nested_supplierrecords['Name'] = supplierrecords_name
        nested_supplierrecords['Supplier'] = supplierrecords_supplier
        nested_supplierrecords['Address'] = supplierrecords_address
        nested_supplierrecords['Description'] = supplierrecords_description
        supplierrecords[supplierID] = nested_supplierrecords
    fileHandle.close()

def save_todolist():
    fileHandle = open(todolist_filename,"w")
    for k in todolist:
        todolist_title = todolist[k]['Title']
        todolist_content = todolist[k]['Content']
        todolist_associated_event = todolist[k]['Associated Event']
        todolist_associated_supplier = todolist[k]['Associated Supplier']
        fileHandle.write(k + "," + todolist_title + "," + todolist_content + "," + todolist_associated_event + "," + todolist_associated_supplier + "\n")
    fileHandle.close()

def load_todolist():
    fileHandle = open(todolist_filename,"r")
    todolist.clear()
    for line in fileHandle:
        todolist_data = line[:-1].split(",")
        todolistID = todolist_data[0]
        todolist_title = todolist_data[1]
        todolist_content = todolist_data[2]
        todolist_associated_event = todolist_data[3]
        todolist_associated_supplier = todolist_data[4]
        nested_todolist = {}
        nested_todolist['Title'] = todolist_title
        nested_todolist['Content'] = todolist_content
        nested_todolist['Associated Event'] = todolist_associated_event
        nested_todolist['Associated Supplier'] = todolist_associated_supplier
        todolist[todolistID] = nested_todolist
    fileHandle.close()

def event():
    while True:
        c = menu_event()
        if c == 1:
            add_event()
        elif c == 2:
            delete_eventschedule(eventscheduler, todolist)
        elif c == 3:
            deleteall_eventschedule(eventscheduler, todolist)                 
        elif c == 4:
            view_event()
        elif c == 5:
            viewall_event()
        elif c == 0:
            break
        else:
            print("\n! ! ! Invalid Input ! ! ! ")

def supplier():
    while True:
        c = menu_supplier()
        if c == 1:
            add_supplier()
        elif c == 2:
            delete_supplierrecord(supplierrecords, eventscheduler, todolist)
        elif c == 3:
            deleteall_supplierrecord(supplierrecords, eventscheduler, todolist)
        elif c == 4:
            view_supplier()
        elif c == 5:
            viewall_supplier()
        elif c == 0:
            break
        else:
            print("\n! ! ! Invalid Input ! ! ! ")

def todolistitems():
    while True:
        c = menu_todolist()
        if c == 1:
            add_todo()
        elif c == 2:
            markasdone()
        elif c == 3:
            view_todo()
        elif c == 4:
            viewall_todo()
        elif c == 0:
            break
        else:
            print("\n! ! ! Invalid Input ! ! ! ")

def Encrypt_Decrypt(key, filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open (filename, "wb")
    file.write(data)
    file.close()

def load_key():
    fileHandle = open(key_filename,"r")
    for line in fileHandle:
        key_data = line[:-1].split(",")
        key_end = int(key_data[0])
    fileHandle.close()
    return key_end

def save_key(key_end):
    fileHandle = open(key_filename,"w")
    fileHandle.write(str(key_end) + "\n")
    fileHandle.close()

fileHandle = open(key_filename,"r")
zxc = 0
for line in fileHandle:
    zxc += 1
if zxc == 0:
    key_end = int(input("\nInput an integer between 1-255 to be used as the key for your encrypted files: "))
    divider()
    while key_end < 1 or key_end > 255:
        print("\n! ! ! Invalid Input ! ! ! ")
        key_end = int(input("\nInput an integer between 1-255 to be used as the key for your encrypted files: "))
        divider()
    save_key(key_end)
elif zxc != 0:
    key_end = load_key()
fileHandle.close()

Encrypt_Decrypt(key_end, eventscheduler_filename)
Encrypt_Decrypt(key_end, supplierrecords_filename)
Encrypt_Decrypt(key_end, todolist_filename)

while True:
    c = section_menu()
    if c == 1:
        if len(supplierrecords) != 0:
            event()
        else:
            print("\nSupplier Records must contain records first before proceeding onto creating Event Schedules")
    elif c == 2:
        supplier()
    elif c == 3:
        if len(eventscheduler) != 0 and len(supplierrecords) != 0:
            todolistitems()
        elif len(eventscheduler) == 0 or len(supplierrecords) == 0:
            print("\nBoth Event Scheduler and Supplier Records must contain records first before proceeding onto creating To Do List Items")
    elif c == 4:
        if len(eventscheduler) > 0:
            divider()
            year = int(input("\nInput year you wish to overview: "))
            divider()
            print("\n< < < Input only the numbers that corresponds to the month of your choice > > >")
            month_validator = False
            while month_validator == False:
                month = int(input("\nInput month you wish to overview: "))
                divider()
                if month < 1 or month > 12:
                    month_validator = False
                    print("\n! ! ! Invalid Month ! ! ! ")
                else:
                    month_validator = True

            if year%4 == 0:
                if month == 2:
                    day_validator = False
                    while day_validator == False:
                        day = int(input("\nInput day you wish to overview: "))
                        divider()
                        if day < 1 or day > 29:
                            day_validator = False
                            print("\n! ! ! Invalid Day ! ! ! ")
                        else:
                            day_validator = True
                
                elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    day_validator = False
                    while day_validator == False:
                        day = int(input("\nInput day you wish to overview: "))
                        divider()
                        if day < 1 or day > 31:
                            day_validator = False
                            print("\n! ! ! Invalid Day ! ! ! ")
                        else:
                            day_validator = True
                
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    day_validator = False
                    while day_validator == False:
                        day = int(input("\nInput day you wish to overview: "))
                        divider()
                        if day < 1 or day > 30:
                            day_validator = False
                            print("\n! ! ! Invalid Day ! ! ! ")
                        else:
                            day_validator = True

            else:
                if month == 2:
                    day_validator = False
                    while day_validator == False:
                        day = int(input("\nInput day you wish to overview: "))
                        divider()
                        if day < 1 or day > 28:
                            day_validator = False
                            print("\n! ! ! Invalid Day ! ! ! ")
                        else:
                            day_validator = True
                
                elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    day_validator = False
                    while day_validator == False:
                        day = int(input("\nInput day you wish to overview: "))
                        divider()
                        if day < 1 or day > 31:
                            day_validator = False
                            print("\n! ! ! Invalid Day ! ! ! ")
                        else:
                            day_validator = True
                
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    day_validator = False
                    while day_validator == False:
                        day = int(input("\nInput day you wish to overview: "))
                        divider()
                        if day < 1 or day > 30:
                            day_validator = False
                            print("\n! ! ! Invalid Day ! ! ! ")
                        else:
                            day_validator = True
            event_date = months_of_the_year[month] + " " + str(day) + " " + str(year)
            print("\n============================== O V E R V I E W ======================================")
            overview(event_date)

        elif len(eventscheduler) == 0:
            print("\nEvent Scheduler has no entries yet, try to put some first")
    elif c == 5:
        save_eventscheduler()
        print("\nEvent Schedules were successfully saved to file " + "(" + str(len(eventscheduler)) + " entries)" )

        save_supplierrecords()
        print("Supplier Records were successfully saved to file " + "(" + str(len(supplierrecords)) + " entries)" )

        save_todolist()
        print("To Do List items were successfully saved to file " + "(" + str(len(todolist)) + " entries)" )
    elif c == 6:
        load_eventscheduler()
        print("\nEvent Schedules were successfully loaded from the file " + "(" + str(len(eventscheduler)) + " entries)" )
        event_initializer = len(eventscheduler)

        load_supplierrecords()
        print("Supplier Records were successfully loaded from the file " + "(" + str(len(supplierrecords)) + " entries)" )
        supplier_initializer = len(supplierrecords)

        load_todolist()
        print("To Do List items were successfully loaded from the file " + "(" + str(len(todolist)) + " entries)" )
        todolist_initializer = len(todolist)
    elif c == 0:
        print("""
                                                .''.       
            .''.      .        *''*    :_\/_:     . 
            :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
        .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
        :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
        : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
        '..'  ':::'     * /\ *     .'/.\'.   '
            *            *..*         :
            *
                *
        """)
        print("\n\t\tThank you for using this program!\n")
        break
    else:
        print("\n! ! ! Invalid input ! ! ! ")

Encrypt_Decrypt(key_end, eventscheduler_filename)
Encrypt_Decrypt(key_end, supplierrecords_filename)
Encrypt_Decrypt(key_end, todolist_filename)