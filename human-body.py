mclass Organ:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Mouth(Organ):
    def chewing_food(self):
        return "Chewing and mixing with saliva"

class Stomach(Organ):
    def storing_into_stomach(self):
        return "Digesting food with gastric juices"

class SmallIntestine(Organ):
    def going_through_small_intestine(self):
        return "Absorbing nutrients into the bloodstream"

class LargeIntestine(Organ):
    def going_through_large_intestine(self):
        return "Absorbing water and forming feces"

class DigestiveSystem:
    def __init__(self, person_type):
        self.mouth = Mouth(f"{person_type} Mouth")
        self.stomach = Stomach(f"{person_type} Stomach")
        self.small_intestine = SmallIntestine(f"{person_type} Small Intestine")
        self.large_intestine = LargeIntestine(f"{person_type} Large Intestine")

    def process_food(self):
        steps = [
            self.mouth.chewing_food,
            self.stomach.storing_into_stomach,
            self.small_intestine.going_through_small_intestine,
            self.large_intestine.going_through_large_intestine
        ]

        for step in steps:
            organ_instance = step.__self__
            print(f"{organ_instance.get_name()}: {step()}")


if __name__ == "__main__":
    men_digestive_system = DigestiveSystem("Men")
    women_digestive_system = DigestiveSystem("Women")

    print("Men's Digestive System:")
    men_digestive_system.process_food()

    print("\nWomen's Digestive System:")
    women_digestive_system.process_food()
