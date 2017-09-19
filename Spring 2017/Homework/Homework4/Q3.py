# Question 3 - Implement function to check password validity
# Asmit De
# 04/28/2017


## Function definition for isValid ----##
# Parameters:   password (string)
# Return:       True or False (Boolean) - True if password is valid, False otherwise
#
def isValid(password):
    
    # If length of password is less than 7,
    # password is invalid - return false. Function terminates
    if len(password) < 7:
        return False

    # Initialize two counters for uppercase letters and digits
    count_uc = 0
    count_dig = 0

    # Run loop through the characters in the password
    for ch in password:

        # If character is uppercase, increase count_uc
        if 'A' <= ch <= 'Z':
            count_uc += 1

        # else if character is digit, increase count_dig
        elif '0' <= ch <= '9':
            count_dig += 1

        # else if the character is not lowercase (meaning,
        # it must be a special character). Password is invalid - return false
        elif not('a' <= ch <= 'z'):
            return False

    # If we reach this point, it means that we have only found upper/lowercase letters or digits.
    # Check if there are at least one uppercase letter and one digit. If so, all our checks have
    # passed - return True, else return False
    if count_uc > 0 and count_dig > 0:
        return True
    else:
        return False

##---- Function definition ends ##


## Main program code ##

# Enter password from the user
pwd = input('Enter password: ')

# Call the isValid function with pwd as argument
# and check the returned value for validity of password.
# Print accordingly.
if isValid(pwd):
    print('The password is valid')
else:
    print('The password is invalid')
