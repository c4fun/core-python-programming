db = {}

def time_stamp():

def new_subscriber():
    name_validated = False
    while name_validated == False:
        prompt = "Input the user name:"
        name = input(prompt)
        if name in db:
            prompt = "Name taken. Use another"
        else:
            name_validated = True
    while True:
        first_time_pwd = input("Please input your password: ")
        second_time_pwd = input("Input your password again to confirm:")
        if first_time_pwd == second_time_pwd:
            db[name] = first_time_pwd
            #todo Set timestamp
            break;
        else:
            print("Password in the first time and the second time is not the same",
                  "Input again.")

def old_subscriber():
    name = input("login name: ")
    pwd = input("login password: ")
    real_pwd = db.get(name)
    if real_pwd == pwd:
        #todo Use timestamp to judge if it is logged in somewhere else
        print("Login successful. Welcome back,", name)
        #todo Set timestamp
    else:
        print("Wrong username/password combination")


def show_menu():
    prompt = """
(N)ew customer Login
(E)xisting customer Login
(Q)uit
Enter choice: """
    exit_flag = False
    while exit_flag == False:
        choice = ''
        
        chosen = False
        while chosen == False:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print("\nYou've picked the [%s] choice"%(choice))
            if choice not in 'neq':
                print("Wrong choice. Please input N or E or Q")
                chosen = False
            else:
                chosen = True

        if choice == 'q':   exit_flag = True
        if choice == 'n':   new_subscriber()
        if choice == 'e':   old_subscriber()
                


if __name__ == '__main__':
    show_menu()
