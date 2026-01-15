import random
import string

NAMES = [
    "Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Елена",
    "Иван", "Мария", "Николай", "Ольга", "Павел", "Светлана",
    "Сергей", "Татьяна", "Юрий", "Юлия", "Антон", "Ирина",
    "Максим", "Наталья", "Алексей", "Екатерина"
]

def generate_unique_email(domain="ya.ru"):
    
    random_suffix = ''.join(random.choices(string.digits, k=5))
    return f"test_user_{random_suffix}@{domain}"

def generate_valid_password(length=10):
   
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def generate_unique_name():
    
    if not hasattr(generate_unique_name, 'used_names'):
        generate_unique_name.used_names = set()

    
    available_names = [name for name in NAMES if name not in generate_unique_name.used_names]
    
    if not available_names:
       
        generate_unique_name.used_names.clear()
        available_names = NAMES.copy()

    name = random.choice(available_names)
    generate_unique_name.used_names.add(name)
    return name


TEST_DATA = {
    "valid": {
        "name": generate_unique_name(),
        "email": generate_unique_email(),
        "password": generate_valid_password()
    },
    "short_password": {
        "name": "Тест",
        "email": "short@test.ru",
        "password": "123"
    }
}


