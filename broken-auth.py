"""
==========================================================
BROKEN AUTHENTICATION
==========================================================

The programmer accidentally authenticates the user
BEFORE verifying the password.

This is NOT a brute-force issue.

The attacker only needs to know a username.

The vulnerability exists because of BAD PROGRAM LOGIC.
==========================================================
"""

users = {
    "admin": "SuperSecretPassword"
}


logged_in_users = []


def login(username, password):

    """
    BUG:

    The developer assumes that if the username exists,
    the user is legitimate.

    They immediately create a session.

    Only afterwards do they check the password.

    Unfortunately...

    The attacker is already logged in.
    """

    if username in users:

        # -----------------------------
        # SECURITY BUG
        # -----------------------------
        # User becomes authenticated
        # BEFORE password verification.
        # -----------------------------

        logged_in_users.append(username)

    # Password check happens too late.
    if username in users and users[username] == password:
        return "Login Successful"

    return "Invalid Password"


login("admin", "wrongpassword")

print(logged_in_users)

# Output:
# ['admin']

# correct behavior would be to return "Invalid Password" and not add the user to logged_in_users.
# correct version of the code would be to check the password first, and only add the user to logged_in_users if the password is correct. 

logged_in_users = []


def secure_login(username, password):

    """
    Correct authentication flow.

    Verify everything FIRST.

    Only then create a session.
    """

    if username not in users:
        return "Unknown User"

    if users[username] != password:
        return "Wrong Password"

    # --------------------------
    # Authentication succeeded
    # --------------------------

    logged_in_users.append(username)

    return "Login Successful"

# output:
print(secure_login("admin", "wrongpassword"))   



# broken session validation 

"""
==========================================================
BROKEN AUTHENTICATION

Protected page WITHOUT session validation.

The developer assumes anyone visiting /dashboard
must already be logged in.

This assumption is WRONG.
==========================================================
"""

logged_in_users = []


def dashboard(username):

    """
    SECURITY BUG

    The application never verifies that the user
    actually has an authenticated session.
    """

    return f"Welcome {username}"


print(dashboard("admin"))

# Output:
# Welcome admin 


# secure version of the code would be to check if the user is in logged_in_users before allowing access to the dashboard.
logged_in_users = ["alice"]


def dashboard(username):

    """
    Always verify authentication
    BEFORE serving protected content.
    """

    if username not in logged_in_users:
        return "403 Forbidden"

    return f"Welcome {username}"

# output:
print(dashboard("admin"))  # Output: 403 Forbidden  



#trusting client input
"""
==========================================================
BROKEN AUTHENTICATION

The application trusts the client's request.

The client tells the server:

"I am an administrator."

The server believes them.

Never trust data coming from the client.
==========================================================
"""


def login(request):

    """
    BAD DESIGN

    Authentication decisions should NEVER be based
    on client-controlled values.
    """

    if request["is_admin"]:
        return "Administrator Login"

    return "Normal User"


attacker_request = {
    "username": "john",
    "is_admin": True
}

print(login(attacker_request))

# Output:
# Administrator Login   




""" 
NOTE: The above code snippets demonstrate various broken authentication mechanisms, including authenticating users before verifying passwords, failing to validate sessions for protected pages, and trusting client input for authentication decisions.
Each snippet highlights the security flaws and provides a secure alternative to mitigate the vulnerabilities. 


Senior Software Engineering Perspective

When reviewing authentication code, I mentally ask four questions:

Is identity verified before a session is created?
Can the client influence the authentication decision?
Are there protections against repeated login attempts (rate limiting, lockout, MFA)?
Does every protected resource independently verify that the user has a valid authenticated session?

If the answer to any of these questions is "no," there is likely an authentication weakness worth investigating.

These examples mirror the kinds of mistakes you'll encounter in real code reviews, penetration tests, and many of the authentication labs in the PortSwigger Web Security Academy.

"""