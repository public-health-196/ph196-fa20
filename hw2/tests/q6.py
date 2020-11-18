test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert fr_train.shape == (2998, 7)
          >>> assert fr_val.shape == (750, 7)
          >>> assert type(y_train) == pd.Series
          >>> assert len(y_train) == 2998
          >>> assert type(y_val) == pd.Series
          >>> assert len(y_val) == 750
          >>> assert split_set(fr_clean, size=0.5)[0].shape == (1874, 7)
          >>> assert split_set(fr_clean, size=0.99)[0].shape == (37, 7)
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
