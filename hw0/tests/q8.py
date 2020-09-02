test = {
  'name': 'q8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert age_range > 30
          >>> assert age_range == sols["q8"]
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
