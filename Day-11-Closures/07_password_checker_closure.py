def create_checker(password):
    def check(attempt):
        return attempt == password

    return check

check = create_checker("python123")
print(check("python123"))
print(check("hello"))