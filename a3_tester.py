# Aaryan Sharma
# 101230220

import a3

def main():
    
    while True:
        
        print("\n1.   Load File\n2.   Display database\n3.  Diplay Dictionary\n4.   Show total cases by dates (0), age groups (1), genders(2)\n5.   Display data for a PHU\n6.  Show total cases in PHUs by age groups\n7.  Show total cases for top-x hotspots\n8.  Quit the Program.")
        action = int(input("\nSelect a number between 1-8: "))

        if action == 1:
            filename = input("Enter a file name: ")
            filename = "Assignment 3/" + filename
            
            if filename == 'Assignment 3/data10.csv' or filename == 'Assignment 3/data25.csv' or filename == 'Assignment 3/data50.csv':

                a3.return_dict(filename)
                a3.return_list(filename)
                dicti = a3.return_dict(filename)
                database = a3.return_list(filename)
                print("Data Loaded Successfully")
            else:
                print("File does not exist.")
        
        elif action == 2:
            a3.display_2Dlist(database)

        elif action == 3:
            a3.dispaly_dict(dicti)

        elif action == 4:
            x = int(input("Please enter what category you want to search by: "))
            a3.get_total_cases(database,x)
        
        elif action == 5:
            id = int(input("Please enter an id: "))
            a3.display_PHU_summary(database,dicti,id)
        
        elif action == 6:
            a3.get_cases_by_PHU_and_age(database,dicti)


        elif action == 7:
            print("\nData not displayable, our apologies for any inconvenience.")     #wasn't able to create a function for this problem unfortunately



        elif action == 8:
            break

    print("Thank you for using this program.")


if __name__ == "__main__":
    main()           



