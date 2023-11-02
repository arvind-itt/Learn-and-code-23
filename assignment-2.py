class HumanBody:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

    def breathe(self):
        return "The human body is breathing."

    def sleep(self):
        return "The human body is sleeping."



class Heart(HumanBody):
    def func1(self):
        return str(5)+" hello"

class Brain(HumanBody):
    def think(self):
        return "The brain is thinking."



def perform_actions(body_part):
    print(body_part.get_name())
    print(body_part.breathe())
    if isinstance(body_part, Brain):
        print(body_part.think())
    elif isinstance(body_part, Heart):
        print(body_part.func1())

# Using the classes

if __name__ == "__main__":
    body = HumanBody("John's Body")
    brain = Brain("John's Brain")
    heart = Heart("John's Heart")

    perform_actions(body)  # Polymorphism - the perform_actions function works for all body parts
    perform_actions(brain)  # Polymorphism - the perform_actions function works for all body parts
    perform_actions(heart)  # Polymorphism - the perform_actions function works for all body parts
