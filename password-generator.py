import string
import secrets 

def generate_password(length=15):
    # Define the alphabet: uppercase, lowercase, digits, and punctuation
    
    alphabet = (
        string.ascii_letters + 
        string.digits + 
        string.punctuation
        )
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    #randomly select characters from the alphabet to form the password and join it into a string
    
    return password

password = generate_password()
print("Generated password:", password)