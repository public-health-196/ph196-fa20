test = {
  'name': 'q3g',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert type(ziadopril_effect) in (int, np.int64, float, np.float64), "The treatment effect should be a numeric type (integer or float)"
          >>> assert ziadopril_effect < np.mean(with_zp_sysbp) - np.mean(without_zp["SYSBP"])
          >>> assert abs(ziadopril_effect - (-20)) <= 3
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
