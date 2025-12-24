friends_flat = {
    "name" : "John",
    "age" : 25,
    "gender" : "male",
    "parent_names" : {
        "father_name" : "father",
        "mother_name" : "mother"
    }
}

for label in friends_flat:
    print(label if type(friends_flat[label]) is int else None)
    