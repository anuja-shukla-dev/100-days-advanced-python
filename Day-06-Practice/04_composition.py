class CPU:
    def cpu_start(self):
        print("CPU started")

class RAM:
    def ram_initialize(self):
        print("RAM initialized")

class Storage:
    def storage_initialize(self):
        print("Storage initialized")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.storage = Storage()

    def start(self):
        self.cpu.cpu_start()
        self.ram.ram_initialize()
        self.storage.storage_initialize()
        print("Computer started")

computer = Computer()
computer.start()