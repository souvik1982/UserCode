#!/bin/tcsh

source /uscmst1/prod/sw/cms/cshrc prod
setenv SCRAM_ARCH slc5_amd64_gcc434

cd /uscms_data/d2/souvik/testedm10/src
eval `scramv1 runtime -csh`

cd /uscms_data/d2/souvik/testedm10/src/ZbbHbb/ZbbHbb/NTuplizer
cmsRun patTuple_PF2PAT_Event_Candidates_MC_H110.py >& patTuple_PF2PAT_Event_Candidates_MC_H110.log
