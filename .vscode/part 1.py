def main():

    email = input("please type email ").strip()

    username, domain = email.split("@")

    if username and domain.endswith(".ac.uk"):
        print("domain vallid")

        if "@" in email and "." in email:

            print("email vallid, welcome ")
        else:
            print("non vallid email, please try again ")
main()
