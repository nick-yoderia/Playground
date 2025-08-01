import time
from collections import defaultdict
from collections import Counter

class Secret:
    def __init__(self, secret_num):
        self.secret = secret_num
        self.price_flux = []
        self.deltas_to_bananas = {}

    def mix(self, x):
        self.secret = self.secret ^ x

    def prune(self):
        self.secret = self.secret % 16777216

    def evolve(self, iterations):
        for i in range(iterations):
            prev_price = self.secret % 10
            x = self.secret << 6
            self.mix(x)
            self.prune()
            x = self.secret >> 5
            self.mix(x)
            self.prune()
            x = self.secret * 2048
            self.mix(x)
            self.prune()
            self.price_flux.append(self.secret % 10 - prev_price)
            if i >= 3 and tuple(self.price_flux[-4:]) not in self.deltas_to_bananas:
                self.deltas_to_bananas[tuple(self.price_flux[-4:])] = self.secret % 10

if __name__ == '__main__':
    start_time = time.perf_counter()

    master_dictionary = None

    with open('input') as file:
        lines = file.readlines()
        secrets = [int(line.strip()) for line in lines]
        for num in secrets:
            secret = Secret(num)
            secret.evolve(2000)
            if master_dictionary is None:
                master_dictionary = secret.deltas_to_bananas
            else:
                master_dictionary = dict(Counter(master_dictionary) + Counter(secret.deltas_to_bananas))
            
    max_value = max(master_dictionary, key=master_dictionary.get)
    print(f"{max_value}: {master_dictionary[max_value]}")

    end_time = time.perf_counter()
    print(f"Runtime: {end_time - start_time:.2f}s")