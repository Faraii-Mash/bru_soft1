#  BRU_SOFT
#  A BRU quotation making system
#  This application is used to calculate the quotations of orders placed
#  import

import csv
import pandas as pd

#  define the functions used by the application

def main_menu():
    print('This is the main menu')
    print('Please select the programme you wish to run')
    user_prog_option = int(input('1: Quotation with prices\n'
                                 '2: Quotation without prices\n'
                                 '3: Product Information\n'
                                 '4: Order load information\n'
                                 '5: Exit\n'))
    # Program option Quotation with prices
    if user_prog_option == 1:
        print(f'You have chosen option number {user_prog_option}: Quotation with prices')
        user_prod_name = input('Please enter the product you would like to view below: \n')
    # Program option Quotation without prices
    elif user_prog_option == 2:
        print(f'You have chosen option number {user_prog_option}: Quotation without prices')
        quote_noprice()
    #  Program option Product Information

    elif user_prog_option == 3:
        data = pd.read_csv('bru_prod_specs.csv')
        print(data)

    #  Program option Order load information
    elif user_prog_option == 4:
        print(f'You have chosen option number {user_prog_option}: Order load information')
        load_order()
    #  Program option EXit
    elif user_prog_option == 5:
        exit_option()
    # Program invalid option
    else:
        print('You have selected an invalid option, Please insert a valid option and try again')
        main_menu()


