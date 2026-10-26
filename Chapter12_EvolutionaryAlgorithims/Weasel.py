import random
import string
import matplotlib.pyplot as plt
target = "METHINKS IT IS LIKE A WEASEL"

print("Target phrase:", target)
print("Target length:", len(target))
def fitness(candidate):
    score = 0

    for i in range(len(target)):
        if candidate[i] == target[i]:
            score += 1

    return score
print("Fitness test:", fitness(target))
def mutate(candidate):
    letters = string.ascii_uppercase + " "
    result = ""

    for char in candidate:
        if random.random() < 0.05:
            result += random.choice(letters)
        else:
            result += char

    return result
print("Original:", target)
print("Mutated:", mutate(target))
letters = string.ascii_uppercase + " "
parent = "".join(random.choice(letters) for _ in range(len(target)))

print("Starting parent:", parent)
print("Starting fitness:", fitness(parent))
generations = 1000
population_size = 100
fitness_history = []

for generation in range(generations):
    offspring = [mutate(parent) for _ in range(population_size)]
    best_offspring = max(offspring, key=fitness)

    if fitness(best_offspring) > fitness(parent):
        parent = best_offspring
        fitness_history.append(fitness(parent))
        print(f"Generation {generation + 1}: {parent} | Fitness: {fitness(parent)}/28")

        if fitness(parent) == len(target):
            break
plt.plot(fitness_history)
plt.title("Evolution of Fitness Over Time")
plt.xlabel("Fitness Improvements")
plt.ylabel("Fitness Score")
plt.savefig("fitness_evolution.png", dpi=300)
plt.show()
