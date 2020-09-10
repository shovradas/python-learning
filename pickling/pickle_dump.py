import pickle

# Sample data
student = {
    'name': {'first_name': 'Bob', 'last_name': 'Marsh'}, 
    'age': '13',
    'city': 'Chemnitz',
    'courses': ['SSE', 'SVS']
}

# Saving serialized data
with open('data', 'wb') as file:
    pickle.dump(student, file)