"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [4, [(0, 0), (3, 3)]],
            "answer": 1,
        },
        {
            "input": [5, [(0, 1), (1, 1), (2, 2)]],
            "answer": 10,
        },
        {
            "input": [6, [(2, 0), (5, 3), (1, 3), (0, 0)]],
            "answer": 19,
        },
    ],
    "Extra": [
        {
            "input": [7, [(4, 4), (1, 2), (6, 5), (1, 5), (4, 2), (1, 4), (4, 5)]],
            "answer": 27,
        },
        {
            "input": [8, [(4, 4), (1, 3), (1, 2), (1, 1), (4, 6), (1, 4), (1, 0), (4, 1)]],
            "answer": 29,
        },
    ]
}
