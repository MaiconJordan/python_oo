from typing import Dict

class PeopleFinderController:   
    def find_by_name(self, person_finder_information: str) -> Dict:
        try:
            self.__validate_fields(person_finder_information)
            # Simulate a database search
            response = self.__format_response(person_finder_information)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "message": str(exception)}