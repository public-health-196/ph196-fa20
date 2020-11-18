test = {
  'name': 'q11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> assert old_treat.shape[0] == new_treat.shape[0]
            >>> assert old_treat.shape[0] == fr_val["BPMEDS"].sum()
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
