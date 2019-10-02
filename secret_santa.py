import random


def secret_santa(names):
    random.shuffle(names)
    return {giver: receiver for giver, receiver in
            zip(names, names[1:] + names[0:1])}


if __name__ == "__main__":
    names = ['Macbeth', 'Duncan', 'Malcolm', 'Banquo', 'Macduff']
    print(secret_santa(names))
