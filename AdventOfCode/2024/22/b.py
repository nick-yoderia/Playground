import time
from collections import Counter

def mix(secret, x):
    return secret ^ x

def prune(secret):
    return secret % 16777216

def evolve(secret):
    secret = prune(mix(secret, secret << 6))
    secret = prune(mix(secret, secret >> 5))
    secret = prune(mix(secret, secret * 2048))
    return secret

if __name__ == '__main__':
    start_time = time.perf_counter()

    master_counter = Counter()

    with open('input') as file:
        lines = file.readlines()
        secrets = [int(line.strip()) for line in lines]

    for secret in secrets:
        price_flux = []
        deltas_to_bananas = {}
        for _ in range(2000):
            prev_secret = secret
            secret = evolve(secret)
            price_flux.append(secret % 10 - prev_secret % 10)
            if len(price_flux) > 3 and tuple(price_flux[-4:]) not in deltas_to_bananas:
                deltas_to_bananas[tuple(price_flux[-4:])] = secret % 10

        if master_counter is None:
            master_counter = deltas_to_bananas
        else:
            master_counter.update(deltas_to_bananas)
            
    most_common = master_counter.most_common(1)[0]
    print(f"{most_common[0]}: {most_common[1]}")

    end_time = time.perf_counter()
    print(f"Runtime: {end_time - start_time:.2f}s")