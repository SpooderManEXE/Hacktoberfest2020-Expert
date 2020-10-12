import random


def calc_pi(trial: int) -> float:
    inside = 0
    for i in range(trial):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1:
            inside += 1
    return (inside << 2) / trial


if __name__ == '__main__':
    print(calc_pi(100))
    print(calc_pi(5 * 10 ** 6))
