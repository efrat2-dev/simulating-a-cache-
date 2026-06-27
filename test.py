from lru import LRUCache
from rr import RRCache
from memory import RAM, MemorySystem


class TestLRUCache:

    def test_basic_insert(self):
        cache = LRUCache(3)
        memory = MemorySystem(cache, RAM({1: "A"}))

        value = memory.access_memory(1)

        assert value == "A"
        assert memory.last_access_miss is True
        assert memory.last_access_hit is False
        assert cache.contains(1) is True

    def test_cache_hit(self):
        cache = LRUCache(3)
        memory = MemorySystem(cache, RAM({1: "A"}))

        memory.access_memory(1)

        value = memory.access_memory(1)

        assert value == "A"
        assert memory.last_access_hit is True
        assert memory.last_access_miss is False

    def test_lru_eviction(self):
        cache = LRUCache(3)

        memory = MemorySystem(
            cache,
            RAM({
                1: "A",
                2: "B",
                3: "C",
                4: "D"
            })
        )

        memory.access_memory(1)
        memory.access_memory(2)
        memory.access_memory(3)

        memory.access_memory(1)

        memory.access_memory(4)

        assert cache.contains(1) is True
        assert cache.contains(3) is True
        assert cache.contains(4) is True
        assert cache.contains(2) is False

    def test_lru_order_update(self):
        cache = LRUCache(2)

        memory = MemorySystem(
            cache,
            RAM({
                1: "A",
                2: "B",
                3: "C"
            })
        )

        memory.access_memory(1)
        memory.access_memory(2)

        memory.access_memory(1)

        memory.access_memory(3)

        assert cache.contains(1) is True
        assert cache.contains(3) is True
        assert cache.contains(2) is False


class TestRandomReplacementCache:

    def test_basic_insert(self):
        cache = RRCache(3)

        memory = MemorySystem(
            cache,
            RAM({1: "A"})
        )

        value = memory.access_memory(1)

        assert value == "A"
        assert memory.last_access_miss is True
        assert memory.last_access_hit is False
        assert cache.contains(1) is True

    def test_cache_hit(self):
        cache = RRCache(3)

        memory = MemorySystem(
            cache,
            RAM({1: "A"})
        )

        memory.access_memory(1)

        value = memory.access_memory(1)

        assert value == "A"
        assert memory.last_access_hit is True
        assert memory.last_access_miss is False


def run_test(test_name, test_function):

    try:
        test_function()

        print(f"{test_name} PASSED")

    except AssertionError:
        print(f"{test_name} FAILED")


def main():

    print("===== RUNNING LRU TESTS =====")
    print()

    lru_tests = TestLRUCache()

    run_test(
        "test_basic_insert",
        lru_tests.test_basic_insert
    )

    run_test(
        "test_cache_hit",
        lru_tests.test_cache_hit
    )

    run_test(
        "test_lru_eviction",
        lru_tests.test_lru_eviction
    )

    run_test(
        "test_lru_order_update",
        lru_tests.test_lru_order_update
    )

    print()

    print("===== RUNNING RR TESTS =====")
    print()

    rr_tests = TestRandomReplacementCache()

    run_test(
        "test_basic_insert",
        rr_tests.test_basic_insert
    )

    run_test(
        "test_cache_hit",
        rr_tests.test_cache_hit
    )

    print()

    print("ALL TESTS FINISHED")


if __name__ == "__main__":
    main()
