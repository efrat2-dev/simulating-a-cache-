import time

from rr import RRCache
from lru import LRUCache
from memory import RAM, MemorySystem


CACHE_SIZE = 3

RR_RUNS = 10

ACCESS_PATTERN = [
    1, 2, 3,
    1, 2,
    4,
] + [1, 2, 4] * 10


RAM_ITEMS = {
    1: "A",
    2: "B",
    3: "C",
    4: "D"
}


def benchmark(memory_system, accesses):

    total_start = time.perf_counter()

    for index in accesses:
        memory_system.access_memory(index)

    total_end = time.perf_counter()

    return (total_end - total_start) * 1000


def run_random_replacement():

    print("===== RANDOM REPLACEMENT =====")
    print()

    runtimes = []

    for run in range(RR_RUNS):

        cache = RRCache(CACHE_SIZE)

        memory = MemorySystem(
            cache,
            RAM(RAM_ITEMS)
        )

        runtime = benchmark(
            memory,
            ACCESS_PATTERN
        )

        runtimes.append(runtime)

        print(
            f"Run {run + 1:<2} "
            f"-> {runtime:.2f} ms"
        )

    average = sum(runtimes) / len(runtimes)

    best = min(runtimes)

    worst = max(runtimes)

    print()
    print("===== RR STATISTICS =====")
    print()

    print(f"Best Runtime   : {best:.2f} ms")
    print(f"Worst Runtime  : {worst:.2f} ms")
    print(f"Average Runtime: {average:.2f} ms")
    print()

    return average, best, worst


def run_lru():

    print("===== LRU =====")
    print()

    cache = LRUCache(CACHE_SIZE)

    memory = MemorySystem(
        cache,
        RAM(RAM_ITEMS)
    )

    runtime = benchmark(
        memory,
        ACCESS_PATTERN
    )

    print(f"LRU Runtime: {runtime:.2f} ms")
    print()

    return runtime


def main():

    print("===== ACCESS PATTERN =====")
    print()

    print(ACCESS_PATTERN)
    print()

    print(f"Total accesses: {len(ACCESS_PATTERN)}")
    print(f"Cache size: {CACHE_SIZE}")
    print(f"RR runs: {RR_RUNS}")

    print()

    rr_average, rr_best, rr_worst = run_random_replacement()

    lru_runtime = run_lru()

    print("===== FINAL COMPARISON =====")
    print()

    print(f"RR Best Runtime    : {rr_best:.2f} ms")
    print(f"RR Worst Runtime   : {rr_worst:.2f} ms")
    print(f"RR Average Runtime : {rr_average:.2f} ms")

    print()

    print(f"LRU Runtime        : {lru_runtime:.2f} ms")

    print()

    avg_improvement = (
        (rr_average - lru_runtime)
        / rr_average
    ) * 100

    worst_improvement = (
        (rr_worst - lru_runtime)
        / rr_worst
    ) * 100

    print(
        f"LRU vs RR Average : "
        f"{avg_improvement:.2f}% faster"
    )

    print(
        f"LRU vs RR Worst   : "
        f"{worst_improvement:.2f}% faster"
    )


if __name__ == "__main__":
    main()
