#Open JSON File and load data
import json
import os
from PIL import Image

#example usage
FILE_PATH = "data/person_db.json"  # Replace with your actual file path
# Definition der Personenklasse

class Person:
    def __init__(self,id : int, date_of_birth : str, firstname: str, lastname : str, picture_path : str, ekg_tests):
        self.id = id
        self.date_of_birth = date_of_birth
        self.firstname = firstname
        self.lastname = lastname
        self.picture_path = picture_path
        self.ekg_tests = ekg_tests
    
    def get_fullname(self):
        return self.lastname +", " + self.firstname

def load_user_objects(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
        person_list = []
    for person_person_dict in data:
        #print(person_person_dict)
        
        current_person = Person(person_person_dict['id'],
                                person_person_dict['date_of_birth'],
                                person_person_dict['firstname'],
                                person_person_dict['lastname'],
                                person_person_dict['picture_path'],
                                person_person_dict['ekg_tests'])
        person_list.append(current_person)    
    return person_list

def get_person_object_from_list_by_name(current_user_name, users):
    """
    Get a Person object from the list by their full name.
    """
    firstname = current_user_name.split(", ")[1]
    lastname = current_user_name.split(", ")[0]

    for person in users:
        if person.firstname == firstname and person.lastname == lastname:
            return person
        else:
            None

if __name__ == "__main__":

    person_list = load_user_objects(FILE_PATH)
    print(person_list)

    #name_list = get_all_names(user_data)
    #print(name_list)
    #person_1  = Person(1, "1990-01-01", "John", "Doe", "figures\Screenshot_HR_Termin3.png.jpg", [])
    #print(person_1.firstname)
    #print(person_1.get_fullname())
