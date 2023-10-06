library_members = [] #makes list

def register_member(name): #adds names to list
    return library_members.append(name), print("Congratulations " + name + "! You are now a library member.")

def find_member(name): #checks if name is on list
    if name in library_members:
        print(name + " is a member.")
    else:
        print(name + " is not a member.")
    return

def display_members():
    print(library_members)
    return
