#!/usr/bin/env python
#
import sys, pwn

sh = pwn.process("/home/uu/Downloads/racecar_challenge/racecar")



name = b'x'
nickname = b'x'

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




sh.interactive()
