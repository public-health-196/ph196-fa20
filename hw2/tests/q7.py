test = {
  'name': 'q7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert type(model) == LogisticRegression
          >>> assert np.isclose(train_acc, 0.73, 10e-2)
          >>> assert np.isclose(val_acc, 0.71, 10e-2)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
