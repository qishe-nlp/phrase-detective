from phrase_recognizer.lib import merge_range, merge

def test_merge_range():
  r = merge_range((1, 3), (4, 8))
  print(r)
  assert r == [(1, 3), (4, 8)]
  r = merge_range((1, 3), (3, 8))
  print(r)
  assert r == [(1, 3), (3, 8)]
  r = merge_range((1, 3), (2, 8))
  print(r)
  assert r == [(1, 8)]


def test_merge():
  r = merge([(1, 4),(3, 6), (4, 7), (9, 12)])
  print(r)
  assert r == [(1, 7), (9, 12)]
