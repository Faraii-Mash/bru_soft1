#  BRU_SOFT
#  A BRU quotation making system
#  This application is used to calculate the quotations of orders placed

#  define the functions used by the application
def main_menu(user_prog_option):
    print('This is the main menu')
    user_prog_option = int(user_prog_option)
    # Program option Quotation with prices
    if user_prog_option == 1:
        print(f'You have chosen option number {user_prog_option}: Quotation with prices')
    # Program option Quotation without prices
    elif user_prog_option == 2:
        print(f'You have chosen option number {user_prog_option}: Quotation without prices')
    #  Program option Product Information
    elif user_prog_option == 3:
        print(f'You have chosen option number {user_prog_option}: Product Information')
    #  Program option Order load information
    elif user_prog_option == 4:
        print(f'You have chosen option number {user_prog_option}: Order load information')
    #  Program option EXit
    elif user_prog_option == 5:
        exit_option()
    # Program invalid option
    else:
        print('You have selected an invalid option, Please insert a valid option and try again')


def prod_info(user_prod_name):
    print(f'You have chosen to view information on the {user_prod_name} product')


def quote_priced():
    print('You have chosen to generate a quotation with prices')


def quote_noprice():
    print('You have chosen to generate a quotation with prices')


def load_order():
    print('You have chosen to view order load information')
    print('Below you will find the information for the load order requested')


def exit_option():
    print('Confirm you want to exit? \n 1: - Exit \n 2: Cancel')
    # requesting a users input and converting it into an integer using the int() functio
    confirm_exit = int(input('Option here: '))
    if confirm_exit == 1:
        print('Goodbye, Thank you for using this Bricks R Us application')
        return exit(0)

    else:
        print('Welcome back to the application')


#  Print introduction to application
print('Welcome to the BRU App')
print('Please select the programme you wish to run')
user_prog_option = input('1: Quotation with prices\n'
                         '2: Quotation without prices\n'
                         '3: Product Information\n'
                         '4: Order load information\n')

user_prod_name = input('Please enter the product you would like to view below: \n')
main_menu(user_prog_option)
