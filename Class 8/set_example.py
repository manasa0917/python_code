myset=set()
#set has no duplicates # It is unordered

farm_animals=["sheep","cow","hen","goat","goat"]
farm_animals_set=set(farm_animals)
farm_animals_set.add("buffalo")
other_animals= ["buffalo","dog","goat"]
other_animals_set=set(other_animals)
print(farm_animals_set)
print(other_animals_set)
animal_set_union= farm_animals_set.union(other_animals_set)
animal_set_intersection=farm_animals_set.intersection(other_animals_set)
print(animal_set_union)
print(animal_set_intersection)
animal_set_diff=farm_animals_set.difference(other_animals_set)
print(animal_set_diff)
animal_set_diff_update


