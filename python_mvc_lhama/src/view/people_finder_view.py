import os
from typing import Dict

class PeopleFinderView:
    def find_person_view(self) -> Dict[str, str]:
        os.system('clear')

        print("Buscar de pessoa\n")
        name = input("Digite o nome da pessoa: ")

        person_finder_information = {
            "name": name
        }

        return person_finder_information