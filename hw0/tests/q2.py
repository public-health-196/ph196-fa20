test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert num_rows == sols["q2"][0]
          >>> assert num_columns == sols["q2"][1]
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
