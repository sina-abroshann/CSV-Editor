# %%
csv_file = 'Actor_Contact_book.csv'
with open('Actor_Contact_book.csv', 'r') as f:
    lst = []
    csv_reader = f.readlines()
    for row in csv_reader[1:]:
        new_row = row.split(',')
        ID = new_row[0]
        ContactCategory = new_row[1]
        FirstName = new_row[2]
        LastName = new_row[3]
        Cell = new_row[4]
        Tell = new_row[5]
        Email = new_row[6]
        instagram = new_row[7]
        Other = new_row[8]
        lst.append([ID, ContactCategory, FirstName, LastName, Cell, Tell, 
                    Email, instagram, Other])
# %%
def Insert_data():
    print('Insert data')
    ID = input('id:')
    ContactCategory = input('ContactCategory:')
    FirstName = input('FirstName:')
    LastName = input('LastName:')
    Cell = input('Cell:')
    Tell = input('Tell:')
    Email = input('Email:')
    instagram = input('instagram:')
    Other = input('Other:')
    lst.append([ID, ContactCategory, FirstName, LastName, Cell, Tell, 
                Email, instagram, Other])
    print(lst)
    return lst
# %%
def Edit():
    print('which id do you like edit?')
    edit_id = int(input('id:'))
    for i in range(len(lst)):
        row = lst[i]
        id = int(row[0])
        if edit_id == id:
            ID_i = input('ID:')
            ContactCategory = input('ContactCategory:')
            FirstName = input('FirstName:')
            LastName = input('LastName:')
            Cell = input('Cell:')
            Tell = input('Tell:')
            Email = input('Email:')
            instagram = input('instagram:')
            Other = input('Other:')
            lst[edit_id-1][0] = str(ID_i)
            lst[edit_id-1][1] = str(ContactCategory)
            lst[edit_id-1][2] = str(FirstName)
            lst[edit_id-1][3] = str(LastName)
            lst[edit_id-1][4] = str(Cell)
            lst[edit_id-1][5] = str(Tell)
            lst[edit_id-1][6] = str(Email)
            lst[edit_id-1][7] = str(instagram)
            lst[edit_id-1][8] = str(Other)
            print(lst)
    return lst
# %%
def Rm_by_name():
    print('which name do you like remove?')
    rm_name = str(input('name:'))
    for i in range(len(lst)-1):
        row = lst[i]
        name = row[2]
        id = int(row[0])
        if rm_name == name:
            lst.pop(i)
            print(lst)
    return 0
# %%
def Rm_by_id():
    print('which id do you like remove?')
    rm_id = int(input('id:'))
    for i in range(len(lst)):
        row = lst[i]
        id = int(row[0])
        if rm_id == id:
            lst.pop(id-1)
            print(lst)
    return lst
# %%
def Search_by_name():
    print('search by name?')
    search_name = input('name:')
    for i in range(len(lst)):
        row = lst[i]
        name = row[2]
        if search_name == name:
            print(lst[i])
            return lst[i]
# %%
def Search_by_id():
    print('search by id?')
    search_id = input('id:')
    for i in range(len(lst)):
        row = lst[i]
        id = row[0]
        if search_id == id:
            print(lst[i])
            return lst[i]
# %%
def Gen_search():
    print('General Search')
    search = input('word:')
    for i in range(len(lst)):
        new_row = lst[i]
        ID = new_row[0]
        ContactCategory = new_row[1]
        FirstName = new_row[2]
        LastName = new_row[3]
        Cell = new_row[4]
        Tell = new_row[5]
        Email = new_row[6]
        instagram = new_row[7]
        Other = new_row[8]
        if search in ID or search in ContactCategory or search in  FirstName or search in  LastName or search in  Cell or search in  Tell or search in  Email or search in  instagram or search in Other:
            print(lst[i])
            return lst[i]
# %%
i=1
while i>=1:
    print('1.add a single contact manually')
    print('2.edit a single contact manually')
    print('3.remove a contact by name')
    print('4.remove a contact by ID')
    print('5.search by name')
    print('6.search by ID')
    print('7.general search')
    print('8.print list')
    print('9.save to csv')
    print('0.Exit')
    i = int(input('Please select 1 to 7:'))
    if i == 1:
        Insert_data()
    elif i == 2:
        Edit()
    elif i == 3:
        Rm_by_name()
    elif i == 4:
        Rm_by_id()
    elif i == 5:
        Search_by_name()
    elif i == 6:
        Search_by_id()
    elif i == 7:
        Gen_search()
    elif i == 8:
        print(lst)
    elif i == 9:
        name = 'test.csv'
        name = input('name of file(test.csv): ')
        with open(name, 'w') as file:
            file.write('ID,ContactCategory,FirstName,LastName,Cell,Tell,Email,instagram,Other/Notes\n')
            for sublist in lst:
                for item in sublist:
                    file.write(str(item) + ',')
                # file.write('\n')
    elif i == 0:
        exit;