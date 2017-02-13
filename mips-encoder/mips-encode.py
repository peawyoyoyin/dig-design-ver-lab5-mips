import json
import sys

instructionsetFile = open("instructionset.json")
instructionset=json.loads(instructionsetFile.read())

def encodeLine(line):
    tokens = line.split()
    try:
        instr = instructionset[tokens[0]]
    except KeyError:
        print("error: instruction "+"'"+tokens[0]+"' not found")
    if(instr["type"] == "R"):
        opcodeBin = "{0:06b}".format(int(instr["opcode"],16))
        functBin = "{0:06b}".format(int(instr["funct"],16))

        rsBin = "{0:05b}".format(int(tokens[1],16))
        rtBin = "{0:05b}".format(int(tokens[2],16))
        rdBin = "{0:05b}".format(int(tokens[3],16))
        shamtBin = "{0:05b}".format(int(tokens[4],16))

        return "".join([opcodeBin,rsBin,rtBin,rdBin,shamtBin,functBin])
    elif(instr["type"] == "I"):
        opcodeBin = "{0:06b}".format(int(instr["opcode"],16))
        rsBin = "{0:05b}".format(int(tokens[1],16))
        rtBin = "{0:05b}".format(int(tokens[2],16))
        immBin = "{0:016b}".format(int(tokens[3],16))

        return "".join([opcodeBin,rsBin,rtBin,immBin])

def encodeFile(filename, outFile=sys.stdout):
    try:
        f=open(filename)
    except FileNotFoundError:
        print("error: file",filename,"not found")
        return

    for line in f:
        print(encodeLine(line.strip()),file=outFile)

# encodeFile(input().strip())
