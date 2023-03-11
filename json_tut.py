import json

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
    return JSONEncoder(self, o)
    
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

from json import JSONEncoder
    
def UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {
                'name': o.name,
                'age': o.age,
                o.__class__.__name__: True
            }
        return JSONEncoder.default(self, o)
    
    
# Error

# userJSON = UserEncoder().encode(user)
# print(userJSON)

def decode_User(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_User)
print(user.name)
print(type(user))