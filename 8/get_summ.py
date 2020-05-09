def get_summ (one, two, delimeter = ' '):
	return str(one) + str(delimeter) + str(two)

a = get_summ('Hello', 'world!', delimeter = '&')
b = get_summ('Hello', 'world!', ' + ')
c = get_summ('Hello', 'world!')
print(a.upper(),b.upper(),c.upper())