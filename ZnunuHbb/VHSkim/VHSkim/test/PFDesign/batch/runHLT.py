#! /usr/bin/env python

import sys
import os
import commands
import string

def oneJob(n):
  os.system("sed 's/RRRR/%s/g' PFDesign_L1FastPFJets.py > PFDesign_L1FastPFJets_%s.py" % (n, n))
  #os.system("nohup cmsRun PFDesign_L1FastPFJets_%s.py >& /data/1b/sdas/RAWHLT1fb/PFDesign_L1FastPFJets_%s.log & " % (n, n))
  os.system("sed 's/RRRR/%s/g' job.csh > job_%s.csh" % (n, n))
  os.system("chmod a+x job_%s.csh" % n)
  #os.system("bsub -q cmscaf1nd job_%s.csh" % n)
  os.system("nohup ./job_%s.csh &" % n)
  
L = [
"6_1_fNr.root",
"10_1_KnH.root",
"11_1_Bc4.root",
"12_1_xhO.root",
"13_1_UcQ.root",
"14_1_1My.root",
"15_1_4jN.root",
"16_1_Rb8.root",
"17_1_EJw.root",
"18_1_DL8.root",
"19_1_M5g.root",
"1_1_EUs.root" ,
"20_1_HdJ.root",
"21_1_ldv.root",
"22_1_TDW.root",
"23_1_9Om.root",
"24_1_fTV.root",
"25_1_odh.root",
"26_1_6EN.root",
"27_1_mr7.root",
"28_1_PfV.root",
"29_1_SQw.root",
"2_1_XBT.root" ,
"30_1_UAc.root",
"31_1_CRe.root",
"32_1_1zK.root",
"33_1_apJ.root",
"34_1_jGd.root",
"35_1_LUa.root",
"36_1_QhR.root",
"37_1_tre.root",
"38_1_Xv6.root",
"39_1_Jxx.root",
"3_1_HBF.root" ,
"40_1_PYN.root",
"41_1_pKd.root",
"42_1_jzg.root",
"43_1_Kse.root",
"44_1_p7H.root",
"45_1_T0Z.root",
"46_1_pBD.root",
"47_1_L9q.root",
"48_1_14T.root",
"49_1_ivt.root",
"4_1_gUu.root" ,
"50_1_evo.root",
"51_1_mB2.root",
"52_1_mBR.root",
"53_1_yDi.root",
"54_1_upq.root",
"55_1_YrC.root",
"56_1_BgK.root",
"57_1_EfH.root",
"58_1_VuI.root",
"59_1_2RT.root",
"5_1_nAa.root" ,
"60_1_a4g.root",
"61_1_6YY.root",
"62_1_evI.root",
"63_1_CFI.root",
"64_1_xcn.root",
"65_1_UnS.root",
"66_1_6Xs.root",
"7_1_BeW.root" ,
"8_1_PhJ.root" ,
"9_1_YbO.root"
]

for item in L:
  oneJob(item)
  
