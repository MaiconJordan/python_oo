from typing import Dict
from src.view.people_finder_view import PeopleFinderView

def people_finder_constructor() -> Dict[str, str]:
    """
    Constructs the view for finding a person.
    This function clears the console and prompts the user to input the name of the person they want to find.
    It returns a dictionary containing the person's name.
    """
    people_finder_view = PeopleFinderView()
    person_finder_information = people_finder_view.find_person_view()