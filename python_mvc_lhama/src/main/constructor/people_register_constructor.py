from src.view.people_register_view import PeopleRegisterView
from src.controller.people_register_controller import PeopleRegisterController

def  people_register_constructor():
    #comentario aleatorio
    people_register_view = PeopleRegisterView()
    people_registter_controller = PeopleRegisterController()


    new_person_informations = people_register_view.registry_person_view()
    respose = people_registter_controller.register(new_person_informations)  

    if respose["success"]:
        people_register_view.registry_person_sucess(respose["message"])
    else:
        people_register_view.registry_person_error(respose["message"])