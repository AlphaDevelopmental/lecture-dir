"""
==========================================================
EXAMPLE 1 - WEAK AUTHENTICATION MECHANISM
==========================================================

This application authenticates users correctly.

However, it does NOT:
    - limit login attempts
    - lock the account
    - delay repeated requests
    - require MFA

An attacker can therefore keep guessing passwords until
they find the correct one.

This is NOT a logic flaw.

The authentication logic is correct.

The SECURITY CONTROLS around authentication are weak.
==========================================================
"""

# Simulated database
users = {
    "alice": "password123"
}


def login(username, password):
    """
    Authenticate a user.

    Step 1:
        Does the username exist?

    Step 2:
        Does the password match?

    If yes -> Login successful.
    """

    if username not in users:
        return "User does not exist."

    if users[username] == password:
        return "Login Successful"

    return "Invalid Password"


# ----------------------------
# Legitimate User
# ----------------------------

print(login("alice", "password123"))

# Output:
# Login Successful


# ----------------------------
# Attacker
# ----------------------------

password_list = [
    "123456",
    "password",
    "admin",
    "welcome",
    "password123"
]

for password in password_list:

    print(f"Trying: {password}")

    result = login("alice", password)

    print(result)

    if result == "Login Successful":
        print("Password Found!")
        break

# Output:
# Trying: 123456
# Invalid Password
# Trying: password
# Invalid Password
# Trying: admin
# Invalid Password
# Trying: welcome
# Invalid Password
# Trying: password123
# Login Successful
# Password Found!

#secure version of the code would include security controls such as limiting login attempts, account lockout, request delays, and multi-factor authentication (MFA) to prevent brute-force attacks

"""
A very simplified example.

Real systems would also use:
    - password hashing
    - MFA
    - IP reputation
    - CAPTCHA
"""

MAX_ATTEMPTS = 5

failed_attempts = {}


def secure_login(username, password):

    # First login attempt?
    if username not in failed_attempts:
        failed_attempts[username] = 0

    # Account locked?
    if failed_attempts[username] >= MAX_ATTEMPTS:
        return "Account Locked"

    if username not in users:
        return "Unknown User"

    if users[username] == password:

        # Reset failed attempts after successful login
        failed_attempts[username] = 0

        return "Login Successful"

    # Wrong password
    failed_attempts[username] += 1

    return "Invalid Password"
#output:
# Trying: 123456
# Invalid Password
# Trying: password
# Invalid Password
# Trying: admin
# Invalid Password
# Trying: welcome
# Invalid Password
# Trying: password123
# Login Successful