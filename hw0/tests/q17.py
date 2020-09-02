test = {
  'name': 'q17',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert fit_lm(fr_clean[["CURSMOKE"]], fr_clean["TOTCHOL"]) is not None, "Did you forget to include a return statement in your function?"
          >>> assert type(fit_lm(fr_clean[["CURSMOKE"]], fr_clean["TOTCHOL"])) == sklearn.linear_model._base.LinearRegression
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
