def snakefill(n):
	e = 0
	while 2**(e+1) <= n**2:
		e+=1
	return e