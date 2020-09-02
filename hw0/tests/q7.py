test = {
  'name': 'q7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert len(over_50) < 0.7 * len(framingham), "Looks like you didn't filter enough rows."
          >>> assert np.all(over_50["AGE"] >= 50)
          >>> assert over_50.equals(sols["q7"])
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
