# If I have a six-character password consisting of uppercase (English) letters and (decimal) digits only,
# how many seconds might it take an adversary to crack, assuming they make one attempt per second?

#   36⁶

from string import digits, ascii_uppercase

for i in digits + ascii_uppercase:
    for j in digits + ascii_uppercase:
        for k in digits + ascii_uppercase:
            for l in digits + ascii_uppercase:
                for m in digits + ascii_uppercase:
                    for n in digits + ascii_uppercase:
                        print(i, j, k, l, m, n)