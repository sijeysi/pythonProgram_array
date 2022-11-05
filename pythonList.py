print("\n")
print("PROGRAMMED BY: Crystal Jane Cadimas")
print("Course/Year:   BSCOE 2-2")

numList = [1, 3, 3, 4, 9, 16, 81, 72, 3, 100, 25, 27, 36, 49, 58, 64, 72, 81, 96, 100]


def main():
    def menu():
        print("\n\n", "-" * 20, "MAIN MENU", "-" * 20)
        print("What would you like to do?\n")
        print("[a] Add an Integer")
        print("[b] Delete an Integer")
        print("[c] Total Number of Integers")
        print("[d] Minimum and Maximum Integer")
        print("[e] Appearance Count of an Integer")
        print("[f] Sum of the Integers")
        print("[g] Reverse the Arrangement")
        print("[h] Ascending and Descending Order of Integers")
        print("[i] Exit Program")

    menu()
    menu = str(input("\nChoose an option: ").lower())

    if menu in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"):
        if menu == "a":
            def add():
                print("\n\n***** ADD AN INTEGER *****")
                addInt = int(input("Enter an integer to add in existing list: "))
                numList.append(addInt)
                print(numList)

                addAgain = input("\nWould you like to add another integer, yes or no?: ")
                if addAgain.lower() == "yes":
                    add()
                elif addAgain.lower() == "no":
                    main()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            add()

        elif menu == "b":
            def delete():
                print("\n\n***** DELETE AN INTEGER *****")
                print(numList, "\n")
                deleteInt = int(input("Enter an integer to delete in existing list: "))
                numList.remove(deleteInt)
                print(numList)

                deleteAgain = input("\nWould you like to add another integer, yes or no?: ")
                if deleteAgain.lower() == "yes":
                    delete()
                elif deleteAgain.lower() == "no":
                    main()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            delete()

        elif menu == "c":
            def total():
                print("\n\n***** TOTAL NUMBER OF INTEGERS *****")
                print("The total number of integers inside the existing list is", len(numList))

                totalAgain = input("\nWould you like to continue, yes or no?: ")
                if totalAgain.lower() == "yes":
                    main()
                elif totalAgain.lower() == "no":
                    print("\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            total()

        elif menu == "d":
            def min_max():
                print("\n\n***** MINIMUM AND MAXIMUM INTEGER *****")
                print(numList, "\n")
                print("Minimum integer:", min(numList))
                print("Maximum integer:", max(numList))

                min_maxAgain = input("\nWould you like to continue, yes or no?: ")
                if min_maxAgain.lower() == "yes":
                    main()
                elif min_maxAgain.lower() == "no":
                    print("\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            min_max()

        elif menu == "e":
            def appear():
                print("\n\n***** APPEARANCE COUNT OF AN INTEGER *****")
                print(numList, "\n")
                appearInt = int(input("Enter an integer you wish to see the times it appear: "))
                countInt = numList.count(appearInt)
                print("Integer appearance count:", countInt)


                appearAgain = input("\nWould you like to see another integer's appearance count, yes or no?: ")
                if appearAgain.lower() == "yes":
                    appear()
                elif appearAgain.lower() == "no":
                    main()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            appear()

        elif menu == "f":
            def sumInt():
                print("\n\n***** SUM OF INTEGERS *****")
                print(numList, "\n")
                totalInt = sum(numList)
                print("Integers' Sum:", totalInt)

                sumAgain = input("\nWould you like to continue, yes or no?: ")
                if sumAgain.lower() == "yes":
                    main()
                elif sumAgain.lower() == "no":
                    print("\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            sumInt()

        elif menu == "g":
            def reverse():
                print("\n\n***** REVERSE ARRANGEMENT OF THE INTEGERS *****")
                print(numList, "\n")
                numList.reverse()
                print("Reverse list:", numList)

                reverseAgain = input("\nWould you like to continue, yes or no?: ")
                if reverseAgain.lower() == "yes":
                    main()
                elif reverseAgain.lower() == "no":
                    print("\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            reverse()


        elif menu == "h":
            def orders():
                print("\n\n***** ASCENDING AND DESCENDING ORDER OF INTEGERS *****")
                print(numList, "\n")
                numList.reverse()
                numList.sort()
                print("Ascending Order:", numList)

                numList.sort()
                numList.reverse()
                print("Descending Order:", numList)

                ordersAgain = input("\nWould you like to continue, yes or no?: ")
                if ordersAgain.lower() == "yes":
                    main()
                elif ordersAgain.lower() == "no":
                    print("\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            orders()

        elif menu == "i":
            def exitProgram():
                exitOption = input("\nAre you sure you want to close this program, yes or no?: ")
                if exitOption == "yes":
                    print("\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                elif exitOption == "no":
                    main()
                else:
                    print("\nInvalid Input! Please try again!")
                    main()
            exitProgram()
    else:
        print("\nInvalid Input! Please try again!")
        main()
main()
