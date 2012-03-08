import FWCore.ParameterSet.Config as cms

process = cms.Process("VH")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring()
)
process.CAsubJetsProducer = cms.EDProducer("SubProducer",
    jetTag = cms.untracked.InputTag("caTopPFJets")
)


process.HLTQuadJet60 = cms.EDProducer("HLTInfoDumperGeneral",
    TriggerEvent = cms.untracked.InputTag("hltTriggerSummaryAOD","","HLT"),
    FilterNames = cms.untracked.VInputTag(cms.InputTag("hltQuadJet60","","HLT")),
    HLTPath = cms.untracked.string('HLT_QuadJet60_v'),
    TriggerResults = cms.untracked.InputTag("TriggerResults","","HLT")
)


process.HbbAnalyzerNew = cms.EDProducer("HbbAnalyzerNew",
    electronTag = cms.InputTag("selectedElectronsMatched"),
    runOnMC = cms.bool(False),
    tauTag = cms.InputTag("patTaus"),
    verbose = cms.untracked.bool(False),
    simplejet2Tag = cms.InputTag("cleanPatJetsAK5PF"),
    simplejet3Tag = cms.InputTag("selectedPatJetsAK7PF"),
    muonTag = cms.InputTag("selectedMuonsMatched"),
    jetTag = cms.InputTag("selectedPatJetsCAPF"),
    photonTag = cms.InputTag("selectedPatPhotons"),
    metTag = cms.InputTag("met"),
    simplejet4Tag = cms.InputTag("selectedPatJetsAK7Calo"),
    subjetTag = cms.InputTag("selectedPatJetssubCAPF"),
    simplejet1Tag = cms.InputTag("selectedPatJets"),
    hltResultsTag = cms.InputTag("TriggerResults","","HLT")
)


process.TauDecayModeCutMutliplexerPrototype = cms.EDProducer("RecoTauDecayModeCutMultiplexer",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        nCharged = cms.uint32(1)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            nCharged = cms.uint32(3)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(3)
        )),
    toMultiplex = cms.InputTag("shrinkingConePFTauDiscriminationByTaNC"),
    PFTauProducer = cms.InputTag("shrinkingConePFTauProducer")
)


process.ak3HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.3)
)


process.ak4HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.4)
)


process.ak5CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doOutputJets = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(True),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    voronoiRfact = cms.double(-0.9),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    inputEtMin = cms.double(0.3),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('CaloJet'),
    src = cms.InputTag("towerMaker"),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    doAreaDiskApprox = cms.bool(False),
    inputEMin = cms.double(0.0),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.5)
)


process.ak5GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.5)
)


process.ak5GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ak5GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ak5HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.5)
)


process.ak5JetExtender = cms.EDProducer("JetExtender",
    jets = cms.InputTag("ak5CaloJets"),
    jet2TracksAtCALO = cms.InputTag("ak5JetTracksAssociatorAtCaloFace"),
    jet2TracksAtVX = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    coneSize = cms.double(0.5)
)


process.ak5JetID = cms.EDProducer("JetIDProducer",
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    hoRecHitsColl = cms.InputTag("horeco"),
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    useRecHits = cms.bool(True),
    src = cms.InputTag("ak5CaloJets")
)


process.ak5JetTracksAssociatorAtCaloFace = cms.EDProducer("JetTracksAssociatorAtCaloFace",
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5),
    extrapolations = cms.InputTag("trackExtrapolator"),
    jets = cms.InputTag("ak5CaloJets")
)


process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5CaloJets")
)


process.ak5PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("ak5PFJets"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.ak5PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doOutputJets = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    voronoiRfact = cms.double(-0.9),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('PFJet'),
    src = cms.InputTag("pfNoElectron"),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    doAreaDiskApprox = cms.bool(False),
    inputEMin = cms.double(0.0),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.5)
)


process.ak5PFJetsLegacyHPSPiZeros = cms.EDProducer("RecoTauPiZeroProducer",
    massHypothesis = cms.double(0.136),
    ranking = cms.VPSet(cms.PSet(
        selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
        selection = cms.string('algoIs("kStrips")'),
        name = cms.string('InStrip'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selectionFailValue = cms.double(1000)
    )),
    jetRegionSrc = cms.InputTag("recoTauAK5PFJets08Region"),
    outputSelection = cms.string('pt > 0'),
    jetSrc = cms.InputTag("ak5PFJets"),
    builders = cms.VPSet(cms.PSet(
        name = cms.string('s'),
        stripPhiAssociationDistance = cms.double(0.2),
        plugin = cms.string('RecoTauPiZeroStripPlugin'),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        makeCombinatoricStrips = cms.bool(False),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        stripEtaAssociationDistance = cms.double(0.05),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices")
    ))
)


process.ak5PFJetsLegacyTaNCPiZeros = cms.EDProducer("RecoTauPiZeroProducer",
    massHypothesis = cms.double(0.136),
    ranking = cms.VPSet(cms.PSet(
        selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
        selection = cms.string('mass() < 0.2'),
        name = cms.string('PFTDM'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selectionFailValue = cms.double(1000)
    )),
    jetRegionSrc = cms.InputTag("recoTauAK5PFJets08Region"),
    outputSelection = cms.string('pt > 1.5'),
    jetSrc = cms.InputTag("ak5PFJets"),
    builders = cms.VPSet(cms.PSet(
        plugin = cms.string('RecoTauPiZeroTrivialPlugin'),
        name = cms.string('1'),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ), 
        cms.PSet(
            maxMass = cms.double(-1.0),
            plugin = cms.string('RecoTauPiZeroCombinatoricPlugin'),
            minMass = cms.double(0.0),
            qualityCuts = cms.PSet(
                minTrackHits = cms.uint32(3),
                minTrackPt = cms.double(0.5),
                maxTrackChi2 = cms.double(100.0),
                minTrackPixelHits = cms.uint32(0),
                minGammaEt = cms.double(0.5),
                useTracksInsteadOfPFHadrons = cms.bool(False),
                maxDeltaZ = cms.double(0.2),
                maxTransverseImpactParameter = cms.double(0.03)
            ),
            choose = cms.uint32(2),
            maxInputGammas = cms.uint32(10),
            name = cms.string('2')
        ))
)


process.ak5PFJetsRecoTauPiZeros = cms.EDProducer("RecoTauPiZeroProducer",
    massHypothesis = cms.double(0.136),
    ranking = cms.VPSet(cms.PSet(
        selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
        selection = cms.string('abs(eta()) < 1.5 & abs(mass() - 0.13579) < 0.05'),
        name = cms.string('nearPiZeroMass'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selectionFailValue = cms.double(1000)
    ), 
        cms.PSet(
            selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
            selection = cms.string('abs(eta()) > 1.5 & mass() < 0.2'),
            name = cms.string('nearPiZeroMass'),
            plugin = cms.string('RecoTauPiZeroStringQuality'),
            selectionFailValue = cms.double(1000)
        ), 
        cms.PSet(
            selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
            selection = cms.string('algoIs("kStrips")'),
            name = cms.string('InStrip'),
            plugin = cms.string('RecoTauPiZeroStringQuality'),
            selectionFailValue = cms.double(1000)
        )),
    jetRegionSrc = cms.InputTag("recoTauAK5PFJets08Region"),
    outputSelection = cms.string('pt > 1.5'),
    jetSrc = cms.InputTag("ak5PFJets"),
    builders = cms.VPSet(cms.PSet(
        maxMass = cms.double(-1.0),
        plugin = cms.string('RecoTauPiZeroCombinatoricPlugin'),
        minMass = cms.double(0.0),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        choose = cms.uint32(2),
        maxInputGammas = cms.uint32(10),
        name = cms.string('2')
    ), 
        cms.PSet(
            name = cms.string('s'),
            stripPhiAssociationDistance = cms.double(0.2),
            plugin = cms.string('RecoTauPiZeroStripPlugin'),
            qualityCuts = cms.PSet(
                minTrackHits = cms.uint32(3),
                minTrackPt = cms.double(0.5),
                maxTrackChi2 = cms.double(100.0),
                minTrackPixelHits = cms.uint32(0),
                minGammaEt = cms.double(0.5),
                useTracksInsteadOfPFHadrons = cms.bool(False),
                maxDeltaZ = cms.double(0.2),
                maxTransverseImpactParameter = cms.double(0.03)
            ),
            makeCombinatoricStrips = cms.bool(False),
            stripCandidatesParticleIds = cms.vint32(2, 4),
            stripEtaAssociationDistance = cms.double(0.05),
            primaryVertexSrc = cms.InputTag("offlinePrimaryVertices")
        ))
)


process.ak7CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doAreaFastjet = cms.bool(False),
    voronoiRfact = cms.double(-0.9),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('CaloJet'),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(True),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("towerMaker"),
    inputEtMin = cms.double(0.3),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ak7GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJets"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ak7GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ak7GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ak7HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.7)
)


process.ak7PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doAreaFastjet = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("pfNoElectron"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(1.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.bcandidates = cms.EDProducer("BCandidateProducer",
    minvecSumIMifsmallDRUnique = cms.untracked.double(5.5),
    src = cms.InputTag("selectedVertices"),
    minDRUnique = cms.untracked.double(0.4),
    minCosPAtomerge = cms.untracked.double(0.99),
    primaryVertices = cms.InputTag("offlinePrimaryVerticesWithBS"),
    maxPtreltomerge = cms.untracked.double(7777.0)
)


process.bhadrons = cms.EDProducer("MCBHadronProducer",
    quarkId = cms.uint32(5)
)


process.ca4GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('CambridgeAachen'),
    rParam = cms.double(0.4)
)


process.ca4GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('CambridgeAachen'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.4),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ca4GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('CambridgeAachen'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.4),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ca6GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('CambridgeAachen'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJets"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ca6GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('CambridgeAachen'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ca6GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('CambridgeAachen'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.ca8GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('CambridgeAachen'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.8),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJets"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.caTopCaloJets = cms.EDProducer("CATopJetProducer",
    sumEtEtaCut = cms.double(3.0),
    ptFracBins = cms.vdouble(0.05, 0.05, 0.05),
    rBins = cms.vdouble(1.2, 1.2, 1.2),
    algorithm = cms.int32(1),
    etFrac = cms.double(0.7),
    useMaxTower = cms.bool(False),
    deltarBins = cms.vdouble(0.19, 0.19, 0.19),
    nCellBins = cms.vdouble(1.9, 1.9, 1.9),
    sumEtBins = cms.vdouble(0, 1600, 2600),
    centralEtaCut = cms.double(2.5),
    debugLevel = cms.untracked.int32(0),
    useAdjacency = cms.int32(0),
    jetCollInstanceName = cms.string('caTopSubJets'),
    verbose = cms.bool(False),
    Active_Area_Repeats = cms.int32(1),
    doOutputJets = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(True),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    voronoiRfact = cms.double(-0.9),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    inputEtMin = cms.double(0.3),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('CaloJet'),
    src = cms.InputTag("towerMaker"),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    doAreaDiskApprox = cms.bool(False),
    inputEMin = cms.double(0.0),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('CambridgeAachen'),
    rParam = cms.double(1.2)
)


process.caTopGenJets = cms.EDProducer("CATopJetProducer",
    sumEtEtaCut = cms.double(3.0),
    ptFracBins = cms.vdouble(0.05, 0.05, 0.05),
    rBins = cms.vdouble(0.8, 0.8, 0.8),
    algorithm = cms.int32(1),
    etFrac = cms.double(0.7),
    useMaxTower = cms.bool(False),
    deltarBins = cms.vdouble(0.19, 0.19, 0.19),
    nCellBins = cms.vdouble(1.9, 1.9, 1.9),
    sumEtBins = cms.vdouble(0, 1600, 2600),
    centralEtaCut = cms.double(2.5),
    debugLevel = cms.untracked.int32(0),
    useAdjacency = cms.int32(2),
    jetCollInstanceName = cms.string('caTopSubJets'),
    verbose = cms.bool(False),
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('CambridgeAachen'),
    rParam = cms.double(0.8)
)


process.caTopPFJets = cms.EDProducer("CATopJetProducer",
    sumEtEtaCut = cms.double(3.0),
    ptFracBins = cms.vdouble(0.05, 0.05, 0.05),
    rBins = cms.vdouble(1.2, 1.2, 1.2),
    algorithm = cms.int32(1),
    etFrac = cms.double(0.7),
    useMaxTower = cms.bool(False),
    deltarBins = cms.vdouble(0.19, 0.19, 0.19),
    nCellBins = cms.vdouble(1.9, 1.9, 1.9),
    sumEtBins = cms.vdouble(0, 1600, 2600),
    centralEtaCut = cms.double(2.5),
    debugLevel = cms.untracked.int32(0),
    useAdjacency = cms.int32(0),
    jetCollInstanceName = cms.string('caTopSubJets'),
    verbose = cms.bool(False),
    Active_Area_Repeats = cms.int32(1),
    doOutputJets = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    voronoiRfact = cms.double(-0.9),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    src = cms.InputTag("pfNoElectron"),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    doAreaDiskApprox = cms.bool(False),
    inputEMin = cms.double(0.0),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('CambridgeAachen'),
    rParam = cms.double(1.2)
)


process.cleanPatElectrons = cms.EDProducer("PATElectronCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatElectrons"),
    checkOverlaps = cms.PSet(
        muons = cms.PSet(
            src = cms.InputTag("cleanPatMuons"),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        )
    ),
    preselection = cms.string('')
)


process.cleanPatJets = cms.EDProducer("PATJetCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatJets"),
    checkOverlaps = cms.PSet(
        taus = cms.PSet(
            src = cms.InputTag("cleanPatTaus"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        photons = cms.PSet(
            src = cms.InputTag("cleanPatPhotons"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        electrons = cms.PSet(
            src = cms.InputTag("cleanPatElectrons"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        muons = cms.PSet(
            src = cms.InputTag("cleanPatMuons"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        tkIsoElectrons = cms.PSet(
            src = cms.InputTag("cleanPatElectrons"),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False)
        )
    ),
    preselection = cms.string('')
)


process.cleanPatJetsAK5PF = cms.EDProducer("PATJetCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatJetsAK5PF"),
    checkOverlaps = cms.PSet(
        muons = cms.PSet(
            src = cms.InputTag("selectedPatMuonsWithIso"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True)
        ),
        electrons = cms.PSet(
            src = cms.InputTag("selectedPatElectronsWithIso"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True)
        )
    ),
    preselection = cms.string('abs(eta)< 5.0 && pt > 15.0')
)


process.cleanPatMuons = cms.EDProducer("PATMuonCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatMuons"),
    checkOverlaps = cms.PSet(

    ),
    preselection = cms.string('')
)


process.cleanPatPhotons = cms.EDProducer("PATPhotonCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatPhotons"),
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            src = cms.InputTag("cleanPatElectrons"),
            requireNoOverlaps = cms.bool(False),
            algorithm = cms.string('bySuperClusterSeed')
        )
    ),
    preselection = cms.string('')
)


process.cleanPatTaus = cms.EDProducer("PATTauCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatTaus"),
    checkOverlaps = cms.PSet(
        muons = cms.PSet(
            src = cms.InputTag("cleanPatMuons"),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        electrons = cms.PSet(
            src = cms.InputTag("cleanPatElectrons"),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        )
    ),
    preselection = cms.string('tauID("leadingTrackFinding") > 0.5 & tauID("leadingPionPtCut") > 0.5 & tauID("byIsolationUsingLeadingPion") > 0.5 & tauID("againstMuon") > 0.5 & tauID("againstElectron") > 0.5 & (signalPFChargedHadrCands.size() = 1 | signalPFChargedHadrCands.size() = 3)')
)


process.combinatoricRecoTaus = cms.EDProducer("RecoTauProducer",
    piZeroSrc = cms.InputTag("ak5PFJetsLegacyHPSPiZeros"),
    modifiers = cms.VPSet(cms.PSet(
        pvSrc = cms.InputTag("offlinePrimaryVertices"),
        name = cms.string('sipt'),
        plugin = cms.string('RecoTauImpactParameterSignificancePlugin')
    ), 
        cms.PSet(
            ElectronPreIDProducer = cms.InputTag("elecpreid"),
            name = cms.string('elec_rej'),
            plugin = cms.string('RecoTauElectronRejectionPlugin'),
            DataType = cms.string('AOD'),
            maximumForElectrionPreIDOutput = cms.double(-0.1),
            EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
            EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
            EcalStripSumE_minClusEnergy = cms.double(0.1),
            ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
            EcalStripSumE_deltaEta = cms.double(0.03)
        ), 
        cms.PSet(
            pfTauTagInfoSrc = cms.InputTag("pfRecoTauTagInfoProducer"),
            name = cms.string('TTIworkaround'),
            plugin = cms.string('RecoTauTagInfoWorkaroundModifer')
        )),
    jetRegionSrc = cms.InputTag("recoTauAK5PFJets08Region"),
    jetSrc = cms.InputTag("ak5PFJets"),
    builders = cms.VPSet(cms.PSet(
        usePFLeptons = cms.bool(True),
        name = cms.string('combinatoric'),
        plugin = cms.string('RecoTauBuilderCombinatoricPlugin'),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        decayModes = cms.VPSet(cms.PSet(
            nPiZeros = cms.uint32(0),
            nCharged = cms.uint32(1),
            maxPiZeros = cms.uint32(0),
            maxTracks = cms.uint32(6)
        ), 
            cms.PSet(
                nPiZeros = cms.uint32(1),
                nCharged = cms.uint32(1),
                maxPiZeros = cms.uint32(6),
                maxTracks = cms.uint32(6)
            ), 
            cms.PSet(
                nPiZeros = cms.uint32(2),
                nCharged = cms.uint32(1),
                maxPiZeros = cms.uint32(5),
                maxTracks = cms.uint32(6)
            ), 
            cms.PSet(
                nPiZeros = cms.uint32(0),
                nCharged = cms.uint32(3),
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6)
            )),
        isolationConeSize = cms.double(0.5),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pfCandSrc = cms.InputTag("particleFlow")
    )),
    buildNullTaus = cms.bool(True)
)


process.combinatoricRecoTausDiscriminationByLeadingPionPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(False),
    PFTauProducer = cms.InputTag("combinatoricRecoTaus")
)


process.combinatoricRecoTausDiscriminationByTanc = cms.EDProducer("RecoTauMVADiscriminator",
    discriminantOptions = cms.PSet(
        BinnedMaskedHcalIsolation = cms.PSet(
            vtxSource = cms.InputTag("recoTauPileUpVertices"),
            mask = cms.PSet(
                finalHcalCone = cms.double(0.08),
                ecalCone = cms.double(0.15),
                hcalCone = cms.double(0.3),
                maxSigmas = cms.double(2)
            ),
            binning = cms.VPSet(cms.PSet(
                binLowEdges = cms.vdouble(1.0, 1.79, 4.03),
                nPUVtx = cms.int32(0)
            ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(1.15, 1.8, 4.03),
                    nPUVtx = cms.int32(1)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(1.22, 1.81, 4.03),
                    nPUVtx = cms.int32(2)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(1.27, 1.83, 4.03),
                    nPUVtx = cms.int32(3)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(1.31, 1.84, 4.03),
                    nPUVtx = cms.int32(4)
                )),
            defaultBinning = cms.vdouble(1.31, 1.84, 4.03),
            plugin = cms.string('RecoTauDiscriminationBinnedMaskedHCALIsolation')
        ),
        InvariantOpeningAngle = cms.PSet(
            defaultRMS = cms.string('max(0.3/max(pt, 1.0), 0.005)'),
            plugin = cms.string('RecoTauDiscriminantInvariantWidth'),
            decayModes = cms.VPSet(cms.PSet(
                nPiZeros = cms.uint32(1),
                rms = cms.string('2.7e-3 + 0.23/max(pt, 1.0)'),
                nCharged = cms.uint32(1),
                mean = cms.string('5.0e-3 + 0.43/max(pt, 1.0)')
            ), 
                cms.PSet(
                    nPiZeros = cms.uint32(2),
                    rms = cms.string('7.5e-3 + 0.3/max(pt, 1.0)'),
                    nCharged = cms.uint32(1),
                    mean = cms.string('4.7e-3 + 0.9/max(pt, 1.0)')
                ), 
                cms.PSet(
                    nPiZeros = cms.uint32(0),
                    rms = cms.string('0.38/max(pt, 1.0)'),
                    nCharged = cms.uint32(3),
                    mean = cms.string('0.87/max(pt, 1.0)')
                )),
            defaultMean = cms.string('max(0.87/max(pt, 1.0), 0.005)')
        ),
        BinnedMaskedEcalIsolation = cms.PSet(
            vtxSource = cms.InputTag("recoTauPileUpVertices"),
            mask = cms.PSet(
                finalHcalCone = cms.double(0.08),
                ecalCone = cms.double(0.15),
                hcalCone = cms.double(0.3),
                maxSigmas = cms.double(2)
            ),
            binning = cms.VPSet(cms.PSet(
                binLowEdges = cms.vdouble(0.5, 0.85, 1.84),
                nPUVtx = cms.int32(0)
            ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.63, 0.91, 1.84),
                    nPUVtx = cms.int32(1)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.7, 0.96, 1.85),
                    nPUVtx = cms.int32(2)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.75, 0.99, 1.85),
                    nPUVtx = cms.int32(3)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.79, 1.02, 1.86),
                    nPUVtx = cms.int32(4)
                )),
            defaultBinning = cms.vdouble(0.79, 1.02, 1.86),
            plugin = cms.string('RecoTauDiscriminationBinnedMaskedECALIsolation')
        ),
        FlightPathSignificance = cms.PSet(
            discSrc = cms.InputTag("hpsTancTausDiscriminationByFlightPath"),
            plugin = cms.string('RecoTauDiscriminantFromDiscriminator')
        ),
        BinnedTrackIsolation = cms.PSet(
            vtxSource = cms.InputTag("recoTauPileUpVertices"),
            binning = cms.VPSet(cms.PSet(
                binLowEdges = cms.vdouble(0.5, 0.86, 1.87),
                nPUVtx = cms.int32(0)
            ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.51, 0.86, 1.87),
                    nPUVtx = cms.int32(1)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.51, 0.86, 1.87),
                    nPUVtx = cms.int32(2)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.52, 0.86, 1.87),
                    nPUVtx = cms.int32(3)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.52, 0.86, 1.87),
                    nPUVtx = cms.int32(4)
                )),
            defaultBinning = cms.vdouble(0.52, 0.86, 1.87),
            plugin = cms.string('RecoTauDiscriminationBinnedTrackIsolation')
        )
    ),
    mvas = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        mvaLabel = cms.string('1prong0pi0'),
        nCharged = cms.uint32(1)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            mvaLabel = cms.string('1prong1pi0'),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            mvaLabel = cms.string('1prong2pi0'),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            mvaLabel = cms.string('3prong0pi0'),
            nCharged = cms.uint32(3)
        )),
    PFTauProducer = cms.InputTag("combinatoricRecoTaus"),
    remapOutput = cms.bool(True),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dbLabel = cms.string('hpstanc')
)


process.combinatoricRecoTausHPSSelector = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    src = cms.InputTag("combinatoricRecoTaus"),
    PFTauProducer = cms.InputTag("combinatoricRecoTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    minTauPt = cms.double(5.0),
    coneSizeFormula = cms.string('0.3'),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        minMass = cms.double(-0.1),
        maxMass = cms.double(1),
        nCharged = cms.uint32(1)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            assumeStripMass = cms.double(0.1349),
            minMass = cms.double(0.3),
            maxMass = cms.double(1.3),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            minPi0Mass = cms.double(0.05),
            maxMass = cms.double(1.2),
            maxPi0Mass = cms.double(0.2),
            nPiZeros = cms.uint32(2),
            minMass = cms.double(0.4),
            nCharged = cms.uint32(1),
            assumeStripMass = cms.double(0.0)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            minMass = cms.double(0.8),
            maxMass = cms.double(1.5),
            nCharged = cms.uint32(3)
        )),
    matchingCone = cms.double(0.1)
)


process.combinatoricRecoTausTancTransform = cms.EDProducer("RecoTauMVATransform",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    transforms = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        transform = cms.PSet(
            max = cms.double(1.99833333333),
            transform = (cms.vdouble(0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508)+cms.vdouble(0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243693947972, 0.2446621342, 0.25648929965, 0.2608766459, 0.265139843949, 0.268288096025, 0.271490633611, 0.274812027295, 0.278726505561, 0.283196361675, 0.287921047203, 0.293485065795, 0.299327353484, 0.305468394708, 0.310410038477, 0.315654364298, 0.320865024837, 0.324875648584, 0.328691660974, 0.332598633349, 0.336484807993, 0.339893814351, 0.343528868912, 0.346311138119, 0.348525259682, 0.350638868762, 0.352500481165, 0.354385202603, 0.356405103778, 0.358448162743, 0.359626155068, 0.361359527277, 0.362911630832, 0.364767207965, 0.365568276809, 0.367161876825, 0.368245783665, 0.369700987138, 0.370891835827, 0.371335926598, 0.372724067775, 0.374122626292, 0.374872824273, 0.376287585272, 0.377808481377, 0.379437962659, 0.380385427158, 0.381454465894, 0.382529530437, 0.383308773065, 0.383900643462, 0.384488881534, 0.385284008411, 0.385778244795, 0.386880706208, 0.387787417873, 0.389206336729, 0.390430843456, 0.391560096158, 0.392490239284, 0.393218300975, 0.394889524946, 0.396474094424, 0.397328157396, 0.398823062781, 0.400437280424, 0.401846875958, 0.402719262685, 0.403705236447, 0.40437725886, 0.405483096559, 0.40715324019, 0.408161946716, 0.408949958358, 0.410194428622, 0.411674966358, 0.412726139917, 0.413994836217, 0.414922434459, 0.415970963664, 0.417494895799, 0.418345516985, 0.419769194149, 0.42120259427, 0.423008169722, 0.424220511323, 0.425684525769, 0.426912279039, 0.428023327968, 0.429389155258, 0.430889124801, 0.432147128025, 0.433793555744, 0.435196517338, 0.436351162787, 0.437253465009, 0.438419065687, 0.439590897333, 0.440949213705, 0.441921470289, 0.442848592497, 0.44396524306, 0.445223842049, 0.446977728682, 0.448745488265, 0.451078381688, 0.451907557714, 0.452739787751, 0.453638395261, 0.45475822595, 0.456165813144, 0.457223834211, 0.457934807034, 0.45922014571, 0.461017229233, 0.461451032994, 0.463048655665, 0.464804181316, 0.466425147476, 0.467542494191, 0.468517661795, 0.470468799941, 0.47198076935, 0.472892624736, 0.474420238705, 0.476266453893, 0.477505267649, 0.479532143347, 0.481200116592, 0.481613637289, 0.483360304775, 0.485061449421, 0.487101659613, 0.488019909526, 0.488999144832, 0.490200759674, 0.491190516798, 0.493849514855, 0.495306102206, 0.495928489713, 0.4964353883, 0.498082556741, 0.49979254034, 0.500775976586, 0.502679733683, 0.504598020717, 0.505078487853, 0.506619141507, 0.508171974823, 0.509336469886, 0.510953930915, 0.512581697566, 0.513998315702, 0.515647034962, 0.515939613111, 0.517975069449, 0.519430445753, 0.519957296262, 0.521273324958, 0.522406663349, 0.523925469498, 0.524625850033, 0.525907581275, 0.527065315655, 0.52822815856, 0.528783474767, 0.529145626115, 0.529453767868, 0.530435650231, 0.532014259582, 0.532782125184, 0.534528955521, 0.535733634238, 0.539584530704, 0.541410067901, 0.543682312792, 0.545138243861, 0.546811742597, 0.548048893429, 0.548459504636, 0.550158093752, 0.551205716597, 0.552261157841, 0.553773021814, 0.554620522074, 0.557022425024, 0.558787346691, 0.55989408991, 0.562351160997, 0.564603650808, 0.567330572538, 0.568251047692, 0.570322191691, 0.570800554836, 0.573840553165, 0.575722428922, 0.578806943369, 0.580018988744, 0.581943439091, 0.583637839285, 0.583719886077, 0.585230062162, 0.586459819001, 0.58819018682, 0.589432428675, 0.590707557501, 0.59199058109, 0.593311935901, 0.596143502405, 0.598713047084, 0.59985869618, 0.60146038335)+cms.vdouble(0.603073645068, 0.60364159568, 0.605493798425, 0.607716165748, 0.611539567166, 0.61344596304, 0.614868728468, 0.616356298487, 0.617243661796, 0.618356139972, 0.620433033442, 0.623603658141, 0.625027738979, 0.626745245057, 0.630061473707, 0.634451273629, 0.636224368987, 0.638386932974, 0.639666729708, 0.641472541416, 0.643376129813, 0.645998175052, 0.648651724655, 0.650614385321, 0.651964427491, 0.654372246094, 0.656912558238, 0.657658356547, 0.658734274882, 0.661006291486, 0.663094362812, 0.664860224717, 0.667639986138, 0.669224738703, 0.670609710516, 0.672008536945, 0.674322956904, 0.676181757848, 0.680504320591, 0.681701882298, 0.683847428048, 0.687028204213, 0.690096183579, 0.692936565842, 0.698333032093, 0.702469873766, 0.704533440299, 0.706621657637, 0.710308262591, 0.713270705866, 0.714865826284, 0.719086552707, 0.722147885763, 0.725885046087, 0.729450681758, 0.732859861331, 0.739185288999, 0.743172463789, 0.74657896386, 0.751327840506, 0.754658774214, 0.758047388164, 0.762059448212, 0.769914558551, 0.775838239214, 0.780728907111, 0.786952215918, 0.793694146175, 0.796885300439, 0.802863959078, 0.813001141474, 0.820597251397, 0.829350775725, 0.837460143471, 0.84199323298, 0.847433416989, 0.854638027367, 0.860714284529, 0.869959964541, 0.876007819869, 0.884455823419, 0.896538436371, 0.904016005807, 0.910382232961, 0.916770946986, 0.93386870405, 0.943467586229, 0.95165443966, 0.971789456433, 0.970755563959, 0.9679163435, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
            min = cms.double(-0.998333333333)
        ),
        nCharged = cms.uint32(3)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            transform = cms.PSet(
                max = cms.double(1.99833333333),
                transform = (cms.vdouble(0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285)+cms.vdouble(0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725625489751, 0.725917318629, 0.727526582607, 0.745748231906, 0.750169168536, 0.757185219071, 0.764249672036, 0.767603981959, 0.772574492642, 0.775097031572, 0.777704615235, 0.779407980465, 0.781767581973, 0.784842584326, 0.786420654919, 0.787883166617, 0.790123535551, 0.79208138528, 0.79327247227, 0.795907708578, 0.798503646112, 0.800206834461, 0.802663946447, 0.8031582666, 0.80490222571, 0.806889568691, 0.809394028316, 0.811861583702, 0.813019057268, 0.81342095915, 0.814698723372, 0.816279445985, 0.818232037783, 0.819367026875, 0.819759858707, 0.821328989638, 0.822878675172, 0.82364763472, 0.825358996088, 0.828499118125, 0.829830087025, 0.831236000117, 0.832703495507, 0.833414247004, 0.834436344112, 0.834946785624, 0.835869791486, 0.836486520822, 0.837364626557, 0.838193318858, 0.839702591039, 0.841531457051, 0.842218371935, 0.843640339114, 0.844222988069, 0.845392038566, 0.846778761898, 0.84769605779, 0.848073950379, 0.848849957765, 0.849494110293, 0.8500905241, 0.851335675181, 0.853500950651, 0.853839833615, 0.854227213103, 0.854567621296, 0.854984559013, 0.855203285083, 0.856470785047, 0.857475859603, 0.85892685241, 0.859008202829, 0.859451257957, 0.860468389831, 0.861489507276, 0.861351261404, 0.861705874851, 0.861659795003, 0.861659795003, 0.86179137032, 0.862147375366, 0.862550177315, 0.863312092458, 0.863805642705, 0.864438066642, 0.864754370118, 0.865480701328, 0.866346092335, 0.867168965701, 0.867397571488, 0.868313201223, 0.868771741382, 0.869186401202, 0.86983185136, 0.869929474522, 0.870346507695, 0.870951429469, 0.870863388987, 0.871514279263, 0.872166654676, 0.872355339191, 0.872776974093, 0.873155878735, 0.873579101025, 0.874003066865, 0.873916467734, 0.874211597253, 0.874402872188, 0.87510742975, 0.87525648792, 0.87525648792, 0.875448860228, 0.875598481234, 0.875512416378, 0.87617785231, 0.87617785231, 0.876371452215, 0.877233539228, 0.877818409805, 0.87840545558, 0.87840545558, 0.878601622981, 0.878601622981, 0.879472984901, 0.879712328244, 0.87982581203, 0.879981638026, 0.880179766123, 0.880378141371, 0.880534852587, 0.880691869776, 0.8811323429, 0.881090533252, 0.881531917098, 0.881732079801, 0.8822162463, 0.882902187113, 0.882979722574, 0.88403281278, 0.885010261835, 0.884928594333, 0.885132644083, 0.885050953876, 0.88525535544, 0.886362380543, 0.886487219509, 0.886652934413, 0.887232935079, 0.887728512003, 0.888561331939, 0.889019284728, 0.889438266521, 0.890358658388, 0.890120720891, 0.890292192785, 0.890675834925, 0.890556765164, 0.890981544778, 0.891699669632, 0.891660238395, 0.891969519877, 0.892319678993, 0.892161931402, 0.892513711208, 0.892729546909, 0.893162065429, 0.893339503795, 0.893339503795, 0.893656248099, 0.894427465173, 0.894606969217, 0.894825762437, 0.894928163898, 0.895703822513, 0.89622167567, 0.896663385868, 0.897404545302, 0.89769650475, 0.899189293203, 0.899525558799, 0.900803884235, 0.901822547362, 0.901939302648, 0.902926505697, 0.903082359676, 0.904038745128, 0.90469561985, 0.904927332682, 0.905283513893, 0.906828000044, 0.907062493553, 0.908109372415, 0.908783021349, 0.90898498498, 0.910379224289, 0.911372920866, 0.911751863015, 0.912477297669, 0.913239550237, 0.91300238707, 0.913422855139, 0.915063352192, 0.916893920936, 0.916979020829, 0.91791358353, 0.918350995783, 0.918790342789, 0.919328152961, 0.919993298628, 0.920982245955, 0.922524618114, 0.923591109364)+cms.vdouble(0.924018850534, 0.924248923821, 0.924479515826, 0.925498182241, 0.926493584801, 0.927436921962, 0.927911825271, 0.928716526512, 0.929225746944, 0.929920622352, 0.931640820211, 0.931772433588, 0.932293506679, 0.932760264784, 0.93386870405, 0.934480569506, 0.934731886916, 0.935797384751, 0.936588472051, 0.936817507478, 0.937277790773, 0.938339506605, 0.938808219887, 0.93993649209, 0.94020045716, 0.940781492864, 0.941047196853, 0.942510417566, 0.942629939, 0.942750378489, 0.943616386541, 0.944163684906, 0.945338814696, 0.945845741457, 0.946028661789, 0.946308362468, 0.946541150838, 0.946751152357, 0.947576555912, 0.948029352938, 0.94826905955, 0.948081416726, 0.949376743021, 0.94926144862, 0.949775296374, 0.949706301122, 0.951268968863, 0.953037066674, 0.95357532021, 0.953770570793, 0.953640586734, 0.953509869657, 0.954300159882, 0.955476996866, 0.956207587781, 0.956355833165, 0.956846568485, 0.957770053042, 0.958723171834, 0.958928454571, 0.959445187694, 0.959807967592, 0.959442259047, 0.960697132989, 0.961203278228, 0.963193467582, 0.963932365293, 0.964461162833, 0.964482886627, 0.96526433234, 0.966030150632, 0.966856588211, 0.969491617691, 0.970743493871, 0.972389419268, 0.973307337131, 0.975623617612, 0.976087161844, 0.975647899082, 0.976736074007, 0.979440008803, 0.981271208497, 0.982207028661, 0.984863078211, 0.986956530647, 0.990258251858, 0.990208776979, 0.990702226892, 0.993228159625, 0.99534336087, 0.996696237239, 0.995185049087, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
                min = cms.double(-0.998333333333)
            ),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            transform = cms.PSet(
                max = cms.double(1.99833333333),
                transform = (cms.vdouble(0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399)+cms.vdouble(0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.786753288885, 0.788132324416, 0.79656141615, 0.810183644995, 0.858360829913, 0.862298212616, 0.867110980413, 0.871372861265, 0.875682014578, 0.880242297589, 0.883696978098, 0.885512278829, 0.887768921813, 0.889264020585, 0.89119925019, 0.892452552697, 0.893185095837, 0.893419577074, 0.894898998675, 0.895774783109, 0.896260903725, 0.896505707407, 0.898082672851, 0.898779137453, 0.89979939771, 0.900120276805, 0.900442301311, 0.900314253861, 0.90063761708, 0.903107169678, 0.903707364412, 0.904624297652, 0.90437518453, 0.904187494019, 0.904648539996, 0.905849328721, 0.90625146477, 0.906593041173, 0.906284313013, 0.906627709554, 0.906627709554, 0.907095652088, 0.906972372385, 0.907318308525, 0.907603995571, 0.907357055463, 0.907233089763, 0.907994846936, 0.908883949265, 0.908883949265, 0.909836831321, 0.909836831321, 0.909776114594, 0.911030037809, 0.911509901723, 0.911871023987, 0.911811279009, 0.911751452972, 0.911691545709, 0.911511334909, 0.911451101085, 0.912784331406, 0.9125455069, 0.9125455069, 0.91297278083, 0.912853317543, 0.912673506387, 0.913592984461, 0.915007651179, 0.915441697726, 0.915324604996, 0.915207187526, 0.915148356591, 0.91552593882, 0.915467174967, 0.9154083293, 0.915290391839, 0.915231299701, 0.915728896806, 0.915728896806, 0.915552071941, 0.916492320764, 0.917377950283, 0.917822427143, 0.918268017622, 0.91871472591, 0.919668295227, 0.919611512782, 0.919554650007, 0.919440682785, 0.919269125195, 0.921306876156, 0.921306876156, 0.921082297245, 0.920969526416, 0.921426208902, 0.921939970027, 0.921939970027, 0.922343069964, 0.923319759486, 0.923727168952, 0.923727168952, 0.92460140151, 0.924492316338, 0.924959238052, 0.926474177051, 0.926474177051, 0.926420752856, 0.926313671218, 0.926785714713, 0.926785714713, 0.926785714713, 0.926732331515, 0.926732331515, 0.926571713811, 0.927521701059, 0.927468561656, 0.927998554333, 0.927945695605, 0.929008220067, 0.928746371941, 0.928693770351, 0.928641091039, 0.929607013105, 0.929554832769, 0.930039996532, 0.93101417799, 0.931554211882, 0.932636161324, 0.932585903271, 0.932585903271, 0.93357188521, 0.933522156167, 0.933967924145, 0.933769185329, 0.934766776762, 0.935267583538, 0.935169629185, 0.935672412756, 0.936176553451, 0.936176553451, 0.93779194569, 0.937554472402, 0.937458974653, 0.937411116161, 0.937970225775, 0.938435668089, 0.938341043455, 0.938341043455, 0.938903099624, 0.93885608225, 0.938808992455, 0.938714594933, 0.939278948765, 0.940409694612, 0.940363611919, 0.940363611919, 0.940884673949, 0.940838860114, 0.940700991551, 0.941179107659, 0.941750185868, 0.941750185868, 0.942276966885, 0.943290568826, 0.943822114749, 0.944267645451, 0.944223792272, 0.944223792272, 0.944223792272, 0.944223792272, 0.944135878551, 0.944091817682, 0.943959217069, 0.944948988041, 0.944817531021, 0.945185418124, 0.945774534438, 0.946869842865, 0.94678443912, 0.947292782482, 0.947803406812, 0.948955745704, 0.949513262437, 0.949431324505, 0.949349120177, 0.949787213059, 0.950350748429, 0.951522477849, 0.952051228023, 0.95197239226, 0.951813940452, 0.951734321829, 0.952189098377, 0.952726227521, 0.952647494583, 0.953226869405, 0.953148724357, 0.95303101596, 0.953497250008, 0.954122169792, 0.954006075021, 0.954594998037, 0.955778170341, 0.955740668477, 0.957457733339, 0.958697023242, 0.958590781777, 0.958519649968, 0.959665182275, 0.960242079268, 0.960242079268, 0.960855701368, 0.960787753107)+cms.vdouble(0.961370655681, 0.961269567079, 0.961823203605, 0.963730727425, 0.963634885553, 0.963570709071, 0.964138473298, 0.964106695414, 0.96404297039, 0.963914839098, 0.963882663464, 0.96452094996, 0.964361812095, 0.96497328025, 0.965587812399, 0.966174859102, 0.966052013818, 0.966021162949, 0.968018795469, 0.96867865254, 0.968592547647, 0.96914294659, 0.969057430126, 0.969000155331, 0.970289180287, 0.971618144708, 0.971511684075, 0.972907637123, 0.972856607143, 0.972753968298, 0.972676478315, 0.973344727784, 0.973217439385, 0.973917083716, 0.973842007934, 0.973791716846, 0.974496912029, 0.974447701286, 0.974373528048, 0.974273957942, 0.974198771106, 0.974791150217, 0.975488253999, 0.976165676348, 0.977513433798, 0.977332925695, 0.978053351441, 0.978734902423, 0.97864854949, 0.979275680612, 0.979190505138, 0.979039751165, 0.978974471583, 0.978886796984, 0.980438334358, 0.981887328142, 0.982567303114, 0.983312443593, 0.983168209088, 0.983021459539, 0.98366063828, 0.983606342672, 0.983441268961, 0.983291720735, 0.985747459607, 0.985615866821, 0.988157949486, 0.988031989052, 0.987786602856, 0.988507380959, 0.988364321833, 0.988127868612, 0.987928555371, 0.987641272072, 0.987408197679, 0.98704162283, 0.986691071046, 0.986360943929, 0.987048151948, 0.989952686544, 0.991766844123, 0.992193166195, 0.99456966538, 0.995655052048, 0.994746673755, 0.993062299865, 0.995491593707, 0.993997811711, 0.991951166261, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
                min = cms.double(-0.998333333333)
            ),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            transform = cms.PSet(
                max = cms.double(1.99833333333),
                transform = (cms.vdouble(0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277)+cms.vdouble(0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320785409267, 0.320785409267, 0.320785409267, 0.320967688479, 0.32115017496, 0.32115017496, 0.32115017496, 0.32115017496, 0.321332869066, 0.321607300294, 0.321790515012, 0.322065728828, 0.322709728783, 0.337811096719, 0.33917314626, 0.341489359417, 0.343051156809, 0.344690580804, 0.34605531485, 0.347729452006, 0.349352972192, 0.351698761571, 0.354076266303, 0.356364861761, 0.357459291064, 0.358806090169, 0.360659074159, 0.361655179522, 0.363285639001, 0.363823848893, 0.365224296488, 0.366635567078, 0.368317558281, 0.36949108301, 0.370409007364, 0.370997606343, 0.372726361337, 0.373488515297, 0.374412657806, 0.375752608537, 0.377534910678, 0.378625338634, 0.379181030815, 0.379877944035, 0.382266731549, 0.382549741971, 0.383828491978, 0.38525242259, 0.386835650852, 0.38785063627, 0.389317222671, 0.390498501728, 0.392134514369, 0.392433445129, 0.393938724972, 0.395003106909, 0.395165758646, 0.395929379967, 0.396695958257, 0.397011143016, 0.398247378442, 0.399356983741, 0.399994683207, 0.401254354869, 0.40236309389, 0.403477977186, 0.404278112546, 0.405403648355, 0.406718341929, 0.408044942586, 0.409053791836, 0.409879342767, 0.410568240656, 0.411067477386, 0.412572498902, 0.413612340683, 0.414628216181, 0.41718987191, 0.417878334739, 0.41856907358, 0.419300644011, 0.420520753157, 0.420777117228, 0.422716149289, 0.423248081689, 0.424315972822, 0.425568676714, 0.426697968924, 0.427784748237, 0.428512348538, 0.429242428143, 0.430526071506, 0.4311350135, 0.432803583714, 0.433609675616, 0.434608917639, 0.436308891919, 0.436878509184, 0.437640316502, 0.438596319943, 0.440520911858, 0.441683795845, 0.443048277506, 0.444696219849, 0.446478472767, 0.44715804854, 0.448645092811, 0.450058431683, 0.450666877959, 0.450755388115, 0.451660727674, 0.452685605028, 0.453508861839, 0.455164391331, 0.456611329026, 0.456920461171, 0.457863702358, 0.45902581005, 0.459451411686, 0.460410936031, 0.461808077134, 0.4630001435, 0.46452516501, 0.465632370863, 0.466972634942, 0.467639712811, 0.468206417853, 0.469000443277, 0.470125946746, 0.471938031657, 0.473437184975, 0.474815974144, 0.475643583896, 0.477037107394, 0.478345116523, 0.479756398109, 0.482127131145, 0.483321305722, 0.484827612962, 0.485378450947, 0.486839313932, 0.488800865348, 0.488631796262, 0.489784626283, 0.49019813266, 0.490696455307, 0.492699918902, 0.493707798202, 0.495481544763, 0.497780890453, 0.499067549901, 0.499842743245, 0.501067711008, 0.501110885208, 0.503739653301, 0.504533670387, 0.507669169039, 0.508207246665, 0.510099534144, 0.511125093239, 0.513041788431, 0.514972912765, 0.517927881794, 0.519848789077, 0.52116702462, 0.522598588906, 0.524038039421, 0.524905522273, 0.525729939569, 0.527349110611, 0.528189103375, 0.529884063982, 0.531038635091, 0.531258876588, 0.533372518417, 0.532652261497, 0.533222445036, 0.533832435241, 0.534714171593, 0.536561182549, 0.536184284139, 0.538295230995, 0.539204274194, 0.539743792118, 0.542257448251, 0.543191981222, 0.54415669717, 0.545124845911, 0.546421082543, 0.548704392123, 0.551006864138, 0.551639517385, 0.554308295208, 0.554286639155, 0.555277851271, 0.557294734318, 0.558661984326, 0.560735788966, 0.561777981725, 0.56352691872, 0.56493793563, 0.567793486879, 0.568888208725, 0.57034433091, 0.570356276084, 0.572191934216, 0.573659294894, 0.574044772549, 0.575543527534, 0.577054482298, 0.578553389267, 0.580816407199, 0.582777514902, 0.58546601664, 0.587013469943, 0.586699955875, 0.587164603914, 0.589909772096, 0.590347109603, 0.591182964289, 0.593622213241, 0.595632610766, 0.596088895792)+cms.vdouble(0.596547219627, 0.597007595967, 0.59905000376, 0.59875479532, 0.600402032492, 0.601476624751, 0.602375325225, 0.604611692334, 0.606308877758, 0.609454442616, 0.612487831768, 0.615198564485, 0.616345932738, 0.617679752716, 0.620364786891, 0.621560433387, 0.622923085077, 0.622771613804, 0.627021967049, 0.629464905691, 0.630636176618, 0.632414811477, 0.635412621765, 0.636860801036, 0.638359784998, 0.642296739762, 0.64372019874, 0.646732193739, 0.649419880322, 0.653004922396, 0.654536589972, 0.657493324695, 0.65872664624, 0.662116021475, 0.666837437051, 0.668332370106, 0.670194812833, 0.671514734427, 0.671514734427, 0.672844093862, 0.672352092845, 0.678607302272, 0.681605563269, 0.681020472505, 0.682082800049, 0.684848783291, 0.686959317553, 0.690918830645, 0.691984674993, 0.694695530605, 0.697455651971, 0.700496795416, 0.703736816672, 0.704917801757, 0.706220722464, 0.707858889942, 0.71018130526, 0.714321429016, 0.720425948473, 0.724503155871, 0.727977004139, 0.730714468803, 0.735012362904, 0.739735756402, 0.750660954162, 0.757799352464, 0.760515374245, 0.768004247792, 0.77935327172, 0.784646260495, 0.789164336822, 0.791123170072, 0.795276817521, 0.804299018936, 0.819103217408, 0.822961151625, 0.833298258018, 0.842807182616, 0.85334688934, 0.86724344838, 0.872176831791, 0.87195156781, 0.87843961359, 0.891494313173, 0.912879175226, 0.924218217451, 0.937234161591, 0.94206607914, 0.958884557005, 0.959595443343, 0.93904371889, 0.927733482302, 0.93386870405, 0.916051159827, 0.943467586229, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
                min = cms.double(-0.998333333333)
            ),
            nCharged = cms.uint32(1)
        )),
    toTransform = cms.InputTag("combinatoricRecoTausDiscriminationByTanc"),
    PFTauProducer = cms.InputTag("combinatoricRecoTaus")
)


process.combinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"), cms.InputTag("softMuonTagInfos"), cms.InputTag("softElectronTagInfos"))
)


process.combinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.combinedSecondaryVertexBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5PF"), cms.InputTag("secondaryVertexTagInfosAK5PF"))
)


process.combinedSecondaryVertexBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7Calo"), cms.InputTag("secondaryVertexTagInfosAK7Calo"))
)


process.combinedSecondaryVertexBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7PF"), cms.InputTag("secondaryVertexTagInfosAK7PF"))
)


process.combinedSecondaryVertexBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"), cms.InputTag("secondaryVertexTagInfosAOD"))
)


process.combinedSecondaryVertexBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCACalo"), cms.InputTag("secondaryVertexTagInfosCACalo"))
)


process.combinedSecondaryVertexBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCAPF"), cms.InputTag("secondaryVertexTagInfosCAPF"))
)


process.combinedSecondaryVertexBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfossubCAPF"), cms.InputTag("secondaryVertexTagInfossubCAPF"))
)


process.combinedSecondaryVertexMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.combinedSecondaryVertexMVABJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5PF"), cms.InputTag("secondaryVertexTagInfosAK5PF"))
)


process.combinedSecondaryVertexMVABJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7Calo"), cms.InputTag("secondaryVertexTagInfosAK7Calo"))
)


process.combinedSecondaryVertexMVABJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7PF"), cms.InputTag("secondaryVertexTagInfosAK7PF"))
)


process.combinedSecondaryVertexMVABJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"), cms.InputTag("secondaryVertexTagInfosAOD"))
)


process.combinedSecondaryVertexMVABJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCACalo"), cms.InputTag("secondaryVertexTagInfosCACalo"))
)


process.combinedSecondaryVertexMVABJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCAPF"), cms.InputTag("secondaryVertexTagInfosCAPF"))
)


process.combinedSecondaryVertexMVABJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfossubCAPF"), cms.InputTag("secondaryVertexTagInfossubCAPF"))
)


process.corMetGlobalMuons = cms.EDProducer("MuonMET",
    muonMETDepositValueMapInputTag = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    metTypeInputTag = cms.InputTag("CaloMET"),
    muonsInputTag = cms.InputTag("muons"),
    uncorMETInputTag = cms.InputTag("met")
)


process.eidCutBasedExt = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('loose'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('robust'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidLoose = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('loose'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('classbased'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidRobustHighEnergy = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('highenergy'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('robust'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidRobustLoose = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('loose'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('robust'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidRobustTight = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('tight'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('robust'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidTight = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('tight'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('classbased'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidVBTFCom70 = cms.EDProducer("EleIdCutBasedExtProducer",
    robust60relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.04, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.02, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust80cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    algorithm = cms.string('eIDCB'),
    verticesCollection = cms.InputTag("offlineBeamSpot"),
    robust95relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.15, 2.0, 0.12, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.08, 0.06, 0.05, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    ),
    robust70relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.025, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    robust70cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.04, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust85cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.09, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust80relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.07, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust90cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust85relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.08, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    electronQuality = cms.string('70cIso'),
    electronIDType = cms.string('robust'),
    electronVersion = cms.string('V04'),
    src = cms.InputTag("gsfElectrons"),
    robust90relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.12, 0.09, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust60cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.02, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    robust95cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.15, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    )
)


process.eidVBTFCom80 = cms.EDProducer("EleIdCutBasedExtProducer",
    robust60relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.04, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.02, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust80cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    algorithm = cms.string('eIDCB'),
    verticesCollection = cms.InputTag("offlineBeamSpot"),
    robust95relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.15, 2.0, 0.12, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.08, 0.06, 0.05, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    ),
    robust70relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.025, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    robust70cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.04, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust85cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.09, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust80relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.07, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust90cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust85relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.08, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    electronQuality = cms.string('80cIso'),
    electronIDType = cms.string('robust'),
    electronVersion = cms.string('V04'),
    src = cms.InputTag("gsfElectrons"),
    robust90relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.12, 0.09, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust60cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.02, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    robust95cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.15, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    )
)


process.eidVBTFCom85 = cms.EDProducer("EleIdCutBasedExtProducer",
    robust60relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.04, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.02, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust80cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    algorithm = cms.string('eIDCB'),
    verticesCollection = cms.InputTag("offlineBeamSpot"),
    robust95relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.15, 2.0, 0.12, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.08, 0.06, 0.05, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    ),
    robust70relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.025, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    robust70cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.04, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust85cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.09, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust80relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.07, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust90cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust85relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.08, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    electronQuality = cms.string('85cIso'),
    electronIDType = cms.string('robust'),
    electronVersion = cms.string('V04'),
    src = cms.InputTag("gsfElectrons"),
    robust90relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.12, 0.09, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust60cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.02, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    robust95cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.15, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    )
)


process.eidVBTFCom95 = cms.EDProducer("EleIdCutBasedExtProducer",
    robust60relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.04, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.02, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust80cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    algorithm = cms.string('eIDCB'),
    verticesCollection = cms.InputTag("offlineBeamSpot"),
    robust95relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.15, 2.0, 0.12, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.08, 0.06, 0.05, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    ),
    robust70relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.025, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    robust70cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.04, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust85cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.09, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust80relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.07, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust90cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust85relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.08, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    electronQuality = cms.string('95cIso'),
    electronIDType = cms.string('robust'),
    electronVersion = cms.string('V04'),
    src = cms.InputTag("gsfElectrons"),
    robust90relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.12, 0.09, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust60cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.02, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    robust95cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.15, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    )
)


process.eidVBTFRel70 = cms.EDProducer("EleIdCutBasedExtProducer",
    robust60relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.04, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.02, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust80cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    algorithm = cms.string('eIDCB'),
    verticesCollection = cms.InputTag("offlineBeamSpot"),
    robust95relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.15, 2.0, 0.12, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.08, 0.06, 0.05, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    ),
    robust70relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.025, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    robust70cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.04, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust85cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.09, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust80relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.07, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust90cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust85relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.08, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    electronQuality = cms.string('70relIso'),
    electronIDType = cms.string('robust'),
    electronVersion = cms.string('V04'),
    src = cms.InputTag("gsfElectrons"),
    robust90relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.12, 0.09, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust60cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.02, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    robust95cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.15, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    )
)


process.eidVBTFRel80 = cms.EDProducer("EleIdCutBasedExtProducer",
    robust60relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.04, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.02, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust80cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    algorithm = cms.string('eIDCB'),
    verticesCollection = cms.InputTag("offlineBeamSpot"),
    robust95relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.15, 2.0, 0.12, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.08, 0.06, 0.05, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    ),
    robust70relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.025, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    robust70cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.04, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust85cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.09, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust80relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.07, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust90cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust85relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.08, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    electronQuality = cms.string('80relIso'),
    electronIDType = cms.string('robust'),
    electronVersion = cms.string('V04'),
    src = cms.InputTag("gsfElectrons"),
    robust90relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.12, 0.09, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust60cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.02, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    robust95cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.15, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    )
)


process.eidVBTFRel85 = cms.EDProducer("EleIdCutBasedExtProducer",
    robust60relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.04, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.02, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust80cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    algorithm = cms.string('eIDCB'),
    verticesCollection = cms.InputTag("offlineBeamSpot"),
    robust95relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.15, 2.0, 0.12, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.08, 0.06, 0.05, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    ),
    robust70relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.025, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    robust70cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.04, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust85cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.09, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust80relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.07, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust90cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust85relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.08, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    electronQuality = cms.string('85relIso'),
    electronIDType = cms.string('robust'),
    electronVersion = cms.string('V04'),
    src = cms.InputTag("gsfElectrons"),
    robust90relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.12, 0.09, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust60cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.02, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    robust95cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.15, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    )
)


process.eidVBTFRel95 = cms.EDProducer("EleIdCutBasedExtProducer",
    robust60relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.04, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.02, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust80cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    algorithm = cms.string('eIDCB'),
    verticesCollection = cms.InputTag("offlineBeamSpot"),
    robust95relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.15, 2.0, 0.12, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.08, 0.06, 0.05, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    ),
    robust70relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.025, 0.025, 0.02, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    robust70cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.03, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.04, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust85cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.09, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.06, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust80relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.07, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.03, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.04, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    robust90cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.07, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust85relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.04, 0.01, 0.06, 0.006, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.09, 0.08, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.04, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.05, 0.025, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    electronQuality = cms.string('95relIso'),
    electronIDType = cms.string('robust'),
    electronVersion = cms.string('V04'),
    src = cms.InputTag("gsfElectrons"),
    robust90relIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.12, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.12, 0.09, 0.1, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.05, 0.03, 0.7, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 0.05, 0.06, 0.03, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.02, 
            0.02)
    ),
    robust60cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.025, 0.01, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.03, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02),
        endcap = cms.vdouble(0.025, 0.03, 0.02, 0.005, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.02, 0.0, -9999.0, 
            9999.0, 9999.0, 0, -1, 0.02, 
            0.02)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    robust95cIsoEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.15, 0.01, 0.8, 0.007, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.15, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0),
        endcap = cms.vdouble(0.07, 0.03, 0.7, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 0.1, 0.0, -9999.0, 
            9999.0, 9999.0, 1, -1, 0.0, 
            0.0)
    )
)


process.eleIsoDepositEcalFromHits = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("gsfElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        isolationVariable = cms.string('et'),
        tryBoth = cms.bool(True),
        intStrip = cms.double(0.0),
        ComponentName = cms.string('EgammaRecHitExtractor'),
        endcapEcalHits = cms.InputTag("reducedEcalRecHitsEE"),
        recHitFlagsToBeExcluded = cms.vint32(3, 5, 9, 10),
        intRadius = cms.double(0.0),
        severityLevelCut = cms.int32(4),
        energyMin = cms.double(0.08),
        extRadius = cms.double(0.6),
        subtractSuperClusterEnergy = cms.bool(False),
        vetoClustered = cms.bool(False),
        etMin = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        barrelEcalHits = cms.InputTag("reducedEcalRecHitsEB")
    )
)


process.eleIsoDepositHcalFromTowers = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("gsfElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        caloTowers = cms.InputTag("towerMaker"),
        ComponentName = cms.string('EgammaTowerExtractor'),
        hcalDepth = cms.int32(-1),
        intRadius = cms.double(0.0),
        extRadius = cms.double(0.6),
        DepositLabel = cms.untracked.string(''),
        etMin = cms.double(-999.0)
    )
)


process.eleIsoDepositTk = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("gsfElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        dzOption = cms.string('vz'),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('EgammaTrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(9999.0),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.0),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        inputTrackCollection = cms.InputTag("generalTracks")
    )
)


process.eleIsoFromDepsEcalFromHitsByCrystal = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("eleIsoDepositEcalFromHits"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('NumCrystalVeto(3.0)', 
            'NumCrystalEtaPhiVeto(1.5,9999.0)', 
            'EcalBarrel:AbsThresholdFromTransverse(0.08)', 
            'EcalEndcaps:AbsThreshold(0.100)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.eleIsoFromDepsHcalFromTowers = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("eleIsoDepositHcalFromTowers"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.15'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.eleIsoFromDepsTk = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("eleIsoDepositTk"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('RectangularEtaPhiVeto(-0.015,0.015,-0.5,0.5)', 
            'Threshold(0.7)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoDepositCharged = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.elePFIsoDepositChargedAll = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedCandidates"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.elePFIsoDepositGamma = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.elePFIsoDepositNeutral = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.elePFIsoDepositPU = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPUChargedCandidates"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.elePFIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositCharged"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositCharged"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositChargedAll"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositChargedAll"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositGamma"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositGamma"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositNeutral"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositNeutral"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositPU"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.elePFIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("elePFIsoDepositPU"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.electronMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("gsfElectrons"),
    maxDPtRel = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.5),
    checkCharge = cms.bool(True),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.fixedConePFTauDecayModeIndexProducer = cms.EDProducer("PFRecoTauDecayModeIndexProducer",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    PFTauDecayModeProducer = cms.InputTag("fixedConePFTauDecayModeProducer")
)


process.fixedConePFTauDecayModeProducer = cms.EDProducer("PFRecoTauDecayModeDeterminator",
    mergeByBestMatch = cms.bool(True),
    refitTracks = cms.bool(False),
    maxPiZeroMass = cms.double(0.2),
    mergeLowPtPhotonsFirst = cms.bool(True),
    setMergedPi0Mass = cms.bool(True),
    setChargedPionMass = cms.bool(True),
    filterPhotons = cms.bool(True),
    minPtFractionSinglePhotons = cms.double(0.1),
    minPtFractionPiZeroes = cms.double(0.15),
    maxNbrOfIterations = cms.int32(10),
    filterTwoProngs = cms.bool(True),
    minPtFractionForSecondProng = cms.double(0.1),
    maxDistance = cms.double(0.01),
    setPi0Mass = cms.bool(True),
    maxPhotonsToMerge = cms.uint32(2),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer")
)


process.fixedConePFTauDiscriminationAgainstElectron = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(-0.1),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("fixedConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    ApplyCut_BremCombined = cms.bool(False),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(False),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.fixedConePFTauDiscriminationAgainstMuon = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon",
    a = cms.double(0.5),
    c = cms.double(0.0),
    b = cms.double(0.5),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("fixedConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    discriminatorOption = cms.string('noSegMatch')
)


process.fixedConePFTauDiscriminationByECALIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("fixedConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.fixedConePFTauDiscriminationByECALIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("fixedConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.fixedConePFTauDiscriminationByIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("fixedConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.fixedConePFTauDiscriminationByIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("fixedConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.fixedConePFTauDiscriminationByLeadingPionPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    UseOnlyChargedHadrons = cms.bool(False)
)


process.fixedConePFTauDiscriminationByLeadingTrackFinding = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.fixedConePFTauDiscriminationByLeadingTrackPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.fixedConePFTauDiscriminationByTrackIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("fixedConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.fixedConePFTauDiscriminationByTrackIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("fixedConePFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("fixedConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.fixedConePFTauProducer = cms.EDProducer("RecoTauProducer",
    piZeroSrc = cms.InputTag("ak5PFJetsRecoTauPiZeros"),
    modifiers = cms.VPSet(cms.PSet(
        ElectronPreIDProducer = cms.InputTag("elecpreid"),
        name = cms.string('shrinkingConeElectronRej'),
        plugin = cms.string('RecoTauElectronRejectionPlugin'),
        DataType = cms.string('AOD'),
        maximumForElectrionPreIDOutput = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
        EcalStripSumE_minClusEnergy = cms.double(0.1),
        ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
        EcalStripSumE_deltaEta = cms.double(0.03)
    )),
    jetRegionSrc = cms.InputTag("recoTauAK5PFJets08Region"),
    jetSrc = cms.InputTag("ak5PFJets"),
    builders = cms.VPSet(cms.PSet(
        usePFLeptons = cms.bool(True),
        signalConeNeutralHadrons = cms.string('0.10'),
        name = cms.string('fixedCone'),
        plugin = cms.string('RecoTauBuilderConePlugin'),
        isoConeChargedHadrons = cms.string('0.5'),
        isoConePiZeros = cms.string('0.5'),
        isoConeNeutralHadrons = cms.string('0.5'),
        matchingCone = cms.string('0.1'),
        signalConeChargedHadrons = cms.string('0.07'),
        leadObjectPt = cms.double(5.0),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalConePiZeros = cms.string('0.15'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pfCandSrc = cms.InputTag("particleFlow")
    )),
    buildNullTaus = cms.bool(True)
)


process.fixedConeRecoTaus = cms.EDProducer("RecoTauProducer",
    piZeroSrc = cms.InputTag("ak5PFJetsRecoTauPiZeros"),
    modifiers = cms.VPSet(cms.PSet(
        ElectronPreIDProducer = cms.InputTag("elecpreid"),
        name = cms.string('shrinkingConeElectronRej'),
        plugin = cms.string('RecoTauElectronRejectionPlugin'),
        DataType = cms.string('AOD'),
        maximumForElectrionPreIDOutput = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
        EcalStripSumE_minClusEnergy = cms.double(0.1),
        ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
        EcalStripSumE_deltaEta = cms.double(0.03)
    )),
    jetRegionSrc = cms.InputTag("recoTauAK5PFJets08Region"),
    jetSrc = cms.InputTag("ak5PFJets"),
    builders = cms.VPSet(cms.PSet(
        usePFLeptons = cms.bool(True),
        signalConeNeutralHadrons = cms.string('0.10'),
        name = cms.string('fixedCone'),
        plugin = cms.string('RecoTauBuilderConePlugin'),
        isoConeChargedHadrons = cms.string('0.5'),
        isoConePiZeros = cms.string('0.5'),
        isoConeNeutralHadrons = cms.string('0.5'),
        matchingCone = cms.string('0.1'),
        signalConeChargedHadrons = cms.string('0.07'),
        leadObjectPt = cms.double(5.0),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalConePiZeros = cms.string('0.15'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pfCandSrc = cms.InputTag("particleFlow")
    )),
    buildNullTaus = cms.bool(True)
)


process.gamIsoDepositEcalFromHits = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("photons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        isolationVariable = cms.string('et'),
        tryBoth = cms.bool(True),
        intStrip = cms.double(0.0),
        ComponentName = cms.string('EgammaRecHitExtractor'),
        endcapEcalHits = cms.InputTag("reducedEcalRecHitsEE"),
        recHitFlagsToBeExcluded = cms.vint32(3, 5, 9, 10),
        intRadius = cms.double(0.0),
        severityLevelCut = cms.int32(4),
        energyMin = cms.double(0.08),
        extRadius = cms.double(0.6),
        subtractSuperClusterEnergy = cms.bool(False),
        vetoClustered = cms.bool(False),
        detector = cms.string('Ecal'),
        etMin = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        barrelEcalHits = cms.InputTag("reducedEcalRecHitsEB")
    )
)


process.gamIsoDepositHcalFromTowers = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("photons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        caloTowers = cms.InputTag("towerMaker"),
        ComponentName = cms.string('EgammaTowerExtractor'),
        hcalDepth = cms.int32(-1),
        intRadius = cms.double(0.0),
        extRadius = cms.double(0.6),
        DepositLabel = cms.untracked.string(''),
        etMin = cms.double(-999.0)
    )
)


process.gamIsoDepositTk = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("photons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        dzOption = cms.string('vz'),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('EgammaTrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(9999.0),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.0),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        inputTrackCollection = cms.InputTag("generalTracks")
    )
)


process.gamIsoFromDepsEcalFromHits = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("gamIsoDepositEcalFromHits"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('EcalBarrel:0.045', 
            'EcalBarrel:RectangularEtaPhiVeto(-0.02,0.02,-0.5,0.5)', 
            'EcalBarrel:AbsThresholdFromTransverse(0.080)', 
            'EcalEndcaps:0.070', 
            'EcalEndcaps:RectangularEtaPhiVeto(-0.02,0.02,-0.5,0.5)', 
            'EcalEndcaps:AbsThreshold(0.100)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.gamIsoFromDepsHcalFromTowers = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("gamIsoDepositHcalFromTowers"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.15'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.gamIsoFromDepsTk = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("gamIsoDepositTk"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('RectangularEtaPhiVeto(-0.015,0.015,-0.5,0.5)', 
            'Threshold(1.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.genParticlesForJets = cms.EDProducer("InputGenJetsParticleSelector",
    src = cms.InputTag("genParticles"),
    ignoreParticleIDs = cms.vuint32(1000022, 1000012, 1000014, 1000016, 2000012, 
        2000014, 2000016, 1000039, 5100039, 4000012, 
        4000014, 4000016, 9900012, 9900014, 9900016, 
        39),
    partonicFinalState = cms.bool(False),
    excludeResonances = cms.bool(True),
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    tausAsJets = cms.bool(False)
)


process.genParticlesForJetsNoMuNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    src = cms.InputTag("genParticles"),
    ignoreParticleIDs = cms.vuint32(1000022, 1000012, 1000014, 1000016, 2000012, 
        2000014, 2000016, 1000039, 5100039, 4000012, 
        4000014, 4000016, 9900012, 9900014, 9900016, 
        39, 12, 13, 14, 16),
    partonicFinalState = cms.bool(False),
    excludeResonances = cms.bool(True),
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    tausAsJets = cms.bool(False)
)


process.genParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    src = cms.InputTag("genParticles"),
    ignoreParticleIDs = cms.vuint32(1000022, 1000012, 1000014, 1000016, 2000012, 
        2000014, 2000016, 1000039, 5100039, 4000012, 
        4000014, 4000016, 9900012, 9900014, 9900016, 
        39, 12, 14, 16),
    partonicFinalState = cms.bool(False),
    excludeResonances = cms.bool(True),
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    tausAsJets = cms.bool(False)
)


process.ghostTrackBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('ghostTrack'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("ghostTrackVertexTagInfos"))
)


process.ghostTrackVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        primcut = cms.double(2.0),
        seccut = cms.double(4.0),
        maxFitChi2 = cms.double(10.0),
        fitType = cms.string('RefitGhostTrackWithVertices'),
        mergeThreshold = cms.double(3.0),
        finder = cms.string('gtvr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(1),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.gk5GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('GeneralizedKt'),
    rParam = cms.double(0.5)
)


process.gk5GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('GeneralizedKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.gk5GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('GeneralizedKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.gk7GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('GeneralizedKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJets"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.gk7GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('GeneralizedKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.gk7GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('GeneralizedKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.hiGenParticlesForJets = cms.EDProducer("InputGenJetsParticleSelector",
    src = cms.InputTag("hiGenParticles"),
    ignoreParticleIDs = cms.vuint32(1000022, 1000012, 1000014, 1000016, 2000012, 
        2000014, 2000016, 1000039, 5100039, 4000012, 
        4000014, 4000016, 9900012, 9900014, 9900016, 
        39),
    partonicFinalState = cms.bool(False),
    excludeResonances = cms.bool(True),
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    tausAsJets = cms.bool(False)
)


process.hpsLooseIsolationCleaner = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("combinatoricRecoTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsMediumIsolationCleaner = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("combinatoricRecoTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(0.8),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.8),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsPFTauDiscriminationByDecayModeFinding = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    minTauPt = cms.double(0.0),
    coneSizeFormula = cms.string('max(min(0.5, 2.8/pt()),0.05)'),
    matchingCone = cms.double(0.1),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        minMass = cms.double(-0.1),
        maxMass = cms.double(1),
        nCharged = cms.uint32(1)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            assumeStripMass = cms.double(0.1349),
            minMass = cms.double(0.3),
            maxMass = cms.double(1.3),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            minPi0Mass = cms.double(0.05),
            maxMass = cms.double(1.2),
            maxPi0Mass = cms.double(0.2),
            nPiZeros = cms.uint32(2),
            minMass = cms.double(0.4),
            nCharged = cms.uint32(1),
            assumeStripMass = cms.double(0.0)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            minMass = cms.double(0.8),
            maxMass = cms.double(1.5),
            nCharged = cms.uint32(3)
        ))
)


process.hpsPFTauDiscriminationByLooseElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(0.6),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    ApplyCut_BremCombined = cms.bool(False),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(False),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.hpsPFTauDiscriminationByLooseIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsPFTauDiscriminationByLooseMuonRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon",
    a = cms.double(0.5),
    c = cms.double(0.0),
    b = cms.double(0.5),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    discriminatorOption = cms.string('noSegMatch')
)


process.hpsPFTauDiscriminationByMediumElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(-0.1),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    ApplyCut_BremCombined = cms.bool(False),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(True),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.hpsPFTauDiscriminationByMediumIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(0.8),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.8),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsPFTauDiscriminationByTightElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(-0.1),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    ApplyCut_BremCombined = cms.bool(True),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(True),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.hpsPFTauDiscriminationByTightIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsPFTauDiscriminationByTightMuonRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon",
    a = cms.double(0.5),
    c = cms.double(0.0),
    b = cms.double(0.5),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    discriminatorOption = cms.string('noAllArbitrated')
)


process.hpsPFTauDiscriminationByVLooseIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(2.0),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.3)
)


process.hpsPFTauProducer = cms.EDProducer("RecoTauCleaner",
    cleaners = cms.VPSet(cms.PSet(
        selectionPassFunction = cms.string('abs(charge())-1'),
        selection = cms.string('signalPFChargedHadrCands().size() = 3'),
        name = cms.string('UnitCharge'),
        plugin = cms.string('RecoTauStringCleanerPlugin'),
        selectionFailValue = cms.double(0)
    ), 
        cms.PSet(
            selectionPassFunction = cms.string('0'),
            selection = cms.string('deltaR(eta, phi, jetRef().eta, jetRef().phi) < 0.1'),
            name = cms.string('MatchingCone'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selectionFailValue = cms.double(1000.0)
        ), 
        cms.PSet(
            src = cms.InputTag("hpsSelectionDiscriminator"),
            name = cms.string('HPS_Select'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin')
        ), 
        cms.PSet(
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum()+isolationPFGammaCandsEtSum()'),
            selection = cms.string('leadPFCand().isNonnull()'),
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selectionFailValue = cms.double(1000.0)
        )),
    src = cms.InputTag("combinatoricRecoTaus")
)


process.hpsSelectionDiscriminator = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("combinatoricRecoTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    minTauPt = cms.double(0.0),
    coneSizeFormula = cms.string('max(min(0.5, 2.8/pt()),0.05)'),
    matchingCone = cms.double(0.1),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        minMass = cms.double(-0.1),
        maxMass = cms.double(1),
        nCharged = cms.uint32(1)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            assumeStripMass = cms.double(0.1349),
            minMass = cms.double(0.3),
            maxMass = cms.double(1.3),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            minPi0Mass = cms.double(0.05),
            maxMass = cms.double(1.2),
            maxPi0Mass = cms.double(0.2),
            nPiZeros = cms.uint32(2),
            minMass = cms.double(0.4),
            nCharged = cms.uint32(1),
            assumeStripMass = cms.double(0.0)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            minMass = cms.double(0.8),
            maxMass = cms.double(1.5),
            nCharged = cms.uint32(3)
        ))
)


process.hpsTancTaus = cms.EDProducer("RecoTauCleaner",
    cleaners = cms.VPSet(cms.PSet(
        selectionPassFunction = cms.string('abs(charge())-1'),
        selection = cms.string('signalPFChargedHadrCands().size() = 3'),
        name = cms.string('UnitCharge'),
        plugin = cms.string('RecoTauStringCleanerPlugin'),
        selectionFailValue = cms.double(0)
    ), 
        cms.PSet(
            selectionPassFunction = cms.string('0'),
            selection = cms.string('deltaR(eta, phi, jetRef().eta, jetRef().phi) < 0.1'),
            name = cms.string('MatchingCone'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selectionFailValue = cms.double(1000.0)
        ), 
        cms.PSet(
            src = cms.InputTag("combinatoricRecoTausDiscriminationByLeadingPionPtCut"),
            name = cms.string('lead pion'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin')
        ), 
        cms.PSet(
            src = cms.InputTag("combinatoricRecoTausHPSSelector"),
            name = cms.string('HPS selection'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin')
        ), 
        cms.PSet(
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum()+isolationPFGammaCandsEtSum()'),
            selection = cms.string('leadPFCand().isNonnull()'),
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selectionFailValue = cms.double(1000.0)
        )),
    src = cms.InputTag("combinatoricRecoTaus")
)


process.hpsTancTausDiscriminationAgainstCaloMuon = cms.EDProducer("PFRecoTauDiscriminationAgainstCaloMuon",
    srcHcalRecHits = cms.InputTag("hbhereco"),
    minLeadTrackPt = cms.double(15.0),
    maxEnToTrackRatio = cms.double(0.25),
    srcVertex = cms.InputTag("offlinePrimaryVerticesWithBS"),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    srcEcalRecHitsBarrel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    dRhcal = cms.double(25.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByLeadingTrackFinding")
        )
    ),
    maxEnEcal = cms.double(3.0),
    maxEnHcal = cms.double(8.0),
    dRecal = cms.double(15.0),
    srcEcalRecHitsEndcap = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    minLeadTrackPtFraction = cms.double(0.8)
)


process.hpsTancTausDiscriminationByDecayModeSelection = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    src = cms.InputTag("combinatoricRecoTaus"),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    minTauPt = cms.double(5.0),
    coneSizeFormula = cms.string('0.3'),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        minMass = cms.double(-0.1),
        maxMass = cms.double(1),
        nCharged = cms.uint32(1)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            assumeStripMass = cms.double(0.1349),
            minMass = cms.double(0.3),
            maxMass = cms.double(1.3),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            minPi0Mass = cms.double(0.05),
            maxMass = cms.double(1.2),
            maxPi0Mass = cms.double(0.2),
            nPiZeros = cms.uint32(2),
            minMass = cms.double(0.4),
            nCharged = cms.uint32(1),
            assumeStripMass = cms.double(0.0)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            minMass = cms.double(0.8),
            maxMass = cms.double(1.5),
            nCharged = cms.uint32(3)
        )),
    matchingCone = cms.double(0.1)
)


process.hpsTancTausDiscriminationByFlightPath = cms.EDProducer("PFRecoTauDiscriminationByFlight",
    refitPV = cms.bool(True),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection")
        )
    ),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    vertexSource = cms.InputTag("offlinePrimaryVertices"),
    beamspot = cms.InputTag("offlineBeamSpot")
)


process.hpsTancTausDiscriminationByLeadingPionPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    UseOnlyChargedHadrons = cms.bool(False)
)


process.hpsTancTausDiscriminationByLeadingTrackFinding = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.hpsTancTausDiscriminationByLeadingTrackPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.hpsTancTausDiscriminationByLooseElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(0.6),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    ApplyCut_BremCombined = cms.bool(False),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(False),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.hpsTancTausDiscriminationByLooseIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsTancTausDiscriminationByLooseMuonRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon",
    a = cms.double(0.5),
    c = cms.double(0.0),
    b = cms.double(0.5),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    discriminatorOption = cms.string('noSegMatch')
)


process.hpsTancTausDiscriminationByMediumElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(-0.1),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    ApplyCut_BremCombined = cms.bool(False),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(True),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.hpsTancTausDiscriminationByMediumIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(0.8),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.8),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsTancTausDiscriminationByTanc = cms.EDProducer("RecoTauMVATransform",
    Prediscriminants = cms.PSet(
        hpsSelect = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection")
        ),
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByLeadingPionPtCut")
        )
    ),
    transforms = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        transform = cms.PSet(
            max = cms.double(1.99833333333),
            transform = (cms.vdouble(0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508)+cms.vdouble(0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243693947972, 0.2446621342, 0.25648929965, 0.2608766459, 0.265139843949, 0.268288096025, 0.271490633611, 0.274812027295, 0.278726505561, 0.283196361675, 0.287921047203, 0.293485065795, 0.299327353484, 0.305468394708, 0.310410038477, 0.315654364298, 0.320865024837, 0.324875648584, 0.328691660974, 0.332598633349, 0.336484807993, 0.339893814351, 0.343528868912, 0.346311138119, 0.348525259682, 0.350638868762, 0.352500481165, 0.354385202603, 0.356405103778, 0.358448162743, 0.359626155068, 0.361359527277, 0.362911630832, 0.364767207965, 0.365568276809, 0.367161876825, 0.368245783665, 0.369700987138, 0.370891835827, 0.371335926598, 0.372724067775, 0.374122626292, 0.374872824273, 0.376287585272, 0.377808481377, 0.379437962659, 0.380385427158, 0.381454465894, 0.382529530437, 0.383308773065, 0.383900643462, 0.384488881534, 0.385284008411, 0.385778244795, 0.386880706208, 0.387787417873, 0.389206336729, 0.390430843456, 0.391560096158, 0.392490239284, 0.393218300975, 0.394889524946, 0.396474094424, 0.397328157396, 0.398823062781, 0.400437280424, 0.401846875958, 0.402719262685, 0.403705236447, 0.40437725886, 0.405483096559, 0.40715324019, 0.408161946716, 0.408949958358, 0.410194428622, 0.411674966358, 0.412726139917, 0.413994836217, 0.414922434459, 0.415970963664, 0.417494895799, 0.418345516985, 0.419769194149, 0.42120259427, 0.423008169722, 0.424220511323, 0.425684525769, 0.426912279039, 0.428023327968, 0.429389155258, 0.430889124801, 0.432147128025, 0.433793555744, 0.435196517338, 0.436351162787, 0.437253465009, 0.438419065687, 0.439590897333, 0.440949213705, 0.441921470289, 0.442848592497, 0.44396524306, 0.445223842049, 0.446977728682, 0.448745488265, 0.451078381688, 0.451907557714, 0.452739787751, 0.453638395261, 0.45475822595, 0.456165813144, 0.457223834211, 0.457934807034, 0.45922014571, 0.461017229233, 0.461451032994, 0.463048655665, 0.464804181316, 0.466425147476, 0.467542494191, 0.468517661795, 0.470468799941, 0.47198076935, 0.472892624736, 0.474420238705, 0.476266453893, 0.477505267649, 0.479532143347, 0.481200116592, 0.481613637289, 0.483360304775, 0.485061449421, 0.487101659613, 0.488019909526, 0.488999144832, 0.490200759674, 0.491190516798, 0.493849514855, 0.495306102206, 0.495928489713, 0.4964353883, 0.498082556741, 0.49979254034, 0.500775976586, 0.502679733683, 0.504598020717, 0.505078487853, 0.506619141507, 0.508171974823, 0.509336469886, 0.510953930915, 0.512581697566, 0.513998315702, 0.515647034962, 0.515939613111, 0.517975069449, 0.519430445753, 0.519957296262, 0.521273324958, 0.522406663349, 0.523925469498, 0.524625850033, 0.525907581275, 0.527065315655, 0.52822815856, 0.528783474767, 0.529145626115, 0.529453767868, 0.530435650231, 0.532014259582, 0.532782125184, 0.534528955521, 0.535733634238, 0.539584530704, 0.541410067901, 0.543682312792, 0.545138243861, 0.546811742597, 0.548048893429, 0.548459504636, 0.550158093752, 0.551205716597, 0.552261157841, 0.553773021814, 0.554620522074, 0.557022425024, 0.558787346691, 0.55989408991, 0.562351160997, 0.564603650808, 0.567330572538, 0.568251047692, 0.570322191691, 0.570800554836, 0.573840553165, 0.575722428922, 0.578806943369, 0.580018988744, 0.581943439091, 0.583637839285, 0.583719886077, 0.585230062162, 0.586459819001, 0.58819018682, 0.589432428675, 0.590707557501, 0.59199058109, 0.593311935901, 0.596143502405, 0.598713047084, 0.59985869618, 0.60146038335)+cms.vdouble(0.603073645068, 0.60364159568, 0.605493798425, 0.607716165748, 0.611539567166, 0.61344596304, 0.614868728468, 0.616356298487, 0.617243661796, 0.618356139972, 0.620433033442, 0.623603658141, 0.625027738979, 0.626745245057, 0.630061473707, 0.634451273629, 0.636224368987, 0.638386932974, 0.639666729708, 0.641472541416, 0.643376129813, 0.645998175052, 0.648651724655, 0.650614385321, 0.651964427491, 0.654372246094, 0.656912558238, 0.657658356547, 0.658734274882, 0.661006291486, 0.663094362812, 0.664860224717, 0.667639986138, 0.669224738703, 0.670609710516, 0.672008536945, 0.674322956904, 0.676181757848, 0.680504320591, 0.681701882298, 0.683847428048, 0.687028204213, 0.690096183579, 0.692936565842, 0.698333032093, 0.702469873766, 0.704533440299, 0.706621657637, 0.710308262591, 0.713270705866, 0.714865826284, 0.719086552707, 0.722147885763, 0.725885046087, 0.729450681758, 0.732859861331, 0.739185288999, 0.743172463789, 0.74657896386, 0.751327840506, 0.754658774214, 0.758047388164, 0.762059448212, 0.769914558551, 0.775838239214, 0.780728907111, 0.786952215918, 0.793694146175, 0.796885300439, 0.802863959078, 0.813001141474, 0.820597251397, 0.829350775725, 0.837460143471, 0.84199323298, 0.847433416989, 0.854638027367, 0.860714284529, 0.869959964541, 0.876007819869, 0.884455823419, 0.896538436371, 0.904016005807, 0.910382232961, 0.916770946986, 0.93386870405, 0.943467586229, 0.95165443966, 0.971789456433, 0.970755563959, 0.9679163435, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
            min = cms.double(-0.998333333333)
        ),
        nCharged = cms.uint32(3)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            transform = cms.PSet(
                max = cms.double(1.99833333333),
                transform = (cms.vdouble(0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285)+cms.vdouble(0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725625489751, 0.725917318629, 0.727526582607, 0.745748231906, 0.750169168536, 0.757185219071, 0.764249672036, 0.767603981959, 0.772574492642, 0.775097031572, 0.777704615235, 0.779407980465, 0.781767581973, 0.784842584326, 0.786420654919, 0.787883166617, 0.790123535551, 0.79208138528, 0.79327247227, 0.795907708578, 0.798503646112, 0.800206834461, 0.802663946447, 0.8031582666, 0.80490222571, 0.806889568691, 0.809394028316, 0.811861583702, 0.813019057268, 0.81342095915, 0.814698723372, 0.816279445985, 0.818232037783, 0.819367026875, 0.819759858707, 0.821328989638, 0.822878675172, 0.82364763472, 0.825358996088, 0.828499118125, 0.829830087025, 0.831236000117, 0.832703495507, 0.833414247004, 0.834436344112, 0.834946785624, 0.835869791486, 0.836486520822, 0.837364626557, 0.838193318858, 0.839702591039, 0.841531457051, 0.842218371935, 0.843640339114, 0.844222988069, 0.845392038566, 0.846778761898, 0.84769605779, 0.848073950379, 0.848849957765, 0.849494110293, 0.8500905241, 0.851335675181, 0.853500950651, 0.853839833615, 0.854227213103, 0.854567621296, 0.854984559013, 0.855203285083, 0.856470785047, 0.857475859603, 0.85892685241, 0.859008202829, 0.859451257957, 0.860468389831, 0.861489507276, 0.861351261404, 0.861705874851, 0.861659795003, 0.861659795003, 0.86179137032, 0.862147375366, 0.862550177315, 0.863312092458, 0.863805642705, 0.864438066642, 0.864754370118, 0.865480701328, 0.866346092335, 0.867168965701, 0.867397571488, 0.868313201223, 0.868771741382, 0.869186401202, 0.86983185136, 0.869929474522, 0.870346507695, 0.870951429469, 0.870863388987, 0.871514279263, 0.872166654676, 0.872355339191, 0.872776974093, 0.873155878735, 0.873579101025, 0.874003066865, 0.873916467734, 0.874211597253, 0.874402872188, 0.87510742975, 0.87525648792, 0.87525648792, 0.875448860228, 0.875598481234, 0.875512416378, 0.87617785231, 0.87617785231, 0.876371452215, 0.877233539228, 0.877818409805, 0.87840545558, 0.87840545558, 0.878601622981, 0.878601622981, 0.879472984901, 0.879712328244, 0.87982581203, 0.879981638026, 0.880179766123, 0.880378141371, 0.880534852587, 0.880691869776, 0.8811323429, 0.881090533252, 0.881531917098, 0.881732079801, 0.8822162463, 0.882902187113, 0.882979722574, 0.88403281278, 0.885010261835, 0.884928594333, 0.885132644083, 0.885050953876, 0.88525535544, 0.886362380543, 0.886487219509, 0.886652934413, 0.887232935079, 0.887728512003, 0.888561331939, 0.889019284728, 0.889438266521, 0.890358658388, 0.890120720891, 0.890292192785, 0.890675834925, 0.890556765164, 0.890981544778, 0.891699669632, 0.891660238395, 0.891969519877, 0.892319678993, 0.892161931402, 0.892513711208, 0.892729546909, 0.893162065429, 0.893339503795, 0.893339503795, 0.893656248099, 0.894427465173, 0.894606969217, 0.894825762437, 0.894928163898, 0.895703822513, 0.89622167567, 0.896663385868, 0.897404545302, 0.89769650475, 0.899189293203, 0.899525558799, 0.900803884235, 0.901822547362, 0.901939302648, 0.902926505697, 0.903082359676, 0.904038745128, 0.90469561985, 0.904927332682, 0.905283513893, 0.906828000044, 0.907062493553, 0.908109372415, 0.908783021349, 0.90898498498, 0.910379224289, 0.911372920866, 0.911751863015, 0.912477297669, 0.913239550237, 0.91300238707, 0.913422855139, 0.915063352192, 0.916893920936, 0.916979020829, 0.91791358353, 0.918350995783, 0.918790342789, 0.919328152961, 0.919993298628, 0.920982245955, 0.922524618114, 0.923591109364)+cms.vdouble(0.924018850534, 0.924248923821, 0.924479515826, 0.925498182241, 0.926493584801, 0.927436921962, 0.927911825271, 0.928716526512, 0.929225746944, 0.929920622352, 0.931640820211, 0.931772433588, 0.932293506679, 0.932760264784, 0.93386870405, 0.934480569506, 0.934731886916, 0.935797384751, 0.936588472051, 0.936817507478, 0.937277790773, 0.938339506605, 0.938808219887, 0.93993649209, 0.94020045716, 0.940781492864, 0.941047196853, 0.942510417566, 0.942629939, 0.942750378489, 0.943616386541, 0.944163684906, 0.945338814696, 0.945845741457, 0.946028661789, 0.946308362468, 0.946541150838, 0.946751152357, 0.947576555912, 0.948029352938, 0.94826905955, 0.948081416726, 0.949376743021, 0.94926144862, 0.949775296374, 0.949706301122, 0.951268968863, 0.953037066674, 0.95357532021, 0.953770570793, 0.953640586734, 0.953509869657, 0.954300159882, 0.955476996866, 0.956207587781, 0.956355833165, 0.956846568485, 0.957770053042, 0.958723171834, 0.958928454571, 0.959445187694, 0.959807967592, 0.959442259047, 0.960697132989, 0.961203278228, 0.963193467582, 0.963932365293, 0.964461162833, 0.964482886627, 0.96526433234, 0.966030150632, 0.966856588211, 0.969491617691, 0.970743493871, 0.972389419268, 0.973307337131, 0.975623617612, 0.976087161844, 0.975647899082, 0.976736074007, 0.979440008803, 0.981271208497, 0.982207028661, 0.984863078211, 0.986956530647, 0.990258251858, 0.990208776979, 0.990702226892, 0.993228159625, 0.99534336087, 0.996696237239, 0.995185049087, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
                min = cms.double(-0.998333333333)
            ),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            transform = cms.PSet(
                max = cms.double(1.99833333333),
                transform = (cms.vdouble(0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399)+cms.vdouble(0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.786753288885, 0.788132324416, 0.79656141615, 0.810183644995, 0.858360829913, 0.862298212616, 0.867110980413, 0.871372861265, 0.875682014578, 0.880242297589, 0.883696978098, 0.885512278829, 0.887768921813, 0.889264020585, 0.89119925019, 0.892452552697, 0.893185095837, 0.893419577074, 0.894898998675, 0.895774783109, 0.896260903725, 0.896505707407, 0.898082672851, 0.898779137453, 0.89979939771, 0.900120276805, 0.900442301311, 0.900314253861, 0.90063761708, 0.903107169678, 0.903707364412, 0.904624297652, 0.90437518453, 0.904187494019, 0.904648539996, 0.905849328721, 0.90625146477, 0.906593041173, 0.906284313013, 0.906627709554, 0.906627709554, 0.907095652088, 0.906972372385, 0.907318308525, 0.907603995571, 0.907357055463, 0.907233089763, 0.907994846936, 0.908883949265, 0.908883949265, 0.909836831321, 0.909836831321, 0.909776114594, 0.911030037809, 0.911509901723, 0.911871023987, 0.911811279009, 0.911751452972, 0.911691545709, 0.911511334909, 0.911451101085, 0.912784331406, 0.9125455069, 0.9125455069, 0.91297278083, 0.912853317543, 0.912673506387, 0.913592984461, 0.915007651179, 0.915441697726, 0.915324604996, 0.915207187526, 0.915148356591, 0.91552593882, 0.915467174967, 0.9154083293, 0.915290391839, 0.915231299701, 0.915728896806, 0.915728896806, 0.915552071941, 0.916492320764, 0.917377950283, 0.917822427143, 0.918268017622, 0.91871472591, 0.919668295227, 0.919611512782, 0.919554650007, 0.919440682785, 0.919269125195, 0.921306876156, 0.921306876156, 0.921082297245, 0.920969526416, 0.921426208902, 0.921939970027, 0.921939970027, 0.922343069964, 0.923319759486, 0.923727168952, 0.923727168952, 0.92460140151, 0.924492316338, 0.924959238052, 0.926474177051, 0.926474177051, 0.926420752856, 0.926313671218, 0.926785714713, 0.926785714713, 0.926785714713, 0.926732331515, 0.926732331515, 0.926571713811, 0.927521701059, 0.927468561656, 0.927998554333, 0.927945695605, 0.929008220067, 0.928746371941, 0.928693770351, 0.928641091039, 0.929607013105, 0.929554832769, 0.930039996532, 0.93101417799, 0.931554211882, 0.932636161324, 0.932585903271, 0.932585903271, 0.93357188521, 0.933522156167, 0.933967924145, 0.933769185329, 0.934766776762, 0.935267583538, 0.935169629185, 0.935672412756, 0.936176553451, 0.936176553451, 0.93779194569, 0.937554472402, 0.937458974653, 0.937411116161, 0.937970225775, 0.938435668089, 0.938341043455, 0.938341043455, 0.938903099624, 0.93885608225, 0.938808992455, 0.938714594933, 0.939278948765, 0.940409694612, 0.940363611919, 0.940363611919, 0.940884673949, 0.940838860114, 0.940700991551, 0.941179107659, 0.941750185868, 0.941750185868, 0.942276966885, 0.943290568826, 0.943822114749, 0.944267645451, 0.944223792272, 0.944223792272, 0.944223792272, 0.944223792272, 0.944135878551, 0.944091817682, 0.943959217069, 0.944948988041, 0.944817531021, 0.945185418124, 0.945774534438, 0.946869842865, 0.94678443912, 0.947292782482, 0.947803406812, 0.948955745704, 0.949513262437, 0.949431324505, 0.949349120177, 0.949787213059, 0.950350748429, 0.951522477849, 0.952051228023, 0.95197239226, 0.951813940452, 0.951734321829, 0.952189098377, 0.952726227521, 0.952647494583, 0.953226869405, 0.953148724357, 0.95303101596, 0.953497250008, 0.954122169792, 0.954006075021, 0.954594998037, 0.955778170341, 0.955740668477, 0.957457733339, 0.958697023242, 0.958590781777, 0.958519649968, 0.959665182275, 0.960242079268, 0.960242079268, 0.960855701368, 0.960787753107)+cms.vdouble(0.961370655681, 0.961269567079, 0.961823203605, 0.963730727425, 0.963634885553, 0.963570709071, 0.964138473298, 0.964106695414, 0.96404297039, 0.963914839098, 0.963882663464, 0.96452094996, 0.964361812095, 0.96497328025, 0.965587812399, 0.966174859102, 0.966052013818, 0.966021162949, 0.968018795469, 0.96867865254, 0.968592547647, 0.96914294659, 0.969057430126, 0.969000155331, 0.970289180287, 0.971618144708, 0.971511684075, 0.972907637123, 0.972856607143, 0.972753968298, 0.972676478315, 0.973344727784, 0.973217439385, 0.973917083716, 0.973842007934, 0.973791716846, 0.974496912029, 0.974447701286, 0.974373528048, 0.974273957942, 0.974198771106, 0.974791150217, 0.975488253999, 0.976165676348, 0.977513433798, 0.977332925695, 0.978053351441, 0.978734902423, 0.97864854949, 0.979275680612, 0.979190505138, 0.979039751165, 0.978974471583, 0.978886796984, 0.980438334358, 0.981887328142, 0.982567303114, 0.983312443593, 0.983168209088, 0.983021459539, 0.98366063828, 0.983606342672, 0.983441268961, 0.983291720735, 0.985747459607, 0.985615866821, 0.988157949486, 0.988031989052, 0.987786602856, 0.988507380959, 0.988364321833, 0.988127868612, 0.987928555371, 0.987641272072, 0.987408197679, 0.98704162283, 0.986691071046, 0.986360943929, 0.987048151948, 0.989952686544, 0.991766844123, 0.992193166195, 0.99456966538, 0.995655052048, 0.994746673755, 0.993062299865, 0.995491593707, 0.993997811711, 0.991951166261, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
                min = cms.double(-0.998333333333)
            ),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            transform = cms.PSet(
                max = cms.double(1.99833333333),
                transform = (cms.vdouble(0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277)+cms.vdouble(0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320785409267, 0.320785409267, 0.320785409267, 0.320967688479, 0.32115017496, 0.32115017496, 0.32115017496, 0.32115017496, 0.321332869066, 0.321607300294, 0.321790515012, 0.322065728828, 0.322709728783, 0.337811096719, 0.33917314626, 0.341489359417, 0.343051156809, 0.344690580804, 0.34605531485, 0.347729452006, 0.349352972192, 0.351698761571, 0.354076266303, 0.356364861761, 0.357459291064, 0.358806090169, 0.360659074159, 0.361655179522, 0.363285639001, 0.363823848893, 0.365224296488, 0.366635567078, 0.368317558281, 0.36949108301, 0.370409007364, 0.370997606343, 0.372726361337, 0.373488515297, 0.374412657806, 0.375752608537, 0.377534910678, 0.378625338634, 0.379181030815, 0.379877944035, 0.382266731549, 0.382549741971, 0.383828491978, 0.38525242259, 0.386835650852, 0.38785063627, 0.389317222671, 0.390498501728, 0.392134514369, 0.392433445129, 0.393938724972, 0.395003106909, 0.395165758646, 0.395929379967, 0.396695958257, 0.397011143016, 0.398247378442, 0.399356983741, 0.399994683207, 0.401254354869, 0.40236309389, 0.403477977186, 0.404278112546, 0.405403648355, 0.406718341929, 0.408044942586, 0.409053791836, 0.409879342767, 0.410568240656, 0.411067477386, 0.412572498902, 0.413612340683, 0.414628216181, 0.41718987191, 0.417878334739, 0.41856907358, 0.419300644011, 0.420520753157, 0.420777117228, 0.422716149289, 0.423248081689, 0.424315972822, 0.425568676714, 0.426697968924, 0.427784748237, 0.428512348538, 0.429242428143, 0.430526071506, 0.4311350135, 0.432803583714, 0.433609675616, 0.434608917639, 0.436308891919, 0.436878509184, 0.437640316502, 0.438596319943, 0.440520911858, 0.441683795845, 0.443048277506, 0.444696219849, 0.446478472767, 0.44715804854, 0.448645092811, 0.450058431683, 0.450666877959, 0.450755388115, 0.451660727674, 0.452685605028, 0.453508861839, 0.455164391331, 0.456611329026, 0.456920461171, 0.457863702358, 0.45902581005, 0.459451411686, 0.460410936031, 0.461808077134, 0.4630001435, 0.46452516501, 0.465632370863, 0.466972634942, 0.467639712811, 0.468206417853, 0.469000443277, 0.470125946746, 0.471938031657, 0.473437184975, 0.474815974144, 0.475643583896, 0.477037107394, 0.478345116523, 0.479756398109, 0.482127131145, 0.483321305722, 0.484827612962, 0.485378450947, 0.486839313932, 0.488800865348, 0.488631796262, 0.489784626283, 0.49019813266, 0.490696455307, 0.492699918902, 0.493707798202, 0.495481544763, 0.497780890453, 0.499067549901, 0.499842743245, 0.501067711008, 0.501110885208, 0.503739653301, 0.504533670387, 0.507669169039, 0.508207246665, 0.510099534144, 0.511125093239, 0.513041788431, 0.514972912765, 0.517927881794, 0.519848789077, 0.52116702462, 0.522598588906, 0.524038039421, 0.524905522273, 0.525729939569, 0.527349110611, 0.528189103375, 0.529884063982, 0.531038635091, 0.531258876588, 0.533372518417, 0.532652261497, 0.533222445036, 0.533832435241, 0.534714171593, 0.536561182549, 0.536184284139, 0.538295230995, 0.539204274194, 0.539743792118, 0.542257448251, 0.543191981222, 0.54415669717, 0.545124845911, 0.546421082543, 0.548704392123, 0.551006864138, 0.551639517385, 0.554308295208, 0.554286639155, 0.555277851271, 0.557294734318, 0.558661984326, 0.560735788966, 0.561777981725, 0.56352691872, 0.56493793563, 0.567793486879, 0.568888208725, 0.57034433091, 0.570356276084, 0.572191934216, 0.573659294894, 0.574044772549, 0.575543527534, 0.577054482298, 0.578553389267, 0.580816407199, 0.582777514902, 0.58546601664, 0.587013469943, 0.586699955875, 0.587164603914, 0.589909772096, 0.590347109603, 0.591182964289, 0.593622213241, 0.595632610766, 0.596088895792)+cms.vdouble(0.596547219627, 0.597007595967, 0.59905000376, 0.59875479532, 0.600402032492, 0.601476624751, 0.602375325225, 0.604611692334, 0.606308877758, 0.609454442616, 0.612487831768, 0.615198564485, 0.616345932738, 0.617679752716, 0.620364786891, 0.621560433387, 0.622923085077, 0.622771613804, 0.627021967049, 0.629464905691, 0.630636176618, 0.632414811477, 0.635412621765, 0.636860801036, 0.638359784998, 0.642296739762, 0.64372019874, 0.646732193739, 0.649419880322, 0.653004922396, 0.654536589972, 0.657493324695, 0.65872664624, 0.662116021475, 0.666837437051, 0.668332370106, 0.670194812833, 0.671514734427, 0.671514734427, 0.672844093862, 0.672352092845, 0.678607302272, 0.681605563269, 0.681020472505, 0.682082800049, 0.684848783291, 0.686959317553, 0.690918830645, 0.691984674993, 0.694695530605, 0.697455651971, 0.700496795416, 0.703736816672, 0.704917801757, 0.706220722464, 0.707858889942, 0.71018130526, 0.714321429016, 0.720425948473, 0.724503155871, 0.727977004139, 0.730714468803, 0.735012362904, 0.739735756402, 0.750660954162, 0.757799352464, 0.760515374245, 0.768004247792, 0.77935327172, 0.784646260495, 0.789164336822, 0.791123170072, 0.795276817521, 0.804299018936, 0.819103217408, 0.822961151625, 0.833298258018, 0.842807182616, 0.85334688934, 0.86724344838, 0.872176831791, 0.87195156781, 0.87843961359, 0.891494313173, 0.912879175226, 0.924218217451, 0.937234161591, 0.94206607914, 0.958884557005, 0.959595443343, 0.93904371889, 0.927733482302, 0.93386870405, 0.916051159827, 0.943467586229, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
                min = cms.double(-0.998333333333)
            ),
            nCharged = cms.uint32(1)
        )),
    toTransform = cms.InputTag("hpsTancTausDiscriminationByTancRaw"),
    PFTauProducer = cms.InputTag("hpsTancTaus")
)


process.hpsTancTausDiscriminationByTancLoose = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        tancCut = cms.PSet(
            cut = cms.double(0.95),
            Producer = cms.InputTag("hpsTancTausDiscriminationByTanc")
        )
    ),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.hpsTancTausDiscriminationByTancMedium = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        tancCut = cms.PSet(
            cut = cms.double(0.97),
            Producer = cms.InputTag("hpsTancTausDiscriminationByTanc")
        )
    ),
    UseOnlyChargedHadrons = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsTancTaus")
)


process.hpsTancTausDiscriminationByTancRaw = cms.EDProducer("RecoTauMVADiscriminator",
    discriminantOptions = cms.PSet(
        BinnedMaskedHcalIsolation = cms.PSet(
            vtxSource = cms.InputTag("recoTauPileUpVertices"),
            mask = cms.PSet(
                finalHcalCone = cms.double(0.08),
                ecalCone = cms.double(0.15),
                hcalCone = cms.double(0.3),
                maxSigmas = cms.double(2)
            ),
            binning = cms.VPSet(cms.PSet(
                binLowEdges = cms.vdouble(1.0, 1.79, 4.03),
                nPUVtx = cms.int32(0)
            ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(1.15, 1.8, 4.03),
                    nPUVtx = cms.int32(1)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(1.22, 1.81, 4.03),
                    nPUVtx = cms.int32(2)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(1.27, 1.83, 4.03),
                    nPUVtx = cms.int32(3)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(1.31, 1.84, 4.03),
                    nPUVtx = cms.int32(4)
                )),
            defaultBinning = cms.vdouble(1.31, 1.84, 4.03),
            plugin = cms.string('RecoTauDiscriminationBinnedMaskedHCALIsolation')
        ),
        InvariantOpeningAngle = cms.PSet(
            defaultRMS = cms.string('max(0.3/max(pt, 1.0), 0.005)'),
            plugin = cms.string('RecoTauDiscriminantInvariantWidth'),
            decayModes = cms.VPSet(cms.PSet(
                nPiZeros = cms.uint32(1),
                rms = cms.string('2.7e-3 + 0.23/max(pt, 1.0)'),
                nCharged = cms.uint32(1),
                mean = cms.string('5.0e-3 + 0.43/max(pt, 1.0)')
            ), 
                cms.PSet(
                    nPiZeros = cms.uint32(2),
                    rms = cms.string('7.5e-3 + 0.3/max(pt, 1.0)'),
                    nCharged = cms.uint32(1),
                    mean = cms.string('4.7e-3 + 0.9/max(pt, 1.0)')
                ), 
                cms.PSet(
                    nPiZeros = cms.uint32(0),
                    rms = cms.string('0.38/max(pt, 1.0)'),
                    nCharged = cms.uint32(3),
                    mean = cms.string('0.87/max(pt, 1.0)')
                )),
            defaultMean = cms.string('max(0.87/max(pt, 1.0), 0.005)')
        ),
        BinnedMaskedEcalIsolation = cms.PSet(
            vtxSource = cms.InputTag("recoTauPileUpVertices"),
            mask = cms.PSet(
                finalHcalCone = cms.double(0.08),
                ecalCone = cms.double(0.15),
                hcalCone = cms.double(0.3),
                maxSigmas = cms.double(2)
            ),
            binning = cms.VPSet(cms.PSet(
                binLowEdges = cms.vdouble(0.5, 0.85, 1.84),
                nPUVtx = cms.int32(0)
            ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.63, 0.91, 1.84),
                    nPUVtx = cms.int32(1)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.7, 0.96, 1.85),
                    nPUVtx = cms.int32(2)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.75, 0.99, 1.85),
                    nPUVtx = cms.int32(3)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.79, 1.02, 1.86),
                    nPUVtx = cms.int32(4)
                )),
            defaultBinning = cms.vdouble(0.79, 1.02, 1.86),
            plugin = cms.string('RecoTauDiscriminationBinnedMaskedECALIsolation')
        ),
        FlightPathSignificance = cms.PSet(
            discSrc = cms.InputTag("hpsTancTausDiscriminationByFlightPath"),
            plugin = cms.string('RecoTauDiscriminantFromDiscriminator')
        ),
        BinnedTrackIsolation = cms.PSet(
            vtxSource = cms.InputTag("recoTauPileUpVertices"),
            binning = cms.VPSet(cms.PSet(
                binLowEdges = cms.vdouble(0.5, 0.86, 1.87),
                nPUVtx = cms.int32(0)
            ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.51, 0.86, 1.87),
                    nPUVtx = cms.int32(1)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.51, 0.86, 1.87),
                    nPUVtx = cms.int32(2)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.52, 0.86, 1.87),
                    nPUVtx = cms.int32(3)
                ), 
                cms.PSet(
                    binLowEdges = cms.vdouble(0.52, 0.86, 1.87),
                    nPUVtx = cms.int32(4)
                )),
            defaultBinning = cms.vdouble(0.52, 0.86, 1.87),
            plugin = cms.string('RecoTauDiscriminationBinnedTrackIsolation')
        )
    ),
    mvas = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        mvaLabel = cms.string('1prong0pi0'),
        nCharged = cms.uint32(1)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            mvaLabel = cms.string('1prong1pi0'),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            mvaLabel = cms.string('1prong2pi0'),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            mvaLabel = cms.string('3prong0pi0'),
            nCharged = cms.uint32(3)
        )),
    remapOutput = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    Prediscriminants = cms.PSet(
        hpsSelect = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection")
        ),
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByLeadingPionPtCut")
        )
    ),
    dbLabel = cms.string('hpstanc')
)


process.hpsTancTausDiscriminationByTancTight = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        tancCut = cms.PSet(
            cut = cms.double(0.985),
            Producer = cms.InputTag("hpsTancTausDiscriminationByTanc")
        )
    ),
    UseOnlyChargedHadrons = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsTancTaus")
)


process.hpsTancTausDiscriminationByTancVLoose = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        tancCut = cms.PSet(
            cut = cms.double(0.9),
            Producer = cms.InputTag("hpsTancTausDiscriminationByTanc")
        )
    ),
    UseOnlyChargedHadrons = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsTancTaus")
)


process.hpsTancTausDiscriminationByTightElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(-0.1),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    ApplyCut_BremCombined = cms.bool(True),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(True),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.hpsTancTausDiscriminationByTightIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsTancTausDiscriminationByTightMuonRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon",
    a = cms.double(0.5),
    c = cms.double(0.0),
    b = cms.double(0.5),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    discriminatorOption = cms.string('noAllArbitrated')
)


process.hpsTancTausDiscriminationByVLooseIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("hpsTancTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.3),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(2.0),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsTightIsolationCleaner = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("combinatoricRecoTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.hpsVLooseIsolationCleaner = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("combinatoricRecoTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.3),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(2.0),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.ic5PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5),
    jets = cms.InputTag("iterativeCone5PFJets")
)


process.impactParameterMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('impactParameterMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.impactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeGhostTrack = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.impactParameterTagInfosAK5PF = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("jetTracksAssociatorAtVertexAK5PF"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.impactParameterTagInfosAK7Calo = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("jetTracksAssociatorAtVertexAK7Calo"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.impactParameterTagInfosAK7PF = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("jetTracksAssociatorAtVertexAK7PF"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.impactParameterTagInfosAOD = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("jetTracksAssociatorAtVertex"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.impactParameterTagInfosCACalo = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("jetTracksAssociatorAtVertexCACalo"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.impactParameterTagInfosCAPF = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("jetTracksAssociatorAtVertexCAPF"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.impactParameterTagInfossubCAPF = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("jetTracksAssociatorAtVertexsubCAPF"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.inclusiveMergedVertices = cms.EDProducer("VertexMerger",
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("inclusiveVertices"),
    maxFraction = cms.double(0.2)
)


process.inclusiveVertexFinder = cms.EDProducer("InclusiveVertexFinder",
    seedMin3DIPValue = cms.double(0.005),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterMaxDistance = cms.double(0.05),
    minHits = cms.uint32(8),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinAngleCosine = cms.double(0.98),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    seedMin3DIPSignificance = cms.double(1.5),
    clusterScale = cms.double(1.0),
    vertexReco = cms.PSet(
        seccut = cms.double(3),
        primcut = cms.double(1.0),
        finder = cms.string('avr'),
        smoothing = cms.bool(True)
    ),
    clusterMaxSignificance = cms.double(3.0),
    vertexMinDLenSig = cms.double(0.5),
    clusterMinAngleCosine = cms.double(0.5),
    maxNTracks = cms.uint32(30),
    minPt = cms.double(0.8)
)


process.inclusiveVertices = cms.EDProducer("TrackVertexArbitrator",
    dLenFraction = cms.double(0.333),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    distCut = cms.double(0.04),
    secondaryVertices = cms.InputTag("vertexMerger"),
    dRCut = cms.double(0.4),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    sigCut = cms.double(5)
)


process.isoDepElectronWithCharged = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.isoDepElectronWithNeutral = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.isoDepElectronWithPhotons = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.isoDepMuonWithCharged = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedMuons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.isoDepMuonWithNeutral = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedMuons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.isoDepMuonWithPhotons = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedMuons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.isoDeposits = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag(""),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag(""),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.isoValElectronWithCharged = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("isoDepElectronWithCharged"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring(),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.isoValElectronWithNeutral = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("isoDepElectronWithNeutral"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.isoValElectronWithPhotons = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("isoDepElectronWithPhotons"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.isoValMuonWithCharged = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("isoDepMuonWithCharged"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring(),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.isoValMuonWithNeutral = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("isoDepMuonWithNeutral"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.isoValMuonWithPhotons = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("isoDepMuonWithPhotons"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.iterativeCone3HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('IterativeCone'),
    rParam = cms.double(0.3)
)


process.iterativeCone4HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('IterativeCone'),
    rParam = cms.double(0.4)
)


process.iterativeCone5GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('IterativeCone'),
    rParam = cms.double(0.5)
)


process.iterativeCone5GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('IterativeCone'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.iterativeCone5GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('IterativeCone'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.iterativeCone5HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('IterativeCone'),
    rParam = cms.double(0.5)
)


process.iterativeCone7HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('IterativeCone'),
    rParam = cms.double(0.7)
)


process.jetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.jetBProbabilityBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5PF"))
)


process.jetBProbabilityBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7Calo"))
)


process.jetBProbabilityBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7PF"))
)


process.jetBProbabilityBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"))
)


process.jetBProbabilityBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCACalo"))
)


process.jetBProbabilityBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCAPF"))
)


process.jetBProbabilityBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfossubCAPF"))
)


process.jetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.jetProbabilityBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5PF"))
)


process.jetProbabilityBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7Calo"))
)


process.jetProbabilityBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7PF"))
)


process.jetProbabilityBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"))
)


process.jetProbabilityBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCACalo"))
)


process.jetProbabilityBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCAPF"))
)


process.jetProbabilityBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfossubCAPF"))
)


process.jetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("ak5CaloJets"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.jetTracksAssociatorAtVertexAK5PF = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("ak5PFJets"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.jetTracksAssociatorAtVertexAK7Calo = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("ak7CaloJets"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.jetTracksAssociatorAtVertexAK7PF = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("ak7PFJets"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.jetTracksAssociatorAtVertexCACalo = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("caTopCaloJets"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.jetTracksAssociatorAtVertexCAPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("caTopPFJets"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.jetTracksAssociatorAtVertexsubCAPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("CAsubJetsProducer"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.kt3HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('Kt'),
    rParam = cms.double(0.3)
)


process.kt4GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('Kt'),
    rParam = cms.double(0.4)
)


process.kt4GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('Kt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.4),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.kt4GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('Kt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.4),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.kt4HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('Kt'),
    rParam = cms.double(0.4)
)


process.kt4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doOutputJets = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    voronoiRfact = cms.double(-0.9),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    src = cms.InputTag("particleFlow"),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    doAreaDiskApprox = cms.bool(False),
    inputEMin = cms.double(0.0),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('Kt'),
    rParam = cms.double(0.4)
)


process.kt6GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('Kt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJets"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.kt6GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('Kt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.kt6GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('Kt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.kt6HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("hiGenParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('Kt'),
    rParam = cms.double(0.6)
)


process.kt6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doAreaFastjet = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    doRhoFastjet = cms.bool(True),
    jetAlgorithm = cms.string('Kt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("particleFlow"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.kt6PFJets25 = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doAreaFastjet = cms.bool(False),
    voronoiRfact = cms.double(-0.9),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(2.5),
    doRhoFastjet = cms.bool(True),
    jetAlgorithm = cms.string('Kt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(2.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("pfNoElectron"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.metJESCorAK5CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('ak5CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('ak5CaloL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(1.8),
    UscaleC = cms.double(-0.06)
)


process.metJESCorAK5CaloJetMuons = cms.EDProducer("MuonMET",
    muonMETDepositValueMapInputTag = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    metTypeInputTag = cms.InputTag("CaloMET"),
    muonsInputTag = cms.InputTag("muons"),
    uncorMETInputTag = cms.InputTag("metJESCorAK5CaloJet")
)


process.metJESCorAK5PFJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('ak5PFJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('PFMET'),
    jetPTthreshold = cms.double(1.0),
    inputUncorMetLabel = cms.string('pfMet'),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('ak5PFL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(1.8),
    UscaleC = cms.double(-0.06)
)


process.metJESCorAK7CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('ak7CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('ak7CaloL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(1.8),
    UscaleC = cms.double(-0.06)
)


process.metJESCorIC5CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('iterativeCone5CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('ic5CaloL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(1.8),
    UscaleC = cms.double(-0.06)
)


process.metJESCorKT4CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('kt4CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('kt4CaloL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(1.8),
    UscaleC = cms.double(-0.06)
)


process.metJESCorKT6CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('kt6CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('kt6CaloL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(1.8),
    UscaleC = cms.double(-0.06)
)


process.metJESCorSC5CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('sisCone5CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('sisCone5CaloL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(1.8),
    UscaleC = cms.double(-0.06)
)


process.metJESCorSC7CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('sisCone7CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('sisCone7CaloL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(1.8),
    UscaleC = cms.double(-0.06)
)


process.muPFIsoDepositCharged = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedMuons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoDepositChargedAll = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedMuons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedCandidates"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoDepositGamma = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedMuons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoDepositNeutral = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedMuons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoDepositPU = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfSelectedMuons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(99999.99),
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPUChargedCandidates"),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string('')
    )
)


process.muPFIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositCharged"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositCharged"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositGamma"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositGamma"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositNeutral"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositNeutral"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositPU"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muPFIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("muPFIsoDepositPU"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.muonMETValueMapProducer = cms.EDProducer("MuonMETValueMapProducer",
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(False),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(False),
        useCalo = cms.bool(True),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(False)
    ),
    beamSpotInputTag = cms.InputTag("offlineBeamSpot"),
    minPt = cms.double(10.0),
    maxNormChi2 = cms.double(10.0),
    minnValidStaHits = cms.int32(1),
    useHO = cms.bool(False),
    minnHits = cms.int32(11),
    useTrackAssociatorPositions = cms.bool(True),
    useRecHits = cms.bool(False),
    maxEta = cms.double(2.5),
    maxd0 = cms.double(0.2),
    towerEtThreshold = cms.double(0.3),
    isAlsoTkMu = cms.bool(True),
    muonInputTag = cms.InputTag("muons")
)


process.muonMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("pfIsolatedMuons"),
    maxDPtRel = cms.double(0.5),
    mcPdgId = cms.vint32(13),
    mcStatus = cms.vint32(1),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.5),
    checkCharge = cms.bool(True),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    embedHighLevelSelection = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    electronSource = cms.InputTag("gsfElectrons"),
    resolutions = cms.PSet(

    ),
    userIsolation = cms.PSet(

    ),
    embedSuperCluster = cms.bool(True),
    linkToPFSource = cms.InputTag(""),
    embedPFCandidate = cms.bool(True),
    pfElectronSource = cms.InputTag("pfIsolatedElectrons"),
    addElectronID = cms.bool(True),
    efficiencies = cms.PSet(

    ),
    embedGsfTrack = cms.bool(True),
    useParticleFlow = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    embedTrack = cms.bool(False),
    addEfficiencies = cms.bool(False),
    usePV = cms.bool(True),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    electronIDSources = cms.PSet(
        eidVBTFRel85 = cms.InputTag("eidVBTFRel85"),
        eidVBTFRel80 = cms.InputTag("eidVBTFRel80"),
        eidVBTFCom70 = cms.InputTag("eidVBTFCom70"),
        eidVBTFRel70 = cms.InputTag("eidVBTFRel70"),
        eidVBTFCom95 = cms.InputTag("eidVBTFCom95"),
        eidVBTFCom85 = cms.InputTag("eidVBTFCom85"),
        eidVBTFCom80 = cms.InputTag("eidVBTFCom80"),
        eidVBTFRel95 = cms.InputTag("eidVBTFRel95")
    ),
    genParticleMatch = cms.InputTag(""),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    isoDeposits = cms.PSet(
        pfNeutralHadrons = cms.InputTag("elePFIsoDepositNeutral"),
        pfChargedHadrons = cms.InputTag("elePFIsoDepositCharged"),
        pfPhotons = cms.InputTag("elePFIsoDepositGamma"),
        pfAllParticles = cms.InputTag("elePFIsoDepositChargedAll")
    ),
    embedGenMatch = cms.bool(False),
    isolationValues = cms.PSet(
        pfNeutralHadrons = cms.InputTag("elePFIsoValueNeutral04"),
        pfChargedHadrons = cms.InputTag("elePFIsoValueCharged04"),
        user = cms.VInputTag(cms.InputTag("elePFIsoValueChargedAll03"), cms.InputTag("elePFIsoValueCharged03"), cms.InputTag("elePFIsoValueNeutral03"), cms.InputTag("elePFIsoValueGamma03"), cms.InputTag("elePFIsoValuePU03"), 
            cms.InputTag("elePFIsoValuePU04")),
        pfPhotons = cms.InputTag("elePFIsoValueGamma04"),
        pfAllParticles = cms.InputTag("elePFIsoValueChargedAll04")
    )
)


process.patHemispheres = cms.EDProducer("PATHemisphereProducer",
    patJets = cms.InputTag("cleanLayer1Jets"),
    maxTauEta = cms.double(-1),
    maxPhotonEta = cms.double(5),
    minMuonEt = cms.double(7),
    patMuons = cms.InputTag("cleanLayer1Muons"),
    seedMethod = cms.int32(3),
    patElectrons = cms.InputTag("cleanLayer1Electrons"),
    patMets = cms.InputTag("layer1METs"),
    maxMuonEta = cms.double(5),
    minTauEt = cms.double(1000000),
    minPhotonEt = cms.double(200000),
    minElectronEt = cms.double(7),
    patPhotons = cms.InputTag("cleanLayer1Photons"),
    combinationMethod = cms.int32(3),
    maxJetEta = cms.double(5),
    maxElectronEta = cms.double(5),
    minJetEt = cms.double(30),
    patTaus = cms.InputTag("cleanLayer1Taus")
)


process.patJetCharge = cms.EDProducer("JetChargeProducer",
    var = cms.string('Pt'),
    src = cms.InputTag("jetTracksAssociatorAtVertex"),
    exp = cms.double(1.0)
)


process.patJetChargeAK5PF = cms.EDProducer("JetChargeProducer",
    var = cms.string('Pt'),
    src = cms.InputTag("jetTracksAssociatorAtVertexAK5PF"),
    exp = cms.double(1.0)
)


process.patJetChargeAK7Calo = cms.EDProducer("JetChargeProducer",
    var = cms.string('Pt'),
    src = cms.InputTag("jetTracksAssociatorAtVertexAK7Calo"),
    exp = cms.double(1.0)
)


process.patJetChargeAK7PF = cms.EDProducer("JetChargeProducer",
    var = cms.string('Pt'),
    src = cms.InputTag("jetTracksAssociatorAtVertexAK7PF"),
    exp = cms.double(1.0)
)


process.patJetChargeCACalo = cms.EDProducer("JetChargeProducer",
    var = cms.string('Pt'),
    src = cms.InputTag("jetTracksAssociatorAtVertexCACalo"),
    exp = cms.double(1.0)
)


process.patJetChargeCAPF = cms.EDProducer("JetChargeProducer",
    var = cms.string('Pt'),
    src = cms.InputTag("jetTracksAssociatorAtVertexCAPF"),
    exp = cms.double(1.0)
)


process.patJetChargesubCAPF = cms.EDProducer("JetChargeProducer",
    var = cms.string('Pt'),
    src = cms.InputTag("jetTracksAssociatorAtVertexsubCAPF"),
    exp = cms.double(1.0)
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    src = cms.InputTag("ak5CaloJets"),
    emf = cms.bool(False),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    useNPV = cms.bool(True),
    rho = cms.InputTag("kt6PFJets","rho"),
    useRho = cms.bool(True),
    payload = cms.string('AK5Calo'),
    flavorType = cms.string('J')
)


process.patJetCorrFactorsAK5PF = cms.EDProducer("JetCorrFactorsProducer",
    src = cms.InputTag("ak5PFJets"),
    emf = cms.bool(False),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    useNPV = cms.bool(True),
    rho = cms.InputTag("kt6PFJets","rho"),
    useRho = cms.bool(True),
    payload = cms.string('AK5PFchs'),
    flavorType = cms.string('J')
)


process.patJetCorrFactorsAK7Calo = cms.EDProducer("JetCorrFactorsProducer",
    src = cms.InputTag("ak7CaloJets"),
    emf = cms.bool(False),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    useNPV = cms.bool(True),
    rho = cms.InputTag("kt6PFJets","rho"),
    useRho = cms.bool(True),
    payload = cms.string('AK7Calo'),
    flavorType = cms.string('J')
)


process.patJetCorrFactorsAK7PF = cms.EDProducer("JetCorrFactorsProducer",
    src = cms.InputTag("ak7PFJets"),
    emf = cms.bool(False),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    useNPV = cms.bool(True),
    rho = cms.InputTag("kt6PFJets","rho"),
    useRho = cms.bool(True),
    payload = cms.string('AK7PF'),
    flavorType = cms.string('J')
)


process.patJetCorrFactorsCACalo = cms.EDProducer("JetCorrFactorsProducer",
    src = cms.InputTag("caTopCaloJets"),
    emf = cms.bool(False),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    useNPV = cms.bool(True),
    rho = cms.InputTag("kt6PFJets","rho"),
    useRho = cms.bool(True),
    payload = cms.string('AK7Calo'),
    flavorType = cms.string('J')
)


process.patJetCorrFactorsCAPF = cms.EDProducer("JetCorrFactorsProducer",
    src = cms.InputTag("caTopPFJets"),
    emf = cms.bool(False),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    useNPV = cms.bool(True),
    rho = cms.InputTag("kt6PFJets","rho"),
    useRho = cms.bool(True),
    payload = cms.string('AK7PF'),
    flavorType = cms.string('J')
)


process.patJetCorrFactorssubCAPF = cms.EDProducer("JetCorrFactorsProducer",
    src = cms.InputTag("CAsubJetsProducer"),
    emf = cms.bool(False),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    useNPV = cms.bool(True),
    rho = cms.InputTag("kt6PFJets","rho"),
    useRho = cms.bool(True),
    payload = cms.string('KT4PF'),
    flavorType = cms.string('J')
)


process.patJetFlavourAssociation = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("patJetPartonAssociation"),
    physicsDefinition = cms.bool(False)
)


process.patJetFlavourAssociationAK5PF = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("patJetPartonAssociationAK5PF"),
    physicsDefinition = cms.bool(False)
)


process.patJetFlavourAssociationAK7Calo = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("patJetPartonAssociationAK7Calo"),
    physicsDefinition = cms.bool(False)
)


process.patJetFlavourAssociationAK7PF = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("patJetPartonAssociationAK7PF"),
    physicsDefinition = cms.bool(False)
)


process.patJetFlavourAssociationCACalo = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("patJetPartonAssociationCACalo"),
    physicsDefinition = cms.bool(False)
)


process.patJetFlavourAssociationCAPF = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("patJetPartonAssociationCAPF"),
    physicsDefinition = cms.bool(False)
)


process.patJetFlavourAssociationsubCAPF = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("patJetPartonAssociationsubCAPF"),
    physicsDefinition = cms.bool(False)
)


process.patJetGenJetMatch = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("ak5CaloJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("ak5GenJets")
)


process.patJetGenJetMatchAK5PF = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("ak5PFJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("ak5GenJets")
)


process.patJetGenJetMatchAK7Calo = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("ak7CaloJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("ak5GenJets")
)


process.patJetGenJetMatchAK7PF = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("ak7PFJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("ak5GenJets")
)


process.patJetGenJetMatchCACalo = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("caTopCaloJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("ak5GenJets")
)


process.patJetGenJetMatchCAPF = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("caTopPFJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("ak5GenJets")
)


process.patJetGenJetMatchsubCAPF = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("CAsubJetsProducer"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("ak5GenJets")
)


process.patJetPartonAssociation = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("ak5CaloJets"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("patJetPartons")
)


process.patJetPartonAssociationAK5PF = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("ak5PFJets"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("patJetPartons")
)


process.patJetPartonAssociationAK7Calo = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("ak7CaloJets"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("patJetPartons")
)


process.patJetPartonAssociationAK7PF = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("ak7PFJets"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("patJetPartons")
)


process.patJetPartonAssociationCACalo = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("caTopCaloJets"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("patJetPartons")
)


process.patJetPartonAssociationCAPF = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("caTopPFJets"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("patJetPartons")
)


process.patJetPartonAssociationsubCAPF = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("CAsubJetsProducer"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("patJetPartons")
)


process.patJetPartonMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("ak5CaloJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patJetPartonMatchAK5PF = cms.EDProducer("MCMatcher",
    src = cms.InputTag("ak5PFJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patJetPartonMatchAK7Calo = cms.EDProducer("MCMatcher",
    src = cms.InputTag("ak7CaloJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patJetPartonMatchAK7PF = cms.EDProducer("MCMatcher",
    src = cms.InputTag("ak7PFJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patJetPartonMatchCACalo = cms.EDProducer("MCMatcher",
    src = cms.InputTag("caTopCaloJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patJetPartonMatchCAPF = cms.EDProducer("MCMatcher",
    src = cms.InputTag("caTopPFJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patJetPartonMatchsubCAPF = cms.EDProducer("MCMatcher",
    src = cms.InputTag("CAsubJetsProducer"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patJetPartons = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)


process.patJets = cms.EDProducer("PATJetProducer",
    addJetCharge = cms.bool(True),
    addGenJetMatch = cms.bool(False),
    embedPFCandidates = cms.bool(True),
    embedGenJetMatch = cms.bool(True),
    addAssociatedTracks = cms.bool(True),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    addGenPartonMatch = cms.bool(False),
    JetPartonMapSource = cms.InputTag(""),
    resolutions = cms.PSet(

    ),
    genPartonMatch = cms.InputTag(""),
    addTagInfos = cms.bool(True),
    addPartonJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag(""),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    jetSource = cms.InputTag("ak5CaloJets"),
    addEfficiencies = cms.bool(False),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactors")),
    trackAssociationSource = cms.InputTag("jetTracksAssociatorAtVertex"),
    tagInfoSources = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"), cms.InputTag("secondaryVertexTagInfosAOD"), cms.InputTag("softMuonTagInfosAOD")),
    discriminatorSources = cms.VInputTag(cms.InputTag("jetBProbabilityBJetTagsAOD"), cms.InputTag("jetProbabilityBJetTagsAOD"), cms.InputTag("trackCountingHighPurBJetTagsAOD"), cms.InputTag("trackCountingHighEffBJetTagsAOD"), cms.InputTag("simpleSecondaryVertexHighEffBJetTagsAOD"), 
        cms.InputTag("simpleSecondaryVertexHighPurBJetTagsAOD"), cms.InputTag("combinedSecondaryVertexBJetTagsAOD"), cms.InputTag("combinedSecondaryVertexMVABJetTagsAOD"), cms.InputTag("softMuonBJetTagsAOD"), cms.InputTag("softMuonByPtBJetTagsAOD"), 
        cms.InputTag("softMuonByIP3dBJetTagsAOD")),
    addBTagInfo = cms.bool(True),
    embedCaloTowers = cms.bool(False),
    addResolutions = cms.bool(False),
    getJetMCFlavour = cms.bool(False),
    addDiscriminators = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    addJetCorrFactors = cms.bool(True),
    jetIDMap = cms.InputTag("AK5JetID"),
    addJetID = cms.bool(False)
)


process.patJetsAK5PF = cms.EDProducer("PATJetProducer",
    addJetCharge = cms.bool(True),
    addGenJetMatch = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    addGenPartonMatch = cms.bool(False),
    JetPartonMapSource = cms.InputTag("AK5PF"),
    resolutions = cms.PSet(

    ),
    genPartonMatch = cms.InputTag("AK5PF"),
    addTagInfos = cms.bool(True),
    addPartonJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag("AK5PF"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    jetSource = cms.InputTag("ak5PFJets"),
    addEfficiencies = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("jetBProbabilityBJetTagsAK5PF"), cms.InputTag("jetProbabilityBJetTagsAK5PF"), cms.InputTag("trackCountingHighPurBJetTagsAK5PF"), cms.InputTag("trackCountingHighEffBJetTagsAK5PF"), cms.InputTag("simpleSecondaryVertexHighEffBJetTagsAK5PF"), 
        cms.InputTag("simpleSecondaryVertexHighPurBJetTagsAK5PF"), cms.InputTag("combinedSecondaryVertexBJetTagsAK5PF"), cms.InputTag("combinedSecondaryVertexMVABJetTagsAK5PF"), cms.InputTag("softMuonBJetTagsAK5PF"), cms.InputTag("softMuonByPtBJetTagsAK5PF"), 
        cms.InputTag("softMuonByIP3dBJetTagsAK5PF")),
    trackAssociationSource = cms.InputTag("jetTracksAssociatorAtVertexAK5PF"),
    tagInfoSources = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5PF"), cms.InputTag("secondaryVertexTagInfosAK5PF"), cms.InputTag("softMuonTagInfosAK5PF")),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK5PF")),
    embedPFCandidates = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addResolutions = cms.bool(False),
    getJetMCFlavour = cms.bool(False),
    addDiscriminators = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetChargeAK5PF"),
    embedCaloTowers = cms.bool(False),
    jetIDMap = cms.InputTag("AK5JetID"),
    addJetID = cms.bool(False)
)


process.patJetsAK7Calo = cms.EDProducer("PATJetProducer",
    addJetCharge = cms.bool(True),
    addGenJetMatch = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    addGenPartonMatch = cms.bool(False),
    JetPartonMapSource = cms.InputTag("AK7Calo"),
    resolutions = cms.PSet(

    ),
    genPartonMatch = cms.InputTag("AK7Calo"),
    addTagInfos = cms.bool(True),
    addPartonJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag("AK7Calo"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    jetSource = cms.InputTag("ak7CaloJets"),
    addEfficiencies = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("jetBProbabilityBJetTagsAK7Calo"), cms.InputTag("jetProbabilityBJetTagsAK7Calo"), cms.InputTag("trackCountingHighPurBJetTagsAK7Calo"), cms.InputTag("trackCountingHighEffBJetTagsAK7Calo"), cms.InputTag("simpleSecondaryVertexHighEffBJetTagsAK7Calo"), 
        cms.InputTag("simpleSecondaryVertexHighPurBJetTagsAK7Calo"), cms.InputTag("combinedSecondaryVertexBJetTagsAK7Calo"), cms.InputTag("combinedSecondaryVertexMVABJetTagsAK7Calo"), cms.InputTag("softMuonBJetTagsAK7Calo"), cms.InputTag("softMuonByPtBJetTagsAK7Calo"), 
        cms.InputTag("softMuonByIP3dBJetTagsAK7Calo")),
    trackAssociationSource = cms.InputTag("jetTracksAssociatorAtVertexAK7Calo"),
    tagInfoSources = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7Calo"), cms.InputTag("secondaryVertexTagInfosAK7Calo"), cms.InputTag("softMuonTagInfosAK7Calo")),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK7Calo")),
    embedPFCandidates = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addResolutions = cms.bool(False),
    getJetMCFlavour = cms.bool(False),
    addDiscriminators = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetChargeAK7Calo"),
    embedCaloTowers = cms.bool(False),
    jetIDMap = cms.InputTag("AK5JetID"),
    addJetID = cms.bool(False)
)


process.patJetsAK7PF = cms.EDProducer("PATJetProducer",
    addJetCharge = cms.bool(True),
    addGenJetMatch = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    addGenPartonMatch = cms.bool(False),
    JetPartonMapSource = cms.InputTag("AK7PF"),
    resolutions = cms.PSet(

    ),
    genPartonMatch = cms.InputTag("AK7PF"),
    addTagInfos = cms.bool(True),
    addPartonJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag("AK7PF"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    jetSource = cms.InputTag("ak7PFJets"),
    addEfficiencies = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("jetBProbabilityBJetTagsAK7PF"), cms.InputTag("jetProbabilityBJetTagsAK7PF"), cms.InputTag("trackCountingHighPurBJetTagsAK7PF"), cms.InputTag("trackCountingHighEffBJetTagsAK7PF"), cms.InputTag("simpleSecondaryVertexHighEffBJetTagsAK7PF"), 
        cms.InputTag("simpleSecondaryVertexHighPurBJetTagsAK7PF"), cms.InputTag("combinedSecondaryVertexBJetTagsAK7PF"), cms.InputTag("combinedSecondaryVertexMVABJetTagsAK7PF"), cms.InputTag("softMuonBJetTagsAK7PF"), cms.InputTag("softMuonByPtBJetTagsAK7PF"), 
        cms.InputTag("softMuonByIP3dBJetTagsAK7PF")),
    trackAssociationSource = cms.InputTag("jetTracksAssociatorAtVertexAK7PF"),
    tagInfoSources = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7PF"), cms.InputTag("secondaryVertexTagInfosAK7PF"), cms.InputTag("softMuonTagInfosAK7PF")),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK7PF")),
    embedPFCandidates = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addResolutions = cms.bool(False),
    getJetMCFlavour = cms.bool(False),
    addDiscriminators = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetChargeAK7PF"),
    embedCaloTowers = cms.bool(False),
    jetIDMap = cms.InputTag("AK5JetID"),
    addJetID = cms.bool(False)
)


process.patJetsCACalo = cms.EDProducer("PATJetProducer",
    addJetCharge = cms.bool(True),
    addGenJetMatch = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    addGenPartonMatch = cms.bool(False),
    JetPartonMapSource = cms.InputTag("CACalo"),
    resolutions = cms.PSet(

    ),
    genPartonMatch = cms.InputTag("CACalo"),
    addTagInfos = cms.bool(True),
    addPartonJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag("CACalo"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    jetSource = cms.InputTag("caTopCaloJets"),
    addEfficiencies = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("jetBProbabilityBJetTagsCACalo"), cms.InputTag("jetProbabilityBJetTagsCACalo"), cms.InputTag("trackCountingHighPurBJetTagsCACalo"), cms.InputTag("trackCountingHighEffBJetTagsCACalo"), cms.InputTag("simpleSecondaryVertexHighEffBJetTagsCACalo"), 
        cms.InputTag("simpleSecondaryVertexHighPurBJetTagsCACalo"), cms.InputTag("combinedSecondaryVertexBJetTagsCACalo"), cms.InputTag("combinedSecondaryVertexMVABJetTagsCACalo"), cms.InputTag("softMuonBJetTagsCACalo"), cms.InputTag("softMuonByPtBJetTagsCACalo"), 
        cms.InputTag("softMuonByIP3dBJetTagsCACalo")),
    trackAssociationSource = cms.InputTag("jetTracksAssociatorAtVertexCACalo"),
    tagInfoSources = cms.VInputTag(cms.InputTag("impactParameterTagInfosCACalo"), cms.InputTag("secondaryVertexTagInfosCACalo"), cms.InputTag("softMuonTagInfosCACalo")),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsCACalo")),
    embedPFCandidates = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addResolutions = cms.bool(False),
    getJetMCFlavour = cms.bool(False),
    addDiscriminators = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetChargeCACalo"),
    embedCaloTowers = cms.bool(False),
    jetIDMap = cms.InputTag("AK5JetID"),
    addJetID = cms.bool(False)
)


process.patJetsCAPF = cms.EDProducer("PATJetProducer",
    addJetCharge = cms.bool(True),
    addGenJetMatch = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    addGenPartonMatch = cms.bool(False),
    JetPartonMapSource = cms.InputTag("CAPF"),
    resolutions = cms.PSet(

    ),
    genPartonMatch = cms.InputTag("CAPF"),
    addTagInfos = cms.bool(True),
    addPartonJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag("CAPF"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    jetSource = cms.InputTag("caTopPFJets"),
    addEfficiencies = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("jetBProbabilityBJetTagsCAPF"), cms.InputTag("jetProbabilityBJetTagsCAPF"), cms.InputTag("trackCountingHighPurBJetTagsCAPF"), cms.InputTag("trackCountingHighEffBJetTagsCAPF"), cms.InputTag("simpleSecondaryVertexHighEffBJetTagsCAPF"), 
        cms.InputTag("simpleSecondaryVertexHighPurBJetTagsCAPF"), cms.InputTag("combinedSecondaryVertexBJetTagsCAPF"), cms.InputTag("combinedSecondaryVertexMVABJetTagsCAPF"), cms.InputTag("softMuonBJetTagsCAPF"), cms.InputTag("softMuonByPtBJetTagsCAPF"), 
        cms.InputTag("softMuonByIP3dBJetTagsCAPF")),
    trackAssociationSource = cms.InputTag("jetTracksAssociatorAtVertexCAPF"),
    tagInfoSources = cms.VInputTag(cms.InputTag("impactParameterTagInfosCAPF"), cms.InputTag("secondaryVertexTagInfosCAPF"), cms.InputTag("softMuonTagInfosCAPF")),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsCAPF")),
    embedPFCandidates = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addResolutions = cms.bool(False),
    getJetMCFlavour = cms.bool(False),
    addDiscriminators = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetChargeCAPF"),
    embedCaloTowers = cms.bool(False),
    jetIDMap = cms.InputTag("AK5JetID"),
    addJetID = cms.bool(False)
)


process.patJetssubCAPF = cms.EDProducer("PATJetProducer",
    addJetCharge = cms.bool(True),
    addGenJetMatch = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    addGenPartonMatch = cms.bool(False),
    JetPartonMapSource = cms.InputTag("subCAPF"),
    resolutions = cms.PSet(

    ),
    genPartonMatch = cms.InputTag("subCAPF"),
    addTagInfos = cms.bool(True),
    addPartonJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag("subCAPF"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    jetSource = cms.InputTag("CAsubJetsProducer"),
    addEfficiencies = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("jetBProbabilityBJetTagssubCAPF"), cms.InputTag("jetProbabilityBJetTagssubCAPF"), cms.InputTag("trackCountingHighPurBJetTagssubCAPF"), cms.InputTag("trackCountingHighEffBJetTagssubCAPF"), cms.InputTag("simpleSecondaryVertexHighEffBJetTagssubCAPF"), 
        cms.InputTag("simpleSecondaryVertexHighPurBJetTagssubCAPF"), cms.InputTag("combinedSecondaryVertexBJetTagssubCAPF"), cms.InputTag("combinedSecondaryVertexMVABJetTagssubCAPF"), cms.InputTag("softMuonBJetTagssubCAPF"), cms.InputTag("softMuonByPtBJetTagssubCAPF"), 
        cms.InputTag("softMuonByIP3dBJetTagssubCAPF")),
    trackAssociationSource = cms.InputTag("jetTracksAssociatorAtVertexsubCAPF"),
    tagInfoSources = cms.VInputTag(cms.InputTag("impactParameterTagInfossubCAPF"), cms.InputTag("secondaryVertexTagInfossubCAPF"), cms.InputTag("softMuonTagInfossubCAPF")),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorssubCAPF")),
    embedPFCandidates = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addResolutions = cms.bool(False),
    getJetMCFlavour = cms.bool(False),
    addDiscriminators = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetChargesubCAPF"),
    embedCaloTowers = cms.bool(False),
    jetIDMap = cms.InputTag("AK5JetID"),
    addJetID = cms.bool(False)
)


process.patMETs = cms.EDProducer("PATMETProducer",
    metSource = cms.InputTag("pfMET"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addResolutions = cms.bool(False),
    addEfficiencies = cms.bool(False),
    genMETSource = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    muonSource = cms.InputTag("muons"),
    resolutions = cms.PSet(

    )
)


process.patMETsHT = cms.EDProducer("MHTProducer",
    JetCollection = cms.InputTag("patJetsAK5PF"),
    MaxJetEta = cms.double(5),
    MinJetPt = cms.double(30)
)


process.patMETsPF = cms.EDProducer("PATMETProducer",
    metSource = cms.InputTag("pfMet"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addResolutions = cms.bool(False),
    muonSource = cms.InputTag("muons"),
    addEfficiencies = cms.bool(False),
    genMETSource = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    resolutions = cms.PSet(

    )
)


process.patMETsTC = cms.EDProducer("PATMETProducer",
    metSource = cms.InputTag("tcMet"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addResolutions = cms.bool(False),
    muonSource = cms.InputTag("muons"),
    addEfficiencies = cms.bool(False),
    genMETSource = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    resolutions = cms.PSet(

    )
)


process.patMHTs = cms.EDProducer("PATMHTProducer",
    verbose = cms.double(0.0),
    muonEtaMax = cms.double(2.5),
    jetTag = cms.untracked.InputTag("allLayer1Jets"),
    eleEtaMax = cms.double(3.0),
    noHF = cms.bool(False),
    muonTag = cms.untracked.InputTag("allLayer1Muons"),
    CaloTowerTag = cms.InputTag("towerMaker"),
    elePhiUncertaintyParameter0 = cms.double(0.01),
    uncertaintyScaleFactor = cms.double(1.0),
    muonPtMin = cms.double(10.0),
    eleEtUncertaintyParameter0 = cms.double(0.01),
    useHO = cms.bool(False),
    jetEtUncertaintyParameter2 = cms.double(0.033),
    jetEtUncertaintyParameter1 = cms.double(1.25),
    jetEMfracMax = cms.double(0.9),
    jetPhiUncertaintyParameter2 = cms.double(0.023),
    jetPhiUncertaintyParameter0 = cms.double(4.75),
    jetPhiUncertaintyParameter1 = cms.double(-0.426),
    tauTag = cms.untracked.InputTag("allLayer1Taus"),
    jetEtUncertaintyParameter0 = cms.double(5.6),
    electronTag = cms.untracked.InputTag("allLayer1Electrons"),
    jetEtaMax = cms.double(5.0),
    elePtMin = cms.double(10.0),
    jetPtMin = cms.double(20.0),
    muonEtUncertaintyParameter0 = cms.double(0.01),
    photonTag = cms.untracked.InputTag("allLayer1Photons"),
    muonPhiUncertaintyParameter0 = cms.double(0.01),
    controlledUncertainty = cms.bool(True),
    towerEtThreshold = cms.double(0.5)
)


process.patMuons = cms.EDProducer("PATMuonProducer",
    embedTpfmsMuon = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedCaloMETMuonCorrs = cms.bool(True),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    resolutions = cms.PSet(

    ),
    userIsolation = cms.PSet(

    ),
    linkToPFSource = cms.InputTag(""),
    embedPFCandidate = cms.bool(True),
    pfMuonSource = cms.InputTag("pfIsolatedMuons"),
    efficiencies = cms.PSet(

    ),
    embedStandAloneMuon = cms.bool(True),
    useParticleFlow = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    embedTrack = cms.bool(False),
    addEfficiencies = cms.bool(False),
    usePV = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(True),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    addTeVRefits = cms.bool(True),
    embedCombinedMuon = cms.bool(True),
    genParticleMatch = cms.InputTag(""),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    muonSource = cms.InputTag("muons"),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    tpfmsSrc = cms.InputTag("tevMuons","firstHit"),
    pickySrc = cms.InputTag("tevMuons","picky"),
    isoDeposits = cms.PSet(
        pfNeutralHadrons = cms.InputTag("muPFIsoDepositNeutral"),
        pfChargedHadrons = cms.InputTag("muPFIsoDepositCharged"),
        pfPhotons = cms.InputTag("muPFIsoDepositGamma"),
        pfAllParticles = cms.InputTag("muPFIsoDepositChargedAll")
    ),
    embedGenMatch = cms.bool(False),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    embedPickyMuon = cms.bool(True),
    isolationValues = cms.PSet(
        pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04"),
        pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04"),
        user = cms.VInputTag(cms.InputTag("muPFIsoValueChargedAll03"), cms.InputTag("muPFIsoValueCharged03"), cms.InputTag("muPFIsoValueNeutral03"), cms.InputTag("muPFIsoValueGamma03"), cms.InputTag("muPFIsoValuePU03"), 
            cms.InputTag("muPFIsoValuePU04")),
        pfPhotons = cms.InputTag("muPFIsoValueGamma04"),
        pfAllParticles = cms.InputTag("muPFIsoValueChargedAll04")
    )
)


process.patPFParticles = cms.EDProducer("PATPFParticleProducer",
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addEfficiencies = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenMatch = cms.bool(False),
    pfCandidateSource = cms.InputTag("pfNoJet"),
    resolutions = cms.PSet(

    ),
    genParticleMatch = cms.InputTag("")
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addEfficiencies = cms.bool(False),
    photonIDSources = cms.PSet(
        PhotonCutBasedIDTight = cms.InputTag("PhotonIDProd","PhotonCutBasedIDTight"),
        PhotonCutBasedIDLoose = cms.InputTag("PhotonIDProd","PhotonCutBasedIDLoose")
    ),
    isoDeposits = cms.PSet(

    ),
    efficiencies = cms.PSet(

    ),
    embedSuperCluster = cms.bool(True),
    embedGenMatch = cms.bool(False),
    resolutions = cms.PSet(

    ),
    addPhotonID = cms.bool(True),
    photonSource = cms.InputTag("photons"),
    userIsolation = cms.PSet(

    ),
    genParticleMatch = cms.InputTag("")
)


process.patTaus = cms.EDProducer("PATTauProducer",
    tauIDSources = cms.PSet(
        leadingTrackFinding = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding"),
        leadingTrackPtCut = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackPtCut"),
        trackIsolation = cms.InputTag("shrinkingConePFTauDiscriminationByTrackIsolation"),
        ecalIsolation = cms.InputTag("shrinkingConePFTauDiscriminationByECALIsolation"),
        byIsolation = cms.InputTag("shrinkingConePFTauDiscriminationByIsolation"),
        againstElectron = cms.InputTag("shrinkingConePFTauDiscriminationAgainstElectron"),
        againstMuon = cms.InputTag("shrinkingConePFTauDiscriminationAgainstMuon"),
        leadingPionPtCut = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingPionPtCut"),
        trackIsolationUsingLeadingPion = cms.InputTag("shrinkingConePFTauDiscriminationByTrackIsolationUsingLeadingPion"),
        ecalIsolationUsingLeadingPion = cms.InputTag("shrinkingConePFTauDiscriminationByECALIsolationUsingLeadingPion"),
        byIsolationUsingLeadingPion = cms.InputTag("shrinkingConePFTauDiscriminationByIsolationUsingLeadingPion"),
        byTaNC = cms.InputTag("shrinkingConePFTauDiscriminationByTaNC"),
        byTaNCfrOnePercent = cms.InputTag("shrinkingConePFTauDiscriminationByTaNCfrOnePercent"),
        byTaNCfrHalfPercent = cms.InputTag("shrinkingConePFTauDiscriminationByTaNCfrHalfPercent"),
        byTaNCfrQuarterPercent = cms.InputTag("shrinkingConePFTauDiscriminationByTaNCfrQuarterPercent"),
        byTaNCfrTenthPercent = cms.InputTag("shrinkingConePFTauDiscriminationByTaNCfrTenthPercent")
    ),
    addGenJetMatch = cms.bool(False),
    embedGenJetMatch = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    resolutions = cms.PSet(

    ),
    userIsolation = cms.PSet(
        pfAllParticles = cms.PSet(
            threshold = cms.double(0.0),
            src = cms.InputTag("tauIsoDepositPFCandidates"),
            deltaR = cms.double(0.5)
        ),
        pfNeutralHadron = cms.PSet(
            threshold = cms.double(0.0),
            src = cms.InputTag("tauIsoDepositPFNeutralHadrons"),
            deltaR = cms.double(0.5)
        ),
        pfChargedHadron = cms.PSet(
            threshold = cms.double(0.0),
            src = cms.InputTag("tauIsoDepositPFChargedHadrons"),
            deltaR = cms.double(0.5)
        ),
        pfGamma = cms.PSet(
            threshold = cms.double(0.0),
            src = cms.InputTag("tauIsoDepositPFGammas"),
            deltaR = cms.double(0.5)
        )
    ),
    embedIsolationPFGammaCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag(""),
    embedIsolationPFCands = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    embedSignalPFCands = cms.bool(False),
    addEfficiencies = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    tauSource = cms.InputTag("pfTaus"),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    addTauID = cms.bool(True),
    genParticleMatch = cms.InputTag(""),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    isoDeposits = cms.PSet(
        pfAllParticles = cms.InputTag("tauIsoDepositPFCandidates"),
        pfNeutralHadron = cms.InputTag("tauIsoDepositPFNeutralHadrons"),
        pfChargedHadron = cms.InputTag("tauIsoDepositPFChargedHadrons"),
        pfGamma = cms.InputTag("tauIsoDepositPFGammas")
    ),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedGenMatch = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False)
)


process.patTrigger = cms.EDProducer("PATTriggerProducer",
    processName = cms.string('HLT'),
    onlyStandAlone = cms.bool(False)
)


process.patTriggerEvent = cms.EDProducer("PATTriggerEventProducer",
    patTriggerMatches = cms.VInputTag(),
    processName = cms.string('HLT'),
    patTriggerProducer = cms.InputTag("patTrigger")
)


process.pfJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5),
    jets = cms.InputTag("pfJets")
)


process.pfJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doAreaFastjet = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("pfNoElectron"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.pfJetsLegacyHPSPiZeros = cms.EDProducer("RecoTauPiZeroProducer",
    massHypothesis = cms.double(0.136),
    ranking = cms.VPSet(cms.PSet(
        selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
        selection = cms.string('algoIs("kStrips")'),
        name = cms.string('InStrip'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selectionFailValue = cms.double(1000)
    )),
    jetRegionSrc = cms.InputTag("pfTauPFJets08Region"),
    outputSelection = cms.string('pt > 0'),
    jetSrc = cms.InputTag("pfJets"),
    builders = cms.VPSet(cms.PSet(
        name = cms.string('s'),
        stripPhiAssociationDistance = cms.double(0.2),
        plugin = cms.string('RecoTauPiZeroStripPlugin'),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        makeCombinatoricStrips = cms.bool(False),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        stripEtaAssociationDistance = cms.double(0.05),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices")
    ))
)


process.pfJetsLegacyTaNCPiZeros = cms.EDProducer("RecoTauPiZeroProducer",
    massHypothesis = cms.double(0.136),
    ranking = cms.VPSet(cms.PSet(
        selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
        selection = cms.string('mass() < 0.2'),
        name = cms.string('PFTDM'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selectionFailValue = cms.double(1000)
    )),
    jetRegionSrc = cms.InputTag("pfTauPFJets08Region"),
    outputSelection = cms.string('pt > 1.5'),
    jetSrc = cms.InputTag("pfJets"),
    builders = cms.VPSet(cms.PSet(
        plugin = cms.string('RecoTauPiZeroTrivialPlugin'),
        name = cms.string('1'),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ), 
        cms.PSet(
            maxMass = cms.double(-1.0),
            plugin = cms.string('RecoTauPiZeroCombinatoricPlugin'),
            minMass = cms.double(0.0),
            qualityCuts = cms.PSet(
                minTrackHits = cms.uint32(3),
                minTrackPt = cms.double(0.5),
                maxTrackChi2 = cms.double(100.0),
                minTrackPixelHits = cms.uint32(0),
                minGammaEt = cms.double(0.5),
                useTracksInsteadOfPFHadrons = cms.bool(False),
                maxDeltaZ = cms.double(0.2),
                maxTransverseImpactParameter = cms.double(0.03)
            ),
            choose = cms.uint32(2),
            maxInputGammas = cms.uint32(10),
            name = cms.string('2')
        ))
)


process.pfJetsPiZeros = cms.EDProducer("RecoTauPiZeroProducer",
    massHypothesis = cms.double(0.136),
    ranking = cms.VPSet(cms.PSet(
        selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
        selection = cms.string('abs(eta()) < 1.5 & abs(mass() - 0.13579) < 0.05'),
        name = cms.string('nearPiZeroMass'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selectionFailValue = cms.double(1000)
    ), 
        cms.PSet(
            selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
            selection = cms.string('abs(eta()) > 1.5 & mass() < 0.2'),
            name = cms.string('nearPiZeroMass'),
            plugin = cms.string('RecoTauPiZeroStringQuality'),
            selectionFailValue = cms.double(1000)
        ), 
        cms.PSet(
            selectionPassFunction = cms.string('abs(mass() - 0.13579)'),
            selection = cms.string('algoIs("kStrips")'),
            name = cms.string('InStrip'),
            plugin = cms.string('RecoTauPiZeroStringQuality'),
            selectionFailValue = cms.double(1000)
        )),
    jetRegionSrc = cms.InputTag("pfTauPFJets08Region"),
    outputSelection = cms.string('pt > 1.5'),
    jetSrc = cms.InputTag("pfJets"),
    builders = cms.VPSet(cms.PSet(
        maxMass = cms.double(-1.0),
        plugin = cms.string('RecoTauPiZeroCombinatoricPlugin'),
        minMass = cms.double(0.0),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        choose = cms.uint32(2),
        maxInputGammas = cms.uint32(10),
        name = cms.string('2')
    ), 
        cms.PSet(
            name = cms.string('s'),
            stripPhiAssociationDistance = cms.double(0.2),
            plugin = cms.string('RecoTauPiZeroStripPlugin'),
            qualityCuts = cms.PSet(
                minTrackHits = cms.uint32(3),
                minTrackPt = cms.double(0.5),
                maxTrackChi2 = cms.double(100.0),
                minTrackPixelHits = cms.uint32(0),
                minGammaEt = cms.double(0.5),
                useTracksInsteadOfPFHadrons = cms.bool(False),
                maxDeltaZ = cms.double(0.2),
                maxTransverseImpactParameter = cms.double(0.03)
            ),
            makeCombinatoricStrips = cms.bool(False),
            stripCandidatesParticleIds = cms.vint32(2, 4),
            stripEtaAssociationDistance = cms.double(0.05),
            primaryVertexSrc = cms.InputTag("offlinePrimaryVertices")
        ))
)


process.pfMET = cms.EDProducer("METProducer",
    HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
    EE_PhiResPar = cms.vdouble(0.02511),
    jdphi3 = cms.vdouble(0.042, 0.043, 0.044, 0.043, 0.041, 
        0.039, 0.039, 0.036, 0.034, 0.031),
    jdpt9 = cms.vdouble(0.843, 0.885, 1.245, 1.665, 1.944, 
        1.981, 1.972, 2.875, 3.923, 7.51),
    jdpt8 = cms.vdouble(0.889, 0.939, 1.166, 1.365, 1.553, 
        1.805, 2.06, 2.22, 2.268, 2.247),
    jdpt7 = cms.vdouble(1.094, 1.139, 1.436, 1.672, 1.831, 
        2.05, 2.267, 2.549, 2.785, 2.86),
    jdpt6 = cms.vdouble(1.213, 1.298, 1.716, 2.015, 2.191, 
        2.612, 2.863, 2.879, 2.925, 2.902),
    jdpt5 = cms.vdouble(1.049, 1.149, 1.607, 1.869, 2.012, 
        2.219, 2.289, 2.412, 2.695, 2.865),
    jdpt4 = cms.vdouble(0.85, 0.961, 1.337, 1.593, 1.854, 
        2.005, 2.209, 2.533, 2.812, 3.047),
    jdpt3 = cms.vdouble(0.929, 1.04, 1.46, 1.74, 2.042, 
        2.289, 2.639, 2.837, 2.946, 2.971),
    jdpt2 = cms.vdouble(0.841, 0.937, 1.316, 1.605, 1.919, 
        2.295, 2.562, 2.722, 2.943, 3.293),
    jdpt1 = cms.vdouble(0.718, 0.813, 1.133, 1.384, 1.588, 
        1.841, 2.115, 2.379, 2.508, 2.772),
    jdpt0 = cms.vdouble(0.749, 0.829, 1.099, 1.355, 1.584, 
        1.807, 2.035, 2.217, 2.378, 2.591),
    HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
    alias = cms.string('pfMET'),
    HF_PhiResPar = cms.vdouble(0.05022),
    PF_PhiResType7 = cms.vdouble(0.02511),
    HE_PhiResPar = cms.vdouble(0.02511),
    EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    noHF = cms.bool(False),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_PhiResType3 = cms.vdouble(0.002),
    HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
    resolutionsEra = cms.string('Spring10'),
    PF_PhiResType6 = cms.vdouble(0.02511),
    InputType = cms.string('PFCandidateCollection'),
    PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
    PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
    ptresolthreshold = cms.double(10.0),
    METType = cms.string('PFMET'),
    HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
    EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    jdphi8 = cms.vdouble(0.059, 0.057, 0.051, 0.044, 0.038, 
        0.035, 0.037, 0.032, 0.028, 0.028),
    globalThreshold = cms.double(0.0),
    jets = cms.InputTag("pfJets"),
    EB_PhiResPar = cms.vdouble(0.00502),
    src = cms.InputTag("particleFlow"),
    jdphi9 = cms.vdouble(0.062, 0.059, 0.053, 0.047, 0.042, 
        0.045, 0.036, 0.032, 0.034, 0.044),
    resolutionsAlgo = cms.string('AK5PF'),
    jdphi4 = cms.vdouble(0.042, 0.042, 0.043, 0.042, 0.038, 
        0.036, 0.036, 0.033, 0.031, 0.031),
    HO_PhiResPar = cms.vdouble(0.02511),
    jdphi2 = cms.vdouble(0.04, 0.04, 0.04, 0.04, 0.04, 
        0.038, 0.036, 0.035, 0.034, 0.033),
    jdphi1 = cms.vdouble(0.034, 0.035, 0.035, 0.035, 0.035, 
        0.034, 0.031, 0.03, 0.029, 0.027),
    jdphi0 = cms.vdouble(0.034, 0.034, 0.034, 0.034, 0.032, 
        0.031, 0.028, 0.027, 0.027, 0.027),
    jdphi7 = cms.vdouble(0.077, 0.072, 0.059, 0.05, 0.045, 
        0.042, 0.039, 0.039, 0.037, 0.031),
    jdphi6 = cms.vdouble(0.084, 0.08, 0.072, 0.065, 0.066, 
        0.06, 0.051, 0.049, 0.045, 0.045),
    jdphi5 = cms.vdouble(0.069, 0.069, 0.064, 0.058, 0.053, 
        0.049, 0.049, 0.043, 0.039, 0.04),
    HB_PhiResPar = cms.vdouble(0.02511),
    PF_PhiResType1 = cms.vdouble(0.002),
    PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
    PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
    PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
    PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
    PF_EtResType1 = cms.vdouble(0.05, 0, 0),
    calculateSignificance = cms.bool(True),
    PF_EtResType3 = cms.vdouble(0.05, 0, 0),
    PF_EtResType2 = cms.vdouble(0.05, 0, 0)
)


process.pfMETNoPU = cms.EDProducer("METProducer",
    resolutionsEra = cms.string('Spring10'),
    PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
    HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
    jdphi6 = cms.vdouble(0.084, 0.08, 0.072, 0.065, 0.066, 
        0.06, 0.051, 0.049, 0.045, 0.045),
    jdphi3 = cms.vdouble(0.042, 0.043, 0.044, 0.043, 0.041, 
        0.039, 0.039, 0.036, 0.034, 0.031),
    jdpt9 = cms.vdouble(0.843, 0.885, 1.245, 1.665, 1.944, 
        1.981, 1.972, 2.875, 3.923, 7.51),
    jdpt8 = cms.vdouble(0.889, 0.939, 1.166, 1.365, 1.553, 
        1.805, 2.06, 2.22, 2.268, 2.247),
    jdpt7 = cms.vdouble(1.094, 1.139, 1.436, 1.672, 1.831, 
        2.05, 2.267, 2.549, 2.785, 2.86),
    jdpt6 = cms.vdouble(1.213, 1.298, 1.716, 2.015, 2.191, 
        2.612, 2.863, 2.879, 2.925, 2.902),
    jdpt5 = cms.vdouble(1.049, 1.149, 1.607, 1.869, 2.012, 
        2.219, 2.289, 2.412, 2.695, 2.865),
    jdpt4 = cms.vdouble(0.85, 0.961, 1.337, 1.593, 1.854, 
        2.005, 2.209, 2.533, 2.812, 3.047),
    jdpt3 = cms.vdouble(0.929, 1.04, 1.46, 1.74, 2.042, 
        2.289, 2.639, 2.837, 2.946, 2.971),
    jdpt2 = cms.vdouble(0.841, 0.937, 1.316, 1.605, 1.919, 
        2.295, 2.562, 2.722, 2.943, 3.293),
    EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    jdpt0 = cms.vdouble(0.749, 0.829, 1.099, 1.355, 1.584, 
        1.807, 2.035, 2.217, 2.378, 2.591),
    HF_PhiResPar = cms.vdouble(0.05022),
    InputType = cms.string('PFCandidateCollection'),
    HE_PhiResPar = cms.vdouble(0.02511),
    jdpt1 = cms.vdouble(0.718, 0.813, 1.133, 1.384, 1.588, 
        1.841, 2.115, 2.379, 2.508, 2.772),
    noHF = cms.bool(False),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_PhiResType3 = cms.vdouble(0.002),
    HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
    resolutionsAlgo = cms.string('AK5PF'),
    PF_PhiResType6 = cms.vdouble(0.02511),
    HB_PhiResPar = cms.vdouble(0.02511),
    PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
    PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
    ptresolthreshold = cms.double(10.0),
    METType = cms.string('PFMET'),
    HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
    EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    PF_PhiResType1 = cms.vdouble(0.002),
    PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
    jets = cms.InputTag("pfJets"),
    EB_PhiResPar = cms.vdouble(0.00502),
    src = cms.InputTag("pfNoPileUp"),
    jdphi9 = cms.vdouble(0.062, 0.059, 0.053, 0.047, 0.042, 
        0.045, 0.036, 0.032, 0.034, 0.044),
    jdphi8 = cms.vdouble(0.059, 0.057, 0.051, 0.044, 0.038, 
        0.035, 0.037, 0.032, 0.028, 0.028),
    jdphi4 = cms.vdouble(0.042, 0.042, 0.043, 0.042, 0.038, 
        0.036, 0.036, 0.033, 0.031, 0.031),
    HO_PhiResPar = cms.vdouble(0.02511),
    jdphi2 = cms.vdouble(0.04, 0.04, 0.04, 0.04, 0.04, 
        0.038, 0.036, 0.035, 0.034, 0.033),
    jdphi1 = cms.vdouble(0.034, 0.035, 0.035, 0.035, 0.035, 
        0.034, 0.031, 0.03, 0.029, 0.027),
    jdphi0 = cms.vdouble(0.034, 0.034, 0.034, 0.034, 0.032, 
        0.031, 0.028, 0.027, 0.027, 0.027),
    jdphi7 = cms.vdouble(0.077, 0.072, 0.059, 0.05, 0.045, 
        0.042, 0.039, 0.039, 0.037, 0.031),
    EE_PhiResPar = cms.vdouble(0.02511),
    jdphi5 = cms.vdouble(0.069, 0.069, 0.064, 0.058, 0.053, 
        0.049, 0.049, 0.043, 0.039, 0.04),
    PF_PhiResType7 = cms.vdouble(0.02511),
    alias = cms.string('pfMET'),
    PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
    globalThreshold = cms.double(0.0),
    PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
    HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
    PF_EtResType1 = cms.vdouble(0.05, 0, 0),
    calculateSignificance = cms.bool(True),
    PF_EtResType3 = cms.vdouble(0.05, 0, 0),
    PF_EtResType2 = cms.vdouble(0.05, 0, 0)
)


process.pfMETNoPUCharge = cms.EDProducer("METProducer",
    resolutionsEra = cms.string('Spring10'),
    PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
    HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
    jdphi6 = cms.vdouble(0.084, 0.08, 0.072, 0.065, 0.066, 
        0.06, 0.051, 0.049, 0.045, 0.045),
    jdphi3 = cms.vdouble(0.042, 0.043, 0.044, 0.043, 0.041, 
        0.039, 0.039, 0.036, 0.034, 0.031),
    jdpt9 = cms.vdouble(0.843, 0.885, 1.245, 1.665, 1.944, 
        1.981, 1.972, 2.875, 3.923, 7.51),
    jdpt8 = cms.vdouble(0.889, 0.939, 1.166, 1.365, 1.553, 
        1.805, 2.06, 2.22, 2.268, 2.247),
    jdpt7 = cms.vdouble(1.094, 1.139, 1.436, 1.672, 1.831, 
        2.05, 2.267, 2.549, 2.785, 2.86),
    jdpt6 = cms.vdouble(1.213, 1.298, 1.716, 2.015, 2.191, 
        2.612, 2.863, 2.879, 2.925, 2.902),
    jdpt5 = cms.vdouble(1.049, 1.149, 1.607, 1.869, 2.012, 
        2.219, 2.289, 2.412, 2.695, 2.865),
    jdpt4 = cms.vdouble(0.85, 0.961, 1.337, 1.593, 1.854, 
        2.005, 2.209, 2.533, 2.812, 3.047),
    jdpt3 = cms.vdouble(0.929, 1.04, 1.46, 1.74, 2.042, 
        2.289, 2.639, 2.837, 2.946, 2.971),
    jdpt2 = cms.vdouble(0.841, 0.937, 1.316, 1.605, 1.919, 
        2.295, 2.562, 2.722, 2.943, 3.293),
    EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    jdpt0 = cms.vdouble(0.749, 0.829, 1.099, 1.355, 1.584, 
        1.807, 2.035, 2.217, 2.378, 2.591),
    HF_PhiResPar = cms.vdouble(0.05022),
    InputType = cms.string('PFCandidateCollection'),
    HE_PhiResPar = cms.vdouble(0.02511),
    jdpt1 = cms.vdouble(0.718, 0.813, 1.133, 1.384, 1.588, 
        1.841, 2.115, 2.379, 2.508, 2.772),
    noHF = cms.bool(False),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_PhiResType3 = cms.vdouble(0.002),
    HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
    resolutionsAlgo = cms.string('AK5PF'),
    PF_PhiResType6 = cms.vdouble(0.02511),
    HB_PhiResPar = cms.vdouble(0.02511),
    PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
    PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
    ptresolthreshold = cms.double(10.0),
    METType = cms.string('PFMET'),
    HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
    EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    PF_PhiResType1 = cms.vdouble(0.002),
    PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
    jets = cms.InputTag("pfJets"),
    EB_PhiResPar = cms.vdouble(0.00502),
    src = cms.InputTag("pfNoPileUpCharge"),
    jdphi9 = cms.vdouble(0.062, 0.059, 0.053, 0.047, 0.042, 
        0.045, 0.036, 0.032, 0.034, 0.044),
    jdphi8 = cms.vdouble(0.059, 0.057, 0.051, 0.044, 0.038, 
        0.035, 0.037, 0.032, 0.028, 0.028),
    jdphi4 = cms.vdouble(0.042, 0.042, 0.043, 0.042, 0.038, 
        0.036, 0.036, 0.033, 0.031, 0.031),
    HO_PhiResPar = cms.vdouble(0.02511),
    jdphi2 = cms.vdouble(0.04, 0.04, 0.04, 0.04, 0.04, 
        0.038, 0.036, 0.035, 0.034, 0.033),
    jdphi1 = cms.vdouble(0.034, 0.035, 0.035, 0.035, 0.035, 
        0.034, 0.031, 0.03, 0.029, 0.027),
    jdphi0 = cms.vdouble(0.034, 0.034, 0.034, 0.034, 0.032, 
        0.031, 0.028, 0.027, 0.027, 0.027),
    jdphi7 = cms.vdouble(0.077, 0.072, 0.059, 0.05, 0.045, 
        0.042, 0.039, 0.039, 0.037, 0.031),
    EE_PhiResPar = cms.vdouble(0.02511),
    jdphi5 = cms.vdouble(0.069, 0.069, 0.064, 0.058, 0.053, 
        0.049, 0.049, 0.043, 0.039, 0.04),
    PF_PhiResType7 = cms.vdouble(0.02511),
    alias = cms.string('pfMET'),
    PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
    globalThreshold = cms.double(0.0),
    PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
    HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
    PF_EtResType1 = cms.vdouble(0.05, 0, 0),
    calculateSignificance = cms.bool(True),
    PF_EtResType3 = cms.vdouble(0.05, 0, 0),
    PF_EtResType2 = cms.vdouble(0.05, 0, 0)
)


process.pfMet = cms.EDProducer("METProducer",
    resolutionsEra = cms.string('Spring10'),
    PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
    HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
    jdphi6 = cms.vdouble(0.084, 0.08, 0.072, 0.065, 0.066, 
        0.06, 0.051, 0.049, 0.045, 0.045),
    jdphi3 = cms.vdouble(0.042, 0.043, 0.044, 0.043, 0.041, 
        0.039, 0.039, 0.036, 0.034, 0.031),
    jdpt9 = cms.vdouble(0.843, 0.885, 1.245, 1.665, 1.944, 
        1.981, 1.972, 2.875, 3.923, 7.51),
    jdpt8 = cms.vdouble(0.889, 0.939, 1.166, 1.365, 1.553, 
        1.805, 2.06, 2.22, 2.268, 2.247),
    jdpt7 = cms.vdouble(1.094, 1.139, 1.436, 1.672, 1.831, 
        2.05, 2.267, 2.549, 2.785, 2.86),
    jdpt6 = cms.vdouble(1.213, 1.298, 1.716, 2.015, 2.191, 
        2.612, 2.863, 2.879, 2.925, 2.902),
    jdpt5 = cms.vdouble(1.049, 1.149, 1.607, 1.869, 2.012, 
        2.219, 2.289, 2.412, 2.695, 2.865),
    jdpt4 = cms.vdouble(0.85, 0.961, 1.337, 1.593, 1.854, 
        2.005, 2.209, 2.533, 2.812, 3.047),
    jdpt3 = cms.vdouble(0.929, 1.04, 1.46, 1.74, 2.042, 
        2.289, 2.639, 2.837, 2.946, 2.971),
    jdpt2 = cms.vdouble(0.841, 0.937, 1.316, 1.605, 1.919, 
        2.295, 2.562, 2.722, 2.943, 3.293),
    EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    jdpt0 = cms.vdouble(0.749, 0.829, 1.099, 1.355, 1.584, 
        1.807, 2.035, 2.217, 2.378, 2.591),
    HF_PhiResPar = cms.vdouble(0.05022),
    HE_PhiResPar = cms.vdouble(0.02511),
    jdpt1 = cms.vdouble(0.718, 0.813, 1.133, 1.384, 1.588, 
        1.841, 2.115, 2.379, 2.508, 2.772),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_PhiResType3 = cms.vdouble(0.002),
    HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
    resolutionsAlgo = cms.string('AK5PF'),
    PF_PhiResType6 = cms.vdouble(0.02511),
    PF_PhiResType7 = cms.vdouble(0.02511),
    PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
    PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
    ptresolthreshold = cms.double(10.0),
    HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
    EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    EB_PhiResPar = cms.vdouble(0.00502),
    jdphi9 = cms.vdouble(0.062, 0.059, 0.053, 0.047, 0.042, 
        0.045, 0.036, 0.032, 0.034, 0.044),
    jdphi8 = cms.vdouble(0.059, 0.057, 0.051, 0.044, 0.038, 
        0.035, 0.037, 0.032, 0.028, 0.028),
    jdphi4 = cms.vdouble(0.042, 0.042, 0.043, 0.042, 0.038, 
        0.036, 0.036, 0.033, 0.031, 0.031),
    HO_PhiResPar = cms.vdouble(0.02511),
    jdphi2 = cms.vdouble(0.04, 0.04, 0.04, 0.04, 0.04, 
        0.038, 0.036, 0.035, 0.034, 0.033),
    jdphi1 = cms.vdouble(0.034, 0.035, 0.035, 0.035, 0.035, 
        0.034, 0.031, 0.03, 0.029, 0.027),
    jdphi0 = cms.vdouble(0.034, 0.034, 0.034, 0.034, 0.032, 
        0.031, 0.028, 0.027, 0.027, 0.027),
    jdphi7 = cms.vdouble(0.077, 0.072, 0.059, 0.05, 0.045, 
        0.042, 0.039, 0.039, 0.037, 0.031),
    EE_PhiResPar = cms.vdouble(0.02511),
    jdphi5 = cms.vdouble(0.069, 0.069, 0.064, 0.058, 0.053, 
        0.049, 0.049, 0.043, 0.039, 0.04),
    HB_PhiResPar = cms.vdouble(0.02511),
    PF_PhiResType1 = cms.vdouble(0.002),
    PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
    PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
    PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
    HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
    PF_EtResType1 = cms.vdouble(0.05, 0, 0),
    PF_EtResType3 = cms.vdouble(0.05, 0, 0),
    PF_EtResType2 = cms.vdouble(0.05, 0, 0),
    src = cms.InputTag("particleFlow"),
    METType = cms.string('PFMET'),
    calculateSignificance = cms.bool(True),
    alias = cms.string('PFMET'),
    noHF = cms.bool(False),
    jets = cms.InputTag("ak5PFJets"),
    globalThreshold = cms.double(0.0),
    InputType = cms.string('PFCandidateCollection')
)


process.pfNoElectron = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("pfNoMuon"),
    enable = cms.bool(False),
    topCollection = cms.InputTag("pfIsolatedElectrons"),
    name = cms.untracked.string('noElectron'),
    verbose = cms.untracked.bool(False)
)


process.pfNoJet = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("pfNoElectron"),
    enable = cms.bool(True),
    topCollection = cms.InputTag("pfJets"),
    name = cms.untracked.string('noJet'),
    verbose = cms.untracked.bool(False)
)


process.pfNoMuon = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("pfNoPileUp"),
    enable = cms.bool(False),
    topCollection = cms.InputTag("pfIsolatedMuons"),
    name = cms.untracked.string('noMuon'),
    verbose = cms.untracked.bool(False)
)


process.pfNoPileUp = cms.EDProducer("TPPileUpPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlow"),
    enable = cms.bool(True),
    topCollection = cms.InputTag("pfPileUp"),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    verbose = cms.untracked.bool(False)
)


process.pfNoTau = cms.EDProducer("TPPFTausOnPFJets",
    bottomCollection = cms.InputTag("pfJets"),
    enable = cms.bool(True),
    topCollection = cms.InputTag("pfTaus"),
    name = cms.untracked.string('noTau'),
    verbose = cms.untracked.bool(False)
)


process.pfPileUp = cms.EDProducer("PFPileUp",
    PFCandidates = cms.InputTag("particleFlow"),
    Enable = cms.bool(True),
    checkClosestZVertex = cms.bool(False),
    verbose = cms.untracked.bool(False),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices")
)


process.pfPileUpCandidates = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlow"),
    enable = cms.bool(True),
    topCollection = cms.InputTag("pfNoPileUp"),
    name = cms.untracked.string('pileUpCandidates'),
    verbose = cms.untracked.bool(False)
)


process.pfRecoTauDiscriminationAgainstCaloMuon = cms.EDProducer("PFRecoTauDiscriminationAgainstCaloMuon",
    srcHcalRecHits = cms.InputTag("hbhereco"),
    minLeadTrackPt = cms.double(15.0),
    maxEnToTrackRatio = cms.double(0.25),
    srcVertex = cms.InputTag("offlinePrimaryVerticesWithBS"),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    srcEcalRecHitsBarrel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    dRhcal = cms.double(25.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    maxEnEcal = cms.double(3.0),
    maxEnHcal = cms.double(8.0),
    dRecal = cms.double(15.0),
    srcEcalRecHitsEndcap = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    minLeadTrackPtFraction = cms.double(0.8)
)


process.pfRecoTauDiscriminationAgainstElectron = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(-0.1),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    ApplyCut_BremCombined = cms.bool(False),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(False),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.pfRecoTauDiscriminationAgainstMuon = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon",
    a = cms.double(0.5),
    c = cms.double(0.0),
    b = cms.double(0.5),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    discriminatorOption = cms.string('noSegMatch')
)


process.pfRecoTauDiscriminationByECALIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.pfRecoTauDiscriminationByECALIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.pfRecoTauDiscriminationByIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.pfRecoTauDiscriminationByIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.pfRecoTauDiscriminationByLeadingPionPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    UseOnlyChargedHadrons = cms.bool(False)
)


process.pfRecoTauDiscriminationByLeadingTrackFinding = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.pfRecoTauDiscriminationByLeadingTrackPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.pfRecoTauDiscriminationByTrackIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.pfRecoTauDiscriminationByTrackIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.pfRecoTauTagInfoProducer = cms.EDProducer("PFRecoTauTagInfoProducer",
    tkminTrackerHitsn = cms.int32(3),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    tkmaxChi2 = cms.double(100.0),
    ChargedHadrCand_AssociationCone = cms.double(0.8),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32(3),
    ChargedHadrCand_tkmaxChi2 = cms.double(100.0),
    tkPVmaxDZ = cms.double(0.2),
    GammaCand_EcalclusMinEt = cms.double(0.5),
    tkminPixelHitsn = cms.int32(0),
    tkminPt = cms.double(0.5),
    PFCandidateProducer = cms.InputTag("particleFlow"),
    ChargedHadrCand_tkminPt = cms.double(0.5),
    ChargedHadrCand_tkmaxipt = cms.double(0.03),
    ChargedHadrCand_tkminPixelHitsn = cms.int32(0),
    UsePVconstraint = cms.bool(True),
    NeutrHadrCand_HcalclusMinEt = cms.double(1.0),
    PFJetTracksAssociatorProducer = cms.InputTag("ak5PFJetTracksAssociatorAtVertex"),
    smearedPVsigmaY = cms.double(0.0015),
    smearedPVsigmaX = cms.double(0.0015),
    smearedPVsigmaZ = cms.double(0.005),
    ChargedHadrCand_tkPVmaxDZ = cms.double(0.2),
    tkmaxipt = cms.double(0.03)
)


process.pfTauDecayMode = cms.EDProducer("PFRecoTauDecayModeDeterminator",
    mergeByBestMatch = cms.bool(True),
    refitTracks = cms.bool(False),
    maxPiZeroMass = cms.double(0.2),
    mergeLowPtPhotonsFirst = cms.bool(True),
    setMergedPi0Mass = cms.bool(True),
    setChargedPionMass = cms.bool(True),
    filterPhotons = cms.bool(True),
    minPtFractionSinglePhotons = cms.double(0.1),
    minPtFractionPiZeroes = cms.double(0.15),
    maxNbrOfIterations = cms.int32(10),
    filterTwoProngs = cms.bool(True),
    minPtFractionForSecondProng = cms.double(0.1),
    maxDistance = cms.double(0.01),
    setPi0Mass = cms.bool(True),
    maxPhotonsToMerge = cms.uint32(2),
    PFTauProducer = cms.InputTag("pfRecoTauProducer")
)


process.pfTauDecayModeHighEfficiency = cms.EDProducer("PFRecoTauDecayModeDeterminator",
    mergeByBestMatch = cms.bool(True),
    refitTracks = cms.bool(False),
    maxPiZeroMass = cms.double(0.2),
    mergeLowPtPhotonsFirst = cms.bool(True),
    setMergedPi0Mass = cms.bool(True),
    setChargedPionMass = cms.bool(True),
    filterPhotons = cms.bool(True),
    minPtFractionSinglePhotons = cms.double(0.1),
    minPtFractionPiZeroes = cms.double(0.15),
    maxNbrOfIterations = cms.int32(10),
    filterTwoProngs = cms.bool(True),
    minPtFractionForSecondProng = cms.double(0.1),
    maxDistance = cms.double(0.01),
    setPi0Mass = cms.bool(True),
    maxPhotonsToMerge = cms.uint32(2),
    PFTauProducer = cms.InputTag("pfRecoTauProducerHighEfficiency")
)


process.pfTauDecayModeIndexProducer = cms.EDProducer("PFRecoTauDecayModeIndexProducer",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    PFTauDecayModeProducer = cms.InputTag("pfRecoTauDecayModeProducer")
)


process.pfTauDecayModeInsideOut = cms.EDProducer("PFRecoTauDecayModeDeterminator",
    mergeByBestMatch = cms.bool(True),
    refitTracks = cms.bool(False),
    maxPiZeroMass = cms.double(0.2),
    mergeLowPtPhotonsFirst = cms.bool(True),
    setMergedPi0Mass = cms.bool(True),
    setChargedPionMass = cms.bool(True),
    filterPhotons = cms.bool(True),
    minPtFractionSinglePhotons = cms.double(0.1),
    minPtFractionPiZeroes = cms.double(0.15),
    maxNbrOfIterations = cms.int32(10),
    filterTwoProngs = cms.bool(True),
    minPtFractionForSecondProng = cms.double(0.1),
    maxDistance = cms.double(0.01),
    setPi0Mass = cms.bool(True),
    maxPhotonsToMerge = cms.uint32(2),
    PFTauProducer = cms.InputTag("pfRecoTauProducerInsideOut")
)


process.pfTauPFJets08Region = cms.EDProducer("RecoTauJetRegionProducer",
    src = cms.InputTag("pfJets"),
    deltaR = cms.double(0.8),
    pfSrc = cms.InputTag("pfNoElectron")
)


process.pfTauTagInfoProducer = cms.EDProducer("PFRecoTauTagInfoProducer",
    tkminTrackerHitsn = cms.int32(3),
    tkminPt = cms.double(0.5),
    tkmaxChi2 = cms.double(100.0),
    ChargedHadrCand_AssociationCone = cms.double(0.8),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32(3),
    ChargedHadrCand_tkmaxChi2 = cms.double(100.0),
    tkPVmaxDZ = cms.double(0.2),
    GammaCand_EcalclusMinEt = cms.double(0.5),
    tkminPixelHitsn = cms.int32(0),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFCandidateProducer = cms.InputTag("pfNoElectron"),
    ChargedHadrCand_tkminPt = cms.double(0.5),
    ChargedHadrCand_tkmaxipt = cms.double(0.03),
    ChargedHadrCand_tkminPixelHitsn = cms.int32(0),
    UsePVconstraint = cms.bool(True),
    NeutrHadrCand_HcalclusMinEt = cms.double(1.0),
    PFJetTracksAssociatorProducer = cms.InputTag("pfJetTracksAssociatorAtVertex"),
    smearedPVsigmaY = cms.double(0.0015),
    smearedPVsigmaX = cms.double(0.0015),
    smearedPVsigmaZ = cms.double(0.005),
    ChargedHadrCand_tkPVmaxDZ = cms.double(0.2),
    tkmaxipt = cms.double(0.03)
)


process.pfTausBase = cms.EDProducer("RecoTauProducer",
    piZeroSrc = cms.InputTag("pfJetsLegacyTaNCPiZeros"),
    modifiers = cms.VPSet(cms.PSet(
        ElectronPreIDProducer = cms.InputTag("elecpreid"),
        name = cms.string('shrinkingConeElectronRej'),
        plugin = cms.string('RecoTauElectronRejectionPlugin'),
        DataType = cms.string('AOD'),
        maximumForElectrionPreIDOutput = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
        EcalStripSumE_minClusEnergy = cms.double(0.1),
        ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
        EcalStripSumE_deltaEta = cms.double(0.03)
    ), 
        cms.PSet(
            pfTauTagInfoSrc = cms.InputTag("pfTauTagInfoProducer"),
            name = cms.string('pfTauTTIworkaround'),
            plugin = cms.string('RecoTauTagInfoWorkaroundModifer')
        )),
    jetRegionSrc = cms.InputTag("pfTauPFJets08Region"),
    jetSrc = cms.InputTag("pfJets"),
    builders = cms.VPSet(cms.PSet(
        usePFLeptons = cms.bool(True),
        signalConeNeutralHadrons = cms.string('0.15'),
        name = cms.string('shrinkingCone'),
        plugin = cms.string('RecoTauBuilderConePlugin'),
        isoConeChargedHadrons = cms.string('0.5'),
        isoConePiZeros = cms.string('0.5'),
        isoConeNeutralHadrons = cms.string('0.5'),
        matchingCone = cms.string('0.1'),
        signalConeChargedHadrons = cms.string('min(max(5.0/et(), 0.07), 0.15)'),
        leadObjectPt = cms.double(5.0),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalConePiZeros = cms.string('0.15'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pfCandSrc = cms.InputTag("pfNoElectron")
    )),
    buildNullTaus = cms.bool(True)
)


process.pfTausBaseDiscriminationByIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfTausBase"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfTausBaseDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.pfTausBaseDiscriminationByLeadingPionPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(False),
    PFTauProducer = cms.InputTag("pfTausBase")
)


process.pfTausBaseDiscriminationByLeadingTrackFinding = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(True),
    PFTauProducer = cms.InputTag("pfTausBase")
)


process.pfTausDiscriminationByIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfTausProducer"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("pfTausDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.pfTausDiscriminationByLeadingPionPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(False),
    PFTauProducer = cms.InputTag("pfTausProducer")
)


process.pfTausDiscriminationByLeadingTrackFinding = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(True),
    PFTauProducer = cms.InputTag("pfTausProducer")
)


process.pfTausProducer = cms.EDProducer("RecoTauProducer",
    piZeroSrc = cms.InputTag("pfJetsLegacyTaNCPiZeros"),
    modifiers = cms.VPSet(cms.PSet(
        ElectronPreIDProducer = cms.InputTag("elecpreid"),
        name = cms.string('shrinkingConeElectronRej'),
        plugin = cms.string('RecoTauElectronRejectionPlugin'),
        DataType = cms.string('AOD'),
        maximumForElectrionPreIDOutput = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
        EcalStripSumE_minClusEnergy = cms.double(0.1),
        ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
        EcalStripSumE_deltaEta = cms.double(0.03)
    ), 
        cms.PSet(
            pfTauTagInfoSrc = cms.InputTag("pfTauTagInfoProducer"),
            name = cms.string('pfTauTTIworkaround'),
            plugin = cms.string('RecoTauTagInfoWorkaroundModifer')
        )),
    jetRegionSrc = cms.InputTag("pfTauPFJets08Region"),
    jetSrc = cms.InputTag("pfJets"),
    builders = cms.VPSet(cms.PSet(
        usePFLeptons = cms.bool(True),
        signalConeNeutralHadrons = cms.string('0.15'),
        name = cms.string('shrinkingCone'),
        plugin = cms.string('RecoTauBuilderConePlugin'),
        isoConeChargedHadrons = cms.string('0.5'),
        isoConePiZeros = cms.string('0.5'),
        isoConeNeutralHadrons = cms.string('0.5'),
        matchingCone = cms.string('0.1'),
        signalConeChargedHadrons = cms.string('min(max(5.0/et(), 0.07), 0.15)'),
        leadObjectPt = cms.double(5.0),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalConePiZeros = cms.string('0.15'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pfCandSrc = cms.InputTag("pfNoElectron")
    )),
    buildNullTaus = cms.bool(True)
)


process.photonMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("photons"),
    maxDPtRel = cms.double(1.0),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.2),
    checkCharge = cms.bool(True),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.recoTauAK5PFJets08Region = cms.EDProducer("RecoTauJetRegionProducer",
    src = cms.InputTag("ak5PFJets"),
    deltaR = cms.double(0.8),
    pfSrc = cms.InputTag("particleFlow")
)


process.secondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(-0.01),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(-0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(-99999.9),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(-3.0),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(-2.5),
        distSig3dMin = cms.double(-99999.9)
    ),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfosAK5PF = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfosAK5PF"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfosAK7Calo = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfosAK7Calo"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfosAK7PF = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfosAK7PF"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfosAOD = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfosAOD"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfosCACalo = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfosCACalo"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfosCAPF = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfosCAPF"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfossubCAPF = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfossubCAPF"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.selectedElectronsMatched = cms.EDProducer("PATTriggerMatchElectronEmbedder",
    matches = cms.VInputTag(cms.InputTag("selectedElectronsTriggerMatch")),
    src = cms.InputTag("selectedPatElectrons")
)


process.selectedElectronsTriggerMatch = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matchedCuts = cms.string('path("*Ele*",0,0)'),
    src = cms.InputTag("selectedPatElectrons"),
    maxDPtRel = cms.double(0.5),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = cms.double(0.3),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("patTrigger")
)


process.selectedMuonsMatched = cms.EDProducer("PATTriggerMatchMuonEmbedder",
    matches = cms.VInputTag(cms.InputTag("selectedMuonsTriggerMatch")),
    src = cms.InputTag("selectedPatMuons")
)


process.selectedMuonsTriggerMatch = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matchedCuts = cms.string('path("*Mu*",0,0)'),
    src = cms.InputTag("selectedPatMuons"),
    maxDPtRel = cms.double(0.5),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = cms.double(0.3),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("patTrigger")
)


process.shrinkingConePFTauDecayModeIndexProducer = cms.EDProducer("PFRecoTauDecayModeIndexProducer",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("shrinkingConePFTauProducer"),
    PFTauDecayModeProducer = cms.InputTag("shrinkingConePFTauDecayModeProducer")
)


process.shrinkingConePFTauDecayModeProducer = cms.EDProducer("PFRecoTauDecayModeDeterminator",
    mergeByBestMatch = cms.bool(True),
    refitTracks = cms.bool(False),
    maxPiZeroMass = cms.double(0.2),
    mergeLowPtPhotonsFirst = cms.bool(True),
    setMergedPi0Mass = cms.bool(True),
    setChargedPionMass = cms.bool(True),
    filterPhotons = cms.bool(True),
    minPtFractionSinglePhotons = cms.double(0.1),
    minPtFractionPiZeroes = cms.double(0.15),
    maxNbrOfIterations = cms.int32(10),
    filterTwoProngs = cms.bool(True),
    minPtFractionForSecondProng = cms.double(0.1),
    maxDistance = cms.double(0.01),
    setPi0Mass = cms.bool(True),
    maxPhotonsToMerge = cms.uint32(2),
    PFTauProducer = cms.InputTag("shrinkingConePFTauProducer")
)


process.shrinkingConePFTauDiscriminationAgainstElectron = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    PFTauProducer = cms.InputTag("pfTaus"),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    ApplyCut_EmFraction = cms.bool(False),
    EmFraction_maxValue = cms.double(0.9),
    BremCombined_Mass = cms.double(0.55),
    ApplyCut_PFElectronMVA = cms.bool(True),
    PFElectronMVA_maxValue = cms.double(-0.1),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    ApplyCut_BremCombined = cms.bool(False),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    ApplyCut_EcalCrackCut = cms.bool(False),
    BremCombined_StripSize = cms.double(0.03),
    EOverPLead_maxValue = cms.double(1.8),
    HcalTotOverPLead_minValue = cms.double(0.1),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Fraction = cms.double(0.99),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8)
)


process.shrinkingConePFTauDiscriminationAgainstMuon = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon",
    a = cms.double(0.5),
    c = cms.double(0.0),
    b = cms.double(0.5),
    PFTauProducer = cms.InputTag("pfTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    discriminatorOption = cms.string('noSegMatch')
)


process.shrinkingConePFTauDiscriminationByECALIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.shrinkingConePFTauDiscriminationByECALIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.shrinkingConePFTauDiscriminationByIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.shrinkingConePFTauDiscriminationByIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.shrinkingConePFTauDiscriminationByLeadingPionPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("pfTaus"),
    UseOnlyChargedHadrons = cms.bool(False)
)


process.shrinkingConePFTauDiscriminationByLeadingTrackFinding = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("pfTaus"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.shrinkingConePFTauDiscriminationByLeadingTrackPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    PFTauProducer = cms.InputTag("pfTaus"),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.shrinkingConePFTauDiscriminationByTaNC = cms.EDProducer("RecoTauMVADiscriminator",
    discriminantOptions = cms.PSet(

    ),
    mvas = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        mvaLabel = cms.string('OneProngNoPiZero'),
        nCharged = cms.uint32(1)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            mvaLabel = cms.string('OneProngOnePiZero'),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            mvaLabel = cms.string('OneProngTwoPiZero'),
            nCharged = cms.uint32(1)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            mvaLabel = cms.string('ThreeProngNoPiZero'),
            nCharged = cms.uint32(3)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            mvaLabel = cms.string('ThreeProngOnePiZero'),
            nCharged = cms.uint32(3)
        )),
    remapOutput = cms.bool(True),
    PFTauProducer = cms.InputTag("pfTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    prefailValue = cms.double(-2.0),
    dbLabel = cms.string('')
)


process.shrinkingConePFTauDiscriminationByTaNCfrHalfPercent = cms.EDProducer("RecoTauDecayModeCutMultiplexer",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        nCharged = cms.uint32(1),
        cut = cms.double(0.9087875)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(1),
            cut = cms.double(0.8707145)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            nCharged = cms.uint32(1),
            cut = cms.double(0.921793)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            nCharged = cms.uint32(3),
            cut = cms.double(0.9451915)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(3),
            cut = cms.double(0.9488565)
        )),
    toMultiplex = cms.InputTag("shrinkingConePFTauDiscriminationByTaNC"),
    PFTauProducer = cms.InputTag("pfTaus")
)


process.shrinkingConePFTauDiscriminationByTaNCfrOnePercent = cms.EDProducer("RecoTauDecayModeCutMultiplexer",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        nCharged = cms.uint32(1),
        cut = cms.double(0.7649845)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(1),
            cut = cms.double(0.699697)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            nCharged = cms.uint32(1),
            cut = cms.double(0.772231)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            nCharged = cms.uint32(3),
            cut = cms.double(0.905071)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(3),
            cut = cms.double(0.9238995)
        )),
    toMultiplex = cms.InputTag("shrinkingConePFTauDiscriminationByTaNC"),
    PFTauProducer = cms.InputTag("pfTaus")
)


process.shrinkingConePFTauDiscriminationByTaNCfrQuarterPercent = cms.EDProducer("RecoTauDecayModeCutMultiplexer",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        nCharged = cms.uint32(1),
        cut = cms.double(0.9539685)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(1),
            cut = cms.double(0.940843)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            nCharged = cms.uint32(1),
            cut = cms.double(0.9645195)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            nCharged = cms.uint32(3),
            cut = cms.double(0.960407)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(3),
            cut = cms.double(0.994065)
        )),
    toMultiplex = cms.InputTag("shrinkingConePFTauDiscriminationByTaNC"),
    PFTauProducer = cms.InputTag("pfTaus")
)


process.shrinkingConePFTauDiscriminationByTaNCfrTenthPercent = cms.EDProducer("RecoTauDecayModeCutMultiplexer",
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    decayModes = cms.VPSet(cms.PSet(
        nPiZeros = cms.uint32(0),
        nCharged = cms.uint32(1),
        cut = cms.double(0.959384)
    ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(1),
            cut = cms.double(0.991353)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(2),
            nCharged = cms.uint32(1),
            cut = cms.double(0.9712775)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(0),
            nCharged = cms.uint32(3),
            cut = cms.double(0.9875015)
        ), 
        cms.PSet(
            nPiZeros = cms.uint32(1),
            nCharged = cms.uint32(3),
            cut = cms.double(1.0234655)
        )),
    toMultiplex = cms.InputTag("shrinkingConePFTauDiscriminationByTaNC"),
    PFTauProducer = cms.InputTag("pfTaus")
)


process.shrinkingConePFTauDiscriminationByTrackIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.shrinkingConePFTauDiscriminationByTrackIsolationUsingLeadingPion = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    PFTauProducer = cms.InputTag("pfTaus"),
    maximumSumPtCut = cms.double(6.0),
    relativeSumPtCut = cms.double(0.0),
    maximumOccupancy = cms.uint32(0),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadPion = cms.PSet(
            cut = cms.double(0.5),
            Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
        )
    ),
    applyOccupancyCut = cms.bool(True),
    applySumPtCut = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(8),
            minTrackPt = cms.double(1.0),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(1.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalQualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        )
    ),
    applyRelativeSumPtCut = cms.bool(False)
)


process.shrinkingConePFTauProducer = cms.EDProducer("RecoTauProducer",
    piZeroSrc = cms.InputTag("ak5PFJetsLegacyTaNCPiZeros"),
    modifiers = cms.VPSet(cms.PSet(
        ElectronPreIDProducer = cms.InputTag("elecpreid"),
        name = cms.string('shrinkingConeElectronRej'),
        plugin = cms.string('RecoTauElectronRejectionPlugin'),
        DataType = cms.string('AOD'),
        maximumForElectrionPreIDOutput = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
        EcalStripSumE_minClusEnergy = cms.double(0.1),
        ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
        EcalStripSumE_deltaEta = cms.double(0.03)
    ), 
        cms.PSet(
            pfTauTagInfoSrc = cms.InputTag("pfRecoTauTagInfoProducer"),
            name = cms.string('TTIworkaround'),
            plugin = cms.string('RecoTauTagInfoWorkaroundModifer')
        )),
    jetRegionSrc = cms.InputTag("recoTauAK5PFJets08Region"),
    jetSrc = cms.InputTag("ak5PFJets"),
    builders = cms.VPSet(cms.PSet(
        usePFLeptons = cms.bool(True),
        signalConeNeutralHadrons = cms.string('0.15'),
        name = cms.string('shrinkingCone'),
        plugin = cms.string('RecoTauBuilderConePlugin'),
        isoConeChargedHadrons = cms.string('0.5'),
        isoConePiZeros = cms.string('0.5'),
        isoConeNeutralHadrons = cms.string('0.5'),
        matchingCone = cms.string('0.1'),
        signalConeChargedHadrons = cms.string('min(max(5.0/et(), 0.07), 0.15)'),
        leadObjectPt = cms.double(5.0),
        qualityCuts = cms.PSet(
            minTrackHits = cms.uint32(3),
            minTrackPt = cms.double(0.5),
            maxTrackChi2 = cms.double(100.0),
            minTrackPixelHits = cms.uint32(0),
            minGammaEt = cms.double(0.5),
            useTracksInsteadOfPFHadrons = cms.bool(False),
            maxDeltaZ = cms.double(0.2),
            maxTransverseImpactParameter = cms.double(0.03)
        ),
        signalConePiZeros = cms.string('0.15'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pfCandSrc = cms.InputTag("particleFlow")
    )),
    buildNullTaus = cms.bool(True)
)


process.simpleSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighEffBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAK5PF"))
)


process.simpleSecondaryVertexHighEffBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAK7Calo"))
)


process.simpleSecondaryVertexHighEffBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAK7PF"))
)


process.simpleSecondaryVertexHighEffBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAOD"))
)


process.simpleSecondaryVertexHighEffBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosCACalo"))
)


process.simpleSecondaryVertexHighEffBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosCAPF"))
)


process.simpleSecondaryVertexHighEffBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfossubCAPF"))
)


process.simpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighPurBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAK5PF"))
)


process.simpleSecondaryVertexHighPurBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAK7Calo"))
)


process.simpleSecondaryVertexHighPurBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAK7PF"))
)


process.simpleSecondaryVertexHighPurBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAOD"))
)


process.simpleSecondaryVertexHighPurBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosCACalo"))
)


process.simpleSecondaryVertexHighPurBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosCAPF"))
)


process.simpleSecondaryVertexHighPurBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfossubCAPF"))
)


process.simpleSecondaryVertexNegativeBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.sisCone5GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('SISCone'),
    rParam = cms.double(0.5)
)


process.sisCone5GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('SISCone'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.sisCone5GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('SISCone'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.5),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.sisCone7GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('SISCone'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJets"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.sisCone7GenJetsNoMuNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('SISCone'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoMuNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.sisCone7GenJetsNoNu = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('SISCone'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.7),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.softElectronBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softElectron'),
    tagInfos = cms.VInputTag(cms.InputTag("softElectronTagInfos"))
)


process.softElectronByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softElectronTagInfos"))
)


process.softElectronByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softElectronTagInfos"))
)


process.softElectronCands = cms.EDProducer("SoftElectronCandProducer",
    BarreldRGsfTrackElectronCuts = cms.vdouble(0.0, 0.017),
    BarrelEemPinRatioCuts = cms.vdouble(-0.9, 0.39),
    BarrelMVACuts = cms.vdouble(-0.1, 1.0),
    BarrelPtCuts = cms.vdouble(2.0, 9999.0),
    ForwarddRGsfTrackElectronCuts = cms.vdouble(0.0, 0.006),
    ForwardPtCuts = cms.vdouble(2.0, 9999.0),
    ForwardMVACuts = cms.vdouble(-0.24, 1.0),
    ForwardInverseFBremCuts = cms.vdouble(1.0, 7.01),
    electrons = cms.InputTag("gsfElectrons")
)


process.softElectronSelector = cms.EDProducer("BtagGsfElectronSelector",
    input = cms.InputTag("gsfElectrons"),
    selection = cms.InputTag("eidLoose"),
    cut = cms.double(0.5)
)


process.softElectronTagInfos = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(0),
    leptons = cms.InputTag("gsfElectrons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag("softElectronCands"),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak5CaloJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(10.0)
)


process.softMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfos"))
)


process.softMuonBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK5PF"))
)


process.softMuonBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK7Calo"))
)


process.softMuonBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK7PF"))
)


process.softMuonBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAOD"))
)


process.softMuonBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosCACalo"))
)


process.softMuonBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosCAPF"))
)


process.softMuonBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfossubCAPF"))
)


process.softMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfos"))
)


process.softMuonByIP3dBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK5PF"))
)


process.softMuonByIP3dBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK7Calo"))
)


process.softMuonByIP3dBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK7PF"))
)


process.softMuonByIP3dBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAOD"))
)


process.softMuonByIP3dBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosCACalo"))
)


process.softMuonByIP3dBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosCAPF"))
)


process.softMuonByIP3dBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfossubCAPF"))
)


process.softMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfos"))
)


process.softMuonByPtBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK5PF"))
)


process.softMuonByPtBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK7Calo"))
)


process.softMuonByPtBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAK7PF"))
)


process.softMuonByPtBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAOD"))
)


process.softMuonByPtBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosCACalo"))
)


process.softMuonByPtBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosCAPF"))
)


process.softMuonByPtBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfossubCAPF"))
)


process.softMuonNoIPBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuonNoIP'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfos"))
)


process.softMuonTagInfos = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak5CaloJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.softMuonTagInfosAK5PF = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak5PFJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.softMuonTagInfosAK7Calo = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak7CaloJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.softMuonTagInfosAK7PF = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak7PFJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.softMuonTagInfosAOD = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak5CaloJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.softMuonTagInfosCACalo = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("caTopCaloJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.softMuonTagInfosCAPF = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("caTopPFJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.softMuonTagInfossubCAPF = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("CAsubJetsProducer"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.tauGenJetMatch = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("pfTaus"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.1),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("tauGenJetsSelectorAllHadrons")
)


process.tauGenJets = cms.EDProducer("TauGenJetProducer",
    includeNeutrinos = cms.bool(False),
    GenParticles = cms.InputTag("genParticles"),
    verbose = cms.untracked.bool(False)
)


process.tauIsoDepositPFCandidates = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfTaus"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(10000.0),
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(10000.0),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("pfTaus"),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1)
    )
)


process.tauIsoDepositPFChargedHadrons = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfTaus"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("pfTaus"),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        candidateSource = cms.InputTag("pfAllChargedHadrons"),
        dRmatchPFTau = cms.double(0.1)
    )
)


process.tauIsoDepositPFGammas = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfTaus"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(10000.0),
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(10000.0),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("pfTaus"),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        candidateSource = cms.InputTag("pfAllPhotons"),
        dRmatchPFTau = cms.double(0.1)
    )
)


process.tauIsoDepositPFNeutralHadrons = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("pfTaus"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(10000.0),
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(10000.0),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("pfTaus"),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        candidateSource = cms.InputTag("pfAllNeutralHadrons"),
        dRmatchPFTau = cms.double(0.1)
    )
)


process.tauMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("pfTaus"),
    maxDPtRel = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(999.9),
    checkCharge = cms.bool(True),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.trackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackCountingHighEffBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5PF"))
)


process.trackCountingHighEffBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7Calo"))
)


process.trackCountingHighEffBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7PF"))
)


process.trackCountingHighEffBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"))
)


process.trackCountingHighEffBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCACalo"))
)


process.trackCountingHighEffBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCAPF"))
)


process.trackCountingHighEffBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfossubCAPF"))
)


process.trackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackCountingHighPurBJetTagsAK5PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5PF"))
)


process.trackCountingHighPurBJetTagsAK7Calo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7Calo"))
)


process.trackCountingHighPurBJetTagsAK7PF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK7PF"))
)


process.trackCountingHighPurBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"))
)


process.trackCountingHighPurBJetTagsCACalo = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCACalo"))
)


process.trackCountingHighPurBJetTagsCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosCAPF"))
)


process.trackCountingHighPurBJetTagssubCAPF = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfossubCAPF"))
)


process.trackVertexArbitrator = cms.EDProducer("TrackVertexArbitrator",
    dLenFraction = cms.double(0.333),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    distCut = cms.double(0.04),
    secondaryVertices = cms.InputTag("vertexMerger"),
    dRCut = cms.double(0.4),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    sigCut = cms.double(5)
)


process.vertexMerger = cms.EDProducer("VertexMerger",
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveVertexFinder"),
    maxFraction = cms.double(0.7)
)


process.EcalDeadCellEventFilter = cms.EDFilter("EcalDeadCellEventFilter",
    maskedEcalChannelStatusThreshold = cms.int32(1),
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    etValToBeFlagged = cms.double(63.75),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    profileRootName = cms.untracked.string('deadCellFilterProfile.root'),
    doEEfilter = cms.untracked.bool(True),
    makeProfileRoot = cms.untracked.bool(False),
    taggingMode = cms.bool(False),
    debug = cms.untracked.bool(False),
    tpDigiCollection = cms.InputTag("ecalTPSkim")
)


process.HBHENoiseFilter = cms.EDFilter("HBHENoiseFilter",
    minRBXHits = cms.int32(999),
    minIsolatedNoiseSumE = cms.double(50.0),
    minHighEHitTime = cms.double(-9999.0),
    minHPDNoOtherHits = cms.int32(10),
    label = cms.InputTag("hcalnoise"),
    minZeros = cms.int32(10),
    minNumIsolatedNoiseChannels = cms.int32(10),
    maxRatio = cms.double(999.0),
    useTS4TS5 = cms.bool(True),
    maxHighEHitTime = cms.double(9999.0),
    maxRBXEMF = cms.double(-999.0),
    minHPDHits = cms.int32(17),
    minIsolatedNoiseSumEt = cms.double(25.0),
    minRatio = cms.double(-999.0)
)


process.bVertexFilter = cms.EDFilter("BVertexFilter",
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    minVertices = cms.int32(0),
    useVertexKinematicAsJetAxis = cms.bool(True),
    vertexFilter = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.1),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    secondaryVertices = cms.InputTag("secondaryVertices")
)


process.countPatElectrons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatElectrons"),
    minNumber = cms.uint32(0)
)


process.countPatJets = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatJets"),
    minNumber = cms.uint32(0)
)


process.countPatLeptons = cms.EDFilter("PATLeptonCountFilter",
    maxNumber = cms.uint32(999999),
    countElectrons = cms.bool(True),
    muonSource = cms.InputTag("selectedPatMuons"),
    minNumber = cms.uint32(0),
    electronSource = cms.InputTag("selectedPatElectrons"),
    tauSource = cms.InputTag("selectedPatTaus"),
    countTaus = cms.bool(False),
    countMuons = cms.bool(True)
)


process.countPatMuons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatMuons"),
    minNumber = cms.uint32(0)
)


process.countPatPFParticles = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("patPFParticles"),
    minNumber = cms.uint32(0)
)


process.countPatPhotons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatPhotons"),
    minNumber = cms.uint32(0)
)


process.countPatTaus = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatTaus"),
    minNumber = cms.uint32(0)
)


process.goodOfflinePrimaryVertices = cms.EDFilter("PrimaryVertexObjectFilter",
    src = cms.InputTag("offlinePrimaryVertices"),
    filterParams = cms.PSet(
        maxZ = cms.double(24.0),
        minNdof = cms.double(4.0),
        maxRho = cms.double(2.0),
        pvSrc = cms.InputTag("offlinePrimaryVertices")
    )
)


process.goodPatJetsAK5PF = cms.EDFilter("PFJetIDSelectionFunctorFilter",
    src = cms.InputTag("selectedPatJetsAK5PF"),
    filterParams = cms.PSet(
        version = cms.string('FIRSTDATA'),
        quality = cms.string('LOOSE')
    )
)


process.hbbBestCSVPt20Candidates = cms.EDFilter("HbbCandidateFinder",
    useHighestPtHiggs = cms.bool(False),
    jetPtThreshold = cms.double(20.0),
    verbose = cms.bool(False),
    VHbbEventLabel = cms.InputTag(""),
    actAsAFilter = cms.bool(False)
)


process.hbbCandidates = cms.EDFilter("HbbCandidateFinder",
    useHighestPtHiggs = cms.bool(False),
    jetPtThreshold = cms.double(30.0),
    verbose = cms.bool(False),
    VHbbEventLabel = cms.InputTag(""),
    actAsAFilter = cms.bool(False)
)


process.hbbHighestPtHiggsPt30Candidates = cms.EDFilter("HbbCandidateFinder",
    useHighestPtHiggs = cms.bool(True),
    jetPtThreshold = cms.double(30.0),
    verbose = cms.bool(False),
    VHbbEventLabel = cms.InputTag(""),
    actAsAFilter = cms.bool(False)
)


process.hltFilter = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    andOr = cms.bool(True),
    HLTPaths = cms.vstring('HLT_QuadJet60_v*'),
    throw = cms.bool(True),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
)


process.pfAllChargedCandidates = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllChargedHadrons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllElectrons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(11, -11),
    src = cms.InputTag("pfNoMuon")
)


process.pfAllMuons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(-13, 13),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllNeutralHadrons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllPhotons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUp")
)


process.pfElectronsFromVertex = cms.EDFilter("IPCutPFCandidateSelector",
    d0Cut = cms.double(0.2),
    src = cms.InputTag("pfAllElectrons"),
    dzSigCut = cms.double(99.0),
    d0SigCut = cms.double(99.0),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    dzCut = cms.double(0.5)
)


process.pfIsolatedElectrons = cms.EDFilter("IsolatedPFCandidateSelector",
    src = cms.InputTag("pfSelectedElectrons"),
    isRelative = cms.bool(True),
    combinedIsolationCut = cms.double(0.35),
    isCombined = cms.bool(True),
    isolationValueMaps = cms.VInputTag(cms.InputTag("isoValElectronWithCharged"), cms.InputTag("isoValElectronWithNeutral"), cms.InputTag("isoValElectronWithPhotons")),
    isolationCuts = cms.vdouble(10, 10, 10)
)


process.pfIsolatedMuons = cms.EDFilter("IsolatedPFCandidateSelector",
    src = cms.InputTag("pfSelectedMuons"),
    isRelative = cms.bool(True),
    combinedIsolationCut = cms.double(0.35),
    isCombined = cms.bool(True),
    isolationValueMaps = cms.VInputTag(cms.InputTag("isoValMuonWithCharged"), cms.InputTag("isoValMuonWithNeutral"), cms.InputTag("isoValMuonWithPhotons")),
    isolationCuts = cms.vdouble(10, 10, 10)
)


process.pfMuonsFromVertex = cms.EDFilter("IPCutPFCandidateSelector",
    d0Cut = cms.double(0.2),
    src = cms.InputTag("pfAllMuons"),
    dzSigCut = cms.double(99.0),
    d0SigCut = cms.double(99.0),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    dzCut = cms.double(0.5)
)


process.pfNoPileUpCharge = cms.EDFilter("GenericPFCandidateSelector",
    src = cms.InputTag("pfNoPileUp"),
    cut = cms.string('charge !=0')
)


process.pfPUChargedCandidates = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfPileUpCandidates")
)


process.pfSelectedElectrons = cms.EDFilter("GenericPFCandidateSelector",
    src = cms.InputTag("pfElectronsFromVertex"),
    cut = cms.string('pt>5 && gsfTrackRef.isNonnull && gsfTrackRef.trackerExpectedHitsInner.numberOfLostHits<2')
)


process.pfSelectedMuons = cms.EDFilter("GenericPFCandidateSelector",
    src = cms.InputTag("pfMuonsFromVertex"),
    cut = cms.string('pt>5')
)


process.pfTauPileUpVertices = cms.EDFilter("RecoTauPileUpVertexSelector",
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices"),
    minTrackSumPt = cms.double(5)
)


process.pfTauSelector = cms.EDFilter("PFTauSelector",
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("fixedConePFTauDiscriminationByIsolation"),
        selectionCut = cms.double(0.5)
    )),
    src = cms.InputTag("fixedConePFTauProducer")
)


process.pfTaus = cms.EDFilter("PFTauSelector",
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("pfTausBaseDiscriminationByIsolation"),
        selectionCut = cms.double(0.5)
    ), 
        cms.PSet(
            discriminator = cms.InputTag("pfTausBaseDiscriminationByLeadingPionPtCut"),
            selectionCut = cms.double(0.5)
        )),
    src = cms.InputTag("pfTausBase")
)


process.recoTauPileUpVertices = cms.EDFilter("RecoTauPileUpVertexSelector",
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices"),
    minTrackSumPt = cms.double(5)
)


process.selectedPatElectrons = cms.EDFilter("PATElectronSelector",
    src = cms.InputTag("patElectrons"),
    cut = cms.string('(ecalDrivenSeed==1) &&pt > 15.0 && abs(eta) < 2.5 &&(isEE || isEB) && !isEBEEGap')
)


process.selectedPatElectronsWithIso = cms.EDFilter("PATElectronSelector",
    src = cms.InputTag("selectedPatElectrons"),
    cut = cms.string('pt > 15.0 && abs(eta) < 2.5 &&(isEE || isEB) && !isEBEEGap &&ecalDrivenSeed==1 && (abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566) && (ecalEnergy*sin(superClusterPosition.theta)>20.0) && (gsfTrack.trackerExpectedHitsInner.numberOfHits == 0) && ((chargedHadronIso + neutralHadronIso + photonIso < 0.15 * pt))  && ((isEB && (sigmaIetaIeta<0.01) && ( -0.8<deltaPhiSuperClusterTrackAtVtx<0.8 ) && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )) || (isEE && (sigmaIetaIeta<0.03) && ( -0.7<deltaPhiSuperClusterTrackAtVtx<0.7 ) && ( -0.01<deltaEtaSuperClusterTrackAtVtx<0.01 )))')
)


process.selectedPatJets = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("patJets"),
    cut = cms.string('pt > 15. & abs(eta) < 5.0')
)


process.selectedPatJetsAK5PF = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("patJetsAK5PF"),
    cut = cms.string('pt > 15. & abs(eta) < 5.0')
)


process.selectedPatJetsAK7Calo = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("patJetsAK7Calo"),
    cut = cms.string('')
)


process.selectedPatJetsAK7PF = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("patJetsAK7PF"),
    cut = cms.string('pt > 15. & abs(eta) < 5.0')
)


process.selectedPatJetsCACalo = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("patJetsCACalo"),
    cut = cms.string('pt > 0. & abs(eta) < 5.0'),
    embedGenJetMatch = cms.bool(False),
    getJetMCFlavour = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    discriminatorSources = cms.VInputTag(),
    addBTagInfo = cms.bool(True),
    addTagInfos = cms.bool(True),
    addDiscriminators = cms.bool(False)
)


process.selectedPatJetsCAPF = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("patJetsCAPF"),
    cut = cms.string('pt > 0. & abs(eta) < 5.0'),
    embedGenJetMatch = cms.bool(False),
    getJetMCFlavour = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    discriminatorSources = cms.VInputTag(),
    addBTagInfo = cms.bool(True),
    addTagInfos = cms.bool(True),
    addDiscriminators = cms.bool(False)
)


process.selectedPatJetssubCAPF = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("patJetssubCAPF"),
    cut = cms.string('')
)


process.selectedPatMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuons"),
    cut = cms.string('isGlobalMuon || (isTrackerMuon && muonID("TrackerMuonArbitrated"))')
)


process.selectedPatMuonsWithIso = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("selectedPatMuons"),
    cut = cms.string('pt > 20 && isGlobalMuon && isTrackerMuon && globalTrack().normalizedChi2 < 10 &&innerTrack().hitPattern().numberOfValidTrackerHits > 10 && innerTrack().hitPattern().numberOfValidPixelHits > 0 && globalTrack().hitPattern().numberOfValidMuonHits > 0 && dB < 0.2 &&  chargedHadronIso + neutralHadronIso + photonIso  < 0.15 * pt && numberOfMatches > 1 && abs(eta) < 2.4')
)


process.selectedPatPFParticles = cms.EDFilter("PATPFParticleSelector",
    src = cms.InputTag("patPFParticles"),
    cut = cms.string('')
)


process.selectedPatPhotons = cms.EDFilter("PATPhotonSelector",
    src = cms.InputTag("patPhotons"),
    cut = cms.string('')
)


process.selectedPatTaus = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("patTaus"),
    cut = cms.string('')
)


process.selectedVertices = cms.EDFilter("BVertexFilter",
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    minVertices = cms.int32(0),
    useVertexKinematicAsJetAxis = cms.bool(True),
    vertexFilter = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.1),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(3),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    secondaryVertices = cms.InputTag("inclusiveMergedVertices")
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    src = cms.InputTag("tauGenJets"),
    select = cms.vstring('oneProng0Pi0', 
        'oneProng1Pi0', 
        'oneProng2Pi0', 
        'oneProngOther', 
        'threeProng0Pi0', 
        'threeProng1Pi0', 
        'threeProngOther', 
        'rare')
)


process.cleanPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    logName = cms.untracked.string('cleanPatCandidates|PATSummaryTables'),
    candidates = cms.VInputTag(cms.InputTag("cleanPatElectrons"), cms.InputTag("cleanPatMuons"), cms.InputTag("cleanPatTaus"), cms.InputTag("cleanPatPhotons"), cms.InputTag("cleanPatJets"))
)


process.dump = cms.EDAnalyzer("EventContentAnalyzer")


process.patCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    logName = cms.untracked.string('patCandidates|PATSummaryTables'),
    candidates = cms.VInputTag(cms.InputTag("patElectrons"), cms.InputTag("patMuons"), cms.InputTag("patTaus"), cms.InputTag("patPhotons"), cms.InputTag("patJets"), 
        cms.InputTag("patMETs"), cms.InputTag("patPFParticles"), cms.InputTag("patMETsTC"), cms.InputTag("patMETsPF"))
)


process.selectedPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    logName = cms.untracked.string('selectedPatCanddiates|PATSummaryTables'),
    candidates = cms.VInputTag(cms.InputTag("selectedPatElectrons"), cms.InputTag("selectedPatMuons"), cms.InputTag("selectedPatTaus"), cms.InputTag("selectedPatPhotons"), cms.InputTag("selectedPatJets"), 
        cms.InputTag("selectedPatPFParticles"))
)


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('fake.edm.root'),
    outputCommands = cms.untracked.vstring('keep *_selectedPatPhotons*_*_*', 
        'keep *_selectedPatElectrons*_*_*', 
        'keep *_selectedPatMuons*_*_*', 
        'keep *_selectedPatTaus*_*_*', 
        'keep *_selectedPatJets*_*_*', 
        'drop *_selectedPatJets_pfCandidates_*', 
        'drop *_*PF_caloTowers_*', 
        'drop *_*JPT_pfCandidates_*', 
        'drop *_*Calo_pfCandidates_*', 
        'keep *_patMETs*_*_*', 
        'keep *_selectedPatPFParticles*_*_*', 
        'keep *_selectedPatTrackCands*_*_*', 
        'drop *_selectedPatJets*_genJets_*')
)


process.out1 = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(99),
    fileName = cms.untracked.string('PAT.edm.root'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('p')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_HbbAnalyzerNew_*_*', 
        'keep VHbbCandidates_*_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep *_bcandidates_*_*', 
        'keep *_bhadrons_*_*', 
        'keep *_HLTDiCentralJet20MET80_*_*', 
        'keep *_HLTDiCentralJet20MET100HBHENoiseFiltered_*_*', 
        'keep *_HLTPFMHT150_*_*', 
        'keep *_HLTQuadJet40_*_*', 
        'keep *_HLTDoubleMu7_*_*', 
        'keep *_EcalDeadCellEventFilter_*_*')
)


process.patElectronTrackIsolation = cms.Sequence(process.eleIsoDepositTk+process.eleIsoFromDepsTk)


process.recoJetId = cms.Sequence(process.ak5JetID)


process.btaggingJetTagsCAPF = cms.Sequence(process.jetBProbabilityBJetTagsCAPF+process.jetProbabilityBJetTagsCAPF+process.trackCountingHighPurBJetTagsCAPF+process.trackCountingHighEffBJetTagsCAPF+process.simpleSecondaryVertexHighEffBJetTagsCAPF+process.simpleSecondaryVertexHighPurBJetTagsCAPF+process.combinedSecondaryVertexBJetTagsCAPF+process.combinedSecondaryVertexMVABJetTagsCAPF+process.softMuonBJetTagsCAPF+process.softMuonByPtBJetTagsCAPF+process.softMuonByIP3dBJetTagsCAPF)


process.pfSortByTypeSequence = cms.Sequence(process.pfAllNeutralHadrons+process.pfAllChargedHadrons+process.pfAllPhotons)


process.recoAllGenJetsNoMuNoNu = cms.Sequence(process.sisCone5GenJetsNoMuNoNu+process.sisCone7GenJetsNoMuNoNu+process.kt4GenJetsNoMuNoNu+process.kt6GenJetsNoMuNoNu+process.iterativeCone5GenJetsNoMuNoNu+process.ak5GenJetsNoMuNoNu+process.ak7GenJetsNoMuNoNu+process.gk5GenJetsNoMuNoNu+process.gk7GenJetsNoMuNoNu+process.ca4GenJetsNoMuNoNu+process.ca6GenJetsNoMuNoNu)


process.btaggingJetTagsCACalo = cms.Sequence(process.jetBProbabilityBJetTagsCACalo+process.jetProbabilityBJetTagsCACalo+process.trackCountingHighPurBJetTagsCACalo+process.trackCountingHighEffBJetTagsCACalo+process.simpleSecondaryVertexHighEffBJetTagsCACalo+process.simpleSecondaryVertexHighPurBJetTagsCACalo+process.combinedSecondaryVertexBJetTagsCACalo+process.combinedSecondaryVertexMVABJetTagsCACalo+process.softMuonBJetTagsCACalo+process.softMuonByPtBJetTagsCACalo+process.softMuonByIP3dBJetTagsCACalo)


process.electronPFIsolationSequence = cms.Sequence(process.elePFIsoDepositCharged+process.elePFIsoDepositChargedAll+process.elePFIsoDepositGamma+process.elePFIsoDepositNeutral+process.elePFIsoDepositPU+process.elePFIsoValueCharged03+process.elePFIsoValueChargedAll03+process.elePFIsoValueGamma03+process.elePFIsoValueNeutral03+process.elePFIsoValuePU03+process.elePFIsoValueCharged04+process.elePFIsoValueChargedAll04+process.elePFIsoValueGamma04+process.elePFIsoValueNeutral04+process.elePFIsoValuePU04)


process.hpsTancTauDiscriminantSequence = cms.Sequence(process.hpsTancTausDiscriminationByTancRaw+process.hpsTancTausDiscriminationByTanc+process.hpsTancTausDiscriminationByTancVLoose+process.hpsTancTausDiscriminationByTancLoose+process.hpsTancTausDiscriminationByTancMedium+process.hpsTancTausDiscriminationByTancTight+process.hpsTancTausDiscriminationByVLooseIsolation+process.hpsTancTausDiscriminationByLooseIsolation+process.hpsTancTausDiscriminationByMediumIsolation+process.hpsTancTausDiscriminationByTightIsolation+process.hpsTancTausDiscriminationByLooseElectronRejection+process.hpsTancTausDiscriminationByMediumElectronRejection+process.hpsTancTausDiscriminationByTightElectronRejection+process.hpsTancTausDiscriminationByLooseMuonRejection+process.hpsTancTausDiscriminationByTightMuonRejection)


process.ak5JTA = cms.Sequence(process.ak5JetTracksAssociatorAtVertex+process.ak5JetTracksAssociatorAtCaloFace+process.ak5JetExtender)


process.btagging = cms.Sequence(process.impactParameterTagInfos+process.trackCountingHighEffBJetTags+process.trackCountingHighPurBJetTags+process.jetProbabilityBJetTags+process.jetBProbabilityBJetTags+process.secondaryVertexTagInfos+process.simpleSecondaryVertexHighEffBJetTags+process.simpleSecondaryVertexHighPurBJetTags+process.combinedSecondaryVertexBJetTags+process.combinedSecondaryVertexMVABJetTags+process.ghostTrackVertexTagInfos+process.ghostTrackBJetTags+process.softElectronCands+process.softElectronTagInfos+process.softElectronByIP3dBJetTags+process.softElectronByPtBJetTags+process.softMuonTagInfos+process.softMuonBJetTags+process.softMuonByIP3dBJetTags+process.softMuonByPtBJetTags)


process.leptonTrigMatch = cms.Sequence(process.selectedElectronsTriggerMatch+process.selectedElectronsMatched+process.selectedMuonsTriggerMatch+process.selectedMuonsMatched)


process.patElectronHcalIsolation = cms.Sequence(process.eleIsoDepositHcalFromTowers+process.eleIsoFromDepsHcalFromTowers)


process.makePatElectrons = cms.Sequence(process.electronMatch+process.patElectrons)


process.muonPFIsolationSequence = cms.Sequence(process.muPFIsoDepositCharged+process.muPFIsoDepositChargedAll+process.muPFIsoDepositGamma+process.muPFIsoDepositNeutral+process.muPFIsoDepositPU+process.muPFIsoValueCharged03+process.muPFIsoValueChargedAll03+process.muPFIsoValueGamma03+process.muPFIsoValueNeutral03+process.muPFIsoValuePU03+process.muPFIsoValueCharged04+process.muPFIsoValueChargedAll04+process.muPFIsoValueGamma04+process.muPFIsoValueNeutral04+process.muPFIsoValuePU04)


process.makePatPhotons = cms.Sequence(process.patPhotons)


process.recoTauCommonSequence = cms.Sequence(process.ak5PFJetTracksAssociatorAtVertex+process.recoTauAK5PFJets08Region+process.recoTauPileUpVertices+process.pfRecoTauTagInfoProducer)


process.recoGenJets = cms.Sequence(process.kt4GenJets+process.kt6GenJets+process.iterativeCone5GenJets+process.ak5GenJets+process.ak7GenJets)


process.btaggingJetTagsAOD = cms.Sequence(process.jetBProbabilityBJetTagsAOD+process.jetProbabilityBJetTagsAOD+process.trackCountingHighPurBJetTagsAOD+process.trackCountingHighEffBJetTagsAOD+process.simpleSecondaryVertexHighEffBJetTagsAOD+process.simpleSecondaryVertexHighPurBJetTagsAOD+process.combinedSecondaryVertexBJetTagsAOD+process.combinedSecondaryVertexMVABJetTagsAOD+process.softMuonBJetTagsAOD+process.softMuonByPtBJetTagsAOD+process.softMuonByIP3dBJetTagsAOD)


process.cleanPatCandidates = cms.Sequence(process.cleanPatMuons+process.cleanPatElectrons+process.cleanPatPhotons+process.cleanPatTaus+process.cleanPatJets+process.cleanPatCandidateSummary)


process.patElectronId = cms.Sequence(process.eidRobustHighEnergy)


process.btaggingJetTagsAK7PF = cms.Sequence(process.jetBProbabilityBJetTagsAK7PF+process.jetProbabilityBJetTagsAK7PF+process.trackCountingHighPurBJetTagsAK7PF+process.trackCountingHighEffBJetTagsAK7PF+process.simpleSecondaryVertexHighEffBJetTagsAK7PF+process.simpleSecondaryVertexHighPurBJetTagsAK7PF+process.combinedSecondaryVertexBJetTagsAK7PF+process.combinedSecondaryVertexMVABJetTagsAK7PF+process.softMuonBJetTagsAK7PF+process.softMuonByPtBJetTagsAK7PF+process.softMuonByIP3dBJetTagsAK7PF)


process.recoAllGenJetsNoNu = cms.Sequence(process.sisCone5GenJetsNoNu+process.sisCone7GenJetsNoNu+process.kt4GenJetsNoNu+process.kt6GenJetsNoNu+process.iterativeCone5GenJetsNoNu+process.ak5GenJetsNoNu+process.ak7GenJetsNoNu+process.gk5GenJetsNoNu+process.gk7GenJetsNoNu+process.ca4GenJetsNoNu+process.ca6GenJetsNoNu)


process.btaggingJetTagsAK5PF = cms.Sequence(process.jetBProbabilityBJetTagsAK5PF+process.jetProbabilityBJetTagsAK5PF+process.trackCountingHighPurBJetTagsAK5PF+process.trackCountingHighEffBJetTagsAK5PF+process.simpleSecondaryVertexHighEffBJetTagsAK5PF+process.simpleSecondaryVertexHighPurBJetTagsAK5PF+process.combinedSecondaryVertexBJetTagsAK5PF+process.combinedSecondaryVertexMVABJetTagsAK5PF+process.softMuonBJetTagsAK5PF+process.softMuonByPtBJetTagsAK5PF+process.softMuonByIP3dBJetTagsAK5PF)


process.RunTanc = cms.Sequence(process.shrinkingConePFTauDiscriminationByTaNCfrOnePercent+process.shrinkingConePFTauDiscriminationByTaNCfrHalfPercent+process.shrinkingConePFTauDiscriminationByTaNCfrQuarterPercent+process.shrinkingConePFTauDiscriminationByTaNCfrTenthPercent)


process.produceHPSPFTaus = cms.Sequence(process.hpsSelectionDiscriminator+process.hpsTightIsolationCleaner+process.hpsMediumIsolationCleaner+process.hpsLooseIsolationCleaner+process.hpsVLooseIsolationCleaner+process.hpsPFTauProducer)


process.patPhotonTrackIsolation = cms.Sequence(process.gamIsoDepositTk+process.gamIsoFromDepsTk)


process.selectedPatCandidates = cms.Sequence(process.selectedPatElectrons+process.selectedPatMuons+process.selectedPatTaus+process.selectedPatPhotons+process.selectedPatJets+process.selectedPatCandidateSummary)


process.genForPF2PATSequence = cms.Sequence(process.genParticlesForJetsNoNu+process.iterativeCone5GenJetsNoNu+process.ak5GenJetsNoNu+process.ak7GenJetsNoNu)


process.countPatCandidates = cms.Sequence(process.countPatElectrons+process.countPatMuons+process.countPatTaus+process.countPatLeptons+process.countPatPhotons+process.countPatJets)


process.produceAndDiscriminateHPSPFTaus = cms.Sequence(process.produceHPSPFTaus+process.hpsPFTauDiscriminationByDecayModeFinding+process.hpsPFTauDiscriminationByVLooseIsolation+process.hpsPFTauDiscriminationByLooseIsolation+process.hpsPFTauDiscriminationByMediumIsolation+process.hpsPFTauDiscriminationByTightIsolation+process.hpsPFTauDiscriminationByLooseElectronRejection+process.hpsPFTauDiscriminationByMediumElectronRejection+process.hpsPFTauDiscriminationByTightElectronRejection+process.hpsPFTauDiscriminationByLooseMuonRejection+process.hpsPFTauDiscriminationByTightMuonRejection)


process.makePatMuons = cms.Sequence(process.patMuons)


process.eidSequence = cms.Sequence(process.eidVBTFRel95+process.eidVBTFRel85+process.eidVBTFRel80+process.eidVBTFRel70+process.eidVBTFCom95+process.eidVBTFCom85+process.eidVBTFCom80+process.eidVBTFCom70)


process.hpsTancTauInitialSequence = cms.Sequence(process.combinatoricRecoTausDiscriminationByLeadingPionPtCut+process.combinatoricRecoTausHPSSelector+process.hpsTancTaus+process.hpsTancTausDiscriminationByLeadingTrackFinding+process.hpsTancTausDiscriminationByLeadingPionPtCut+process.hpsTancTausDiscriminationByLeadingTrackPtCut+process.hpsTancTausDiscriminationByDecayModeSelection+process.hpsTancTausDiscriminationByFlightPath)


process.produceAndDiscriminateShrinkingConePFTaus = cms.Sequence(process.shrinkingConePFTauProducer+process.shrinkingConePFTauDiscriminationByLeadingTrackFinding+process.shrinkingConePFTauDiscriminationByLeadingTrackPtCut+process.shrinkingConePFTauDiscriminationByLeadingPionPtCut+process.shrinkingConePFTauDiscriminationByIsolation+process.shrinkingConePFTauDiscriminationByTrackIsolation+process.shrinkingConePFTauDiscriminationByECALIsolation+process.shrinkingConePFTauDiscriminationByIsolationUsingLeadingPion+process.shrinkingConePFTauDiscriminationByTrackIsolationUsingLeadingPion+process.shrinkingConePFTauDiscriminationByECALIsolationUsingLeadingPion+process.shrinkingConePFTauDiscriminationAgainstElectron+process.shrinkingConePFTauDiscriminationAgainstMuon)


process.pfElectronIsoDepositsSequence = cms.Sequence(process.isoDepElectronWithCharged+process.isoDepElectronWithNeutral+process.isoDepElectronWithPhotons)


process.patJetFlavourId = cms.Sequence(process.patJetPartons+process.patJetPartonAssociation+process.patJetFlavourAssociation)


process.btaggingTagInfosAOD = cms.Sequence(process.impactParameterTagInfosAOD+process.secondaryVertexTagInfosAOD+process.softMuonTagInfosAOD+process.btaggingJetTagsAOD)


process.pfJetSequence = cms.Sequence(process.pfJets)


process.btaggingTagInfosCACalo = cms.Sequence(process.impactParameterTagInfosCACalo+process.secondaryVertexTagInfosCACalo+process.softMuonTagInfosCACalo+process.btaggingJetTagsCACalo)


process.recoAllGenJets = cms.Sequence(process.sisCone5GenJets+process.sisCone7GenJets+process.kt4GenJets+process.kt6GenJets+process.iterativeCone5GenJets+process.ak5GenJets+process.ak7GenJets+process.gk5GenJets+process.gk7GenJets+process.ca4GenJets+process.ca6GenJets)


process.patPhotonEcalIsolation = cms.Sequence(process.gamIsoDepositEcalFromHits+process.gamIsoFromDepsEcalFromHits)


process.pfMuonIsoDepositsSequence = cms.Sequence(process.isoDepMuonWithCharged+process.isoDepMuonWithNeutral+process.isoDepMuonWithPhotons)


process.patPFTauIsolation = cms.Sequence(process.tauIsoDepositPFCandidates+process.tauIsoDepositPFChargedHadrons+process.tauIsoDepositPFNeutralHadrons+process.tauIsoDepositPFGammas)


process.pfMuonIsolationFromDepositsSequence = cms.Sequence(process.isoValMuonWithCharged+process.isoValMuonWithNeutral+process.isoValMuonWithPhotons)


process.produceAndDiscriminateFixedConePFTaus = cms.Sequence(process.fixedConePFTauProducer+process.fixedConePFTauDiscriminationByLeadingTrackFinding+process.fixedConePFTauDiscriminationByLeadingTrackPtCut+process.fixedConePFTauDiscriminationByLeadingPionPtCut+process.fixedConePFTauDiscriminationByIsolation+process.fixedConePFTauDiscriminationByTrackIsolation+process.fixedConePFTauDiscriminationByECALIsolation+process.fixedConePFTauDiscriminationByIsolationUsingLeadingPion+process.fixedConePFTauDiscriminationByTrackIsolationUsingLeadingPion+process.fixedConePFTauDiscriminationByECALIsolationUsingLeadingPion+process.fixedConePFTauDiscriminationAgainstElectron+process.fixedConePFTauDiscriminationAgainstMuon)


process.pfTausPreSequence = cms.Sequence(process.pfJetTracksAssociatorAtVertex+process.pfTauPFJets08Region+process.pfTauPileUpVertices+process.pfTauTagInfoProducer+process.pfJetsPiZeros+process.pfJetsLegacyTaNCPiZeros+process.pfJetsLegacyHPSPiZeros)


process.inclusiveVertexing = cms.Sequence(process.inclusiveVertexFinder+process.vertexMerger+process.inclusiveVertices)


process.pfPileUpCandidatesSequence = cms.Sequence(process.pfPileUpCandidates+process.pfPUChargedCandidates+process.pfAllChargedCandidates)


process.pfNoPileUpSequence = cms.Sequence(process.pfPileUp+process.pfNoPileUp)


process.btaggingJetTagsAK7Calo = cms.Sequence(process.jetBProbabilityBJetTagsAK7Calo+process.jetProbabilityBJetTagsAK7Calo+process.trackCountingHighPurBJetTagsAK7Calo+process.trackCountingHighEffBJetTagsAK7Calo+process.simpleSecondaryVertexHighEffBJetTagsAK7Calo+process.simpleSecondaryVertexHighPurBJetTagsAK7Calo+process.combinedSecondaryVertexBJetTagsAK7Calo+process.combinedSecondaryVertexMVABJetTagsAK7Calo+process.softMuonBJetTagsAK7Calo+process.softMuonByPtBJetTagsAK7Calo+process.softMuonByIP3dBJetTagsAK7Calo)


process.pfTausBaseSequence = cms.Sequence(process.pfTausBase+process.pfTausBaseDiscriminationByLeadingTrackFinding+process.pfTausBaseDiscriminationByIsolation+process.pfTausBaseDiscriminationByLeadingPionPtCut)


process.recoTauClassicFixedConeSequence = cms.Sequence(process.recoTauCommonSequence+process.ak5PFJetsRecoTauPiZeros+process.produceAndDiscriminateFixedConePFTaus)


process.btaggingTagInfosCAPF = cms.Sequence(process.impactParameterTagInfosCAPF+process.secondaryVertexTagInfosCAPF+process.softMuonTagInfosCAPF+process.btaggingJetTagsCAPF)


process.patDefaultSequenceTrigger = cms.Sequence(process.patTrigger)


process.btaggingJetTagssubCAPF = cms.Sequence(process.jetBProbabilityBJetTagssubCAPF+process.jetProbabilityBJetTagssubCAPF+process.trackCountingHighPurBJetTagssubCAPF+process.trackCountingHighEffBJetTagssubCAPF+process.simpleSecondaryVertexHighEffBJetTagssubCAPF+process.simpleSecondaryVertexHighPurBJetTagssubCAPF+process.combinedSecondaryVertexBJetTagssubCAPF+process.combinedSecondaryVertexMVABJetTagssubCAPF+process.softMuonBJetTagssubCAPF+process.softMuonByPtBJetTagssubCAPF+process.softMuonByIP3dBJetTagssubCAPF)


process.patJetCorrections = cms.Sequence(process.patJetCorrFactors)


process.makePatMHTs = cms.Sequence(process.patMHTs)


process.pfTauSequence = cms.Sequence(process.pfTausPreSequence+process.pfTausBaseSequence+process.pfTaus)


process.genJetParticles = cms.Sequence(process.genParticlesForJets)


process.MetType1Corrections = cms.Sequence(process.metJESCorIC5CaloJet+process.metJESCorKT4CaloJet+process.metJESCorKT6CaloJet+process.metJESCorAK5CaloJet+process.metJESCorAK7CaloJet+process.metJESCorSC5CaloJet+process.metJESCorSC7CaloJet)


process.eIdSequence = cms.Sequence(process.eidRobustLoose+process.eidRobustTight+process.eidRobustHighEnergy+process.eidLoose+process.eidTight)


process.pfCandsForIsolationSequence = cms.Sequence(process.pfNoPileUpSequence+process.pfSortByTypeSequence+process.pfPileUpCandidatesSequence)


process.patElectronEcalIsolation = cms.Sequence(process.eleIsoDepositEcalFromHits+process.eleIsoFromDepsEcalFromHitsByCrystal)


process.patDefaultSequenceTriggerEvent = cms.Sequence(process.patTriggerEvent)


process.recoTauHPSTancSequence = cms.Sequence(process.recoTauCommonSequence+process.ak5PFJetsLegacyHPSPiZeros+process.combinatoricRecoTaus+process.hpsTancTauInitialSequence+process.hpsTancTauDiscriminantSequence)


process.pfMuonIsolationSequence = cms.Sequence(process.pfMuonIsoDepositsSequence+process.pfMuonIsolationFromDepositsSequence)


process.hiRecoGenJets = cms.Sequence(process.iterativeCone5HiGenJets+process.iterativeCone7HiGenJets+process.ak5HiGenJets+process.ak7HiGenJets+process.kt4HiGenJets+process.kt6HiGenJets)


process.patPhotonHcalIsolation = cms.Sequence(process.gamIsoDepositHcalFromTowers+process.gamIsoFromDepsHcalFromTowers)


process.produceShrinkingConeDiscriminationByTauNeuralClassifier = cms.Sequence(process.shrinkingConePFTauDiscriminationByTaNC+process.shrinkingConePFTauDiscriminationByTaNCfrOnePercent+process.shrinkingConePFTauDiscriminationByTaNCfrHalfPercent+process.shrinkingConePFTauDiscriminationByTaNCfrQuarterPercent+process.shrinkingConePFTauDiscriminationByTaNCfrTenthPercent)


process.pfElectronIsolationFromDepositsSequence = cms.Sequence(process.isoValElectronWithCharged+process.isoValElectronWithNeutral+process.isoValElectronWithPhotons)


process.patMETCorrections = cms.Sequence(process.metJESCorAK5CaloJet+process.metJESCorAK5CaloJetMuons)


process.recoTauClassicShrinkingConeSequence = cms.Sequence(process.recoTauCommonSequence+process.ak5PFJetsLegacyTaNCPiZeros+process.produceAndDiscriminateShrinkingConePFTaus)


process.btaggingAOD = cms.Sequence(process.btaggingTagInfosAOD)


process.patElectronIsolation = cms.Sequence(process.patElectronTrackIsolation+process.patElectronEcalIsolation+process.patElectronHcalIsolation)


process.patJetMETCorrections = cms.Sequence(process.patJetCorrections)


process.pfMuonSequence = cms.Sequence(process.pfAllMuons+process.pfMuonsFromVertex+process.pfSelectedMuons+process.pfMuonIsolationSequence+process.pfIsolatedMuons)


process.btaggingCACalo = cms.Sequence(process.btaggingTagInfosCACalo)


process.patShrinkingConePFTauDiscrimination = cms.Sequence(process.shrinkingConePFTauDiscriminationByLeadingTrackFinding+process.shrinkingConePFTauDiscriminationByLeadingTrackPtCut+process.shrinkingConePFTauDiscriminationByLeadingPionPtCut+process.shrinkingConePFTauDiscriminationByIsolation+process.shrinkingConePFTauDiscriminationByTrackIsolation+process.shrinkingConePFTauDiscriminationByECALIsolation+process.shrinkingConePFTauDiscriminationByIsolationUsingLeadingPion+process.shrinkingConePFTauDiscriminationByTrackIsolationUsingLeadingPion+process.shrinkingConePFTauDiscriminationByECALIsolationUsingLeadingPion+process.shrinkingConePFTauDiscriminationAgainstElectron+process.shrinkingConePFTauDiscriminationAgainstMuon+process.produceShrinkingConeDiscriminationByTauNeuralClassifier)


process.recoTauClassicHPSSequence = cms.Sequence(process.recoTauCommonSequence+process.ak5PFJetsLegacyHPSPiZeros+process.combinatoricRecoTaus+process.produceAndDiscriminateHPSPFTaus)


process.patPFCandidateIsoDepositSelection = cms.Sequence(process.pfNoPileUpSequence+process.pfAllNeutralHadrons+process.pfAllChargedHadrons+process.pfAllPhotons)


process.makePatTaus = cms.Sequence(process.patPFTauIsolation+process.patTaus)


process.recoTauClassicShrinkingConeMVASequence = cms.Sequence(process.produceShrinkingConeDiscriminationByTauNeuralClassifier)


process.btaggingTagInfosAK7PF = cms.Sequence(process.impactParameterTagInfosAK7PF+process.secondaryVertexTagInfosAK7PF+process.softMuonTagInfosAK7PF+process.btaggingJetTagsAK7PF)


process.btaggingAK7PF = cms.Sequence(process.btaggingTagInfosAK7PF)


process.makePatMETs = cms.Sequence(process.patMETCorrections+process.patMETs)


process.patPhotonIsolation = cms.Sequence(process.patPhotonTrackIsolation+process.patPhotonEcalIsolation+process.patPhotonHcalIsolation)


process.btaggingCAPF = cms.Sequence(process.btaggingTagInfosCAPF)


process.btaggingTagInfossubCAPF = cms.Sequence(process.impactParameterTagInfossubCAPF+process.secondaryVertexTagInfossubCAPF+process.softMuonTagInfossubCAPF+process.btaggingJetTagssubCAPF)


process.PFTau = cms.Sequence(process.recoTauCommonSequence+process.recoTauClassicShrinkingConeSequence+process.recoTauClassicHPSSequence+process.recoTauClassicShrinkingConeMVASequence+process.recoTauHPSTancSequence)


process.btaggingTagInfosAK5PF = cms.Sequence(process.impactParameterTagInfosAK5PF+process.secondaryVertexTagInfosAK5PF+process.softMuonTagInfosAK5PF+process.btaggingJetTagsAK5PF)


process.btaggingTagInfosAK7Calo = cms.Sequence(process.impactParameterTagInfosAK7Calo+process.secondaryVertexTagInfosAK7Calo+process.softMuonTagInfosAK7Calo+process.btaggingJetTagsAK7Calo)


process.pfElectronIsolationSequence = cms.Sequence(process.pfElectronIsoDepositsSequence+process.pfElectronIsolationFromDepositsSequence)


process.makePatJets = cms.Sequence(process.patJetCorrections+process.patJetCharge+process.patJets)


process.btaggingsubCAPF = cms.Sequence(process.btaggingTagInfossubCAPF)


process.patCandidates = cms.Sequence(process.makePatElectrons+process.makePatMuons+process.makePatTaus+process.makePatPhotons+process.makePatJets+process.makePatMETs+process.patCandidateSummary)


process.pfElectronSequence = cms.Sequence(process.pfAllElectrons+process.pfElectronsFromVertex+process.pfSelectedElectrons+process.pfElectronIsolationSequence+process.pfIsolatedElectrons)


process.patPF2PATSequence = cms.Sequence(process.pfNoPileUpSequence+process.pfAllNeutralHadrons+process.pfAllChargedHadrons+process.pfAllPhotons+process.pfMuonSequence+process.pfNoMuon+process.pfElectronSequence+process.pfNoElectron+process.pfJets+process.pfNoJet+process.pfTauSequence+process.pfNoTau+process.pfMET+process.patElectrons+process.patMuons+process.patPFCandidateIsoDepositSelection+process.patPFTauIsolation+process.patShrinkingConePFTauDiscrimination+process.patTaus+process.kt6PFJets+process.patJetCorrFactors+process.jetTracksAssociatorAtVertex+process.impactParameterTagInfosAOD+process.secondaryVertexTagInfosAOD+process.softMuonTagInfosAOD+process.jetBProbabilityBJetTagsAOD+process.jetProbabilityBJetTagsAOD+process.trackCountingHighPurBJetTagsAOD+process.trackCountingHighEffBJetTagsAOD+process.simpleSecondaryVertexHighEffBJetTagsAOD+process.simpleSecondaryVertexHighPurBJetTagsAOD+process.combinedSecondaryVertexBJetTagsAOD+process.combinedSecondaryVertexMVABJetTagsAOD+process.softMuonBJetTagsAOD+process.softMuonByPtBJetTagsAOD+process.softMuonByIP3dBJetTagsAOD+process.patJetCharge+process.patJets+process.patMETs+process.patPFParticles+process.patCandidateSummary+process.selectedPatElectrons+process.selectedPatMuons+process.selectedPatTaus+process.selectedPatJets+process.selectedPatPFParticles+process.selectedPatCandidateSummary+process.countPatElectrons+process.countPatMuons+process.countPatTaus+process.countPatLeptons+process.countPatJets+process.countPatPFParticles)


process.PF2PAT = cms.Sequence(process.pfNoPileUpSequence+process.pfAllNeutralHadrons+process.pfAllChargedHadrons+process.pfAllPhotons+process.pfMuonSequence+process.pfNoMuon+process.pfElectronSequence+process.pfNoElectron+process.pfJetSequence+process.pfNoJet+process.pfTauSequence+process.pfNoTau+process.pfMET)


process.btaggingAK7Calo = cms.Sequence(process.btaggingTagInfosAK7Calo)


process.btaggingAK5PF = cms.Sequence(process.btaggingTagInfosAK5PF)


process.patDefaultSequence = cms.Sequence(process.patElectrons+process.patMuons+process.patPFCandidateIsoDepositSelection+process.patPFTauIsolation+process.patShrinkingConePFTauDiscrimination+process.patTaus+process.kt6PFJets+process.kt6PFJets+process.patJetCorrFactors+process.kt6PFJets+process.patJetCorrFactorsAK7PF+process.kt6PFJets+process.patJetCorrFactorsAK5PF+process.kt6PFJets+process.patJetCorrFactorsAK7Calo+process.kt6PFJets+process.patJetCorrFactorssubCAPF+process.kt6PFJets+process.patJetCorrFactorsCAPF+process.kt6PFJets+process.patJetCorrFactorsCACalo+process.jetTracksAssociatorAtVertex+process.btaggingAOD+process.btaggingAOD+process.jetTracksAssociatorAtVertexCACalo+process.btaggingCACalo+process.jetTracksAssociatorAtVertexCAPF+process.btaggingCAPF+process.jetTracksAssociatorAtVertexsubCAPF+process.btaggingsubCAPF+process.jetTracksAssociatorAtVertexAK7Calo+process.btaggingAK7Calo+process.jetTracksAssociatorAtVertexAK5PF+process.btaggingAK5PF+process.jetTracksAssociatorAtVertexAK7PF+process.btaggingAK7PF+process.jetTracksAssociatorAtVertex+process.btaggingAOD+process.patJetCharge+process.patJetChargeAK7PF+process.patJetChargeAK5PF+process.patJetChargeAK7Calo+process.patJetChargesubCAPF+process.patJetChargeCAPF+process.patJetChargeCACalo+process.patJets+process.patJetsAK7PF+process.patJetsAK5PF+process.patJetsAK7Calo+process.patJetssubCAPF+process.patJetsCAPF+process.patJetsCACalo+process.patMETs+process.patMETsPF+process.patMETsTC+process.patPFParticles+process.patCandidateSummary+process.selectedPatElectrons+process.selectedPatMuons+process.selectedPatTaus+process.selectedPatJets+process.selectedPatJetsAK7PF+process.selectedPatJetsAK5PF+process.selectedPatJetsAK7Calo+process.selectedPatJetssubCAPF+process.selectedPatJetsCAPF+process.selectedPatJetsCACalo+process.selectedPatPFParticles+process.selectedPatCandidateSummary+process.countPatElectrons+process.countPatMuons+process.countPatTaus+process.countPatLeptons+process.countPatJets+process.countPatPFParticles+process.patDefaultSequenceTrigger+process.patDefaultSequenceTriggerEvent)


process.nTuplizePath = cms.Path(process.HLTQuadJet60)


process.p = cms.Path(process.hltFilter+process.goodOfflinePrimaryVertices+process.PF2PAT+process.pfCandsForIsolationSequence+process.muonPFIsolationSequence+process.electronPFIsolationSequence+process.ak5CaloJets+process.ak7CaloJets+process.kt6PFJets+process.kt6PFJets25+process.ak5PFJets+process.ak7PFJets+process.caTopCaloJets+process.caTopPFJets+process.CAsubJetsProducer+process.eidSequence+process.patDefaultSequence+process.selectedPatMuonsWithIso+process.selectedPatElectronsWithIso+process.cleanPatJetsAK5PF+process.patMETsHT+process.pfMETNoPU+process.pfNoPileUpCharge+process.pfMETNoPUCharge+process.leptonTrigMatch+process.inclusiveVertexing+process.inclusiveMergedVertices+process.selectedVertices+process.bcandidates+process.HbbAnalyzerNew)


process.hbhepath = cms.Path(process.HBHENoiseFilter)


process.ecalFilter = cms.Path(process.EcalDeadCellEventFilter)


process.e = cms.EndPath(process.out1)


process.BtagPerformanceESProducer_BTAGCSVL = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGCSVLwp_v6_offline'),
    ComponentName = cms.string('BTAGCSVL'),
    PayloadName = cms.string('BTagBTAGCSVLtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGCSVM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGCSVMwp_v6_offline'),
    ComponentName = cms.string('BTAGCSVM'),
    PayloadName = cms.string('BTagBTAGCSVMtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGCSVT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGCSVTwp_v6_offline'),
    ComponentName = cms.string('BTAGCSVT'),
    PayloadName = cms.string('BTagBTAGCSVTtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGJBPL = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGJBPLwp_v6_offline'),
    ComponentName = cms.string('BTAGJBPL'),
    PayloadName = cms.string('BTagBTAGJBPLtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGJBPM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGJBPMwp_v6_offline'),
    ComponentName = cms.string('BTAGJBPM'),
    PayloadName = cms.string('BTagBTAGJBPMtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGJBPT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGJBPTwp_v6_offline'),
    ComponentName = cms.string('BTAGJBPT'),
    PayloadName = cms.string('BTagBTAGJBPTtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGJPL = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGJPLwp_v6_offline'),
    ComponentName = cms.string('BTAGJPL'),
    PayloadName = cms.string('BTagBTAGJPLtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGJPM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGJPMwp_v6_offline'),
    ComponentName = cms.string('BTAGJPM'),
    PayloadName = cms.string('BTagBTAGJPMtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGJPT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGJPTwp_v6_offline'),
    ComponentName = cms.string('BTAGJPT'),
    PayloadName = cms.string('BTagBTAGJPTtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGSSVHEM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGSSVHEMwp_v6_offline'),
    ComponentName = cms.string('BTAGSSVHEM'),
    PayloadName = cms.string('BTagBTAGSSVHEMtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGSSVHPT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGSSVHPTwp_v6_offline'),
    ComponentName = cms.string('BTAGSSVHPT'),
    PayloadName = cms.string('BTagBTAGSSVHPTtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGTCHEL = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGTCHELwp_v6_offline'),
    ComponentName = cms.string('BTAGTCHEL'),
    PayloadName = cms.string('BTagBTAGTCHELtable_v6_offline')
)


process.BtagPerformanceESProducer_BTAGTCHEM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGTCHEMwp_v7_offline'),
    ComponentName = cms.string('BTAGTCHEM'),
    PayloadName = cms.string('BTagBTAGTCHEMtable_v7_offline')
)


process.BtagPerformanceESProducer_BTAGTCHPM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGTCHPMwp_v7_offline'),
    ComponentName = cms.string('BTAGTCHPM'),
    PayloadName = cms.string('BTagBTAGTCHPMtable_v7_offline')
)


process.BtagPerformanceESProducer_BTAGTCHPT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagBTAGTCHPTwp_v6_offline'),
    ComponentName = cms.string('BTAGTCHPT'),
    PayloadName = cms.string('BTagBTAGTCHPTtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGCSVL = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGCSVLwp_v6_offline'),
    ComponentName = cms.string('MISTAGCSVL'),
    PayloadName = cms.string('BTagMISTAGCSVLtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGCSVM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGCSVMwp_v6_offline'),
    ComponentName = cms.string('MISTAGCSVM'),
    PayloadName = cms.string('BTagMISTAGCSVMtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGCSVT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGCSVTwp_v6_offline'),
    ComponentName = cms.string('MISTAGCSVT'),
    PayloadName = cms.string('BTagMISTAGCSVTtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGJBPL = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGJBPLwp_v6_offline'),
    ComponentName = cms.string('MISTAGJBPL'),
    PayloadName = cms.string('BTagMISTAGJBPLtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGJBPM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGJBPMwp_v6_offline'),
    ComponentName = cms.string('MISTAGJBPM'),
    PayloadName = cms.string('BTagMISTAGJBPMtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGJBPT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGJBPTwp_v6_offline'),
    ComponentName = cms.string('MISTAGJBPT'),
    PayloadName = cms.string('BTagMISTAGJBPTtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGJPL = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGJPLwp_v6_offline'),
    ComponentName = cms.string('MISTAGJPL'),
    PayloadName = cms.string('BTagMISTAGJPLtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGJPM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGJPMwp_v6_offline'),
    ComponentName = cms.string('MISTAGJPM'),
    PayloadName = cms.string('BTagMISTAGJPMtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGJPT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGJPTwp_v6_offline'),
    ComponentName = cms.string('MISTAGJPT'),
    PayloadName = cms.string('BTagMISTAGJPTtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGSSVHEM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGSSVHEMwp_v6_offline'),
    ComponentName = cms.string('MISTAGSSVHEM'),
    PayloadName = cms.string('BTagMISTAGSSVHEMtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGSSVHPT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGSSVHPTwp_v6_offline'),
    ComponentName = cms.string('MISTAGSSVHPT'),
    PayloadName = cms.string('BTagMISTAGSSVHPTtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGTCHEL = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGTCHELwp_v6_offline'),
    ComponentName = cms.string('MISTAGTCHEL'),
    PayloadName = cms.string('BTagMISTAGTCHELtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGTCHEM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGTCHEMwp_v6_offline'),
    ComponentName = cms.string('MISTAGTCHEM'),
    PayloadName = cms.string('BTagMISTAGTCHEMtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGTCHPM = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGTCHPMwp_v6_offline'),
    ComponentName = cms.string('MISTAGTCHPM'),
    PayloadName = cms.string('BTagMISTAGTCHPMtable_v6_offline')
)


process.BtagPerformanceESProducer_MISTAGTCHPT = cms.ESProducer("BtagPerformanceESProducer",
    WorkingPointName = cms.string('BTagMISTAGTCHPTwp_v6_offline'),
    ComponentName = cms.string('MISTAGTCHPT'),
    PayloadName = cms.string('BTagMISTAGTCHPTtable_v6_offline')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string(''),
    useDDD = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    alignmentsLabel = cms.string(''),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP")


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    label = cms.untracked.string('parametrizedField')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    useDDD = cms.untracked.bool(False),
    compatibiltyWith11 = cms.untracked.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle')
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    fromDDD = cms.bool(False)
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
    overrideMasterSector = cms.bool(False),
    useParametrizedTrackerField = cms.bool(True),
    label = cms.untracked.string(''),
    version = cms.string('grid_1103l_090322_3_8t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('parametrizedField'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    rootDDName = cms.string('cms:OCMS'),
    label = cms.string('Extended')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.combinedMVA = cms.ESProducer("CombinedMVAJetTagESProducer",
    useCategories = cms.bool(False),
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        variables = cms.bool(False),
        jetTagComputer = cms.string('jetProbability')
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            variables = cms.bool(False),
            jetTagComputer = cms.string('combinedSecondaryVertex')
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            variables = cms.bool(False),
            jetTagComputer = cms.string('softMuon')
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            variables = cms.bool(False),
            jetTagComputer = cms.string('softElectron')
        ))
)


process.combinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    useTrackWeights = cms.bool(True),
    pseudoMultiplicityMin = cms.uint32(2),
    correctVertexMass = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    charmCut = cms.double(1.5),
    vertexFlip = cms.bool(False),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackMultiplicityMin = cms.uint32(3),
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip2dSig'),
    trackFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    useCategories = cms.bool(True),
    categoryVariableName = cms.string('vertexCategory')
)


process.combinedSecondaryVertexMVA = cms.ESProducer("CombinedSecondaryVertexESProducer",
    useTrackWeights = cms.bool(True),
    pseudoMultiplicityMin = cms.uint32(2),
    correctVertexMass = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    charmCut = cms.double(1.5),
    vertexFlip = cms.bool(False),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackMultiplicityMin = cms.uint32(3),
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip2dSig'),
    trackFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVMVARecoVertex', 
        'CombinedSVMVAPseudoVertex', 
        'CombinedSVMVANoVertex'),
    useCategories = cms.bool(True),
    categoryVariableName = cms.string('vertexCategory')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.vuint32(1, 2046, 0, 0, 0, 
        64512),
    timeThresh = cms.double(2.0),
    flagMask = cms.vuint32(1, 114, 896, 4, 49152, 
        3080)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.ghostTrack = cms.ESProducer("GhostTrackESProducer",
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    charmCut = cms.double(1.5),
    trackSort = cms.string('sip2dSig'),
    minimumTrackWeight = cms.double(0.5),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    calibrationRecords = cms.vstring('GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'),
    useCategories = cms.bool(True),
    categoryVariableName = cms.string('vertexCategory')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    file = cms.untracked.string(''),
    dump = cms.untracked.vstring('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    useDDD = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    alignmentsLabel = cms.string('fakeForIdeal'),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(False)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string('fakeForIdeal')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string('fakeForIdeal')
)


process.impactParameterMVAComputer = cms.ESProducer("GenericMVAJetTagESProducer",
    useCategories = cms.bool(False),
    calibrationRecord = cms.string('ImpactParameterMVA')
)


process.jetBProbability = cms.ESProducer("JetBProbabilityESProducer",
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    trackIpSign = cms.int32(1),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    maximumDecayLength = cms.double(5.0)
)


process.jetProbability = cms.ESProducer("JetProbabilityESProducer",
    deltaR = cms.double(0.3),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    trackIpSign = cms.int32(1),
    minimumProbability = cms.double(0.005),
    maximumDecayLength = cms.double(5.0)
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.125),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    printDebug = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    APVGain = cms.VPSet(cms.PSet(
        Record = cms.string('SiStripApvGainRcd'),
        NormalizationFactor = cms.untracked.double(1.0),
        Label = cms.untracked.string('')
    ), 
        cms.PSet(
            Record = cms.string('SiStripApvGain2Rcd'),
            NormalizationFactor = cms.untracked.double(1.0),
            Label = cms.untracked.string('')
        )),
    AutomaticNormalization = cms.bool(False)
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    appendToDataLabel = cms.string(''),
    PrintDebugOutput = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        ))
)


process.simpleSecondaryVertex2Trk = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    useSignificance = cms.bool(True),
    use3d = cms.bool(True)
)


process.simpleSecondaryVertex3Trk = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    useSignificance = cms.bool(True),
    use3d = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.softElectron = cms.ESProducer("ElectronTaggerESProducer",
    ipSign = cms.string('any')
)


process.softLeptonByIP3d = cms.ESProducer("LeptonTaggerByIPESProducer",
    use3d = cms.bool(True),
    ipSign = cms.string('any')
)


process.softLeptonByPt = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softMuon = cms.ESProducer("MuonTaggerESProducer",
    ipSign = cms.string('any')
)


process.softMuonNoIP = cms.ESProducer("MuonTaggerNoIPESProducer",
    ipSign = cms.string('any')
)


process.trackCounting3D2nd = cms.ESProducer("TrackCountingESProducer",
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    maximumDecayLength = cms.double(5.0),
    nthTrack = cms.int32(2)
)


process.trackCounting3D3rd = cms.ESProducer("TrackCountingESProducer",
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    maximumDecayLength = cms.double(5.0),
    nthTrack = cms.int32(3)
)


process.BTagRecord = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord'),
    firstValid = cms.vuint32(1)
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    toGet = cms.VPSet(),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    globaltag = cms.string('GR_R_42_V19::All')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.PoolDBESSourcebtag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('PerformancePayloadRecord'),
        tag = cms.string('BTagBTAGCSVLtable_v6_offline'),
        label = cms.untracked.string('BTagBTAGCSVLtable_v6_offline')
    ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGCSVLwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGCSVLwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGCSVMtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGCSVMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGCSVMwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGCSVMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGCSVTtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGCSVTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGCSVTwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGCSVTwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGJBPLtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGJBPLtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGJBPLwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGJBPLwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGJBPMtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGJBPMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGJBPMwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGJBPMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGJBPTtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGJBPTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGJBPTwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGJBPTwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGJPLtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGJPLtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGJPLwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGJPLwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGJPMtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGJPMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGJPMwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGJPMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGJPTtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGJPTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGJPTwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGJPTwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGSSVHEMtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGSSVHEMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGSSVHEMwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGSSVHEMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGSSVHPTtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGSSVHPTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGSSVHPTwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGSSVHPTwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGTCHELtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGTCHELtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGTCHELwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGTCHELwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGTCHEMtable_v7_offline'),
            label = cms.untracked.string('BTagBTAGTCHEMtable_v7_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGTCHEMwp_v7_offline'),
            label = cms.untracked.string('BTagBTAGTCHEMwp_v7_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGTCHPMtable_v7_offline'),
            label = cms.untracked.string('BTagBTAGTCHPMtable_v7_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGTCHPMwp_v7_offline'),
            label = cms.untracked.string('BTagBTAGTCHPMwp_v7_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagBTAGTCHPTtable_v6_offline'),
            label = cms.untracked.string('BTagBTAGTCHPTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagBTAGTCHPTwp_v6_offline'),
            label = cms.untracked.string('BTagBTAGTCHPTwp_v6_offline')
        ))
)


process.PoolDBESSourcemistag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('PerformancePayloadRecord'),
        tag = cms.string('BTagMISTAGCSVLtable_v6_offline'),
        label = cms.untracked.string('BTagMISTAGCSVLtable_v6_offline')
    ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGCSVLwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGCSVLwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGCSVMtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGCSVMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGCSVMwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGCSVMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGCSVTtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGCSVTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGCSVTwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGCSVTwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGJBPLtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJBPLtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGJBPLwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJBPLwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGJBPMtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJBPMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGJBPMwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJBPMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGJBPTtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJBPTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGJBPTwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJBPTwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGJPLtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJPLtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGJPLwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJPLwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGJPMtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJPMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGJPMwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJPMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGJPTtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJPTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGJPTwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGJPTwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGSSVHEMtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGSSVHEMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGSSVHEMwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGSSVHEMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGSSVHPTtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGSSVHPTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGSSVHPTwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGSSVHPTwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGTCHELtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGTCHELtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGTCHELwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGTCHELwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGTCHEMtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGTCHEMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGTCHEMwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGTCHEMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGTCHPMtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGTCHPMtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGTCHPMwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGTCHPMwp_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformancePayloadRecord'),
            tag = cms.string('BTagMISTAGTCHPTtable_v6_offline'),
            label = cms.untracked.string('BTagMISTAGTCHPTtable_v6_offline')
        ), 
        cms.PSet(
            record = cms.string('PerformanceWPRecord'),
            tag = cms.string('BTagMISTAGTCHPTwp_v6_offline'),
            label = cms.untracked.string('BTagMISTAGTCHPTwp_v6_offline')
        ))
)


process.ak5CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloL6SLB')
)


process.ak5CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak5CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Offset', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Offset', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.ak5CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloL6SLB')
)


process.ak5CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    level = cms.string('L2Relative'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    era = cms.string('Spring10')
)


process.ak5CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    level = cms.string('L3Absolute'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    era = cms.string('Spring10')
)


process.ak5CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ak5CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ak5CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.ak5CaloResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    level = cms.string('L2L3Residual'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    era = cms.string('Spring10DataV2')
)


process.ak5JPTL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5JPTL1Fastjet', 
        'ak5JPTL1Offset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5JPTL1Fastjet', 
        'ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak5JPTL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5JPTL1Offset', 
        'ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5JPTL1Offset', 
        'ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.ak5JPTL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Summer10'),
    section = cms.string(''),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2Relative')
)


process.ak5JPTL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Summer10'),
    section = cms.string(''),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L3Absolute')
)


process.ak5JPTResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2L3Residual')
)


process.ak5L1JPTOffset = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Summer10'),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset')
)


process.ak5PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFL6SLB')
)


process.ak5PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak5PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.ak5PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFL6SLB')
)


process.ak5PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ak5PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ak5PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.ak5PFResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak5TrackL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5TrackL2Relative', 
        'ak5TrackL3Absolute')
)


process.ak5TrackL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5TrackL2Relative', 
        'ak5TrackL3Absolute')
)


process.ak5TrackL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak5TrackL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak7CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.ak7CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.ak7CaloResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7JPTL1Fastjet', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak7JPTL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7JPTL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.ak7JPTL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7L1JPTOffset = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Summer10'),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset')
)


process.ak7PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak7PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.ak7PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.ak7PFResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10DataV2'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.eegeom = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd'),
    firstValid = cms.vuint32(1)
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring('GainWidths')
)


process.essourceEcalSev = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd'),
    firstValid = cms.vuint32(1)
)


process.ic5CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ic5CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.ic5CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.ic5CaloResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ic5PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.ic5PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.ic5PFResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10DataV2'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.kt4CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.kt4CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.kt4CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.kt4CaloResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.kt4PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.kt4PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.kt4PFResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10DataV2'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.kt6CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.kt6CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.kt6CaloResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.kt6PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Fall10')
)


process.kt6PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.kt6PFResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10DataV2'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.magfield = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMagneticField.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml', 
        'Geometry/CMSCommonData/data/materials.xml'),
    rootNodeName = cms.string('cmsMagneticField:MAGF')
)


process.prefer("magfield")

process.AnomalousCellParameters = cms.PSet(
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999)
)

process.CATopJetParameters = cms.PSet(
    ptFracBins = cms.vdouble(0.05, 0.05, 0.05),
    rBins = cms.vdouble(0.8, 0.8, 0.8),
    algorithm = cms.int32(1),
    etFrac = cms.double(0.7),
    useMaxTower = cms.bool(False),
    deltarBins = cms.vdouble(0.19, 0.19, 0.19),
    nCellBins = cms.vdouble(1.9, 1.9, 1.9),
    useAdjacency = cms.int32(2),
    sumEtBins = cms.vdouble(0, 1600, 2600),
    centralEtaCut = cms.double(2.5),
    debugLevel = cms.untracked.int32(0),
    sumEtEtaCut = cms.double(3.0),
    jetCollInstanceName = cms.string('caTopSubJets'),
    verbose = cms.bool(False)
)

process.CaloJetParameters = cms.PSet(
    Active_Area_Repeats = cms.int32(1),
    doOutputJets = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(True),
    minSeed = cms.uint32(14327),
    voronoiRfact = cms.double(-0.9),
    Ghost_EtaMax = cms.double(5.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    inputEtMin = cms.double(0.3),
    doPUOffsetCorr = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    src = cms.InputTag("towerMaker"),
    doAreaDiskApprox = cms.bool(False),
    jetType = cms.string('CaloJet'),
    radiusPU = cms.double(0.5)
)

process.CondDBCommon = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    connect = cms.string('protocol://db/schema')
)

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    )
)

process.GenJetParameters = cms.PSet(
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doPUOffsetCorr = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetType = cms.string('GenJet'),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    inputEMin = cms.double(0.0)
)

process.METSignificance_params = cms.PSet(
    resolutionsEra = cms.string('Spring10'),
    HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
    EE_PhiResPar = cms.vdouble(0.02511),
    jdpt9 = cms.vdouble(0.843, 0.885, 1.245, 1.665, 1.944, 
        1.981, 1.972, 2.875, 3.923, 7.51),
    jdpt8 = cms.vdouble(0.889, 0.939, 1.166, 1.365, 1.553, 
        1.805, 2.06, 2.22, 2.268, 2.247),
    jdpt7 = cms.vdouble(1.094, 1.139, 1.436, 1.672, 1.831, 
        2.05, 2.267, 2.549, 2.785, 2.86),
    jdpt6 = cms.vdouble(1.213, 1.298, 1.716, 2.015, 2.191, 
        2.612, 2.863, 2.879, 2.925, 2.902),
    jdpt5 = cms.vdouble(1.049, 1.149, 1.607, 1.869, 2.012, 
        2.219, 2.289, 2.412, 2.695, 2.865),
    jdpt4 = cms.vdouble(0.85, 0.961, 1.337, 1.593, 1.854, 
        2.005, 2.209, 2.533, 2.812, 3.047),
    jdpt3 = cms.vdouble(0.929, 1.04, 1.46, 1.74, 2.042, 
        2.289, 2.639, 2.837, 2.946, 2.971),
    jdpt2 = cms.vdouble(0.841, 0.937, 1.316, 1.605, 1.919, 
        2.295, 2.562, 2.722, 2.943, 3.293),
    jdpt1 = cms.vdouble(0.718, 0.813, 1.133, 1.384, 1.588, 
        1.841, 2.115, 2.379, 2.508, 2.772),
    jdpt0 = cms.vdouble(0.749, 0.829, 1.099, 1.355, 1.584, 
        1.807, 2.035, 2.217, 2.378, 2.591),
    HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
    HF_PhiResPar = cms.vdouble(0.05022),
    PF_PhiResType7 = cms.vdouble(0.02511),
    HE_PhiResPar = cms.vdouble(0.02511),
    EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_PhiResType3 = cms.vdouble(0.002),
    HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
    resolutionsAlgo = cms.string('AK5PF'),
    PF_PhiResType6 = cms.vdouble(0.02511),
    HB_PhiResPar = cms.vdouble(0.02511),
    PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
    PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
    ptresolthreshold = cms.double(10.0),
    EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    jdphi8 = cms.vdouble(0.059, 0.057, 0.051, 0.044, 0.038, 
        0.035, 0.037, 0.032, 0.028, 0.028),
    EB_PhiResPar = cms.vdouble(0.00502),
    jdphi9 = cms.vdouble(0.062, 0.059, 0.053, 0.047, 0.042, 
        0.045, 0.036, 0.032, 0.034, 0.044),
    PF_PhiResType1 = cms.vdouble(0.002),
    jdphi4 = cms.vdouble(0.042, 0.042, 0.043, 0.042, 0.038, 
        0.036, 0.036, 0.033, 0.031, 0.031),
    HO_PhiResPar = cms.vdouble(0.02511),
    jdphi2 = cms.vdouble(0.04, 0.04, 0.04, 0.04, 0.04, 
        0.038, 0.036, 0.035, 0.034, 0.033),
    jdphi1 = cms.vdouble(0.034, 0.035, 0.035, 0.035, 0.035, 
        0.034, 0.031, 0.03, 0.029, 0.027),
    jdphi0 = cms.vdouble(0.034, 0.034, 0.034, 0.034, 0.032, 
        0.031, 0.028, 0.027, 0.027, 0.027),
    jdphi7 = cms.vdouble(0.077, 0.072, 0.059, 0.05, 0.045, 
        0.042, 0.039, 0.039, 0.037, 0.031),
    jdphi6 = cms.vdouble(0.084, 0.08, 0.072, 0.065, 0.066, 
        0.06, 0.051, 0.049, 0.045, 0.045),
    jdphi5 = cms.vdouble(0.069, 0.069, 0.064, 0.058, 0.053, 
        0.049, 0.049, 0.043, 0.039, 0.04),
    HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
    jdphi3 = cms.vdouble(0.042, 0.043, 0.044, 0.043, 0.041, 
        0.039, 0.039, 0.036, 0.034, 0.031),
    PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
    PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
    PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
    PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
    PF_EtResType1 = cms.vdouble(0.05, 0, 0),
    PF_EtResType3 = cms.vdouble(0.05, 0, 0),
    PF_EtResType2 = cms.vdouble(0.05, 0, 0)
)

process.ModifiedPF2PATEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_generalTracks_*_*', 
        'keep *_electronGsfTracks_*_*', 
        'keep *_genParticles_*_*', 
        'keep *_genMetTrue_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep patMuons_*_*_*', 
        'keep patElectrons_*_*_*', 
        'keep patJets_*_*_*', 
        'keep patTaus_*_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoVertexs_offlinePrimaryVertices_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_pfElectronTranslator_*_*')
)

process.OneProngNoPiZero = cms.PSet(
    applyIsolation = cms.bool(False),
    cut = cms.double(-10.0),
    computerName = cms.string('OneProngNoPiZero'),
    decayModeIndices = cms.vint32(0)
)

process.OneProngNoPiZeroIso = cms.PSet(
    applyIsolation = cms.bool(True),
    cut = cms.double(-10.0),
    computerName = cms.string('OneProngNoPiZeroIso'),
    decayModeIndices = cms.vint32(0)
)

process.OneProngOnePiZero = cms.PSet(
    applyIsolation = cms.bool(False),
    cut = cms.double(-10.0),
    computerName = cms.string('OneProngOnePiZero'),
    decayModeIndices = cms.vint32(1)
)

process.OneProngOnePiZeroIso = cms.PSet(
    applyIsolation = cms.bool(True),
    cut = cms.double(-10.0),
    computerName = cms.string('OneProngOnePiZeroIso'),
    decayModeIndices = cms.vint32(1)
)

process.OneProngTwoPiZero = cms.PSet(
    applyIsolation = cms.bool(False),
    cut = cms.double(-10.0),
    computerName = cms.string('OneProngTwoPiZero'),
    decayModeIndices = cms.vint32(2)
)

process.OneProngTwoPiZeroIso = cms.PSet(
    applyIsolation = cms.bool(True),
    cut = cms.double(-10.0),
    computerName = cms.string('OneProngTwoPiZeroIso'),
    decayModeIndices = cms.vint32(2)
)

process.PATEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_genMetTrue_*_*', 
        'keep recoGenJets_iterativeCone5GenJets_*_*', 
        'keep patElectrons_selectedLayer1Electrons_*_*', 
        'keep patMuons_selectedLayer1Muons_*_*', 
        'keep patJets_selectedLayer1Jets_*_*', 
        'keep patMETs_*_*_*', 
        'keep patTaus_selectedLayer1Taus_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*')
)

process.PF2PATEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop recoGenJets_*_*_HLT', 
        'keep *_genParticles_*_*', 
        'keep *_genMetTrue_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_pfIsolatedElectrons_*_*', 
        'keep *_pfIsolatedMuons_*_*', 
        'keep *_pfNoJet_*_*', 
        'keep recoIsoDepositedmValueMap_*_*_*', 
        'keep recoPFJets_pfNoTau_*_*', 
        'keep *_pfTaus_*_*', 
        'keep recoPFTauDiscriminator_*_*_*', 
        'keep *_offlinePrimaryVertice_*_*', 
        'keep *_pfMET_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*')
)

process.PF2PATStudiesEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoPFJets_*_*_*', 
        'keep *_decaysFromZs_*_*', 
        'keep recoPFCandidates_*_*_PF2PAT', 
        'keep recoPFCandidates_*_*_PAT', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoMuons_*_*_*', 
        'keep *_pf*_*_*')
)

process.PFJetParameters = cms.PSet(
    Active_Area_Repeats = cms.int32(1),
    doOutputJets = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    voronoiRfact = cms.double(-0.9),
    Ghost_EtaMax = cms.double(5.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doPUOffsetCorr = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    src = cms.InputTag("particleFlow"),
    doAreaDiskApprox = cms.bool(False),
    jetType = cms.string('PFJet'),
    radiusPU = cms.double(0.5)
)

process.PFTauQualityCuts = cms.PSet(
    isolationQualityCuts = cms.PSet(
        minTrackHits = cms.uint32(8),
        minTrackPt = cms.double(1.0),
        maxTrackChi2 = cms.double(100.0),
        minTrackPixelHits = cms.uint32(0),
        minGammaEt = cms.double(1.5),
        useTracksInsteadOfPFHadrons = cms.bool(False),
        maxDeltaZ = cms.double(0.2),
        maxTransverseImpactParameter = cms.double(0.03)
    ),
    signalQualityCuts = cms.PSet(
        minTrackHits = cms.uint32(3),
        minTrackPt = cms.double(0.5),
        maxTrackChi2 = cms.double(100.0),
        minTrackPixelHits = cms.uint32(0),
        minGammaEt = cms.double(0.5),
        useTracksInsteadOfPFHadrons = cms.bool(False),
        maxDeltaZ = cms.double(0.2),
        maxTransverseImpactParameter = cms.double(0.03)
    )
)

process.SingleNet = cms.PSet(
    applyIsolation = cms.bool(False),
    cut = cms.double(-10.0),
    computerName = cms.string('SingleNet'),
    decayModeIndices = cms.vint32(0, 1, 2, 10, 11)
)

process.SingleNetIso = cms.PSet(
    applyIsolation = cms.bool(True),
    cut = cms.double(-10.0),
    computerName = cms.string('SingleNetIso'),
    decayModeIndices = cms.vint32(0, 1, 2, 10, 11)
)

process.ThreeProngNoPiZero = cms.PSet(
    applyIsolation = cms.bool(False),
    cut = cms.double(-10.0),
    computerName = cms.string('ThreeProngNoPiZero'),
    decayModeIndices = cms.vint32(10)
)

process.ThreeProngNoPiZeroIso = cms.PSet(
    applyIsolation = cms.bool(True),
    cut = cms.double(-10.0),
    computerName = cms.string('ThreeProngNoPiZeroIso'),
    decayModeIndices = cms.vint32(10)
)

process.ThreeProngOnePiZero = cms.PSet(
    applyIsolation = cms.bool(False),
    cut = cms.double(-10.0),
    computerName = cms.string('ThreeProngOnePiZero'),
    decayModeIndices = cms.vint32(11)
)

process.ThreeProngOnePiZeroIso = cms.PSet(
    applyIsolation = cms.bool(True),
    cut = cms.double(-10.0),
    computerName = cms.string('ThreeProngOnePiZeroIso'),
    decayModeIndices = cms.vint32(11)
)

process.TrackAssociatorParameterBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    )
)

process.TrackAssociatorParameters = cms.PSet(
    muonMaxDistanceSigmaX = cms.double(0.0),
    muonMaxDistanceSigmaY = cms.double(0.0),
    CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
    dRHcal = cms.double(9999.0),
    dREcal = cms.double(9999.0),
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    useEcal = cms.bool(True),
    dREcalPreselection = cms.double(0.05),
    HORecHitCollectionLabel = cms.InputTag("horeco"),
    dRMuon = cms.double(9999.0),
    propagateAllDirections = cms.bool(True),
    muonMaxDistanceX = cms.double(5.0),
    muonMaxDistanceY = cms.double(5.0),
    useHO = cms.bool(True),
    trajectoryUncertaintyTolerance = cms.double(-1.0),
    usePreshower = cms.bool(False),
    DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
    EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    dRHcalPreselection = cms.double(0.2),
    useMuon = cms.bool(True),
    useCalo = cms.bool(False),
    accountForTrajectoryChangeCalo = cms.bool(False),
    EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    dRMuonPreselection = cms.double(0.2),
    truthMatch = cms.bool(False),
    HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
    useHcal = cms.bool(True)
)

process.combinedSecondaryVertexCommon = cms.PSet(
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    useTrackWeights = cms.bool(True),
    pseudoMultiplicityMin = cms.uint32(2),
    correctVertexMass = cms.bool(True),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    charmCut = cms.double(1.5),
    vertexFlip = cms.bool(False),
    minimumTrackWeight = cms.double(0.5),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackMultiplicityMin = cms.uint32(3),
    trackSort = cms.string('sip2dSig'),
    trackFlip = cms.bool(False)
)

process.discriminantConfiguration = cms.PSet(
    BinnedMaskedHcalIsolation = cms.PSet(
        vtxSource = cms.InputTag("recoTauPileUpVertices"),
        mask = cms.PSet(
            finalHcalCone = cms.double(0.08),
            ecalCone = cms.double(0.15),
            hcalCone = cms.double(0.3),
            maxSigmas = cms.double(2)
        ),
        binning = cms.VPSet(cms.PSet(
            binLowEdges = cms.vdouble(1.0, 1.79, 4.03),
            nPUVtx = cms.int32(0)
        ), 
            cms.PSet(
                binLowEdges = cms.vdouble(1.15, 1.8, 4.03),
                nPUVtx = cms.int32(1)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(1.22, 1.81, 4.03),
                nPUVtx = cms.int32(2)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(1.27, 1.83, 4.03),
                nPUVtx = cms.int32(3)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(1.31, 1.84, 4.03),
                nPUVtx = cms.int32(4)
            )),
        defaultBinning = cms.vdouble(1.31, 1.84, 4.03),
        plugin = cms.string('RecoTauDiscriminationBinnedMaskedHCALIsolation')
    ),
    InvariantOpeningAngle = cms.PSet(
        defaultRMS = cms.string('max(0.3/max(pt, 1.0), 0.005)'),
        plugin = cms.string('RecoTauDiscriminantInvariantWidth'),
        decayModes = cms.VPSet(cms.PSet(
            nPiZeros = cms.uint32(1),
            rms = cms.string('2.7e-3 + 0.23/max(pt, 1.0)'),
            nCharged = cms.uint32(1),
            mean = cms.string('5.0e-3 + 0.43/max(pt, 1.0)')
        ), 
            cms.PSet(
                nPiZeros = cms.uint32(2),
                rms = cms.string('7.5e-3 + 0.3/max(pt, 1.0)'),
                nCharged = cms.uint32(1),
                mean = cms.string('4.7e-3 + 0.9/max(pt, 1.0)')
            ), 
            cms.PSet(
                nPiZeros = cms.uint32(0),
                rms = cms.string('0.38/max(pt, 1.0)'),
                nCharged = cms.uint32(3),
                mean = cms.string('0.87/max(pt, 1.0)')
            )),
        defaultMean = cms.string('max(0.87/max(pt, 1.0), 0.005)')
    ),
    BinnedMaskedEcalIsolation = cms.PSet(
        vtxSource = cms.InputTag("recoTauPileUpVertices"),
        mask = cms.PSet(
            finalHcalCone = cms.double(0.08),
            ecalCone = cms.double(0.15),
            hcalCone = cms.double(0.3),
            maxSigmas = cms.double(2)
        ),
        binning = cms.VPSet(cms.PSet(
            binLowEdges = cms.vdouble(0.5, 0.85, 1.84),
            nPUVtx = cms.int32(0)
        ), 
            cms.PSet(
                binLowEdges = cms.vdouble(0.63, 0.91, 1.84),
                nPUVtx = cms.int32(1)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(0.7, 0.96, 1.85),
                nPUVtx = cms.int32(2)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(0.75, 0.99, 1.85),
                nPUVtx = cms.int32(3)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(0.79, 1.02, 1.86),
                nPUVtx = cms.int32(4)
            )),
        defaultBinning = cms.vdouble(0.79, 1.02, 1.86),
        plugin = cms.string('RecoTauDiscriminationBinnedMaskedECALIsolation')
    ),
    FlightPathSignificance = cms.PSet(
        discSrc = cms.InputTag("hpsTancTausDiscriminationByFlightPath"),
        plugin = cms.string('RecoTauDiscriminantFromDiscriminator')
    ),
    BinnedTrackIsolation = cms.PSet(
        vtxSource = cms.InputTag("recoTauPileUpVertices"),
        binning = cms.VPSet(cms.PSet(
            binLowEdges = cms.vdouble(0.5, 0.86, 1.87),
            nPUVtx = cms.int32(0)
        ), 
            cms.PSet(
                binLowEdges = cms.vdouble(0.51, 0.86, 1.87),
                nPUVtx = cms.int32(1)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(0.51, 0.86, 1.87),
                nPUVtx = cms.int32(2)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(0.52, 0.86, 1.87),
                nPUVtx = cms.int32(3)
            ), 
            cms.PSet(
                binLowEdges = cms.vdouble(0.52, 0.86, 1.87),
                nPUVtx = cms.int32(4)
            )),
        defaultBinning = cms.vdouble(0.52, 0.86, 1.87),
        plugin = cms.string('RecoTauDiscriminationBinnedTrackIsolation')
    )
)

process.fieldScaling = cms.PSet(
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991)
)

process.ghostTrackCommon = cms.PSet(
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    charmCut = cms.double(1.5),
    trackSort = cms.string('sip2dSig'),
    minimumTrackWeight = cms.double(0.5)
)

process.ghostTrackVertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        primcut = cms.double(2.0),
        seccut = cms.double(4.0),
        maxFitChi2 = cms.double(10.0),
        fitType = cms.string('RefitGhostTrackWithVertices'),
        mergeThreshold = cms.double(3.0),
        finder = cms.string('gtvr')
    )
)

process.hpsTancRequireDecayMode = cms.PSet(
    BooleanOperator = cms.string('and'),
    decayMode = cms.PSet(
        cut = cms.double(0.5),
        Producer = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection")
    )
)

process.j2tParametersCALO = cms.PSet(
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5),
    extrapolations = cms.InputTag("trackExtrapolator")
)

process.j2tParametersVX = cms.PSet(
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)

process.leadTrackFinding = cms.PSet(
    cut = cms.double(0.5),
    Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
)

process.looseSoftPFElectronCleanerBarrelCuts = cms.PSet(
    BarreldRGsfTrackElectronCuts = cms.vdouble(0.0, 0.017),
    BarrelEemPinRatioCuts = cms.vdouble(-0.9, 0.39),
    BarrelMVACuts = cms.vdouble(-0.1, 1.0),
    BarrelPtCuts = cms.vdouble(2.0, 9999.0)
)

process.looseSoftPFElectronCleanerForwardCuts = cms.PSet(
    ForwarddRGsfTrackElectronCuts = cms.vdouble(0.0, 0.006),
    ForwardPtCuts = cms.vdouble(2.0, 9999.0),
    ForwardMVACuts = cms.vdouble(-0.24, 1.0),
    ForwardInverseFBremCuts = cms.vdouble(1.0, 7.01)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.mediumSoftPFElectronCleanerBarrelCuts = cms.PSet(
    BarreldRGsfTrackElectronCuts = cms.vdouble(0.0, 0.0047),
    BarrelEemPinRatioCuts = cms.vdouble(-0.9, 0.54),
    BarrelMVACuts = cms.vdouble(0.6, 1.0),
    BarrelPtCuts = cms.vdouble(2.0, 9999.0)
)

process.mediumSoftPFElectronCleanerForwardCuts = cms.PSet(
    ForwarddRGsfTrackElectronCuts = cms.vdouble(0.0, 0.003),
    ForwardPtCuts = cms.vdouble(2.0, 9999.0),
    ForwardMVACuts = cms.vdouble(0.37, 1.0),
    ForwardInverseFBremCuts = cms.vdouble(1.0, 20.0)
)

process.noPrediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.prunedAODForPF2PATEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop recoCaloTau*_*_*_*', 
        'drop recoPFTau*_*_*_*', 
        'drop recoCaloJet*_*_*_*', 
        'drop recoPFJet*_*_*_*', 
        'drop recoConversions_*_*_*', 
        'drop recoJetedmRefToBaseProdTofloatsAssociationVector_*_*_*', 
        'drop recoPreshowerClusters_*_*_*', 
        'drop recoMETs_*_*_*', 
        'drop recoPFMETs_*_*_*', 
        'drop recoCaloMETs_*_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_tevMuons_*_*', 
        'drop *_generalV0Candidates_*_*', 
        'drop *_*TracksFromConversions_*_*', 
        'drop recoPhoton*_*_*_*', 
        'drop *_muIsoDeposit*_*_*', 
        'drop recoMuonMETCorrectionDataedmValueMap_*_*_*', 
        'drop *_*JetTracksAssociator*_*_*', 
        'drop *_*JetExtender_*_*', 
        'drop recoSoftLeptonTagInfos_*_*_*', 
        'drop *_impactParameterTagInfos_*_*', 
        'drop *_towerMaker_*_*', 
        'drop *_sisCone*_*_*', 
        'drop *_PhotonIDProd_*_*', 
        'drop recoHFEMClusterShapes_*_*_*', 
        'drop recoCaloClustersToOnereco*_*_*_*', 
        'drop EcalRecHitsSorted_*_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop *_particleFlow_electrons_*', 
        'drop recoPreshowerClusterShapes_*_*_*', 
        'drop *_hfRecoEcalCandidate_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep recoSuperClusters_corrected*_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*')
)

process.requireDecayMode = cms.PSet(
    BooleanOperator = cms.string('and'),
    decayMode = cms.PSet(
        cut = cms.double(0.5),
        Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding")
    )
)

process.requireLeadPion = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadPion = cms.PSet(
        cut = cms.double(0.5),
        Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
    )
)

process.requireLeadTrack = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
        cut = cms.double(0.5),
        Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding")
    )
)

process.requireLeadTrackCalo = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
        cut = cms.double(0.5),
        Producer = cms.InputTag("caloRecoTauDiscriminationByLeadingTrackFinding")
    )
)

process.shrinkingConeLeadTrackFinding = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
        cut = cms.double(0.5),
        Producer = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
    )
)

process.standardDecayModeParams = cms.PSet(
    mergeByBestMatch = cms.bool(True),
    refitTracks = cms.bool(False),
    maxNbrOfIterations = cms.int32(10),
    mergeLowPtPhotonsFirst = cms.bool(True),
    setMergedPi0Mass = cms.bool(True),
    setChargedPionMass = cms.bool(True),
    filterPhotons = cms.bool(True),
    minPtFractionPiZeroes = cms.double(0.15),
    maxPhotonsToMerge = cms.uint32(2),
    filterTwoProngs = cms.bool(True),
    maxPiZeroMass = cms.double(0.2),
    minPtFractionForSecondProng = cms.double(0.1),
    maxDistance = cms.double(0.01),
    setPi0Mass = cms.bool(True),
    minPtFractionSinglePhotons = cms.double(0.1)
)

process.tautagInfoModifer = cms.PSet(
    pfTauTagInfoSrc = cms.InputTag("pfRecoTauTagInfoProducer"),
    name = cms.string('TTIworkaround'),
    plugin = cms.string('RecoTauTagInfoWorkaroundModifer')
)

process.tightSoftPFElectronCleanerBarrelCuts = cms.PSet(
    BarreldRGsfTrackElectronCuts = cms.vdouble(0.0, 0.006),
    BarrelEemPinRatioCuts = cms.vdouble(-0.9, 0.065),
    BarrelMVACuts = cms.vdouble(0.58, 1.0),
    BarrelPtCuts = cms.vdouble(2.0, 9999.0)
)

process.tightSoftPFElectronCleanerForwardCuts = cms.PSet(
    ForwarddRGsfTrackElectronCuts = cms.vdouble(0.0, 0.01),
    ForwardPtCuts = cms.vdouble(2.0, 9999.0),
    ForwardMVACuts = cms.vdouble(0.6, 1.0),
    ForwardInverseFBremCuts = cms.vdouble(1.0, 15.0)
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    )
)

process.vertexCutsBlock = cms.PSet(
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    )
)

process.vertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    )
)

process.vertexSelectionBlock = cms.PSet(
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)

process.vertexTrackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    )
)

process.MultiNetIso = cms.VPSet(cms.PSet(
    applyIsolation = cms.bool(True),
    cut = cms.double(-10.0),
    computerName = cms.string('OneProngNoPiZeroIso'),
    decayModeIndices = cms.vint32(0)
), 
    cms.PSet(
        applyIsolation = cms.bool(True),
        cut = cms.double(-10.0),
        computerName = cms.string('OneProngOnePiZeroIso'),
        decayModeIndices = cms.vint32(1)
    ), 
    cms.PSet(
        applyIsolation = cms.bool(True),
        cut = cms.double(-10.0),
        computerName = cms.string('OneProngTwoPiZeroIso'),
        decayModeIndices = cms.vint32(2)
    ), 
    cms.PSet(
        applyIsolation = cms.bool(True),
        cut = cms.double(-10.0),
        computerName = cms.string('ThreeProngNoPiZeroIso'),
        decayModeIndices = cms.vint32(10)
    ), 
    cms.PSet(
        applyIsolation = cms.bool(True),
        cut = cms.double(-10.0),
        computerName = cms.string('ThreeProngOnePiZeroIso'),
        decayModeIndices = cms.vint32(11)
    ))

process.SingleNetBasedTauID = cms.VPSet(cms.PSet(
    applyIsolation = cms.bool(False),
    cut = cms.double(-10.0),
    computerName = cms.string('SingleNet'),
    decayModeIndices = cms.vint32(0, 1, 2, 10, 11)
))

process.TaNC = cms.VPSet(cms.PSet(
    applyIsolation = cms.bool(False),
    cut = cms.double(-10.0),
    computerName = cms.string('OneProngNoPiZero'),
    decayModeIndices = cms.vint32(0)
), 
    cms.PSet(
        applyIsolation = cms.bool(False),
        cut = cms.double(-10.0),
        computerName = cms.string('OneProngOnePiZero'),
        decayModeIndices = cms.vint32(1)
    ), 
    cms.PSet(
        applyIsolation = cms.bool(False),
        cut = cms.double(-10.0),
        computerName = cms.string('OneProngTwoPiZero'),
        decayModeIndices = cms.vint32(2)
    ), 
    cms.PSet(
        applyIsolation = cms.bool(False),
        cut = cms.double(-10.0),
        computerName = cms.string('ThreeProngNoPiZero'),
        decayModeIndices = cms.vint32(10)
    ), 
    cms.PSet(
        applyIsolation = cms.bool(False),
        cut = cms.double(-10.0),
        computerName = cms.string('ThreeProngOnePiZero'),
        decayModeIndices = cms.vint32(11)
    ))

process.transforms = cms.VPSet(cms.PSet(
    nPiZeros = cms.uint32(0),
    transform = cms.PSet(
        max = cms.double(1.99833333333),
        transform = (cms.vdouble(0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508)+cms.vdouble(0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243539974508, 0.243693947972, 0.2446621342, 0.25648929965, 0.2608766459, 0.265139843949, 0.268288096025, 0.271490633611, 0.274812027295, 0.278726505561, 0.283196361675, 0.287921047203, 0.293485065795, 0.299327353484, 0.305468394708, 0.310410038477, 0.315654364298, 0.320865024837, 0.324875648584, 0.328691660974, 0.332598633349, 0.336484807993, 0.339893814351, 0.343528868912, 0.346311138119, 0.348525259682, 0.350638868762, 0.352500481165, 0.354385202603, 0.356405103778, 0.358448162743, 0.359626155068, 0.361359527277, 0.362911630832, 0.364767207965, 0.365568276809, 0.367161876825, 0.368245783665, 0.369700987138, 0.370891835827, 0.371335926598, 0.372724067775, 0.374122626292, 0.374872824273, 0.376287585272, 0.377808481377, 0.379437962659, 0.380385427158, 0.381454465894, 0.382529530437, 0.383308773065, 0.383900643462, 0.384488881534, 0.385284008411, 0.385778244795, 0.386880706208, 0.387787417873, 0.389206336729, 0.390430843456, 0.391560096158, 0.392490239284, 0.393218300975, 0.394889524946, 0.396474094424, 0.397328157396, 0.398823062781, 0.400437280424, 0.401846875958, 0.402719262685, 0.403705236447, 0.40437725886, 0.405483096559, 0.40715324019, 0.408161946716, 0.408949958358, 0.410194428622, 0.411674966358, 0.412726139917, 0.413994836217, 0.414922434459, 0.415970963664, 0.417494895799, 0.418345516985, 0.419769194149, 0.42120259427, 0.423008169722, 0.424220511323, 0.425684525769, 0.426912279039, 0.428023327968, 0.429389155258, 0.430889124801, 0.432147128025, 0.433793555744, 0.435196517338, 0.436351162787, 0.437253465009, 0.438419065687, 0.439590897333, 0.440949213705, 0.441921470289, 0.442848592497, 0.44396524306, 0.445223842049, 0.446977728682, 0.448745488265, 0.451078381688, 0.451907557714, 0.452739787751, 0.453638395261, 0.45475822595, 0.456165813144, 0.457223834211, 0.457934807034, 0.45922014571, 0.461017229233, 0.461451032994, 0.463048655665, 0.464804181316, 0.466425147476, 0.467542494191, 0.468517661795, 0.470468799941, 0.47198076935, 0.472892624736, 0.474420238705, 0.476266453893, 0.477505267649, 0.479532143347, 0.481200116592, 0.481613637289, 0.483360304775, 0.485061449421, 0.487101659613, 0.488019909526, 0.488999144832, 0.490200759674, 0.491190516798, 0.493849514855, 0.495306102206, 0.495928489713, 0.4964353883, 0.498082556741, 0.49979254034, 0.500775976586, 0.502679733683, 0.504598020717, 0.505078487853, 0.506619141507, 0.508171974823, 0.509336469886, 0.510953930915, 0.512581697566, 0.513998315702, 0.515647034962, 0.515939613111, 0.517975069449, 0.519430445753, 0.519957296262, 0.521273324958, 0.522406663349, 0.523925469498, 0.524625850033, 0.525907581275, 0.527065315655, 0.52822815856, 0.528783474767, 0.529145626115, 0.529453767868, 0.530435650231, 0.532014259582, 0.532782125184, 0.534528955521, 0.535733634238, 0.539584530704, 0.541410067901, 0.543682312792, 0.545138243861, 0.546811742597, 0.548048893429, 0.548459504636, 0.550158093752, 0.551205716597, 0.552261157841, 0.553773021814, 0.554620522074, 0.557022425024, 0.558787346691, 0.55989408991, 0.562351160997, 0.564603650808, 0.567330572538, 0.568251047692, 0.570322191691, 0.570800554836, 0.573840553165, 0.575722428922, 0.578806943369, 0.580018988744, 0.581943439091, 0.583637839285, 0.583719886077, 0.585230062162, 0.586459819001, 0.58819018682, 0.589432428675, 0.590707557501, 0.59199058109, 0.593311935901, 0.596143502405, 0.598713047084, 0.59985869618, 0.60146038335)+cms.vdouble(0.603073645068, 0.60364159568, 0.605493798425, 0.607716165748, 0.611539567166, 0.61344596304, 0.614868728468, 0.616356298487, 0.617243661796, 0.618356139972, 0.620433033442, 0.623603658141, 0.625027738979, 0.626745245057, 0.630061473707, 0.634451273629, 0.636224368987, 0.638386932974, 0.639666729708, 0.641472541416, 0.643376129813, 0.645998175052, 0.648651724655, 0.650614385321, 0.651964427491, 0.654372246094, 0.656912558238, 0.657658356547, 0.658734274882, 0.661006291486, 0.663094362812, 0.664860224717, 0.667639986138, 0.669224738703, 0.670609710516, 0.672008536945, 0.674322956904, 0.676181757848, 0.680504320591, 0.681701882298, 0.683847428048, 0.687028204213, 0.690096183579, 0.692936565842, 0.698333032093, 0.702469873766, 0.704533440299, 0.706621657637, 0.710308262591, 0.713270705866, 0.714865826284, 0.719086552707, 0.722147885763, 0.725885046087, 0.729450681758, 0.732859861331, 0.739185288999, 0.743172463789, 0.74657896386, 0.751327840506, 0.754658774214, 0.758047388164, 0.762059448212, 0.769914558551, 0.775838239214, 0.780728907111, 0.786952215918, 0.793694146175, 0.796885300439, 0.802863959078, 0.813001141474, 0.820597251397, 0.829350775725, 0.837460143471, 0.84199323298, 0.847433416989, 0.854638027367, 0.860714284529, 0.869959964541, 0.876007819869, 0.884455823419, 0.896538436371, 0.904016005807, 0.910382232961, 0.916770946986, 0.93386870405, 0.943467586229, 0.95165443966, 0.971789456433, 0.970755563959, 0.9679163435, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
        min = cms.double(-0.998333333333)
    ),
    nCharged = cms.uint32(3)
), 
    cms.PSet(
        nPiZeros = cms.uint32(1),
        transform = cms.PSet(
            max = cms.double(1.99833333333),
            transform = (cms.vdouble(0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285)+cms.vdouble(0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725479663285, 0.725625489751, 0.725917318629, 0.727526582607, 0.745748231906, 0.750169168536, 0.757185219071, 0.764249672036, 0.767603981959, 0.772574492642, 0.775097031572, 0.777704615235, 0.779407980465, 0.781767581973, 0.784842584326, 0.786420654919, 0.787883166617, 0.790123535551, 0.79208138528, 0.79327247227, 0.795907708578, 0.798503646112, 0.800206834461, 0.802663946447, 0.8031582666, 0.80490222571, 0.806889568691, 0.809394028316, 0.811861583702, 0.813019057268, 0.81342095915, 0.814698723372, 0.816279445985, 0.818232037783, 0.819367026875, 0.819759858707, 0.821328989638, 0.822878675172, 0.82364763472, 0.825358996088, 0.828499118125, 0.829830087025, 0.831236000117, 0.832703495507, 0.833414247004, 0.834436344112, 0.834946785624, 0.835869791486, 0.836486520822, 0.837364626557, 0.838193318858, 0.839702591039, 0.841531457051, 0.842218371935, 0.843640339114, 0.844222988069, 0.845392038566, 0.846778761898, 0.84769605779, 0.848073950379, 0.848849957765, 0.849494110293, 0.8500905241, 0.851335675181, 0.853500950651, 0.853839833615, 0.854227213103, 0.854567621296, 0.854984559013, 0.855203285083, 0.856470785047, 0.857475859603, 0.85892685241, 0.859008202829, 0.859451257957, 0.860468389831, 0.861489507276, 0.861351261404, 0.861705874851, 0.861659795003, 0.861659795003, 0.86179137032, 0.862147375366, 0.862550177315, 0.863312092458, 0.863805642705, 0.864438066642, 0.864754370118, 0.865480701328, 0.866346092335, 0.867168965701, 0.867397571488, 0.868313201223, 0.868771741382, 0.869186401202, 0.86983185136, 0.869929474522, 0.870346507695, 0.870951429469, 0.870863388987, 0.871514279263, 0.872166654676, 0.872355339191, 0.872776974093, 0.873155878735, 0.873579101025, 0.874003066865, 0.873916467734, 0.874211597253, 0.874402872188, 0.87510742975, 0.87525648792, 0.87525648792, 0.875448860228, 0.875598481234, 0.875512416378, 0.87617785231, 0.87617785231, 0.876371452215, 0.877233539228, 0.877818409805, 0.87840545558, 0.87840545558, 0.878601622981, 0.878601622981, 0.879472984901, 0.879712328244, 0.87982581203, 0.879981638026, 0.880179766123, 0.880378141371, 0.880534852587, 0.880691869776, 0.8811323429, 0.881090533252, 0.881531917098, 0.881732079801, 0.8822162463, 0.882902187113, 0.882979722574, 0.88403281278, 0.885010261835, 0.884928594333, 0.885132644083, 0.885050953876, 0.88525535544, 0.886362380543, 0.886487219509, 0.886652934413, 0.887232935079, 0.887728512003, 0.888561331939, 0.889019284728, 0.889438266521, 0.890358658388, 0.890120720891, 0.890292192785, 0.890675834925, 0.890556765164, 0.890981544778, 0.891699669632, 0.891660238395, 0.891969519877, 0.892319678993, 0.892161931402, 0.892513711208, 0.892729546909, 0.893162065429, 0.893339503795, 0.893339503795, 0.893656248099, 0.894427465173, 0.894606969217, 0.894825762437, 0.894928163898, 0.895703822513, 0.89622167567, 0.896663385868, 0.897404545302, 0.89769650475, 0.899189293203, 0.899525558799, 0.900803884235, 0.901822547362, 0.901939302648, 0.902926505697, 0.903082359676, 0.904038745128, 0.90469561985, 0.904927332682, 0.905283513893, 0.906828000044, 0.907062493553, 0.908109372415, 0.908783021349, 0.90898498498, 0.910379224289, 0.911372920866, 0.911751863015, 0.912477297669, 0.913239550237, 0.91300238707, 0.913422855139, 0.915063352192, 0.916893920936, 0.916979020829, 0.91791358353, 0.918350995783, 0.918790342789, 0.919328152961, 0.919993298628, 0.920982245955, 0.922524618114, 0.923591109364)+cms.vdouble(0.924018850534, 0.924248923821, 0.924479515826, 0.925498182241, 0.926493584801, 0.927436921962, 0.927911825271, 0.928716526512, 0.929225746944, 0.929920622352, 0.931640820211, 0.931772433588, 0.932293506679, 0.932760264784, 0.93386870405, 0.934480569506, 0.934731886916, 0.935797384751, 0.936588472051, 0.936817507478, 0.937277790773, 0.938339506605, 0.938808219887, 0.93993649209, 0.94020045716, 0.940781492864, 0.941047196853, 0.942510417566, 0.942629939, 0.942750378489, 0.943616386541, 0.944163684906, 0.945338814696, 0.945845741457, 0.946028661789, 0.946308362468, 0.946541150838, 0.946751152357, 0.947576555912, 0.948029352938, 0.94826905955, 0.948081416726, 0.949376743021, 0.94926144862, 0.949775296374, 0.949706301122, 0.951268968863, 0.953037066674, 0.95357532021, 0.953770570793, 0.953640586734, 0.953509869657, 0.954300159882, 0.955476996866, 0.956207587781, 0.956355833165, 0.956846568485, 0.957770053042, 0.958723171834, 0.958928454571, 0.959445187694, 0.959807967592, 0.959442259047, 0.960697132989, 0.961203278228, 0.963193467582, 0.963932365293, 0.964461162833, 0.964482886627, 0.96526433234, 0.966030150632, 0.966856588211, 0.969491617691, 0.970743493871, 0.972389419268, 0.973307337131, 0.975623617612, 0.976087161844, 0.975647899082, 0.976736074007, 0.979440008803, 0.981271208497, 0.982207028661, 0.984863078211, 0.986956530647, 0.990258251858, 0.990208776979, 0.990702226892, 0.993228159625, 0.99534336087, 0.996696237239, 0.995185049087, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
            min = cms.double(-0.998333333333)
        ),
        nCharged = cms.uint32(1)
    ), 
    cms.PSet(
        nPiZeros = cms.uint32(0),
        transform = cms.PSet(
            max = cms.double(1.99833333333),
            transform = (cms.vdouble(0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399)+cms.vdouble(0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.785563102399, 0.786753288885, 0.788132324416, 0.79656141615, 0.810183644995, 0.858360829913, 0.862298212616, 0.867110980413, 0.871372861265, 0.875682014578, 0.880242297589, 0.883696978098, 0.885512278829, 0.887768921813, 0.889264020585, 0.89119925019, 0.892452552697, 0.893185095837, 0.893419577074, 0.894898998675, 0.895774783109, 0.896260903725, 0.896505707407, 0.898082672851, 0.898779137453, 0.89979939771, 0.900120276805, 0.900442301311, 0.900314253861, 0.90063761708, 0.903107169678, 0.903707364412, 0.904624297652, 0.90437518453, 0.904187494019, 0.904648539996, 0.905849328721, 0.90625146477, 0.906593041173, 0.906284313013, 0.906627709554, 0.906627709554, 0.907095652088, 0.906972372385, 0.907318308525, 0.907603995571, 0.907357055463, 0.907233089763, 0.907994846936, 0.908883949265, 0.908883949265, 0.909836831321, 0.909836831321, 0.909776114594, 0.911030037809, 0.911509901723, 0.911871023987, 0.911811279009, 0.911751452972, 0.911691545709, 0.911511334909, 0.911451101085, 0.912784331406, 0.9125455069, 0.9125455069, 0.91297278083, 0.912853317543, 0.912673506387, 0.913592984461, 0.915007651179, 0.915441697726, 0.915324604996, 0.915207187526, 0.915148356591, 0.91552593882, 0.915467174967, 0.9154083293, 0.915290391839, 0.915231299701, 0.915728896806, 0.915728896806, 0.915552071941, 0.916492320764, 0.917377950283, 0.917822427143, 0.918268017622, 0.91871472591, 0.919668295227, 0.919611512782, 0.919554650007, 0.919440682785, 0.919269125195, 0.921306876156, 0.921306876156, 0.921082297245, 0.920969526416, 0.921426208902, 0.921939970027, 0.921939970027, 0.922343069964, 0.923319759486, 0.923727168952, 0.923727168952, 0.92460140151, 0.924492316338, 0.924959238052, 0.926474177051, 0.926474177051, 0.926420752856, 0.926313671218, 0.926785714713, 0.926785714713, 0.926785714713, 0.926732331515, 0.926732331515, 0.926571713811, 0.927521701059, 0.927468561656, 0.927998554333, 0.927945695605, 0.929008220067, 0.928746371941, 0.928693770351, 0.928641091039, 0.929607013105, 0.929554832769, 0.930039996532, 0.93101417799, 0.931554211882, 0.932636161324, 0.932585903271, 0.932585903271, 0.93357188521, 0.933522156167, 0.933967924145, 0.933769185329, 0.934766776762, 0.935267583538, 0.935169629185, 0.935672412756, 0.936176553451, 0.936176553451, 0.93779194569, 0.937554472402, 0.937458974653, 0.937411116161, 0.937970225775, 0.938435668089, 0.938341043455, 0.938341043455, 0.938903099624, 0.93885608225, 0.938808992455, 0.938714594933, 0.939278948765, 0.940409694612, 0.940363611919, 0.940363611919, 0.940884673949, 0.940838860114, 0.940700991551, 0.941179107659, 0.941750185868, 0.941750185868, 0.942276966885, 0.943290568826, 0.943822114749, 0.944267645451, 0.944223792272, 0.944223792272, 0.944223792272, 0.944223792272, 0.944135878551, 0.944091817682, 0.943959217069, 0.944948988041, 0.944817531021, 0.945185418124, 0.945774534438, 0.946869842865, 0.94678443912, 0.947292782482, 0.947803406812, 0.948955745704, 0.949513262437, 0.949431324505, 0.949349120177, 0.949787213059, 0.950350748429, 0.951522477849, 0.952051228023, 0.95197239226, 0.951813940452, 0.951734321829, 0.952189098377, 0.952726227521, 0.952647494583, 0.953226869405, 0.953148724357, 0.95303101596, 0.953497250008, 0.954122169792, 0.954006075021, 0.954594998037, 0.955778170341, 0.955740668477, 0.957457733339, 0.958697023242, 0.958590781777, 0.958519649968, 0.959665182275, 0.960242079268, 0.960242079268, 0.960855701368, 0.960787753107)+cms.vdouble(0.961370655681, 0.961269567079, 0.961823203605, 0.963730727425, 0.963634885553, 0.963570709071, 0.964138473298, 0.964106695414, 0.96404297039, 0.963914839098, 0.963882663464, 0.96452094996, 0.964361812095, 0.96497328025, 0.965587812399, 0.966174859102, 0.966052013818, 0.966021162949, 0.968018795469, 0.96867865254, 0.968592547647, 0.96914294659, 0.969057430126, 0.969000155331, 0.970289180287, 0.971618144708, 0.971511684075, 0.972907637123, 0.972856607143, 0.972753968298, 0.972676478315, 0.973344727784, 0.973217439385, 0.973917083716, 0.973842007934, 0.973791716846, 0.974496912029, 0.974447701286, 0.974373528048, 0.974273957942, 0.974198771106, 0.974791150217, 0.975488253999, 0.976165676348, 0.977513433798, 0.977332925695, 0.978053351441, 0.978734902423, 0.97864854949, 0.979275680612, 0.979190505138, 0.979039751165, 0.978974471583, 0.978886796984, 0.980438334358, 0.981887328142, 0.982567303114, 0.983312443593, 0.983168209088, 0.983021459539, 0.98366063828, 0.983606342672, 0.983441268961, 0.983291720735, 0.985747459607, 0.985615866821, 0.988157949486, 0.988031989052, 0.987786602856, 0.988507380959, 0.988364321833, 0.988127868612, 0.987928555371, 0.987641272072, 0.987408197679, 0.98704162283, 0.986691071046, 0.986360943929, 0.987048151948, 0.989952686544, 0.991766844123, 0.992193166195, 0.99456966538, 0.995655052048, 0.994746673755, 0.993062299865, 0.995491593707, 0.993997811711, 0.991951166261, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
            min = cms.double(-0.998333333333)
        ),
        nCharged = cms.uint32(1)
    ), 
    cms.PSet(
        nPiZeros = cms.uint32(2),
        transform = cms.PSet(
            max = cms.double(1.99833333333),
            transform = (cms.vdouble(0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277)+cms.vdouble(0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320694347277, 0.320785409267, 0.320785409267, 0.320785409267, 0.320967688479, 0.32115017496, 0.32115017496, 0.32115017496, 0.32115017496, 0.321332869066, 0.321607300294, 0.321790515012, 0.322065728828, 0.322709728783, 0.337811096719, 0.33917314626, 0.341489359417, 0.343051156809, 0.344690580804, 0.34605531485, 0.347729452006, 0.349352972192, 0.351698761571, 0.354076266303, 0.356364861761, 0.357459291064, 0.358806090169, 0.360659074159, 0.361655179522, 0.363285639001, 0.363823848893, 0.365224296488, 0.366635567078, 0.368317558281, 0.36949108301, 0.370409007364, 0.370997606343, 0.372726361337, 0.373488515297, 0.374412657806, 0.375752608537, 0.377534910678, 0.378625338634, 0.379181030815, 0.379877944035, 0.382266731549, 0.382549741971, 0.383828491978, 0.38525242259, 0.386835650852, 0.38785063627, 0.389317222671, 0.390498501728, 0.392134514369, 0.392433445129, 0.393938724972, 0.395003106909, 0.395165758646, 0.395929379967, 0.396695958257, 0.397011143016, 0.398247378442, 0.399356983741, 0.399994683207, 0.401254354869, 0.40236309389, 0.403477977186, 0.404278112546, 0.405403648355, 0.406718341929, 0.408044942586, 0.409053791836, 0.409879342767, 0.410568240656, 0.411067477386, 0.412572498902, 0.413612340683, 0.414628216181, 0.41718987191, 0.417878334739, 0.41856907358, 0.419300644011, 0.420520753157, 0.420777117228, 0.422716149289, 0.423248081689, 0.424315972822, 0.425568676714, 0.426697968924, 0.427784748237, 0.428512348538, 0.429242428143, 0.430526071506, 0.4311350135, 0.432803583714, 0.433609675616, 0.434608917639, 0.436308891919, 0.436878509184, 0.437640316502, 0.438596319943, 0.440520911858, 0.441683795845, 0.443048277506, 0.444696219849, 0.446478472767, 0.44715804854, 0.448645092811, 0.450058431683, 0.450666877959, 0.450755388115, 0.451660727674, 0.452685605028, 0.453508861839, 0.455164391331, 0.456611329026, 0.456920461171, 0.457863702358, 0.45902581005, 0.459451411686, 0.460410936031, 0.461808077134, 0.4630001435, 0.46452516501, 0.465632370863, 0.466972634942, 0.467639712811, 0.468206417853, 0.469000443277, 0.470125946746, 0.471938031657, 0.473437184975, 0.474815974144, 0.475643583896, 0.477037107394, 0.478345116523, 0.479756398109, 0.482127131145, 0.483321305722, 0.484827612962, 0.485378450947, 0.486839313932, 0.488800865348, 0.488631796262, 0.489784626283, 0.49019813266, 0.490696455307, 0.492699918902, 0.493707798202, 0.495481544763, 0.497780890453, 0.499067549901, 0.499842743245, 0.501067711008, 0.501110885208, 0.503739653301, 0.504533670387, 0.507669169039, 0.508207246665, 0.510099534144, 0.511125093239, 0.513041788431, 0.514972912765, 0.517927881794, 0.519848789077, 0.52116702462, 0.522598588906, 0.524038039421, 0.524905522273, 0.525729939569, 0.527349110611, 0.528189103375, 0.529884063982, 0.531038635091, 0.531258876588, 0.533372518417, 0.532652261497, 0.533222445036, 0.533832435241, 0.534714171593, 0.536561182549, 0.536184284139, 0.538295230995, 0.539204274194, 0.539743792118, 0.542257448251, 0.543191981222, 0.54415669717, 0.545124845911, 0.546421082543, 0.548704392123, 0.551006864138, 0.551639517385, 0.554308295208, 0.554286639155, 0.555277851271, 0.557294734318, 0.558661984326, 0.560735788966, 0.561777981725, 0.56352691872, 0.56493793563, 0.567793486879, 0.568888208725, 0.57034433091, 0.570356276084, 0.572191934216, 0.573659294894, 0.574044772549, 0.575543527534, 0.577054482298, 0.578553389267, 0.580816407199, 0.582777514902, 0.58546601664, 0.587013469943, 0.586699955875, 0.587164603914, 0.589909772096, 0.590347109603, 0.591182964289, 0.593622213241, 0.595632610766, 0.596088895792)+cms.vdouble(0.596547219627, 0.597007595967, 0.59905000376, 0.59875479532, 0.600402032492, 0.601476624751, 0.602375325225, 0.604611692334, 0.606308877758, 0.609454442616, 0.612487831768, 0.615198564485, 0.616345932738, 0.617679752716, 0.620364786891, 0.621560433387, 0.622923085077, 0.622771613804, 0.627021967049, 0.629464905691, 0.630636176618, 0.632414811477, 0.635412621765, 0.636860801036, 0.638359784998, 0.642296739762, 0.64372019874, 0.646732193739, 0.649419880322, 0.653004922396, 0.654536589972, 0.657493324695, 0.65872664624, 0.662116021475, 0.666837437051, 0.668332370106, 0.670194812833, 0.671514734427, 0.671514734427, 0.672844093862, 0.672352092845, 0.678607302272, 0.681605563269, 0.681020472505, 0.682082800049, 0.684848783291, 0.686959317553, 0.690918830645, 0.691984674993, 0.694695530605, 0.697455651971, 0.700496795416, 0.703736816672, 0.704917801757, 0.706220722464, 0.707858889942, 0.71018130526, 0.714321429016, 0.720425948473, 0.724503155871, 0.727977004139, 0.730714468803, 0.735012362904, 0.739735756402, 0.750660954162, 0.757799352464, 0.760515374245, 0.768004247792, 0.77935327172, 0.784646260495, 0.789164336822, 0.791123170072, 0.795276817521, 0.804299018936, 0.819103217408, 0.822961151625, 0.833298258018, 0.842807182616, 0.85334688934, 0.86724344838, 0.872176831791, 0.87195156781, 0.87843961359, 0.891494313173, 0.912879175226, 0.924218217451, 0.937234161591, 0.94206607914, 0.958884557005, 0.959595443343, 0.93904371889, 0.927733482302, 0.93386870405, 0.916051159827, 0.943467586229, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)+cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)),
            min = cms.double(-0.998333333333)
        ),
        nCharged = cms.uint32(1)
    ))

process.schedule = cms.Schedule(process.p,process.hbhepath,process.nTuplizePath,process.ecalFilter,process.e)
