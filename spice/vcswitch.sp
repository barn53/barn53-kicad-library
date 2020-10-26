*Voltage controlled switch
.subckt vcswitch 1 2 3 4
*the switch instance
S1 3 4 1 2 TheSwitch
*the switch model
.model TheSwitch SW(Ron=1 Roff=100Meg Vt=.5 Vh=0)
.ends
