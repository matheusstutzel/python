palavra=raw_input("Digite uma palavra: ")
n=len(palavra)
cont=0
for i in range(0,n):
    x=n-i-1
    if palavra[x]==palavra[i]:
        cont+=1
if cont==n:
    print "E um palindromo"
else:
    print "Nao e um palindromo"
#parte 2
###################################
palavra=raw_input("Digite uma palavra: ")
n=len(palavra)
u="sim"
while u=="sim" and i<=n//2:
    for i in range (0,n//2+1):
        x=n-1-i
        if palavra[x]!=palavra[i]:
            u=="nao"
if u=="sim":
    print "E um palindromo"
else:
    print "Nao e um palindromo"
