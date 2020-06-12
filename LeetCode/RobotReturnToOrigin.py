class solution: 
	def judgeCircles(moves:str) -> bool:
		if ((moves.lower().count('u')) == (moves.lower().count('d')) and (moves.lower().count('r')) == moves.lower().count('l')):
			return True

		return False

	if (judgeCircles('rlrud')):
		print('tru')
	else:
		print('not tru')


