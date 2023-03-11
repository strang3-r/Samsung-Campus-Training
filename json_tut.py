import json
from json import JSONEncoder

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "title": ["engineer", "programmer"]}


personJSON = json.dumps(
    person, indent=4, sort_keys=False, separators=('; ', ': '))

# print(personJSON)

# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)
#     print(person)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)



class User:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {
            'name': o.name,
            'age': o.age,
            o.__class__.__name__: True
        }
    else:
        raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')
    
    
def UserEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, User):
            return {
                'name': o.name,
                'age': o.age,
                o.__class__.__name__: True
            }
        else:
            return JSONEncoder.default(self, o)

# userJSON = json.dumps(user, default=encode_user)
# print(userJSON)

userJSON = UserEncoder(JSONEncoder).encode(user)
print(userJSON)