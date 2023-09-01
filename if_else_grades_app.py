# Stanich, Oliva 
# This app is called if_else_grades_app
# This app has you enter a student's first and last name and their GPA 
# entering ZZZ will have the app quit 
# the app will output a message saying if the student has made it on the Dean's list, honor roll, or if they don't qualify for either 

def main():
    while True:
        last_name = input("Enter student's last name or 'ZZZ' to quit: ")

        if last_name == 'ZZZ':
            break
        elif last_name == 'zzz':
            break

        first_name = input("Please enter a student's first name: ")

        while True:
            try:
                GPA = float(input("Please enter the student's GPA: "))
                if 0.0 <= GPA <= 4.0:
                    break
                else:
                    print("That's an Invalid GPA. Please enter a value between 0.0 and 4.0")
            except ValueError:
                print("Invalid GPA. Please enter a valid GPA.")

        if GPA >= 3.5:
            print(f"Congratulations! {first_name} {last_name} has made the Dean's List!")
        elif GPA >= 3.25:
            print(f"Congratulations! {first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")

        print()


if __name__ == "__main__":
    main()