test = {
  'name': 'q10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert "PROB" in fr_val.columns
          >>> assert np.all(fr_val["PROB"] < 1)
          >>> assert np.all(fr_val["PROB"] > 0)
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
