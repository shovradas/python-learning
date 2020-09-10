import pickle

# Loading and deserialize
with open('data', 'rb') as file:
    student = pickle.load(file)
    print(student)