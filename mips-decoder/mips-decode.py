import json
import string
####init
## load instructionset.json

instructionsetFile = open("instructionset.json")
instructionset = json.loads(instructionsetFile.read())

## input binary file
def decode(filename, rtl=False):
    try:
        f=open(filename)
    except FileNotFoundError:
        print("file not found")
        return
        
    for line in f:
        opcodeBin = line[0:6]
        opcode = "{0:02x}".format(int(opcodeBin,2))
        instruction = instructionset[opcode]

        if(instruction["type"] == "R"):
            rsBin = line[6:11]
            rtBin = line[11:16]
            rdBin = line[16:21]
            shamtBin = line[21:26]            
            functBin = line[26:32].strip()

            rs = "{0:02x}".format(int(rsBin,2))
            rt = "{0:02x}".format(int(rtBin,2))
            rd = "{0:02x}".format(int(rdBin,2))
            shamt = "{0:02x}".format(int(shamtBin,2))
            
            funct = "{0:02x}".format(int(functBin,2))

            instr_var = instruction["variations"][funct]

            rtlTemplate = string.Template(instr_var["rtl"])
            rtlString = rtlTemplate.substitute(rs=rs, rt=rt, rd=rd, shamt=shamt)

            if(rtl):
                print(rtlString)
            else:
                print(instr_var["name"],rs,rt,rd,shamt)

            
        if(instruction["type"] == "I"):
            rsBin = line[6:11]
            rtBin = line[11:16]
            immBin = line[16:32]

            #calculate SignExtImmBin
            if(immBin[0] == "1"):
                SignExtImmBin = "1111111111111111" + immBin
            elif(immBin[0] == "0"):
                SignExtImmBin = "0000000000000000" + immBin

            rs = "{0:02x}".format(int(rsBin,2))
            rt = "{0:02x}".format(int(rtBin,2))
            imm = "{0:04x}".format(int(immBin,2))
            SignExtImm = "{0:04x}".format(int(immBin,2))

            rtlTemplate = string.Template(instruction["rtl"])
            rtlString = rtlTemplate.substitute(rs=rs, rt=rt, imm=imm, SignExtImm=SignExtImm)

            if(rtl):
                print(rtlString)
            else:
                print(instruction["name"],rs,rt,imm)
                

decode(input("input filename"), [False,True][input("rtl?(Y/N)").strip() == "Y"])
