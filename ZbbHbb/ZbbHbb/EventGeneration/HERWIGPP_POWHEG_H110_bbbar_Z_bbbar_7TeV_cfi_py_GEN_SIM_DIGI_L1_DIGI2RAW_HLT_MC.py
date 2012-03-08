# Auto generated configuration file
# using: 
# Revision: 1.303.2.7 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: HERWIGPP_POWHEG_H110_bbbar_Z_bbbar_7TeV_cfi.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT --conditions FrontierConditions_GlobalTag,MC_42_V13::All --datatier GEN-SIM-RAW --eventcontent RAWSIM -n 1000 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic7TeV2011Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\\$Revision: 1.1 $'),
    annotation = cms.untracked.string('HERWIGPP/POWHEG: (H->bb)(Z->bb), m(H)=110 GeV'),
    name = cms.untracked.string('\\$Source: /afs/cern.ch/project/cvs/reps/CMSSW/CMSSW/Configuration/GenProduction/python/HERWIGPP_POWHEG_H110_bbbar_Z_bb_7TeV_cfi.py,v $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('HERWIGPP_POWHEG_H110_bbbar_Z_bbbar_7TeV_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RAW')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'MC_42_V13::All'

process.generator = cms.EDFilter("ThePEGGeneratorFilter",
    cm10TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV'),
    run = cms.string('LHC'),
    repository = cms.string('HerwigDefaults.rpo'),
    cm14TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 14000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV'),
    dataLocation = cms.string('${HERWIGPATH}'),
    pdfCTEQ5L = cms.vstring('mkdir /LHAPDF', 
        'cd /LHAPDF', 
        'create ThePEG::LHAPDF CTEQ5L', 
        'set CTEQ5L:PDFName cteq5l.LHgrid', 
        'set CTEQ5L:RemnantHandler /Herwig/Partons/HadronRemnants', 
        'cp CTEQ5L /cmsPDFSet', 
        'cd /'),
    lheDefaults = cms.vstring('cd /Herwig/Cuts', 
        'create ThePEG::Cuts NoCuts', 
        'cd /Herwig/EventHandlers', 
        'create ThePEG::LesHouchesInterface LHEReader', 
        'set LHEReader:Cuts /Herwig/Cuts/NoCuts', 
        'create ThePEG::LesHouchesEventHandler LHEHandler', 
        'set LHEHandler:WeightOption VarWeight', 
        'set LHEHandler:PartonExtractor /Herwig/Partons/QCDExtractor', 
        'set LHEHandler:CascadeHandler /Herwig/Shower/ShowerHandler', 
        'set LHEHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler', 
        'set LHEHandler:DecayHandler /Herwig/Decays/DecayHandler', 
        'insert LHEHandler:LesHouchesReaders 0 LHEReader', 
        'cd /Herwig/Generators', 
        'set LHCGenerator:EventHandler /Herwig/EventHandlers/LHEHandler', 
        'cd /Herwig/Shower', 
        'set Evolver:HardVetoScaleSource Read', 
        'set Evolver:MECorrMode No', 
        'cd /'),
    cmsDefaults = cms.vstring('+pdfMRST2001', 
        '+basicSetup', 
        '+cm14TeV', 
        '+setParticlesStableForDetector'),
    lheDefaultPDFs = cms.vstring('cd /Herwig/EventHandlers', 
        'set LHEReader:PDFA /cmsPDFSet', 
        'set LHEReader:PDFB /cmsPDFSet', 
        'cd /'),
    pdfMRST2001 = cms.vstring('cp /Herwig/Partons/MRST /cmsPDFSet'),
    generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    basicSetup = cms.vstring('cd /Herwig/Generators', 
        'create ThePEG::RandomEngineGlue /Herwig/RandomGlue', 
        'set LHCGenerator:RandomNumberGenerator /Herwig/RandomGlue', 
        'set LHCGenerator:NumberOfEvents 10000000', 
        'set LHCGenerator:DebugLevel 1', 
        'set LHCGenerator:PrintEvent 0', 
        'set LHCGenerator:MaxErrors 10000', 
        'cd /Herwig/Particles', 
        'set p+:PDF /cmsPDFSet', 
        'set pbar-:PDF /cmsPDFSet', 
        'cd /'),
    setParticlesStableForDetector = cms.vstring('cd /Herwig/Particles', 
        'set mu-:Stable Stable', 
        'set mu+:Stable Stable', 
        'set Sigma-:Stable Stable', 
        'set Sigmabar+:Stable Stable', 
        'set Lambda0:Stable Stable', 
        'set Lambdabar0:Stable Stable', 
        'set Sigma+:Stable Stable', 
        'set Sigmabar-:Stable Stable', 
        'set Xi-:Stable Stable', 
        'set Xibar+:Stable Stable', 
        'set Xi0:Stable Stable', 
        'set Xibar0:Stable Stable', 
        'set Omega-:Stable Stable', 
        'set Omegabar+:Stable Stable', 
        'set pi+:Stable Stable', 
        'set pi-:Stable Stable', 
        'set K+:Stable Stable', 
        'set K-:Stable Stable', 
        'set K_S0:Stable Stable', 
        'set K_L0:Stable Stable', 
        'cd /'),
    pdfCTEQ6L1 = cms.vstring('mkdir /LHAPDF', 
        'cd /LHAPDF', 
        'create ThePEG::LHAPDF CTEQ6L1', 
        'set CTEQ6L1:PDFName cteq6ll.LHpdf', 
        'set CTEQ6L1:RemnantHandler /Herwig/Partons/HadronRemnants', 
        'cp CTEQ6L1 /cmsPDFSet', 
        'cd /'),
    cm7TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 7000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV'),
    HbbZbbParameters = cms.vstring('cd /Herwig/MatrixElements/', 
        'insert SimpleQCD:MatrixElements[0] PowhegMEPP2ZH', 
        'set /Herwig/Cuts/JetKtCut:MinKT 0.0*GeV', 
        'set /Herwig/Particles/h0:NominalMass 110.*GeV', 
        'set /Herwig/Particles/h0/h0->b,bbar;:OnOff On', 
        'set /Herwig/Particles/h0/h0->b,bbar;:BranchingRatio 0.7195', 
        'set /Herwig/Particles/h0/h0->W+,W-;:OnOff Off', 
        'set /Herwig/Particles/h0/h0->tau-,tau+;:OnOff Off', 
        'set /Herwig/Particles/h0/h0->g,g;:OnOff Off', 
        'set /Herwig/Particles/h0/h0->c,cbar;:OnOff Off', 
        'set /Herwig/Particles/h0/h0->Z0,Z0;:OnOff Off', 
        'set /Herwig/Particles/h0/h0->gamma,gamma;:OnOff Off', 
        'set /Herwig/Particles/h0/h0->mu-,mu+;:OnOff Off', 
        'set /Herwig/Particles/h0/h0->t,tbar;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->d,dbar;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->s,sbar;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->b,bbar;:OnOff On', 
        'set /Herwig/Particles/Z0/Z0->u,ubar;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->c,cbar;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->nu_e,nu_ebar;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->nu_mu,nu_mubar;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->nu_tau,nu_taubar;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->e-,e+;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->mu-,mu+;:OnOff Off', 
        'set /Herwig/Particles/Z0/Z0->tau-,tau+;:OnOff Off'),
    filterEfficiency = cms.untracked.double(1.0),
    pdfCTEQ6M = cms.vstring('mkdir /LHAPDF', 
        'cd /LHAPDF', 
        'create ThePEG::LHAPDF CTEQ6M', 
        'set CTEQ6M:PDFName cteq6mE.LHgrid', 
        'set CTEQ6M:RemnantHandler /Herwig/Partons/HadronRemnants', 
        'cp CTEQ6M /cmsPDFSet', 
        'cd /'),
    configFiles = cms.vstring(),
    powhegDefaults = cms.vstring('# Need to use an NLO PDF', 
        'cp /Herwig/Partons/MRST-NLO /cmsPDFSet', 
        '# and strong coupling', 
        'create Herwig::O2AlphaS O2AlphaS', 
        'set /Herwig/Generators/LHCGenerator:StandardModelParameters:QCD/RunningAlphaS O2AlphaS', 
        '# Setup the POWHEG shower', 
        'cd /Herwig/Shower', 
        '# use the general recon for now', 
        'set KinematicsReconstructor:ReconstructionOption General', 
        '# create the Powheg evolver and use it instead of the default one', 
        'create Herwig::PowhegEvolver PowhegEvolver HwPowhegShower.so', 
        'set ShowerHandler:Evolver PowhegEvolver', 
        'set PowhegEvolver:ShowerModel ShowerModel', 
        'set PowhegEvolver:SplittingGenerator SplittingGenerator', 
        'set PowhegEvolver:MECorrMode 0', 
        '# create and use the Drell-yan hard emission generator', 
        'create Herwig::DrellYanHardGenerator DrellYanHardGenerator', 
        'set DrellYanHardGenerator:ShowerAlpha AlphaQCD', 
        'insert PowhegEvolver:HardGenerator 0 DrellYanHardGenerator', 
        '# create and use the gg->H hard emission generator', 
        'create Herwig::GGtoHHardGenerator GGtoHHardGenerator', 
        'set GGtoHHardGenerator:ShowerAlpha AlphaQCD', 
        'insert PowhegEvolver:HardGenerator 0 GGtoHHardGenerator'),
    crossSection = cms.untracked.double(1.0),
    parameterSets = cms.vstring('cm7TeV', 
        'powhegDefaults', 
        'HbbZbbParameters', 
        'basicSetup', 
        'setParticlesStableForDetector')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 
