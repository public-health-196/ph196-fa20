test = {
  'name': 'q8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert fr_train_t1.shape[0] == y_train_t1.shape[0], "Features and labels should be the same length"
          >>> assert fr_train_t1.shape[0] == 458, "Did you filter to just the treatment group?"
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
