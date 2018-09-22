def magic_eight():
	while True:
		answer = input('What is your question?')
		if answer == "quit":
			break
		elif answer[-1] != "?":
			print('I am sorry, I can only answer questions.')
