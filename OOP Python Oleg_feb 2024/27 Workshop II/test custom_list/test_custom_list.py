from unittest import TestCase, main

from custom_exceptions import EmptyListException
from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.l = CustomList()

    def test_initializer(self):
        self.assertEqual(self.l._CustomList__values, [])

    def test_add(self):
        self.assertEqual(self.l._CustomList__values, [])

        self.l.append(5)
        self.assertEqual(self.l._CustomList__values, [5])

    def test_add_multiple_existing_elements_add_element_at_the_end(self):
        self.l._CustomList__values = [1, 2, 3]

        self.assertEqual(self.l._CustomList__values, [1, 2, 3])
        self.assertEqual(len(self.l._CustomList__values), 3)

        self.l.append(5)
        self.assertEqual(self.l._CustomList__values, [1, 2, 3, 5])

        last_element = self.l._CustomList__values[-1]
        self.assertEqual(last_element, 5)
        self.assertEqual(len(self.l._CustomList__values), 4)

    def test_add_returns_the_same_list(self):
        self.l._CustomList__values = [1, 2, 3]

        result = self.l.append(5)

        self.assertIs(result, self.l._CustomList__values)

    def test_type_of_index_is_not_integer_raises(self):
        invalid_args = [2.5, "asd", [1, 23], {"1": 1}]

        for invalid_arg in invalid_args:
            with self.assertRaises(TypeError) as ex:
                self.l.remove(invalid_arg)
            self.assertEqual(str(ex.exception), f"Index must be of type integer")

    def test_check_index_argument_is_not_positive_or_zero_integer_raises(self):
        invalid_value = -1
        with self.assertRaises(ValueError) as ex:
            self.l.remove(invalid_value)
        self.assertEqual(str(ex.exception.args[0]), "Integer must be 0 or positive")

    def test_index_is_not_in_array_boundary_raises(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(len(self.l._CustomList__values), 3)

        index_out_of_range = [3, 4]

        for index in index_out_of_range:
            with self.assertRaises(ValueError) as ex:
                self.l.remove(index)
            self.assertEqual(str(ex.exception.args[0]), "Index is out of range")

    def test_remove_value_on_given_index(self):
        self.l._CustomList__values = [1, 2, 3, 1]
        self.assertEqual(self.l._CustomList__values, [1, 2, 3, 1])
        self.assertEqual(len(self.l._CustomList__values), 4)

        result = self.l.remove(0)
        self.assertEqual(self.l._CustomList__values, [2, 3, 1])
        self.assertEqual(len(self.l._CustomList__values), 3)

        self.assertEqual(result, 1)

    def test_get_type_of_index_is_not_integer_raises(self):
        invalid_args = [2.5, "asd", [1, 23], {"1": 1}]

        for invalid_arg in invalid_args:
            with self.assertRaises(TypeError) as ex:
                self.l.get(invalid_arg)
            self.assertEqual(str(ex.exception.args[0]), f"Index must be of type integer")

    def test_get_check_index_argument_is_not_positive_or_zero_integer_raises(self):
        invalid_value = -1
        with self.assertRaises(ValueError) as ex:
            self.l.get(invalid_value)
        self.assertEqual(str(ex.exception.args[0]), "Integer must be 0 or positive")

    def test_get_index_is_not_in_array_boundary(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(len(self.l._CustomList__values), 3)

        index_out_of_range = [3, 4]

        for index in index_out_of_range:
            with self.assertRaises(ValueError) as ex:
                self.l.get(index)
            self.assertEqual(str(ex.exception.args[0]), "Index is out of range")

    def test_get_valid_index_returns_the_element(self):
        self.l._CustomList__values = [1, 2, 3, 1]

        result = self.l.get(0)
        self.assertEqual(result, 1)

    def test_args_is_not_iterable_raises_value_error(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(self.l._CustomList__values, [1, 2, 3])

        invalid_values = [1, 2.4]

        for invalid in invalid_values:
            with self.assertRaises(ValueError) as ex:
                self.l.extend(invalid)
            self.assertEqual(str(ex.exception.args[0]), "Value is not an iterable")

        self.assertEqual(self.l._CustomList__values, [1, 2, 3])

    def test_extend_extends_list_with_values_by_unpacking_them(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(self.l._CustomList__values, [1, 2, 3])

        result = self.l.extend([3, 4])
        self.assertEqual(self.l._CustomList__values, [1, 2, 3, 3, 4])

        self.assertIs(result, self.l._CustomList__values)

    def test_insert_type_of_index_is_not_integer_raises(self):
        invalid_args = [2.5, "asd", [1, 23], {"1": 1}]

        for invalid_arg in invalid_args:
            with self.assertRaises(TypeError) as ex:
                self.l.insert(invalid_arg, 5)
            self.assertEqual(str(ex.exception.args[0]), f"Index must be of type integer")

    def test_insert_check_index_argument_is_not_positive_or_zero_integer_raises(self):
        invalid_value = -1
        with self.assertRaises(ValueError) as ex:
            self.l.insert(invalid_value, 5)
        self.assertEqual(str(ex.exception.args[0]), "Integer must be 0 or positive")

    def test_insert_index_is_not_in_array_boundary_raises(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(len(self.l._CustomList__values), 3)

        index_out_of_range = [3, 4]

        for index in index_out_of_range:
            with self.assertRaises(ValueError) as ex:
                self.l.insert(index, 5)
            self.assertEqual(str(ex.exception.args[0]), "Index is out of range")

    def test_insert_adds_value_on_correct_index(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(self.l._CustomList__values, [1, 2, 3])

        result = self.l.insert(0, 5)
        self.assertEqual(self.l._CustomList__values, [5, 1, 2, 3])
        self.assertIs(result, self.l._CustomList__values)

        result = self.l.insert(2, 100)
        self.assertEqual(self.l._CustomList__values, [5, 1, 100, 2, 3])
        self.assertIs(result, self.l._CustomList__values)

    def test_pop_empty_list_raises(self):
        self.assertEqual(self.l._CustomList__values, [])

        with self.assertRaises(EmptyListException) as ex:
            self.l.pop()

        self.assertEqual(str(ex.exception.args[0]), "Can not pop from an empty list")

    def test_pop_last_element_leaves_list_empty(self):
        self.l._CustomList__values = [100]
        self.assertEqual(self.l._CustomList__values, [100])

        result = self.l.pop()
        self.assertEqual(self.l._CustomList__values, [])
        self.assertEqual(result, 100)

    def test_pop_only_last_element(self):
        self.l._CustomList__values = [100, 1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

        self.l.pop()
        self.assertEqual(self.l._CustomList__values, [100, 1, 2])

    def test_clear_empty_list(self):
        self.assertEqual(self.l._CustomList__values, [])

        self.l.clear()

        self.assertEqual(self.l._CustomList__values, [])

    def test_clear_delete_all_elements(self):
        self.l._CustomList__values = [100, 1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

        result = self.l.clear()

        self.assertIsNone(result)
        self.assertEqual(self.l._CustomList__values, [])

    def test_index_value_does_not_exist(self):
        self.l._CustomList__values = [100, 1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

        with self.assertRaises(ValueError) as ex:
            self.l.index(3)
        self.assertEqual(str(ex.exception.args[0]), "Value is not in the list")

    def test_index_returns_first_occurrence_of_the_value(self):
        self.l._CustomList__values = [100, 1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

        result = self.l.index(100)

        self.assertEqual(result, 0)
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

    def test_count_value_is_not_in_the_list_returns_0(self):
        self.l._CustomList__values = [100, 1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

        result = self.l.count(3)

        self.assertEqual(result, 0)
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

    def test_count_value_returns_count(self):
        self.l._CustomList__values = [100, 1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

        result = self.l.count(100)

        self.assertEqual(result, 2)
        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])

    def test_reverse_empty_list(self):
        self.assertEqual(self.l._CustomList__values, [])

        result = self.l.reverse()

        self.assertEqual(self.l._CustomList__values, [])
        self.assertIsNot(self.l._CustomList__values, result)

    def test_reverse_returns_new_list_with_reversed_value_order(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [1, 2, 100])

        result = self.l.reverse()

        self.assertEqual(self.l._CustomList__values, [1, 2, 100])
        self.assertEqual(result, [100, 2, 1])
        self.assertIsNot(result, self.l._CustomList__values)

    def test_copy_empty_list(self):
        self.assertEqual(self.l._CustomList__values, [])

        result = self.l.copy()

        self.assertEqual(self.l._CustomList__values, [])
        self.assertIsNot(self.l._CustomList__values, result)

    def test_copy_returns_same_values_new_list(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [1, 2, 100])

        result = self.l.copy()

        self.assertEqual(self.l._CustomList__values, [1, 2, 100])
        self.assertEqual(result, [1, 2, 100])
        self.assertIsNot(result, self.l._CustomList__values)

    def test_size_empty_list_returns_0(self):
        self.assertEqual(self.l._CustomList__values, [])
        self.assertEqual(len(self.l._CustomList__values), 0)

        result = self.l.size()

        self.assertEqual(self.l._CustomList__values, [])
        self.assertEqual(result, 0)


    def test_size_returns_length_of_the_list(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [1, 2, 100])
        self.assertEqual(len(self.l._CustomList__values), 3)

        result = self.l.size()

        self.assertEqual(self.l._CustomList__values, [1, 2, 100])
        self.assertEqual(result, 3)

    def test_add_first_empty_list_ends_up_with_one_element(self):
        self.assertEqual(self.l._CustomList__values, [])
        self.assertEqual(len(self.l._CustomList__values), 0)

        result = self.l.add_first(5)

        self.assertIsNone(result)

        self.assertEqual(self.l._CustomList__values, [5])
        self.assertEqual(len(self.l._CustomList__values), 1)

    def test_add_first_elements_in_list_ends_up_with_the_element_at_index_0(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual(self.l._CustomList__values, [1, 2, 100])
        self.assertEqual(len(self.l._CustomList__values), 3)

        result = self.l.add_first(100)

        self.assertEqual(self.l._CustomList__values, [100, 1, 2, 100])
        self.assertEqual(len(self.l._CustomList__values), 4)

        self.assertIsNone(result)

if __name__ == "__main__":
    main()
