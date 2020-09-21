test = {
  'name': 'q4a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> assert fr_clean.shape == sols['q4a'].shape, "Incorrect DataFrame shape. Check your rows and columns"
            >>> assert ~(fr_clean.isnull()).values.all(), "You have at least one missing value"
            >>> assert np.mean(fr_clean["HEARTRTE"]) == np.mean(sols['q4a']["HEARTRTE"]), "BMI column has incorrect mean"
            >>> assert np.sum(fr_clean["AGE"]) == np.sum(sols['q4a']["AGE"]), "Incorrect AGE column sum"
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
