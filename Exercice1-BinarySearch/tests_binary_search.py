from binary_search import binary_search

def test_binary_search():
    nums = [1, 3, 5, 7, 9, 11, 15]
    
    assert binary_search(nums, 5) == 2
    assert binary_search(nums, 6) == -1
    assert binary_search(nums, 1) == 0
    assert binary_search(nums, 15) == 6
    assert binary_search([], 10) == -1

    print("Tous les tests sont passés avec succès !")

if __name__ == "__main__":
    test_binary_search()
