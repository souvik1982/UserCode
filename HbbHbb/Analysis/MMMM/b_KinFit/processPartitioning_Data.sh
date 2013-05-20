root -l -b -q '../../HbbHbb_Partitioning.cc++("8TeVData2012B_Skim", 90, 1)'
root -l -b -q '../../HbbHbb_Partitioning.cc++("8TeVData2012C_Skim", 90, 1)'
root -l -b -q '../../HbbHbb_Partitioning.cc++("8TeVData2012Cpart2_Skim", 90, 1)'
root -l -b -q '../../HbbHbb_Partitioning.cc++("8TeVData2012D_Skim", 90, 1)'
say "Partitioning all data at 90 done"
hadd -f Histograms_8TeVData2012BCD_Skim.root Histograms_8TeVData2012B_Skim.root Histograms_8TeVData2012C_Skim.root Histograms_8TeVData2012Cpart2_Skim.root Histograms_8TeVData2012D_Skim.root 
