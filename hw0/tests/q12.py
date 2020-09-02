test = {
  'name': 'q12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert ci_low == sols["q12"][0]
          >>> assert ci_high == sols["q12"][1]
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
