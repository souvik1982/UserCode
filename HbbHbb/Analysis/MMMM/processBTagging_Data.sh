#root -l -b -q '../HbbHbbPileupWeight.c++("glugluToX600ToHHTobbbb_8TeV_FASTSIM_PU_Signal_2", "8TeVData2012BCD_V5_Data_2", "PUWeight.root")'
#say "Pileup Weights for Signal Monte Carlo created."

root -l -b -q '../HbbHbb_bTagging.cc++("Data", "8TeVData2012B_Skim", "MMMM")' 
say "2012B b-tagging done"
root -l -b -q '../HbbHbb_bTagging.cc++("Data", "8TeVData2012C_Skim", "MMMM")' 
say "2012C b-tagging done"
root -l -b -q '../HbbHbb_bTagging.cc++("Data", "8TeVData2012Cpart2_Skim", "MMMM")' 
say "2012C part 2 b-tagging done"
root -l -b -q '../HbbHbb_bTagging.cc++("Data", "8TeVData2012D_Skim", "MMMM")' 
say "2012D b-tagging done"
