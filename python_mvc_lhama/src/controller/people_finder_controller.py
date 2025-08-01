from typing import Dict

class PeopleFinderController:   
    def find_by_name(self, person_finder_information: str) -> Dict:
        try:
            self.__validate_fields(person_finder_information)
            # Simulate a database search
            response = self.__format_response(None)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "message": str(exception)}
        
    def __validate_fields(self, person_finder_information: Dict) -> None:
        if not isinstance(person_finder_information["name"], str):
            raise ValueError("O nome é obrigatório e deve ser uma string não vazia.")
        
    def __format_response(self, person: str) -> Dict:
        # Simulate a response format
        return {
            "count": 1,
            "type": "Person",
            "infos": {
                "name": "meu nome teste"
            }
        }