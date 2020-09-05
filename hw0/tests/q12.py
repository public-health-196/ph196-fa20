test = {
  'name': 'q12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert np.isclose(ci_low, sols["q12"][0]) or np.isclose(ci_low, sols["q12"][1])
          >>> assert np.isclose(ci_high, sols["q12"][2]) or np.isclose(ci_high, sols["q12"][3])
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
