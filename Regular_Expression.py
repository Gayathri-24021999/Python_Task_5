# Email address
def validate_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        local_part, domain_part = email.split("@")
        if all(c.isalnum() or c in "._+-" for c in local_part) and \
           all(c.isalnum() or c in "-." for c in domain_part):
            return True
    return False

# Test example
print(validate_email("gayu99.p@gmail.com"))

# Mobile number of Bangladesh
def validate_bd_mobile(number):
    if number.startswith("+8801") or number.startswith("01"):
        number = number.replace("+880", "")
        if len(number) == 11 and number[0] == '1' and number[1] in "3456789" and number[2:].isdigit():
            return True
    return False

# Test examples
print(validate_bd_mobile("+8801704782586"))
print(validate_bd_mobile("01712345678"))

#Telephone number of USA
def validate_us_telephone(number):
    number = number.replace(" ", "").replace("-", "").replace(".", "").replace("(", "").replace(")", "")
    if number.startswith("+1"):
        number = number[2:]
    if len(number) == 10 and number.isdigit():
        return True
    return False

# Test examples
print(validate_us_telephone("+1 (123) 456-7890"))
print(validate_us_telephone("123-456-7890"))

#16 Character Alphanumeric Password

def validate_password(password):
    if len(password) != 16:
        return False
    has_upper = has_lower = has_digit = has_special = False
    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c in "@$!%*?&":
            has_special = True
    return has_upper and has_lower and has_digit and has_special

# Test examples
print(validate_password("A1b2C3d4E5f6G7h!"))
print(validate_password("A1b2C3d4E5f6G7")) 

