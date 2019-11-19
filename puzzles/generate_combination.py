def genFromArray(arr, k):
	if len(arr) < k: #no solution exists
		return []

	if len(arr) == k: #only one solution exists
		return [arr]

	if(k==1):
		return [[x] for x in arr]

	solutions = []
	for first in arr:
		rest = [x for x in arr if x > first]
		down = genFromArray(rest, k-1)
		if len(down):
			sol = [[first] + i for i in down]
			solutions = solutions + sol;

	return solutions

def generateCombinations(n,k):
	solutions = []
	candidates = list(range(1,n+1))
	solutions = genFromArray(candidates, k)
	for s in solutions:
		print(s)


generateCombinations(12,10)