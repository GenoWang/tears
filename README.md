# tears

A pwnable challenge for BHU CTF organized by Lancet.

**Challenge Description**

Three lines of tears.

**Difficulty**

Easy.

You can compile the binary by running
```bash
make clean & make all
```
build the docker by running
```bash
docker build -t "tears" .
```
run the docker by running
```bash
docker run -d -p "0.0.0.0:2333:9999" tears
```
and the challenge will run at port 2333.


## Vulnerability

Three times of writing 4-byte anything anywhere. 

Noticed that .text segment is writable(RWX).

Step 1: Overwrite return address to `hack()`(4 bytes);

Step 2~3: Overwrite `echo flag` to `/bin/sh `(8 bytes), getshell. 

- You may find that the addess of the stack in docker enviroment is different from the address in your local enviroment. The `relative` number is used to judge that.

- If you only want to overwrite `echo` to `more`, the string left will be ruined, so overwrite to `/bin/sh` is more reliable.