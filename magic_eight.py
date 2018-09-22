from random import randint

def magic_eight():

	answerlist=['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.',  'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again', 'Ask again later.','Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.',  'My sources say no.', 'Outlook not so good.', 'Very doubtful.']


	while True:
		answer = input('What is your question?')
		if answer == "quit":
			break
		elif answer[-1] != "?":
			print('I am sorry, I can only answer questions.')
		else:
			final_return = answerlist[randint(0, len(answerlist))]
			print(final_return)
			return final_return

magic_eight()

