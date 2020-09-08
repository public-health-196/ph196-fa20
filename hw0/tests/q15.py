test = {
  'name': 'q15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert np.all(np.isclose(map_grouped_by_age["MAP"], sols["q15"]["MAP"]))
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
