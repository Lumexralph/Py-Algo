from binary_search.binary_search import binary_search

class TestBinarySearch:
    def test_that_the_item_is_found(self):

        my_list = [1, 2, 3, 4, 5]

        pos = binary_search(my_list, 4)

        assert my_list[pos] == 4

    def test_that_the_item_is_not_found(self):

        my_list = [1, 2, 3, 4, 5]

        pos = binary_search(my_list, 6)

        assert pos == 'item not found in the array'
