#!/bin/tcsh
setenv SCRAM_ARCH slc5_amd64_gcc434
cd /afs/cern.ch/user/s/sdas/CMSSW_4_2_7_hltpatch1/src
cmsenv
cd /afs/cern.ch/user/s/sdas/CMSSW_4_2_7_hltpatch1/src/VHSkim/VHSkim/test/PFDesign/batch
#rm -f /tmp/sdas/*
cmsRun PFDesign_L1FastPFJets_RRRR.py >& /tmp/sdas/PFDesign_L1FastPFJets_RRRR.log
scp /tmp/sdas/PFDesign_L1FastPFJets_RRRR.log pcufl1.cern.ch:/data/1b/sdas/RAWHLT1fb
rfcp /tmp/sdas/HLT_PFDesign_Skimmed_RRRR /castor/cern.ch/user/s/sdas/METbb/PFDesign_L1ETM30Filtered/RAWHLT1fb
rm -f /tmp/sdas/HLT_PFDesign_Skimmed_RRRR
rm -f /tmp/sdas/PFDesign_L1FastPFJets_RRRR.log
