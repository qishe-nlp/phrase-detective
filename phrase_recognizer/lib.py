def merge_range(first, second):
  if first[1] <= second[0] or first[0] >= second[1]:
    return [first, second]
  else:
    return [(min(first[0], second[0]), max(first[1], second[1]))]


def merge(ranges):
  if len(ranges) == 0:
    return []
  ordered = sorted(ranges, key=lambda pair: pair[0])
  result = [ordered[0]] 
  for e in ordered[1:]:
    merged = merge_range(result[-1], e)
    del result[-1]
    result.extend(merged)
  return result


#print(merge([(1, 4),(3, 6), (4, 7), (9, 12)]))
