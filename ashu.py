nth=int(input("Enter No. : "))
b=0 
l=0
num = 1
while b != nth:
  sum = 0
  a = num
  while a != 0:
    rem = a % 10
    a = a // 10
    sum = sum * 10 + rem
  if num==sum:
    c=0
    for i in range(1,sum+1):
      if sum%i==0:
        c=c+1
      else:
        continue
    if c==2:
      b = b + 1
      l = num
  num=num+1
print(l)