def prod_info():
    print('Product informaiton below')
    file = open('bru_prod_specs.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    file.close()

def quote_priced():
    print('You have chosen to generate a quotation with prices')
    print('You have chosen to generate a quantity report')
    # setting the constants
    labour = 3.50
    quarry_dust = 0.05
    customer_name = input('Please enter the Customer name below: \n')
    area_measured = int(input('Please enter the area to be covered (in Sqaure metres) below: \n'))
    user_load_opt = int(input('Please enter the product to be calculated below: \n'
                              '1. Interlocking Pavers (60mm 80mm) \n2. Round Dumbell Pavers \n3. Hexagon Pavers '
                              '4. Rectangular Pavers \n5. Dog Bone Pavers \n6. Bone Pavers \n7. Z Shape Pavers '
                              '8. Clover Pavers \n9. Star Pavers  \n10. Exit\n'))
    split = int(input('Number of colors chosen (1,2 or 3)'))


def quote_noprice():
    print('You have chosen to generate a quantity report')
    #setting the constants
    quarry_dust = 0.05
    customer_name = input('Please enter the Customer name below: \n')
    area_measured = int(input('Please enter the area to be covered (in Sqaure metres) below: \n'))
    user_load_opt = int(input('Please enter the product to be calculated below: \n'
                              '1. Interlocking Pavers (60mm 80mm) \n2. Round Dumbell Pavers \n3. Hexagon Pavers '
                              '4. Rectangular Pavers \n5. Dog Bone Pavers \n6. Bone Pavers \n7. Z Shape Pavers '
                              '8. Clover Pavers \n9. Star Pavers  \n10. Exit\n'))
    split = int(input('Number of colors chosen (1,2 or 3)\n'))
    bricks_per_m = [50, 42, 62, 50, 50, 50, 42, 62, 50]
    total_pavers = area_measured * bricks_per_m[user_load_opt - 1]
    total_quarry_dust = quarry_dust * area_measured
    pallets = total_pavers/500
    if split == 1:
        print('Below is your Quantity report')
        print(f'Customer Name: {customer_name} \n'
              f'The total bricks required are {total_pavers} \n'
              f'The total Quarry dust needed is {total_quarry_dust} cubic metres \n'
              f'The number of pallets is {pallets} \n')
        menu_option = int(input('Do you wish to return to: \n1. Return to main menu \n2. Exit\n'))
        if menu_option == 1:
            main_menu()
        elif menu_option == 2:
            exit_option()
        else:
            print('You have selected an invalid option. Please try again')
            main_menu()
    elif split == 2:
        working_paver = 0
        working_paver = total_pavers / 2
        print('Below is your Quantity report')
        print(f'Customer Name: {customer_name} \n'
              f'The bricks required are {working_paver} per color and {total_pavers} total pavers\n'
              f'The total Quarry dust needed is {total_quarry_dust} cubic metres \n'
              f'The number of pallets is {pallets} \n')
        menu_option = int(input('Do you wish to return to: \n1. Return to main menu \n2. Exit\n'))
        if menu_option == 1:
            main_menu()
        elif menu_option == 2:
            exit_option()
        else:
            print('You have selected an invalid option. Please try again')
            main_menu()
    elif split == 3:
        working_paver = 0
        working_paver = total_pavers / 3
        print('Below is your Quantity report')
        print(f'Customer Name: {customer_name} \n'
              f'The bricks required are {working_paver} per color and {total_pavers} total pavers\n'
              f'The total Quarry dust needed is {total_quarry_dust} cubic metres \n'
              f'The number of pallets is {pallets} \n')
        menu_option = int(input('Do you wish to return to: \n1. Return to main menu \n2. Exit\n'))
        if menu_option == 1:
            main_menu()
        elif menu_option == 2:
            exit_option()
        else:
            print('You have selected an invalid option. Please try again')
            main_menu()


def load_order():
    user_load_opt = int(input('Please enter the product to be calculated below: \n'
                              '1. Classic Pavers \n2. Concrete common bricks \n3. 60mm Interlocking Paver'
                              '4. 80mm Interlocking Paver \n5. Face bricks  \n6. Block M4 \n7. Block M6'
                              '8. Block M9 \n9. Industrial Kerbstones \n10. Domestic Kerbstones \n'
                              '11. Paving Slabs\n12. 3 Hole Brick \n13. Exit\n'))
    # start option
    if user_load_opt == 1:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Classic Pavers')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        classic_paver_weight = 2.6
        # multiply weight by pallet size
        total_weight = classic_paver_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 2:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Concrete Common Bricks')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        concrete_com_weight = 3.5
        # multiply weight by pallet size
        total_weight = concrete_com_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 3:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} 60mm Interlocking Paver')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        intloc_60_weight = 2.6
        # multiply weight by pallet size
        total_weight = intloc_60_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 4:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} 80mm Interlocking Paver')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        intloc_80_weight = 3.5
        # multiply weight by pallet size
        total_weight = intloc_80_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 5:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Face bricks')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        facebrick_weight = 3.5
        # multiply weight by pallet size
        total_weight = facebrick_weight * 500 * num_pallets
        print(f'The total weight for the {num_pallets} pallets is {total_weight} KG')
    elif user_load_opt == 6:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Block M4')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        block_m4_weight = 20
        # multiply weight by pallet size
        total_weight = block_m4_weight * num_pallets
        print(f'The total weight for the {num_pallets} blocks is {total_weight} KG')
    elif user_load_opt == 7:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Block M6')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        block_m6_weight = 24
        # multiply weight by pallet size
        total_weight = block_m6_weight * num_pallets
        print(f'The total weight for the {num_pallets} blocks is {total_weight} KG')
    elif user_load_opt == 8:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Block M4')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        block_m6_weight = 33
        # multiply weight by pallet size
        total_weight = block_m6_weight * num_pallets
        print(f'The total weight for the {num_pallets} blocks is {total_weight} KG')
    elif user_load_opt == 9:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Industrial Kerbstones')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        kerbstone_weight = 90
        # multiply weight by pallet size
        total_weight = kerbstone_weight * num_pallets
        print(f'The total weight for the {num_pallets} Kerbstones is {total_weight} KG')
    elif user_load_opt == 10:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Domestic Kerbstones')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        kerbstone_weight = 45
        # multiply weight by pallet size
        total_weight = kerbstone_weight * num_pallets
        print(f'The total weight for the {num_pallets} Kerbstone is {total_weight} KG')
    elif user_load_opt == 11:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} Paving Slabs')
        num_pallets = int(input('Please input the number of pallets here: \n'))
        slabs_weight = 23
        # multiply weight by pallet size
        total_weight = slabs_weight * num_pallets
        print(f'The total weight for the {num_pallets} blocks is {total_weight} KG')
    elif user_load_opt == 12:
        print('Below you will find the information for the load order requested')
        print(f'You have chosen option: {user_load_opt} 3 Hole Facebrick')
        num_pallets = int(input('Please input the number of pallets here: \n'))
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
        main_menu()

#  Print introduction to application
print('Welcome to the BRU App')

main_menu()
