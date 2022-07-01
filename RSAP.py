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
def EUCLIDES(a,b):
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

def eucExt(a,b):
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
 return [r[i-1], s[i-1], t[i-1]]
e1 = 7
e2 = 11
n = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
#phin = 15340386030041214054180649250360211715379547632640
c1 = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
c2 = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184

x1y1 = eucExt(e1,e2)
d1 = x1y1[0]
x1 = x1y1[1]
y1 = x1y1[2]
c2n = EUCLIDES(c2,n)
m = 0
if d1 == 1 and c2n == 1:
  c1_prima = INVERSO(c1,n)
  m = ((c1_prima**(-1*x1))*(c2**y1))%n
  print(m)
c_ = Cifrado(m,e1,n)
print(c_)
c_ = Cifrado(m,e2,n)
print(c_)