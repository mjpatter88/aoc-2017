
def parse_triplet(triplet):
    numbers = triplet[triplet.index('<') + 1: triplet.index('>')]
    return [int(num.strip()) for num in numbers.split(',')]

def manhattan_distance(position):
    return sum(abs(coord) for coord in position)

def resolve_collisions(particles):
    for particle in particles:
        if not mark_collided(particles, particle.position):
            particle.collided = False
    return [particle for particle in particles if not particle.collided]

def mark_collided(particles, position):
    # Hack: there will always be at least one particle with equal position, itself
    # so we need to basically ignore that and not count the self collisions
    num_collisions = 0
    for particle in particles:
        if particle.position == position:
            particle.collided = True
            num_collisions += 1
    return num_collisions > 1


class Particle:
    def __init__(self, row):
        triplets = row.split(", ")
        self.position = parse_triplet(triplets[0])
        self.velocity = parse_triplet(triplets[1])
        self.acceleration = parse_triplet(triplets[2])
        self.collided = False

    def __repr__(self):
        return f"p=<{self.position}>, v={self.velocity}, a=<{self.acceleration}>"

    def step(self):
        for index in range(3):
            self.velocity[index] = self.velocity[index] + self.acceleration[index]
            self.position[index] = self.position[index] + self.velocity[index]


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

turns_with_no_change = 0
current_size = len(particles)

# Run steps in the simulation
while True:
    for particle in particles:
        particle.step()
    particles = resolve_collisions(particles)
    if len(particles) == current_size:
        turns_with_no_change += 1
    else:
        turns_with_no_change = 0
        current_size = len(particles)

    # A bit of trial and error, but if there hasn't been a collision in a while that might provide an answer
    if turns_with_no_change > 50:
        break
print(f'Part 2 answer: {len(particles)}')
