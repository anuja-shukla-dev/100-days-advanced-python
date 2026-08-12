class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return f"{self._username}"

    @username.deleter
    def username(self):
        print("Username deleted")
        del self._username

user = User("Rahul")
print(user.username)
del user.username