test = {
  'name': 'q4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert fr_clean.shape[1] == 8, "Wrong number of columns. Did you include the label column?"
          >>> assert fr_clean.shape[0] == 3748, "Wrong number of rows. Did you drop rows with NaN values?"
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
