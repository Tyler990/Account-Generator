# Random Free Account Generator for Streaming Services

import random
import string

def generate_username(length=8):
    """Generate a random username."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def generate_account(service):
    """Generate a random account for a given streaming service."""
    username = generate_username()
    password = generate_password()
    return {
        'service': service,
        'username': username,
        'password': password
    }

def main():
    services = ['Netflix', 'Hulu', 'Amazon Prime', 'Disney+', 'HBO Max']
    accounts = [generate_account(service) for service in services]
    
    for account in accounts:
        print(f"Service: {account['service']}, Username: {account['username']}, Password: {account['password']}")

if __name__ == "__main__":
    main()
