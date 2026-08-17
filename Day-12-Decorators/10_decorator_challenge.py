def security_check(func):
    def wrapper():
        print("Checking security...")
        print("Access granted")
        func()

    return wrapper

@security_check
def access_account():
    print("Access opened")
    print()

@security_check
def view_profile():
    print("Profile opened")

access_account()
view_profile()