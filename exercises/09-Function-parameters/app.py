# Your code goes here:
def render_person(name, birth_date, eye_color, age, gender):
    sentence = f"{name} is a {age} years old {gender} born in {birth_date} with {eye_color} eyes"
    return sentence


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))