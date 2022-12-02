import random


people = []
people_picked = []
drawn_list = {}

def Main():
    for person_drawing_for_secret_santa in people:
        person = person_drawing_for_secret_santa
        pull(people, people_picked,person)


def pull(people, people_picked, person):
    name = random.choice(people)
    if name != person:
        if name in people_picked:
            pull(people, people_picked, person)
        else:
            people_picked.append(name)
            drawn_list[person] = name
    else:
        pull(people, people_picked, person)


while True:
    print("\nenter " +"S"+ " after imputting your names")
    name_input = input("Enter Name of secret santa player: ")
    name_input = name_input.strip().lower()

    if name_input == "s":
        break
    else:
        if name_input == "":
            print("Enter a name")
            continue

    if name_input in people:
        print("Name already added\n")

    else:
        people.append(name_input)



Main()
print(drawn_list)