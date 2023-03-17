import random

def generate_seed():
    """
    Generate a random seed.
    """
    seed = random.randrange(1, 10)
    for j in range(random.randrange(1, 6)):
        seed *= random.randrange(1, 10**6)
    for k in range(random.randrange(0, 4)):
        op = random.choice(['+', '-', '*', '/', '%', '&', '|', '^', '<<', '>>'])
        if op == '+':
            seed = (seed + random.randrange(1, 10**16)) % (10**16)
        elif op == '-':
            seed = (seed - random.randrange(1, 10**16)) % (10**16)
        elif op == '*':
            seed = (seed * random.randrange(1, 10**2)) % (10**16)
        elif op == '/':
            seed = (seed // random.randrange(1, 10**2)) % (10**16)
        elif op == '%':
            seed = (seed % random.randrange(1, 10**2)) % (10**16)
        elif op == '&':
            seed = (seed & random.randrange(1, 10**16)) % (10**16)
        elif op == '|':
            seed = (seed | random.randrange(1, 10**16)) % (10**16)
        elif op == '^':
            seed = (seed ^ random.randrange(1, 10**16)) % (10**16)
        elif op == '<<':
            seed = (seed << random.randrange(1, 9)) % (10**16)
        elif op == '>>':
            seed = (seed >> random.randrange(1, 9)) % (10**16)
    
    # Ensure the seed doesn't contain a 0
    while '0' in str(seed):
        seed = generate_seed()

    return seed

random.seed(404)

seeds = []
while len(seeds) < 16:
    seed = generate_seed()
    if hex(seed) not in seeds:
        seeds.append(hex(seed))

for i, seed in enumerate(seeds):
    if random.random() < 0.25:
        if random.random() < 0.05:
            seeds[i] = "*" + seed[2:].zfill(16)
        elif random.random() < 0.10:
            seeds[i] = "/" + seed[2:].zfill(16)

print(seeds)
