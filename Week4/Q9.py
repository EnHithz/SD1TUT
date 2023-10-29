
for choice in range(1,5):
    
    try:
        choice = int(input("Select an option (1-4): "))
        
        if choice == 1:
            print("1 selected")
        elif choice == 2:
            print("2 selected")
        elif choice == 3:
            print("3 selected")
        elif choice == 4:
            print("Quit selected")
            break  # Exit the loop if '4' is selected
        else:
            print("Option not recognized")
    except ValueError:
        print("Invalid input. Please enter an integer (1-4).")