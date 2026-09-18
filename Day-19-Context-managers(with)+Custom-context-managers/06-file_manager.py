class FileManager:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.f = open(self.file, 'w')
        return self.f

    def __exit__(self, exc_type, exc, tb):
        self.f.close()

with FileManager("Day-19-Context-managers(with)+Custom-context-managers/data.txt") as file:
    file.write("Hello from advanced python!")
