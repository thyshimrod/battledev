#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable );
#* to display simple variables in a dedicated area.
#* ***/
import sys

lines = []
i = 0
maxlen = 0
"""for line in sys.stdin:
    if i > 0:
        val = line.rstrip('\n')
        if len(val) > maxlen:
            maxlen = len(val)
        lines.append(val)

    i += 1
"""
lines.append("ACT")
lines.append("AGGG")
lines.append("GGT")
lines.append("CCAC")

lines.append("GTG")
lines.append("TAC")
lines.append("TCCC")
lines.append("AATG")

totalLen = 0
for l in lines:
    totalLen += len(l)

def inverse(val):
    result = ""
    for v in val:
        if v == "A":
            result += "T"
        elif v=="T":
            result +="A"
        elif v=="G":
            result +="C"
        else:
            result += "G"
    return result
a = ""
b = ""

size = totalLen //2
def combin(val, lines):
    result = ""
    tab = []
    for i in range(len(lines)):
        result = val + " " + lines[i]
        if len(result.replace(" ","")) == size:
            tab.append(result)
        elif len(result.replace(" ","")) < size:
            t2 =[]
            for j in range(len(lines)):
                if j != i:
                  t2.append(lines[j])
            p = combin(result,t2)
            for t in p:
                tab.append(t)
    return tab


tab= []

for i in range(len(lines)):
    val = lines[i]
    if len(val) == size:
        tab.append(val)
    else:
        t = []
        for j in range(len(lines)):
            if j != i:
                t.append(lines[j])
        vals = combin(val, t)
        for v in vals:
            tab.append(v)

print (tab)
for t in tab:
    if t != "":
        inv = inverse(t.replace(" ",""))
        for i in tab:
            if i.replace(" ","") == inv:
                a = t
                b = i
                break

print(a +"#" + b)
