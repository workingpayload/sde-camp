def solve(n, k, s):
			if len(n)==1:
				return n[-1]
			n.pop(s)
			l = len(n)
			s = (s+k-1)%l
			return solve(n,k,s)
		l = list(range(1, n+1))
		x = (0+k-1)%n
		ans = solve(l, k, x)
		return ans
