def main():

    email = input("please type email ").strip()

    if "@" in email and "." in email:

        print("email valled, welcome ")
    else:
        print("non valled email, please try again ")
main()
