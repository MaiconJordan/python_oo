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
    
    def find_sucess_view(self, message: Dict) -> None:
        os.system('clear')

        sucess_message = f'''
        Pessoa encontrada com sucesso!

        tipo: {message['type']}
        Registros encontrados: {message['count']}
        Nome: {message['infos']['name']}
        '''
        print(sucess_message)

