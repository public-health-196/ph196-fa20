test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> assert np.all([fr_clean[c].dtype in (int, np.int64) for c in list(fr_clean.columns)]), "Column is not type int"
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
