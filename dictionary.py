from helper import produce_stars


def presenter_name(presenter_identification):
    return presenter_identification["name"] + " " + presenter_identification["lastname"]


agenda = [
    "Dictionary",
]

definition = "A dictionary is a collection which is unordered, changeable and indexed."
presenter = {"name": "Lucas", "lastname": "Piffer"}

print(produce_stars(20), agenda[0], produce_stars(20), end="\n")

print("Defining a dictionary", {"name": "Lucas", "lastname": "Piffer"})
print("Checking the type", (type({})).__name__)
print("What is the presenter name?", presenter["name"])
print("Could you inform the presenters' lastname?", presenter.get("lastname"))
presenter["name"] = "Snoop"
presenter["lastname"] = "Dog"
print("I think it is time to change the presenter. Who is the new presenter?", presenter_name(presenter) )
print("Lets check if the key exists", ("age" in presenter))
print("Could you tell me your size?", (len(presenter)))
