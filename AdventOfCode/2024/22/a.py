import time

class Secret:
    def __init__(self, secret_num):
        self.secret = secret_num

    def mix(self, x):
        self.secret = self.secret ^ x

    def prune(self):
        self.secret = self.secret % 16777216

    def evolve(self, iterations):
        for _ in range(iterations):
            x = self.secret * 64
            self.mix(x)
            self.prune()
            x = self.secret // 32
            self.mix(x)
            self.prune()
            x = self.secret * 2048
            self.mix(x)
            self.prune()

if __name__ == '__main__':
    start_time = time.perf_counter()
    solutions = {}

    with open('input') as file:
        lines = file.readlines()
        secrets = [int(line.strip()) for line in lines]
        for num in secrets:
            secret = Secret(num)
            secret.evolve(2000)
            solutions[num] = secret.secret
    
    answer = 0
    for solution in solutions:
        # print(f"{solution}: {solutions[solution]}")
        answer += solutions[solution]
    print(answer)

    end_time = time.perf_counter()
    print(f"Runtime: {end_time - start_time:.2f}s")