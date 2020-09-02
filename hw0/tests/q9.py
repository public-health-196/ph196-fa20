test = {
  'name': 'q9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert sorted_by_age["AGE"].iloc[0] > 50, "Looks like you may have not sorted in the correct order."
          >>> assert sorted_by_age.equals(sols["q9"])
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import pickle; \
        file = open("solutions.pkl", "rb");\
        sols = pickle.load(file);\
        file.close()',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
