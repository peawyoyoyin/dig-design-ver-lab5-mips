# dig design verilog's lab5 mips encoder

for lab5's mips encoder
translates binary files into human-interpretable language, and compile commands into binary.
written in python 3.5.1

#### to compile a file into binary
- run `mips-encode.py`
- call `encodeFile(filename)` (or `encodeFile(filename, outFile)`

example
```python
encodeFile("test.txt") # This prints output to stdout
encodeFile("test.txt", open("out.txt","w")) # This prints output to file
```

#### to translate binary into commands
- run `mips-decode.py`
- call `decodeFile(filename)` or `decodeFile(filename, outFile)`

example
```python
decodeFile("instmem.txt") # This prints output to stdout
decodeFile("instmem.txt", open("out.txt","w")) # This prints output to file
```
