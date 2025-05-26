class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        self._age = 0
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        print(self._age)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        print(self._name)

def main():
    kof = Octopus("monkey")
    shimon = Octopus()
    kof.get_name()
    shimon.get_name()
    shimon.set_name("Elefant")
    shimon.get_name()
    print(Octopus.count_animals)

main()
