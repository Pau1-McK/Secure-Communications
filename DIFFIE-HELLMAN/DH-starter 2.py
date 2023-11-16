p = 28151

for g in range(2, p):
    for n in range(2,p):

        if pow(g,n,p) == g:
            break

    else:
        print(g)
        break
    

