import FWCore.ParameterSet.Config as cms

process = cms.Process("Skim")

process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring( '/store/data/Run2011A/MinimumBias/RAW/v1/000/167/913/9AEA807A-ABA1-E011-ABE8-003048F11DE2.root' )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilter.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hltFilter.HLTPaths = ["HLT_L1ETM30_v*"]

process.out = cms.OutputModule("PoolOutputModule",
  fileName=cms.untracked.string("HLT_L1ETM30_Skimmed.root"),
  SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_L1ETM30_v*:HLT'))
  outputCommands = cms.untracked.vstring("drop FEDRawDataCollection_source_*_HLT")
)

process.filter_path = cms.Path(process.hltFilter)
process.endPath = cms.EndPath(process.out)
