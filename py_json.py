# JSON IS COMMONLY USED WITH DATA APIS . HERE IS HOW WE CAN PARSE JSON INTO PYTHON DIRECTORY

import json
# Sample JSON
userJSON = '{"firstName": "alabi", "lastName": "dan","age": 29}'

# Parse to dictionary
user = json.loads(userJSON)


# print(user)
# print(user['firstName'])




car = {'make': 'Ford', 'model': 'mustang','year': 1981}
carJSON = json.dumps(car)

print(carJSON)