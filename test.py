class Cat:
    def __init__(self, name):
        self.name = name

    def mauv(self):
        print("Cat " + self.name + " say mauv")


cat = Cat("jango")
cat2 = Cat("texo")
print(cat.name)
cat.mauv()
cat2.mauv()


# def main():
#     print("main")
#
#
# main()
