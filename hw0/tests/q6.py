test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert len(small_data) == 10, "Looks like you didn't select 10 rows."
          >>> assert "SYSBP" not in small_data.columns, "Looks like you have some column(s) that shouldn't be there."
          >>> assert small_data.equals(sols["q6"])
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import pickle; \
        file = open("solutions.pkl", "rb");\
        sols = pickle.load(file);\
        file.close()',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
