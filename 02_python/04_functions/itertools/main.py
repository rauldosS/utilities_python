# itertools module iterators
import itertools

def condition(x):
    return x < 40

def main():
    # Cycle iterator can be used as the iterator to iterate over
    # a list
    people = ["Jessica", "Leticia", "Gustavo"]
    cycle = itertools.cycle(people)
    print(next(cycle)) # Jessica
    print(next(cycle)) # Leticia
    print(next(cycle)) # Gustavo
    print(next(cycle)) # Jessica

    # use count to create a simple counter
    counter = itertools.count(100, 10)
    print(next(counter)) # 100
    print(next(counter)) # 110
    print(next(counter)) # 120

    # The accumulate function creates an iterdor that accumulates values
    values = [10, 20, 30, 40, 50, 40, 30]
    accumulated = itertools.accumulate(values, max)
    print(list(accumulated)) # [10, 20, 30, 40, 50, 50, 50]

    # Use the chain function to connect lists
    x = itertools.chain("ABCD", "1234")
    print(list(x)) # ['A', 'B', 'C', 'D', '1', '2', '3', '4']

    # The dropwhile and takewhile functions will return values ​​up to
    # that a condition is met
    print(list(itertools.dropwhile(condition, values))) # [40, 50, 40, 30]
    print(list(itertools.takewhile(condition, values))) # [10, 20, 30]

if __name__ == "__main__":
    main()