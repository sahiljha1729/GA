from flask import Flask, render_template, request
import random
import string
from math import floor

app = Flask(__name__)

def randomchar():
    return random.choice(string.ascii_letters + " ")

class DNA:
    def __init__(self, length):
        self.genes = [randomchar() for _ in range(length)]
        self.fitness = 0.0

    def crossover(self, partner):
        child = DNA(len(self.genes))
        mid = random.randint(1, len(self.genes) - 1) if len(self.genes) > 1 else 0
        for i in range(len(child.genes)):
            if i < mid:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

def create_random_population(popsz, target_len):
    return [DNA(target_len) for _ in range(popsz)]

def check_fitness(population, target):
    for p in population:
        score = sum(1 for i in range(len(target)) if p.genes[i] == target[i])
        p.fitness = score / len(target)

def create_mating_pool(population):
    matingpool = []
    for p in population:
        count = floor((p.fitness ** 2) * 100) + 1
        matingpool.extend([p] * count)
    return matingpool

def breed_new_population(popsz, mating_pool):
    newpop = []
    for _ in range(popsz):
        parentA = random.choice(mating_pool)
        parentB = random.choice(mating_pool)
        child = parentA.crossover(parentB)
        newpop.append(child)
    return newpop

def mutate(population, mutation_rate):
    for p in population:
        for i in range(len(p.genes)):
            if random.random() < mutation_rate:
                p.genes[i] = randomchar()
    return population

@app.route("/", methods=["GET", "POST"])
def index():
    # Default values
    target = "Hehe There"
    popsz = 100
    mutation_rate = 0.01
    logs = []
    total_generations = 0

    if request.method == "POST":
        target = request.form.get("target", "Hehe There")
        popsz = int(request.form.get("popsz", 100))
        mutation_rate = float(request.form.get("mutation_rate", 0.01))

        # Run Genetic Algorithm
        population = create_random_population(popsz, len(target))
        check_fitness(population, target)
        generation = 0

        while True:
            best = max(population, key=lambda p: p.fitness)
            best_str = "".join(best.genes)
            avg_fitness = sum(p.fitness for p in population) / popsz

            logs.append({
                "gen": generation,
                "best": best_str,
                "fitness": f"{best.fitness * 100:.1f}%",
                "avg": f"{avg_fitness * 100:.1f}%"
            })

            if best.fitness == 1.0 or generation >= 1000:
                break

            mating_pool = create_mating_pool(population)
            population = breed_new_population(popsz, mating_pool)
            generation += 1
            population = mutate(population, mutation_rate)
            check_fitness(population, target)

        total_generations = generation

    return render_template(
        "index.html",
        target=target,
        popsz=popsz,
        mutation_rate=mutation_rate,
        logs=logs,
        total_generations=total_generations
    )

if __name__ == "__main__":
    app.run(debug=True)