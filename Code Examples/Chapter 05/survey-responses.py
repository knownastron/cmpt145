def survey_results( responses ):
    """
    Purpose:
        To count the number of people who gave the same response in a survey.
    Pre-Condition(s):
        responses: List containing responses from a survey.
    Post-Condition(s):
        (none)
    Return(s):
        Dictionary mapping each response to number of people.
    """

    results = {}  # mapping of response to number who gave that response

    # for every response, add its count to the relevant response tally
    for choice in responses:
        if choice not in results:
            results[choice] = 1
        else:
            results[choice] += 1

    return results
