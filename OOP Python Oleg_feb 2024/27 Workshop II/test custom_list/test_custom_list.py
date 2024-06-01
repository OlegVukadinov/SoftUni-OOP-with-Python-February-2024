from unittest import TestCase, main

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
            self.assertEqual(str(ex.exception.args[0]), f"Index must be of type integer")

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

if __name__ == "__main__":
    main()
