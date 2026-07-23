"""
Authentication vulnerabilities are not just hacking concepts—they are software engineering mistakes.

Every authentication vulnerability can usually be traced back to either:

Poor application design, or
Poor implementation of authentication logic.
"""


"""
=========================================================
NORMAL PASSWORD-BASED AUTHENTICATION
=========================================================

Every login request follows these steps.

1. Receive username and password
2. Find the user
3. Verify password
4. Create session
5. Grant access

Nothing magical happens.
Everything is simply software logic.
=========================================================
"""

# Simulated database
users = {
    "alice": "Password123!"
}


def login(username, password):

    # ----------------------------------------
    # STEP 1
    # Does this username exist?
    # ----------------------------------------
    if username not in users:
        return "Invalid credentials"

    # ----------------------------------------
    # STEP 2
    # Compare supplied password
    # with stored password.
    # ----------------------------------------
    if users[username] != password:
        return "Invalid credentials"

    # ----------------------------------------
    # STEP 3
    # User proved their identity.
    # Create a session.
    # ----------------------------------------

    session = {
        "username": username,
        "authenticated": True
    }

    return session


# output:
print(login("alice", "Password123!"))



"""
             Browser
                │
                ▼
     Username + Password
                │
                ▼
      Server receives request
                │
                ▼
      Username exists?
          │          │
         NO         YES
          │          ▼
      Reject      Check Password
                      │
              ┌───────┴────────┐
              │                │
             Wrong          Correct
              │                │
           Reject      Create Session
                           │
                           ▼
                     User Logged In



Because everything depends on one secret. PASSWORD. If the password is compromised, the attacker can impersonate the user.








Every lab answers two questions:

How can an attacker exploit this?
What mistake did the developer make?


for lab 1, the answer is: 
"""
def login(username, password):

    if username not in users:
        return "Invalid username"

    if users[username] != password:
        return "Incorrect password"

    return "Login Successful"

# output:
print(login("alice", "Password123!"))  # Login Successful   

"""
the correct behavior is to check the password first, and only create a session if the password is correct.

"""
def login(username, password):

    if username not in users:
        return "Invalid username or password"

    if users[username] != password:
        return "Invalid username or password"

    return "Login Successful"




"""
Why Response Length Changes


if username not in users:
    return render("Invalid username")

if password != users[username]:
    return render("Incorrect password")
"""