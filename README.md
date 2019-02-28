# tears

A pwnable challenge for BHU CTF organized by Lancet.

**Challenge Description**

Three lines of tears.

**Difficulty**

Easy.

## Vulnerability

Three times of Writing 4 bytes anywhere. 

Noticed that .text segment is writable.

Step 1: Overwrite return address to `hack()`(4 bytes);

Step 2~3: Overwrite `echo flag` to `/bin/sh `(8 bytes), getshell. 

