def check_equal(description: str, outcome, expected) -> None:
    """
   Returns test passed if the "expected" value of function "name" matches 
    "actual", otherwise returns test failed if the test fails.    
    
    >>> check_equals("Testing Rating:", 2, 2)
    Test Passed
    >>> check_equals("Testing Author:", 'Stephen King', 'Stephen King')
    Test Passed
    >>> check_equals("Testing Title:", "'Salem's Lot", "'Salem's Lot")
    Test Passed
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    book_dictionary = {}
    if outcome_type != expected_type:
        print("{0} FAILED: expected ({1}) has type {2}, " 
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
        return 1
    print("------")
    return 0