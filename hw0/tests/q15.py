test = {
  'name': 'q15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert map_grouped_by_age.equals(sols["q15"])
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
