print "How many pets do you have?"
has_pets = int(raw_input())
print "How many dogs do you have?"
pet_dogs = int(raw_input())
print "How many cats do you have?"
pet_cats = int(raw_input())
other_pets = has_pets - (pet_dogs + pet_cats)

print "So, you have %r pets. \nYou have %r cats, %r dogs, and %r other pets." % (
    has_pets, pet_dogs, pet_cats, other_pets
)
