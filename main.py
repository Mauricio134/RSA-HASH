def Fermat(a, x, n):
  if x == 0:
    return 1
  elif x%2 == 0:
    t = Fermat(a, x/2, n)
    return (t*t)%n
  else:
    t = Fermat(a, x-1, n)
    c = a%n
    return (t*c)%n

def Cifrado(m,e,n):
  P = Fermat(m,e,n)
  return P
def Descifrado(c,d,n):
  S = Fermat(c,d,n)
  return S
def EUCLIDES(a, b):
  if b == 0:
    return a
  else:
    return EUCLIDES(b, a%b)

def EUCLIDES_EXT(a,b):
 r = [a,b]
 s = [1,0] 
 t = [0,1]
 i = 1 
 q = [[]]
 while (r[i] != 0): 
  q = q + [r[i-1] // r[i]]
  r = r + [r[i-1] % r[i]]
  s = s + [s[i-1] - q[i]*s[i]]
  t = t + [t[i-1] - q[i]*t[i]]
  i = i+1
 return s[i-1]
def INVERSO(a, n):
    if EUCLIDES(a,n) == 1:
      return EUCLIDES_EXT(a,n)%n
    else:
      return 0

e = 65537
n = 999630013489
phi_n = 999628013860
c = 747120213790
d = INVERSO(e,phi_n)
for x in range(1,n):
  if EUCLIDES(x,n)==1:
    break
c_ = (c*Fermat(x,e,n))%n
m_ = Descifrado(c_,d,n)
x_ =INVERSO(x,n)
m = (m_*x_)%n
p = Cifrado(m,e,n)
print(m)
