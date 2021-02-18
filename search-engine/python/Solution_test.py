import unittest
import Solution

class SolutionTests(unittest.TestCase):
    def test_complex_case(self):
        searchEngine = Solution.SearchEngine()
        
        commands = [
            ("add", "dog", None),
            ("add", "document", None),
            ("exists", "dog", True),
            ("exists", "do.", True),
            ("exists", "...", True),
            ("exists", "....", False),
            ("add", "doge", None),
            ("exists", "....", True)
        ]

        for (command, param, expectation) in commands:
            if command == "add":
                searchEngine.add(param)
            elif command == "exists":
                self.assertEqual(searchEngine.exists(param), expectation)
            else:
                self.fail(f"{command} is not supported")

    def test_simple_case_with_dot(self):
        searchEngine = Solution.SearchEngine()
        
        commands = [
            ("add", "dog", None),
            ("exists", "do.", True),
        ]

        for (command, param, expectation) in commands:
            if command == "add":
                searchEngine.add(param)
            elif command == "exists":
                self.assertEqual(searchEngine.exists(param), expectation)
            else:
                self.fail(f"{command} is not supported")

    
    def test_simple_case_without_dots(self):
        searchEngine = Solution.SearchEngine()
        
        commands = [
            ("add", "dog", None),
            ("exists", "do", False),
            ("exists", "dog", True),
        ]

        for (command, param, expectation) in commands:
            if command == "add":
                searchEngine.add(param)
            elif command == "exists":
                self.assertEqual(searchEngine.exists(param), expectation)
            else:
                self.fail(f"{command} is not supported")

    def test_raises_error_when_adding_word_with_dot(self):
        searchEngine = Solution.SearchEngine()
        self.assertRaises(AssertionError, searchEngine.add, "dog.o")