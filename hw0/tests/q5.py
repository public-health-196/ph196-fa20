test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert type(person_age) in [int, np.int64], "The age should be an integer."
          >>> assert person_age == sols["q5"]
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
