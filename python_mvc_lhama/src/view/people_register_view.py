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
    
    def registry_person_sucess(self, message: Dict) -> None:
        os.system('clear')
        
        sucess_message = f'''
        Cadastro realizado com sucesso!
        I
        tipo: {message["type"] }
        Registro: {message["count"]}
        infos:
            nome: {message["attribute"]["name"]}
            idade: {message["attribute"]["age"]}
'''
        print(sucess_message)

    def registry_person_error(self, error: str) -> None:
        os.system('clear')
        fail_message = f'''
        Ocorreu um erro ao cadastrar a pessoa:
        
        error: {error}
'''