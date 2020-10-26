.SUBCKT irlml6244pbf 1 2 3
* SPICE3 MODEL WITH THERMAL RC NETWORK
**************************************
*      Model Generated by MODPEX     *
*Copyright(c) Symmetry Design Systems*
*         All Rights Reserved        *
*    UNPUBLISHED LICENSED SOFTWARE   *
*   Contains Proprietary Information *
*      Which is The Property of      *
*     SYMMETRY OR ITS LICENSORS      *
*Commercial Use or Resale Restricted *
*   by Symmetry License Agreement    *
**************************************
* Model generated on Aug 24, 10
* MODEL FORMAT: SPICE3
* Symmetry POWER MOS Model (Version 1.0)
* External Node Designations
* Node 1 -> Drain
* Node 2 -> Gate
* Node 3 -> Source
M1 9 7 8 8 MM L=100u W=100u
.MODEL MM NMOS LEVEL=1 IS=1e-32
+VTO=1.38659 LAMBDA=0.015733 KP=104.351
+CGSO=6.60124e-06 CGDO=6.01393e-07
RS 8 3 0.0101583
D1 3 1 MD
.MODEL MD D IS=6.97168e-10 RS=0.013416 N=1.08301 BV=20
+IBV=0.00025 EG=1.2 XTI=4 TT=1e-07
+CJO=1.39713e-10 VJ=1.80182 M=0.548803 FC=0.5
RDS 3 1 5e+07
RD 9 1 0.0001
RG 2 7 2.54887
D2 4 5 MD1
* Default values used in MD1:
*   RS=0 EG=1.11 XTI=3.0 TT=0
*   BV=infinite IBV=1mA
.MODEL MD1 D IS=1e-32 N=50
+CJO=8.0476e-10 VJ=0.5 M=0.9 FC=1e-08
D3 0 5 MD2
* Default values used in MD2:
*   EG=1.11 XTI=3.0 TT=0 CJO=0
*   BV=infinite IBV=1mA
.MODEL MD2 D IS=1e-10 N=0.495928 RS=3e-06
RL 5 10 1
FI2 7 9 VFI2 -1
VFI2 4 0 0
EV16 10 0 9 7 1
CAP 11 10 8.0476e-10
FI1 7 9 VFI1 -1
VFI1 11 6 0
RCAP 6 10 1
D4 0 6 MD3
* Default values used in MD3:
*   EG=1.11 XTI=3.0 TT=0 CJO=0
*   RS=0 BV=infinite IBV=1mA
.MODEL MD3 D IS=1e-10 N=0.495928
.ENDS irlml6244pbf
*SPICE Thermal Model Subcircuit
.SUBCKT irlml6244pbft 5 1

R_RTHERM1         5 4  6.056535
R_RTHERM2         4 3  42.170180
R_RTHERM3         3 2  33.134799
R_RTHERM4         2 1  18.526125
C_CTHERM1         5 1  0.000124
C_CTHERM2         4 1  0.005292
C_CTHERM3         3 1  0.04229
C_CTHERM4         2 1  0.001162

.ENDS irlml6244pbft 

 



