test = {
  'name': 'q3f',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert type(conditioned_meds_effect) in (np.float64, float), "Your treatment effect should be a float"
          >>> assert np.isclose(conditioned_meds_effect, sols["q3f"])
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
