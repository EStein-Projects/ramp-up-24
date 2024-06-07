def stutter(word):
	return word[0:2] + "... " + word[0:2] + "... " + word + "?"
    # should've been: return f"{word[0:2]}... {word[0:2]}... {word}?",
	# but wasn't supported