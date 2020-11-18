test = {
  'name': 'q9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert type(model_t1) == LogisticRegression
          >>> assert np.isclose(train_acc_t1, 0.64, 10e-2)
          >>> assert np.isclose(val_acc_t1, 0.71, 10e-2)
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
