class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(human["name"], human["age"]) for human in people]

    def find_human(name: str) -> Person:
        return next((human for human in person_list if human.name == name), None)

    for human in people:
        if "wife" in human and human["wife"] is not None:
            husband = find_human(human["name"])
            wife = find_human(human["wife"])
            husband.wife = wife
            wife.husband = husband

    return person_list
