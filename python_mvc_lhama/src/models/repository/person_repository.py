class __PersonRepository:
    def __init__(self):
        self._people = []

    def registry_person(self, person):
        self._people.append(person)


    def find_person_by_name(self, name):
        for person in self._people:
            if person.name == name:
                return person
        return None

    def remove_person(self, person):
        if person in self._people:
            self._people.remove(person)

person_repository = __PersonRepository()