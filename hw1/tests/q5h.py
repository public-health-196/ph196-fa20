test = {
  'name': 'q5h',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> assert len(get_roc(fr_one[[feature_names[0]]], fr_one["CVD"], models[0])) == 3, "Your function should return 3 things"
            >>> assert len(get_roc(fr_one[[feature_names[0]]], fr_one["CVD"], models[0])[0]) == 100, "Did you test 100 thresholds?"
            >>> assert get_roc(fr_one[[feature_names[0]]], fr_one["CVD"], models[0])[0][0] <= 1, "FPR/TPR should be between 0 and 1"
            >>> assert get_roc(fr_one[[feature_names[0]]], fr_one["CVD"], models[0])[0][0] >= 0, "FPR/TPR should be between 0 and 1"
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
