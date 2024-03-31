driving = input('Have you ever driven a car?')
if driving != 'yes' and driving != 'no':
	print('you can only answer yes or no')
	raise SystemExit

age = input('How old are you?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('You are pass')
	else:
		print('OMG you are illegal!')
elif driving == 'no':
	if age >= 18:
		print('you can get a liscence why not?')
	else:
		print('well, you can get a liscence in the future')
else:
	print('you can only answer yes or no')