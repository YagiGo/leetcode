# dead simple for python, but may not be allowed to use, in which case refer to the doc, and just copy paste the original data

Class solution(object):
  def permutations(nums):
    return list(itertools.permutaions(nums))
   
   def combinations(n, k):
    return list(itertools.combinations(range(1,n+1), k)
