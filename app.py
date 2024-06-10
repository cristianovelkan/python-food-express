import os

def show_app_name():
    
    print('Food Express')

def show_menu():
    print('1. Create Restaurant')
    print('2. Get Restaurant')
    print('3. Activate Restaurant')
    print('4. Logout\n')
    
def finish_app():
    os.system('cls')
    print('Logout successfully')
    
def choose_option():
    option = int(input('Choose an option:'))
    
    if option == 1:
        print('Create Restaurant')
    elif option == 2:
        print('Get Restaurant')        
    elif option == 3:
        print('Activate Restaurant')
    else:
        finish_app()
    # print(f'You selected option {option}')
    
def main():
    show_app_name()
    show_menu()
    choose_option()
    
if __name__ == '__main__':
    main()
