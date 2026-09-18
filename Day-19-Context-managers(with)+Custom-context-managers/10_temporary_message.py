class TemporaryMessage:
    def __init__(self):
        self.original = "Normal"

    def __enter__(self):
        return self.original

    def __exit__(self, exc_type, exc, tb):
        print("Restoring original message")
        
with TemporaryMessage() as message:
    print(message)

print("Context finished")
