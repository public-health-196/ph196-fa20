test = {
  'name': 'q4b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> assert abs(len(fr_one) - 0.8 * len(fr_clean)) <= 1, "fr_one has an incorrect number of rows"
            >>> assert abs(len(fr_two) - 0.2 * len(fr_clean)) <= 1, "fr_two has an incorrect number of rows"
            >>> assert len(fr_one.append(fr_two).drop_duplicates()) == len(fr_one) + len(fr_two), "Looks like you have some datapoints that are in both the datasets."
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
