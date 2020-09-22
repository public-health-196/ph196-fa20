test = {
  'name': 'q5b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> assert type(get_accuracy(fr_one[[feature_names[0]]], fr_one["CVD"], models[0])) in (float, np.float64), "get_accuracy should return a float"
            >>> assert get_accuracy(fr_one[[feature_names[0]]], fr_one["CVD"], models[0]) >= 0.7, "Your get_accuracy function is producing very low accuracies, are you sure you're calculating accuracy correctly?"
            >>> assert get_accuracy(fr_one[[feature_names[0]]], fr_one["CVD"], models[0]) <= 0.8, "Your get_accuracy function is producing very high accuracies, are you sure you're calculating accuracy correctly?"
            >>> assert get_accuracy(fr_one[[feature_names[0]]], fr_one["CVD"], models[0]) >= 0, "Accuracies can't be less than 0"
            >>> assert get_accuracy(fr_one[[feature_names[0]]], fr_one["CVD"], models[0]) <= 1, "Accuracies can't be greater than 1"
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
