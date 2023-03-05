import time

def main():
    SQFT_PER_ACRE = 43560
    
    length = float(input("Enter the field in feet: "))
    width = float(input("Enter the width in feet: "))

    acres = length * width / SQFT_PER_ACRE

    time.sleep(1)
    
    print("The area of the field is", acres, "acres")
    
main()

def cal_again():
    again = input('Do you want to calculate again? y/n ')

    if again == 'y':
        main()
        
    elif again == 'n':
        print('Goodbye')
        exit()

cal_again()
