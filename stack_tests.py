import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
# from stack_array import Stack


from stack_linked import Stack


class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

    def test_num(self):
        s = Stack(3)
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size(), 0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertFalse(s.is_empty())
        self.assertTrue(s.is_full())
        self.assertEqual(s.peek(), 3)
        s.pop()
        self.assertEqual(s.peek(), 2)

    def test_str(self):
        s = Stack(3)
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size(), 0)
        s.push("a")
        s.push("b")
        s.push("c")
        self.assertFalse(s.is_empty())
        self.assertTrue(s.is_full())
        self.assertEqual(s.peek(), "c")
        s.pop()
        self.assertEqual(s.peek(), "b")
        s.push("d")

    def test_except(self):
        s = Stack(1)
        try:
            s.pop()
        except IndexError:
            print("empty")
        try:
            s.peek()
        except IndexError:
            print("empty")
        s.push("x")
        try:
            s.push("y")
        except IndexError:
            print("full")


if __name__ == '__main__':
    unittest.main()
