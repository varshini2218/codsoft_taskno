import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        print("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")
        return
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level of the password: \n -> LOW \n -> MEDIUM\n -> HIGH\n ").lower()
    
    password = generate_password(length, complexity)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()