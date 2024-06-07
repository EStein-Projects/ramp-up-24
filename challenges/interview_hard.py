def interview(lst, tot):
	q = tot <= 120 and len(lst) == 8
	if q:
		for i, t in enumerate(lst):
			i = (i+2) * 2.5 // 5
			if t > i*5:
				q = False
				break
	if q:
		return "qualified"
	return "disqualified"