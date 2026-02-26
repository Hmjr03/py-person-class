class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife: "Person | None" = None
        self.husband: "Person | None" = None
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list["Person"]:
    Person.people.clear()

    person_list = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]

        wife_name = data.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]

        husband_name = data.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]

    return person_list
