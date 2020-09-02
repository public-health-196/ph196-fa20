test = {
  'name': 'q18',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert type(coeff) is not np.ndarray, "The coefficient on CURSMOKE should be a number not an array."
          >>> assert intercept == sols["q18"][0]
          >>> assert coeff == sols["q18"][1]
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
