test = {
  'name': 'q10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert len(fr_clean) > 400, "Looks like you have dropped too many rows. Just drop the NaNs in the TOTCHOL column."
          >>> assert fr_clean.equals(sols["q10"])
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
