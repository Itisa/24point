import sys

def points(a,b,c,d):
	ans3 = 0
	p1 = 0
	p2 = 0
	for z in range(24):
		p1 += 1
		if p1 < 3:
			a1 = a
			b1 = b
			if p1 == 1:
				c1 = c
				d1 = c
			else:
				c1 = d
				d1 = c
		elif p1 > 2 and p1 < 5:
			b1 = a
			c1 = b
			if p1 == 3:
				d1 = c
				a1 = d
			else:
				d1 = d
				a1 = c
		elif p1 > 4 and p1 < 7:
			c1 = a
			d1 = b
			if p1 == 5:
				a1 = c
				b1 = d
			else:
				a1 = d
				b1 = c
		elif p1 > 6 and p1 < 9:
			d1 = a
			a1 = b
			if p1 == 7:
				b1 = c
				c1 = d
			else:
				b1 = d
				c1 = c
		elif p1 > 8 and p1 < 11:
			a1 = a
			c1 = b
			if p1 == 9:
				b1 = c
				d1 = d
			else:
				b1 = d
				d1 = b
		elif p1 > 10 and p1 < 13:
			b1 = a
			d1 = b
			if p1 == 11:
				a1 = c
				c1 = d
			else:
				a1 = d
				c1 = c
		elif p1 > 12 and p1 < 15:
			c1 = a
			a1 = b
			if p1 == 13:
				b1 = c
				d1 = d
			else:
				b1 = d 
				d1 = c
		elif p1 > 14 and p1 < 17:
			d1 = a
			b1 = b
			if p1 == 13:
				a1 = c
				b1 = d
			else:
				a1 = d
				b1 = c
		elif p1 > 14 and p1 < 17:
			a1 = b
			b1 = a
			if p1 == 13:
				c1 = c
				d1 = d
			else:
				c1 = d 
				d1 = c
		elif p1 >16 and p1 < 19:
			b1 = a
			c1 = b
			if p1 == 16:
				d1 = c
				a1 = d
			else:
				d1 = d
				a1 = c
		elif p1 >18 and p1 < 21:
			c1 = a
			d1 = b
			if p1 == 18:
				a1 = c
				b1 = d
			else:
				a1 = d
				b1 = c
		elif p1 >20 and p1 < 23:
			d1 = a
			a1 = b
			if p1 == 20:
				b1 = c
				c1 = d
			else:
				b1 = d
				c1 = c
		elif p1 >22 and p1 < 25:
			a1 = b
			c1 = a
			if p1 == 22:
				b1 = c
				d1 = d
			else:
				b1 = d
				d1 = c
		elif p1 >24 and p1 < 27:
			b1 = b
			d1 = a
			if p1 == 24:
				c1 = c
				a1 = d
			else:
				c1 = d
				a1 = c
		elif p1 >26 and p1 < 29:
			c1 = b
			a1 = a
			if p1 ==26:
				d1 = c
				b1 = d
			else:
				d1 = d
				b1 = c
		else:
			d1 = b
			b1 = a
			if p1 == 28:
				a1 = c
				c1 = d
			else:
				a1 = d
				c1 = c
		if ans3 == 24:
			break
		a2 = 0
		for z1 in range(96):
			a2 += 1
			if a2 >= 1 and a2 <=24:
				ans1 = a1 + b1
				fu1 = '+' 
			elif a2 >= 25 and a2 <= 48:
				ans1 = a1- b1
				fu1 = '-'
			elif a2 >= 49 and a2 <= 72:
				ans1 = a1* b1
				fu1 = '*'
			else:
				ans1 = a1/b1
				fu1 = '/'

			if a2 % 16 >= 1 and a2%16 <=4:
				ans2 = ans1 + c1
				fu2 = '+'
			elif a2 % 16 >= 5 and a2%16 <=8:
				ans2 = ans1 - c1
				fu2 = '-'
			elif a2 % 16 >= 9 and a2%16 <=12:
				ans2 = ans1 * c1
				fu2 = '*'
			else:
				ans2 = ans1 / c1
				fu2 = '/'

			if a2 % 4 == 1 :
				ans3 = ans2 + d1
				fu3 = '+'
			elif a2 % 4  == 2:
				ans1 = ans2 - d1
				fu3 = '-'
			elif a2 % 4 == 3:
				ans1 = ans2 * d1
				fu3 = '*'
			else:
				ans3 = ans2 / d1
				fu3 = '/'
				
			if ans3 == 24:								
				s = [a1,fu1,b1,fu2,c1,fu3,d1]
				for z in s:
					print z, 
				print '= 24'
				break
points(10,10,4,4)