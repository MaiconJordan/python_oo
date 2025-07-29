from src.view.people_register_view import PeopleRegisterView

def  people_register_constructor():
    """
    Constructs the view for registering a person.
    This function clears the console and prompts the user to input the person's details.
    It returns a dictionary containing the person's information.
    """
    people_register_view = PeopleRegisterView()
    new_person_informations = people_register_view.registry_person_view()
    
   