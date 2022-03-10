#  BRU_SOFT
#  A BRU quotation making system
#  This application is used to calculate the quotations of orders placed

#  define the functions used by the application
def main_menu():
    print('This is the main menu')
    print('Please select the programme you wish to run')
    user_prog_option = int(input('1: Quotation with prices\n'
                                 '2: Quotation without prices\n'
                                 '3: Product Information\n'
                                 '4: Order load information\n'))

    # Program option Quotation with prices
    if user_prog_option == 1:
        print(f'You have chosen option number {user_prog_option}: Quotation with prices')
        user_prod_name = input('Please enter the product you would like to view below: \n')
    # Program option Quotation without prices
    elif user_prog_option == 2:
        print(f'You have chosen option number {user_prog_option}: Quotation without prices')
        user_prod_name = input('Please enter the product you would like to view below: \n')
    #  Program option Product Information
    elif user_prog_option == 3:
        print(f'You have chosen option number {user_prog_option}: Product Information')
        user_prod_name = input('Please enter the product you would like to view below: \n')
    #  Program option Order load information
    elif user_prog_option == 4:
        print(f'You have chosen option number {user_prog_option}: Order load information')
        user_load_opt = int(input('Please enter the product to be calculated below: \n'
                                  '1. Classic Pavers \n2. Concrete common bricks \n3. 60mm Interlocking Paver'
                                  '4. 80mm Interlocking Paver \n5. Face bricks  \n6. Block M4 \n7. Block M6'
                                  '8. Block M9 \n9. Industrial Kerbstones \n10. Domestic Kerbstones \n11. Paving Slabs\n'
                                  '12. 3 Hole Brick \n 13. Exit\n'))
        num_pallets = int(input('Please input the number of pallets here: '
                                'For Blocks, Slabs and kerbstones enter the total number of product:\n'))
        load_order(user_load_opt, num_pallets)

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


def load_order(user_load_opt, num_pallets):
    print('You have chosen to view order load information')
    print('Below you will find the information for the load order requested')

    if user_load_opt == 1:
        print(f'You have chosen option: {user_load_opt} Classic Pavers')
        classic_paver_weight = 2.6
        # multiply weight by pallet size
        total_weight = classic_paver_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 2:
        print(f'You have chosen option: {user_load_opt} Concrete Common Bricks')
        concrete_com_weight = 3.5
        # multiply weight by pallet size
        total_weight = concrete_com_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 3:
        print(f'You have chosen option: {user_load_opt} 60mm Interlocking Paver')
        intloc_60_weight = 2.6
        # multiply weight by pallet size
        total_weight = intloc_60_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 4:
        print(f'You have chosen option: {user_load_opt} 80mm Interlocking Paver')
        intloc_80_weight = 3.5
        # multiply weight by pallet size
        total_weight = intloc_80_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 5:
        print(f'You have chosen option: {user_load_opt} Face bricks')
        facebrick_weight = 3.5
        # multiply weight by pallet size
        total_weight = facebrick_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 6:
        print(f'You have chosen option: {user_load_opt} Block M4')
        block_m4_weight = 20
        # multiply weight by pallet size
        total_weight = block_m4_weight * num_pallets
        print(f'The total weight for the {num_pallets} blocks is {total_weight} KG')
    elif user_load_opt == 7:
        print(f'You have chosen option: {user_load_opt} Block M6')
        block_m6_weight = 24
        # multiply weight by pallet size
        total_weight = block_m6_weight * num_pallets
        print(f'The total weight for the {num_pallets} blocks is {total_weight} KG')
    elif user_load_opt == 8:
        print(f'You have chosen option: {user_load_opt} Block M4')
        block_m6_weight = 33
        # multiply weight by pallet size
        total_weight = block_m6_weight * num_pallets
        print(f'The total weight for the {num_pallets} blocks is {total_weight} KG')
    elif user_load_opt == 9:
        print(f'You have chosen option: {user_load_opt} Industrial Kerbstones')
        kerbstone_weight = 90
        # multiply weight by pallet size
        total_weight = kerbstone_weight * num_pallets
        print(f'The total weight for the {num_pallets} Kerbstones is {total_weight} KG')
    elif user_load_opt == 10:
        print(f'You have chosen option: {user_load_opt} Domestic Kerbstones')
        kerbstone_weight = 45
        # multiply weight by pallet size
        total_weight = kerbstone_weight * num_pallets
        print(f'The total weight for the {num_pallets} Kerbstone is {total_weight} KG')
    elif user_load_opt == 11:
        print(f'You have chosen option: {user_load_opt} Paving Slabs')
        slabs_weight = 23
        # multiply weight by pallet size
        total_weight = slabs_weight * num_pallets
        print(f'The total weight for the {num_pallets} blocks is {total_weight} KG')
    elif user_load_opt == 12:
        print(f'You have chosen option: {user_load_opt} 3 Hole Facebrick')
        brick_weight = 3
        # multiply weight by pallet size
        total_weight = brick_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets of bricks is {total_weight} KG')
    elif user_load_opt == 13:
        exit_option()
    else:
        print('You have selected an invalid option, Please try again')


def exit_option():
    print('Confirm you want to exit? \n 1: - Exit \n 2: Cancel')
    # requesting a users input and converting it into an integer using the int() function
    confirm_exit = int(input('Option here: '))
    if confirm_exit == 1:
        print('Goodbye, Thank you for using this Bricks R Us application')
        return exit(0)

    else:
        print('Welcome back to the application')


#  Print introduction to application
print('Welcome to the BRU App')
main_menu()
