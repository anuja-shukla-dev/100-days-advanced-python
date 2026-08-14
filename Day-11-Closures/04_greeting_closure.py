def create_greeting(name):
    def greet(message):
        return f"{message}, {name}!"

    return greet

greet = create_greeting("Anuja")
print(greet("Good morning"))
