import random
import string

def generate_unique_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_part}@example.com"


TEST_USER = {
    "name": "Ольга Спиридониди",
    "email": generate_unique_email(),
    "password": "123456"
}

INVALID_PASSWORD = "123"  
