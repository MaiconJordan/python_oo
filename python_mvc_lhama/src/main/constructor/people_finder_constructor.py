from typing import Dict
from src.view.people_finder_view import PeopleFinderView
from src.controller.people_finder_controller import PeopleFinderController

def people_finder_constructor() -> Dict[str, str]:
    """
    Constructs the view for finding a person.
    This function clears the console and prompts the user to input the name of the person they want to find.
    It returns a dictionary containing the person's name.
    """
    people_finder_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController()



    person_finder_information = people_finder_view.find_person_view()
    response = people_finder_controller.find_by_name(person_finder_information)
    
    if response["success"]:
        people_finder_view.find_sucess_view(response["message"])
    else:
        people_finder_view.find_person_error(response["error"])