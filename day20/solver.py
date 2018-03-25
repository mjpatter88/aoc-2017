
def parse_triplet(triplet):
    numbers = triplet[triplet.index('<') + 1: triplet.index('>')]
    return tuple(int(num.strip()) for num in numbers.split(','))

def manhattan_distance(position):
    return sum(abs(coord) for coord in position)


class Particle:
    def __init__(self, row):
        triplets = row.split(", ")
        self.position = parse_triplet(triplets[0])
        self.velocity = parse_triplet(triplets[1])
        self.acceleration = parse_triplet(triplets[2])

    def __repr__(self):
        return f"p=<{self.position}>, v={self.velocity}, a=<{self.acceleration}>"


particles = []
with open("input.txt") as inp:
    for line in inp:
        particles.append(Particle(line))

min_index = 0
min_dist = 1000
for index, particle in enumerate(particles):
    dist = manhattan_distance(particle.acceleration)
    if dist < min_dist:
        min_dist = dist
        min_index = index
print(f'Part 1 answer: {min_index}')
# print(f'Part 2 answer: {(network.steps)}')
