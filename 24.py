import sys

a = 4
b = 3
c = 2
d = 1

e = 0
for z in range(24):
        e = e + 1
        if e >=1 and e <=6:
            ae = a
        elif e >= 7 and e <= 12:
            ae = b
        elif e >= 13 and e <= 18:
            ae = c
        elif e >=19 and e <= 24:
            ae = d

        if e == 7 or e == 8 or e == 13 or e == 14 or e == 19 or e == 20:
            ee = a
        elif e == 1 or e == 2 or e == 15 or e == 16 or e == 21 or e == 22:
            ee = b
        elif e == 3 or e == 4 or e == 9 or e == 10 or e == 23 or e == 24:
            ee = c
        elif e == 5 or e == 6 or e == 11 or e == 12 or e == 17 or e == 18:
            ee = d

        if e == 9 or e == 11 or e == 15 or e == 17 or e == 21 or e == 23:
            ce = a
        elif e == 3 or e == 5 or e == 13 or e == 18 or e == 19 or e == 24:
            ce = b
        elif e == 1 or e == 6 or e == 7 or e == 12 or e == 20 or e == 22:
            ce = c
        elif e == 2 or e == 4 or e == 8 or e == 10 or e == 14 or e == 16:
            ce = d

        if e == 10 or e == 12 or e == 16 or e == 18 or e == 22 or e == 24:
            de = a
        elif e == 4 or e == 2 or e == 14 or e ==17 or e == 20 or e == 23:
            de = b
        elif e == 2 or e == 5 or e == 8 or e == 11 or e == 19 or e == 21:
            de = c
        elif e == 1 or e == 3 or e == 7 or e == 9 or e == 13 or e == 15:
            de = d

        if e == 25:
            e = 1

        a2 = 0
        for z1 in range(96):
            a2 = a2 + 1

            if a2 >= 1 and a2 <=24:
                ans1 = ae + ee
                fu1 = '+'
            elif a2 >= 25 and a2 <= 48:
                ans1 = ae- ee
                fu1 = '-'
            elif a2 >= 49 and a2 <= 72:
                ans1 = ae* ee
                fu1 = '*'
            else:
                ans1 = ae/ee
                fu1 = '/'

            if a2 % 16 >= 1 and a2%16 <=4:
                ans2 = ans1 + ce
                fu2 = '+'
            elif a2 % 16 >= 5 and a2%16 <=8:
                ans2 = ans1 - ce
                fu2 = '-'
            elif a2 % 16 >= 9 and a2%16 <=12:
                ans2 = ans1 * ce
                fu2 = '*'
            else:
                ans2 = ans1 / ce
                fu2 = '/'

            if a2 % 4 == 1 :
                ans3 = ans2 + de
                fu3 = '+'
            elif a2 % 4  == 2:
                ans1 = ans2 - de
                fu3 = '-'
            elif a2 % 4 == 3:
                ans1 = ans2 * de
                fu3 = '*'
            else:
                ans3 = ans2 / de
                fu3 = '/'
                
                if ans3 == 24:
                    break

print ae,ee,ce,de,ans1,ans2,ans3
s = [ae,fu1,ee,fu2,ce,fu3,de]
for z in s:
    print z,

#count24(10,10,4,4)
