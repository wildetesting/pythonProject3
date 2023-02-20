# some object oriented basic structure to work with
# classes and objects in Python

# the blueprint of objects i would like to create
class Parrot:
    # class attributes
    name = ""
    age = 0

    #class functions
    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I can sleep")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print("hi")

    # create a few objects
    parrot1 = Parrot()
    parrot1.name = 'blue'
    parrot1.age = 10

    # create another object
    parrot2 = Parrot()
    parrot2.name = 'woo'
    parrot2.age = 12

    print(f"{parrot1.name} is {parrot1.age} years old.")
    print(f"{parrot2.name} is {parrot2.age} years old.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
