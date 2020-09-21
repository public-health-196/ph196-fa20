test = {
  'name': 'q5a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> assert len(models) == len(feature_names), "Looks like you don't have the right number of models"
            >>> assert type(models[0]) == sklearn.linear_model._base.LinearRegression, "Your models list be a list of LinearRegression models"
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import sklearn.linear_model',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
