import os
from typing import Dict

class PeopleRegisterView:
    def registry_person_view(self):
        os.system('clear')

        print("Cadastro de pessoa\n")
        name = input("Digite o nome: ")
        age = input("Digite a idade: ")
        hight = input("Digite a altura: ")

        new_person_informations = {
            "name": name,
            "age": age,
            "hight": hight
        }

        return  new_person_informations