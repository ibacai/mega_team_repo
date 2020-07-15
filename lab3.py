# python3.6  
# coding: utf-8  
# store the human preproinsulin sequence in a variable called preproinsulin:  
#preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# store the remaining sequence elements of human insulin in variables:  
#lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
#cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin
# "giveqcctsicslyqlenycncrreaedlqvgqvelgggpgagslqplalegslqkr"

pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

print(insulin.count('y'))

seqCount = {x : insulin.count(x) for x in ['y','c','k','h','r','d','e']}
print(seqCount)
#bank = {"M" : 100, "C" : 200}
#y : float(insulin.count(y)
#c : float(insulin.count(c)
#k : float(insulin.count(k)
pH= 0
#print(netCharge) 
while(pH <= 14):
  netCharge = (
    +(sum({x : ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x : ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
  print('{0:.2f}'.format(pH), netCharge)
  pH += 1
