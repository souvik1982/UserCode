import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/uscms_data/d1/souvik/ZbbHbb/SignalEvents/H_110/res/HERWIGPP_POWHEG_H110_bbbar_Z_bbbar_7TeV_cfi_py_GEN_FASTSIM_HLT_6_1_a5O.root'
    )
)

process.demo = cms.EDAnalyzer("TriggerSignal",
    TriggerResults = cms.untracked.InputTag('TriggerResults', '', 'HLT')
)


process.p = cms.Path(process.demo)
