from typing import Dict
from src.view.people_finder_view import PeopleFinderView
from src.controller.people_finder_controller import PeopleFinderController

def people_finder_constructor() -> Dict[str, str]:
  
    people_finder_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController()



    person_finder_information = people_finder_view.find_person_view()
    response = people_finder_controller.find_by_name(person_finder_information)
    
    if response["success"]:
        people_finder_view.find_sucess_view(response["message"])
    else:
        people_finder_view.find_person_fail(response.get("error", "Erro desconhecido")) 