import re

def evaluate_password_strength(password):
    # Define the password strength criteria
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    elif (re.search(r'[A-Z]', password) and
          re.search(r'[a-z]', password) and
          re.search(r'[0-9]', password) and
          re.search(r'[\W_]', password)):
        if len(password) >= 16:
            return "Awesome"
        else:
            return "Strong"
    else:
        return "Moderate"

def evaluate_single_password():
    password = input("Enter a password to evaluate its strength: ")
    strength = evaluate_password_strength(password)
    print(f"\nPassword strength: {strength.capitalize()}")

def evaluate_passwords_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            report = []
            users_to_contact = []
            for line in lines:
                user, password = line.strip().split(',')
                strength = evaluate_password_strength(password)
                report.append(f"User: {user}, Password: {password}, Strength: {strength}")
                if strength == "Weak" or strength == "Moderate":
                    users_to_contact.append(user)
            
            if users_to_contact:
                print("\nUsers with weak passwords (to be contacted):")
                for user in users_to_contact:
                    print(f"- {user}")
            
            return report
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Choose an option:")
    print("1. Evaluate a single password")
    print("2. Evaluate passwords from a file")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        evaluate_single_password()
    elif choice == '2':
        file_path = input("Enter the file path: ")
        report = evaluate_passwords_from_file(file_path)
        if report:
            print("\nPassword evaluation report:")
            for line in report:
                print(line)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
