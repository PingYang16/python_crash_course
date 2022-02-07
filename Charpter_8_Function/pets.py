def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
describe_pet('willie', 'dog')

# can change order iff:
describe_pet(animal_type = 'hamster', pet_name = 'harry')

# when you define a default value for 'animal type', you can just pass a pet_name:
describe_pet(pet_name='willie')
# or even
describe_pet('willie')
# pay attention, the order of the parameters in the function definition
# the parameters have default value should be placed behind
describe_pet('harry', 'hamester')