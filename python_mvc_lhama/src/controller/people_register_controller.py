from typing import Dict

class PeopleRegisterController:
    def register(self, new_person_register_information: Dict) -> Dict:
        try:
            self.__validate_fields(new_person_register_information)

            response = self.__format_response(new_person_register_information)
            return {"success": True, "message": response}
        except Exception as exeption:
            return {"success": False, "message": str(exeption)}
        

    def __validate_fields(self, new_person_information: Dict):
        if not isinstance(new_person_information["name"], str):
            raise ValueError("O nome é obrigatório.")
        
        try: int(new_person_information["age"])
        except ValueError: raise ValueError("A idade deve ser um número.")

        try: int(new_person_information["hight"])
        except ValueError: raise ValueError("A altura deve ser um número.")

    def __format_response(self, new_person_register_information: Dict) -> str:
        return {
            "id": 1,
            "type": "Person",
            "attribute": new_person_register_information
        }