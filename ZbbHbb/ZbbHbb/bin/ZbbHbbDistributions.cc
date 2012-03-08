#include <TH1F.h>
#include <TH2F.h>
#include <TROOT.h>
#include <TFile.h>
#include <TTree.h>
#include <TSystem.h>
#include "DataFormats/FWLite/interface/Event.h"
#include "DataFormats/FWLite/interface/Handle.h"
#include "DataFormats/FWLite/interface/ChainEvent.h"
#include "FWCore/FWLite/interface/AutoLibraryLoader.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "FWCore/ParameterSet/interface/ProcessDesc.h"
#include "FWCore/PythonParameterSet/interface/PythonProcessDesc.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"

#include "VHbbAnalysis/VHbbDataFormats/interface/VHbbEvent.h"
#include "VHbbAnalysis/VHbbDataFormats/interface/VHbbEventAuxInfo.h"
#include "VHbbAnalysis/VHbbDataFormats/interface/VHbbCandidate.h"
#include "VHbbAnalysis/VHbbDataFormats/interface/TriggerReader.h"
#include "VHbbAnalysis/VHbbDataFormats/interface/TopMassReco.h"

bool truthMatch(TLorentzVector reco_p4, TLorentzVector gen_p4)
{
	bool returnValue=false;
	double match_cut=0.1;
	double dR=reco_p4.DeltaR(gen_p4); 
	if (dR<match_cut) returnValue=true;
	return returnValue;
}

float resolutionBias(float eta)
{
  if(eta<1.1) return 0.05;
  if(eta<2.5) return 0.10;
  if(eta<5.0) return 0.30;
  return 0;
}

int main(int argc, char* argv[])
{
  // load framework libraries
  gSystem->Load("libFWCoreFWLite");
  AutoLibraryLoader::enable();
	
	std::string H_string(argv[1]);
	std::cout<<"H_string="<<H_string<<std::endl;
  
	bool jetCorrections;
	if (std::string(argv[2])=="0") jetCorrections=false;
	if (std::string(argv[2])=="1") jetCorrections=true;
	
  double pi=3.14159265358979;
	double Z_mass;
	if (H_string=="H_110")
	{
		Z_mass=85;
	} else if (H_string=="H_130")
	{
		Z_mass=85.0;
	} else if (H_string=="H_150")
	{
		Z_mass=88.0;
	}
	double bTagCSV_cut=0.679; // 0.679
	double jetpT_cut=30.0;
	
	fwlite::TFileService outFile=fwlite::TFileService("distributions_"+H_string+".root");
	TH1I *h_nJets=outFile.make<TH1I>("h_nJets", "# Cleaned PAT Jets; n", 10, 0, 10);
	
	TH1F *h_Jet1_E=outFile.make<TH1F>("h_Jet1_E", "Jet1 Energy; E (GeV)", 100, 0., 500.);
	TH1F *h_Jet1_pT=outFile.make<TH1F>("h_Jet1_pT", "Jet1 p_T; p_T (GeV)", 100, 0., 500.);
	TH1F *h_Jet1_eta=outFile.make<TH1F>("h_Jet1_eta", "Jet1 #eta; #eta", 100, -5., 5.);
	TH1F *h_Jet1_phi=outFile.make<TH1F>("h_Jet1_phi", "Jet1 #Phi; #Phi", 100, 0., pi);
	TH1F *h_Jet1_CSV=outFile.make<TH1F>("h_Jet1_CSV", "Jet1 CSV; CSV", 100, 0., 1.);
	TH1F *h_Jet1_pT_bZMatched=outFile.make<TH1F>("h_Jet1_pT_bZMatched", "Jet 1 #p_T matched to b from Z; #p_T", 100, 0., 500.);
	TH1F *h_Jet1_pT_bbZMatched=outFile.make<TH1F>("h_Jet1_pT_bbZMatched", "Jet 1 #p_T matched to #bar{b} from Z; #p_T", 100, 0., 500.);
	TH1F *h_Jet1_pT_bHMatched=outFile.make<TH1F>("h_Jet1_pT_bHMatched", "Jet 1 #p_T matched to b from H; #p_T", 100, 0., 500.);
	TH1F *h_Jet1_pT_bbHMatched=outFile.make<TH1F>("h_Jet1_pT_bbHMatched", "Jet 1 #p_T matched to #bar{b} from H; #p_T", 100, 0., 500.);
	TH1F *h_Jet1_eta_bZMatched=outFile.make<TH1F>("h_Jet1_eta_bZMatched", "Jet 1 #eta matched to b from Z; #eta", 100, -5., 5.);
	TH1F *h_Jet1_eta_bbZMatched=outFile.make<TH1F>("h_Jet1_eta_bbZMatched", "Jet 1 #eta matched to #bar{b} from Z; #eta", 100, -5., 5.);
	TH1F *h_Jet1_eta_bHMatched=outFile.make<TH1F>("h_Jet1_eta_bHMatched", "Jet 1 #eta matched to b from H; #eta", 100, -5., 5.);
	TH1F *h_Jet1_eta_bbHMatched=outFile.make<TH1F>("h_Jet1_eta_bbHMatched", "Jet 1 #eta matched to #bar{b} from H; #eta", 100, -5., 5.);
	TH1F *h_Jet1_CSV_bZMatched=outFile.make<TH1F>("h_Jet1_CSV_bZMatched", "Jet 1 CSV matched to b from Z; CSV", 100, 0., 1.);
	TH1F *h_Jet1_CSV_bbZMatched=outFile.make<TH1F>("h_Jet1_CSV_bbZMatched", "Jet 1 CSV matched to #bar{b} from Z; CSV", 100, 0., 1.);
	TH1F *h_Jet1_CSV_bHMatched=outFile.make<TH1F>("h_Jet1_CSV_bHMatched", "Jet 1 CSV matched to b from H; CSV", 100, 0., 1.);
	TH1F *h_Jet1_CSV_bbHMatched=outFile.make<TH1F>("h_Jet1_CSV_bbHMatched", "Jet 1 CSV matched to #bar{b} from H; CSV", 100, 0., 1.);
	TH1F *h_dR=outFile.make<TH1F>("h_dR", "Matching #DeltaR", 100, 0., 5.);
	
	TH1F *h_Jet2_E=outFile.make<TH1F>("h_Jet2_E", "Jet2 Energy; E (GeV)", 100, 0., 500.);
	TH1F *h_Jet2_pT=outFile.make<TH1F>("h_Jet2_pT", "Jet2 p_T; p_T (GeV)", 100, 0., 500.);
	TH1F *h_Jet2_eta=outFile.make<TH1F>("h_Jet2_eta", "Jet2 #eta; #eta", 100, -5., 5.);
	TH1F *h_Jet2_phi=outFile.make<TH1F>("h_Jet2_phi", "Jet2 #Phi; #Phi", 100, 0., pi);
	TH1F *h_Jet2_CSV=outFile.make<TH1F>("h_Jet2_CSV", "Jet2 CSV; CSV", 100, 0., 1.);
	TH1F *h_Jet2_pT_bZMatched=outFile.make<TH1F>("h_Jet2_pT_bZMatched", "Jet 2 #p_T matched to b from Z; #p_T", 100, 0., 500.);
	TH1F *h_Jet2_pT_bbZMatched=outFile.make<TH1F>("h_Jet2_pT_bbZMatched", "Jet 2 #p_T matched to #bar{b} from Z; #p_T", 100, 0., 500.);
	TH1F *h_Jet2_pT_bHMatched=outFile.make<TH1F>("h_Jet2_pT_bHMatched", "Jet 2 #p_T matched to b from H; #p_T", 100, 0., 500.);
	TH1F *h_Jet2_pT_bbHMatched=outFile.make<TH1F>("h_Jet2_pT_bbHMatched", "Jet 2 #p_T matched to #bar{b} from H; #p_T", 100, 0., 500.);
	TH1F *h_Jet2_eta_bZMatched=outFile.make<TH1F>("h_Jet2_eta_bZMatched", "Jet 2 #eta matched to b from Z; #eta", 100, -5., 5.);
	TH1F *h_Jet2_eta_bbZMatched=outFile.make<TH1F>("h_Jet2_eta_bbZMatched", "Jet 2 #eta matched to #bar{b} from Z; #eta", 100, -5., 5.);
	TH1F *h_Jet2_eta_bHMatched=outFile.make<TH1F>("h_Jet2_eta_bHMatched", "Jet 2 #eta matched to b from H; #eta", 100, -5., 5.);
	TH1F *h_Jet2_eta_bbHMatched=outFile.make<TH1F>("h_Jet2_eta_bbHMatched", "Jet 2 #eta matched to #bar{b} from H; #eta", 100, -5., 5.);
	TH1F *h_Jet2_CSV_bZMatched=outFile.make<TH1F>("h_Jet2_CSV_bZMatched", "Jet 2 CSV matched to b from Z; CSV", 100, 0., 1.);
	TH1F *h_Jet2_CSV_bbZMatched=outFile.make<TH1F>("h_Jet2_CSV_bbZMatched", "Jet 2 CSV matched to #bar{b} from Z; CSV", 100, 0., 1.);
	TH1F *h_Jet2_CSV_bHMatched=outFile.make<TH1F>("h_Jet2_CSV_bHMatched", "Jet 2 CSV matched to b from H; CSV", 100, 0., 1.);
	TH1F *h_Jet2_CSV_bbHMatched=outFile.make<TH1F>("h_Jet2_CSV_bbHMatched", "Jet 2 CSV matched to #bar{b} from H; CSV", 100, 0., 1.);
	
	TH1F *h_Jet3_E=outFile.make<TH1F>("h_Jet3_E", "Jet3 Energy; E (GeV)", 100, 0., 500.);
	TH1F *h_Jet3_pT=outFile.make<TH1F>("h_Jet3_pT", "Jet3 p_T; p_T (GeV)", 100, 0., 500.);
	TH1F *h_Jet3_eta=outFile.make<TH1F>("h_Jet3_eta", "Jet3 #eta; #eta", 100, -5., 5.);
	TH1F *h_Jet3_phi=outFile.make<TH1F>("h_Jet3_phi", "Jet3 #Phi; #Phi", 100, 0., pi);
	TH1F *h_Jet3_CSV=outFile.make<TH1F>("h_Jet3_CSV", "Jet3 CSV; CSV", 100, 0., 1.);
	TH1F *h_Jet3_pT_bZMatched=outFile.make<TH1F>("h_Jet3_pT_bZMatched", "Jet 3 #p_T matched to b from Z; #p_T", 100, 0., 500.);
	TH1F *h_Jet3_pT_bbZMatched=outFile.make<TH1F>("h_Jet3_pT_bbZMatched", "Jet 3 #p_T matched to #bar{b} from Z; #p_T", 100, 0., 500.);
	TH1F *h_Jet3_pT_bHMatched=outFile.make<TH1F>("h_Jet3_pT_bHMatched", "Jet 3 #p_T matched to b from H; #p_T", 100, 0., 500.);
	TH1F *h_Jet3_pT_bbHMatched=outFile.make<TH1F>("h_Jet3_pT_bbHMatched", "Jet 3 #p_T matched to #bar{b} from H; #p_T", 100, 0., 500.);
	TH1F *h_Jet3_eta_bZMatched=outFile.make<TH1F>("h_Jet3_eta_bZMatched", "Jet 3 #eta matched to b from Z; #eta", 100, -5., 5.);
	TH1F *h_Jet3_eta_bbZMatched=outFile.make<TH1F>("h_Jet3_eta_bbZMatched", "Jet 3 #eta matched to #bar{b} from Z; #eta", 100, -5., 5.);
	TH1F *h_Jet3_eta_bHMatched=outFile.make<TH1F>("h_Jet3_eta_bHMatched", "Jet 3 #eta matched to b from H; #eta", 100, -5., 5.);
	TH1F *h_Jet3_eta_bbHMatched=outFile.make<TH1F>("h_Jet3_eta_bbHMatched", "Jet 3 #eta matched to #bar{b} from H; #eta", 100, -5., 5.);
	TH1F *h_Jet3_CSV_bZMatched=outFile.make<TH1F>("h_Jet3_CSV_bZMatched", "Jet 3 CSV matched to b from Z; CSV", 100, 0., 1.);
	TH1F *h_Jet3_CSV_bbZMatched=outFile.make<TH1F>("h_Jet3_CSV_bbZMatched", "Jet 3 CSV matched to #bar{b} from Z; CSV", 100, 0., 1.);
	TH1F *h_Jet3_CSV_bHMatched=outFile.make<TH1F>("h_Jet3_CSV_bHMatched", "Jet 3 CSV matched to b from H; CSV", 100, 0., 1.);
	TH1F *h_Jet3_CSV_bbHMatched=outFile.make<TH1F>("h_Jet3_CSV_bbHMatched", "Jet 3 CSV matched to #bar{b} from H; CSV", 100, 0., 1.);
	
	TH1F *h_Jet4_E=outFile.make<TH1F>("h_Jet4_E", "Jet4 Energy; E (GeV)", 100, 0., 500.);
	TH1F *h_Jet4_pT=outFile.make<TH1F>("h_Jet4_pT", "Jet4 p_T; p_T (GeV)", 100, 0., 500.);
	TH1F *h_Jet4_eta=outFile.make<TH1F>("h_Jet4_eta", "Jet4 #eta; #eta", 100, -5., 5.);
	TH1F *h_Jet4_phi=outFile.make<TH1F>("h_Jet4_phi", "Jet4 #Phi; #Phi", 100, 0., pi);
	TH1F *h_Jet4_CSV=outFile.make<TH1F>("h_Jet4_CSV", "Jet4 CSV; CSV", 100, 0., 1.);
	TH1F *h_Jet4_pT_bZMatched=outFile.make<TH1F>("h_Jet4_pT_bZMatched", "Jet 4 #p_T matched to b from Z; #p_T", 100, 0., 500.);
	TH1F *h_Jet4_pT_bbZMatched=outFile.make<TH1F>("h_Jet4_pT_bbZMatched", "Jet 4 #p_T matched to #bar{b} from Z; #p_T", 100, 0., 500.);
	TH1F *h_Jet4_pT_bHMatched=outFile.make<TH1F>("h_Jet4_pT_bHMatched", "Jet 4 #p_T matched to b from H; #p_T", 100, 0., 500.);
	TH1F *h_Jet4_pT_bbHMatched=outFile.make<TH1F>("h_Jet4_pT_bbHMatched", "Jet 4 #p_T matched to #bar{b} from H; #p_T", 100, 0., 500.);
	TH1F *h_Jet4_eta_bZMatched=outFile.make<TH1F>("h_Jet4_eta_bZMatched", "Jet 4 #eta matched to b from Z; #eta", 100, -5., 5.);
	TH1F *h_Jet4_eta_bbZMatched=outFile.make<TH1F>("h_Jet4_eta_bbZMatched", "Jet 4 #eta matched to #bar{b} from Z; #eta", 100, -5., 5.);
	TH1F *h_Jet4_eta_bHMatched=outFile.make<TH1F>("h_Jet4_eta_bHMatched", "Jet 4 #eta matched to b from H; #eta", 100, -5., 5.);
	TH1F *h_Jet4_eta_bbHMatched=outFile.make<TH1F>("h_Jet4_eta_bbHMatched", "Jet 4 #eta matched to #bar{b} from H; #eta", 100, -5., 5.);
	TH1F *h_Jet4_CSV_bZMatched=outFile.make<TH1F>("h_Jet4_CSV_bZMatched", "Jet 4 CSV matched to b from Z; CSV", 100, 0., 1.);
	TH1F *h_Jet4_CSV_bbZMatched=outFile.make<TH1F>("h_Jet4_CSV_bbZMatched", "Jet 4 CSV matched to #bar{b} from Z; CSV", 100, 0., 1.);
	TH1F *h_Jet4_CSV_bHMatched=outFile.make<TH1F>("h_Jet4_CSV_bHMatched", "Jet 4 CSV matched to b from H; CSV", 100, 0., 1.);
	TH1F *h_Jet4_CSV_bbHMatched=outFile.make<TH1F>("h_Jet4_CSV_bbHMatched", "Jet 4 CSV matched to #bar{b} from H; CSV", 100, 0., 1.);
	
	TH1F *h_DiJet_mass=outFile.make<TH1F>("h_DiJet_mass", "DiJet mass", 50, 0., 200.);
	TH1F *h_DiJet_mass_best=outFile.make<TH1F>("h_DiJet_mass_best", "DiJet mass best", 50., 0., 200.);
	TH1F *h_DiJet_mass_bZbHMatched=outFile.make<TH1F>("h_DiJet_mass_bZbHMatched", "DiJet mass b(Z)b(H)", 50, 0., 200.);
	TH1F *h_DiJet_mass_bHbHMatched=outFile.make<TH1F>("h_DiJet_mass_bHbHMatched", "DiJet mass b(H)b(H)", 50, 0., 200.);
	TH1F *h_DiJet_mass_bZbZMatched=outFile.make<TH1F>("h_DiJet_mass_bZbZMatched", "DiJet mass b(Z)b(Z)", 50, 0., 200.);
	TH1F *h_Z_E=outFile.make<TH1F>("h_Z_E", "Z Energy; E (GeV)", 50, 0., 500.);
	TH1F *h_Z_pT=outFile.make<TH1F>("h_Z_pT", "Z #p_T, #p_T (GeV)", 50, 0., 500.);
	
	TH1F *h_H_mass=outFile.make<TH1F>("h_H_mass", "H mass; mass (GeV)", 50, 0., 200.);
	TH1F *h_H_mass_highest=outFile.make<TH1F>("h_H_mass_highest", "Highest H mass; mass (GeV)", 50, 0., 200.);
	TH1F *h_H_mass_bZbHMatched=outFile.make<TH1F>("h_H_mass_bZbHMatched", "H mass b(Z)b(H)", 50, 0., 200.);
	TH1F *h_H_mass_bZbZMatched=outFile.make<TH1F>("h_H_mass_bZbZMatched", "H mass b(Z)b(Z)", 50, 0., 200.);
	TH1F *h_H_mass_bHbHMatched=outFile.make<TH1F>("h_H_mass_bHbHMatched", "H mass b(H)b(H)", 50, 0., 200.);
	
	TH1F *h_ZH_dPhi=outFile.make<TH1F>("h_ZH_dPhi", "#Delta#Phi(Z,H); #Delta#Phi(Z,H)", 50, -pi, pi);
	
	std::vector<std::string> inFilenames;
	if (H_string=="H_110") inFilenames.push_back("file:/uscms_data/d2/souvik/ZbbHbb/SignalEvents/H_110/PAT_H_110.edm.root");
	if (H_string=="H_130") inFilenames.push_back("file:/uscms_data/d2/souvik/ZbbHbb/SignalEvents/H_130/PAT_H_130.edm.root");
	if (H_string=="H_150") inFilenames.push_back("file:/uscms_data/d2/souvik/ZbbHbb/SignalEvents/H_150/PAT_H_150.edm.root");
	
	fwlite::ChainEvent events(inFilenames);
	for (events.toBegin(); !events.atEnd(); ++events)
	{
	  fwlite::Handle<VHbbEventAuxInfo> vhbbAuxHandle;
		vhbbAuxHandle.getByLabel(events, "HbbAnalyzerNew");
		const VHbbEventAuxInfo &aux=*vhbbAuxHandle.product();
		
		TLorentzVector Z_gen_p4, H_gen_p4, bZ_gen_p4, bbZ_gen_p4, bH_gen_p4, bbH_gen_p4;
		for (unsigned int i=0; i<aux.mcZ.size(); ++i)
		{
			if (aux.mcZ.at(i).dauid.size()==2)
			{
				if (aux.mcZ.at(i).dauid.at(0)==-5 && aux.mcZ.at(i).dauid.at(1)==5)
				{
					Z_gen_p4=aux.mcZ.at(i).p4;
					bbZ_gen_p4=aux.mcZ.at(i).dauFourMomentum.at(0);
					bZ_gen_p4=aux.mcZ.at(i).dauFourMomentum.at(1);
				}
			}
		}
		for (unsigned int i=0; i<aux.mcH.size(); ++i)
		{
			if (aux.mcH.at(i).dauid.size()==2)
			{
				if (aux.mcH.at(i).dauid.at(0)==5 && aux.mcH.at(i).dauid.at(1)==-5)
				{
					H_gen_p4=aux.mcH.at(i).p4;
					bH_gen_p4=aux.mcH.at(i).dauFourMomentum.at(0);
					bbH_gen_p4=aux.mcH.at(i).dauFourMomentum.at(1);
				}
			}
		}
		
		fwlite::Handle<VHbbEvent> vhbbHandle;
		vhbbHandle.getByLabel(events, "HbbAnalyzerNew");
		VHbbEvent modifiedEvent=*vhbbHandle.product();
		if (jetCorrections)
		{
		  for (unsigned int i=0; i<modifiedEvent.simpleJets2.size(); ++i)
			{
				TLorentzVector &p4=modifiedEvent.simpleJets2[i].p4;
				TLorentzVector &mcp4=modifiedEvent.simpleJets2[i].bestMCp4;
				if ((fabs(p4.Pt()-mcp4.Pt())/p4.Pt())<0.5)
				{
					double cor=(p4.Pt()+resolutionBias(fabs(p4.Eta()))*(p4.Pt()-mcp4.Pt()))/p4.Pt();
					// std::cout<<"cor = "<<cor<<std::endl;
					p4.SetPtEtaPhiE(p4.Pt()*cor, p4.Eta(), p4.Phi(), p4.E()*cor);
				}
			}
		}
		const VHbbEvent &event=modifiedEvent;
		
		unsigned int nJets=event.simpleJets2.size();
		h_nJets->Fill(nJets);
		unsigned int nBJets=0;
		for (unsigned int i=0; i<nJets; ++i)
		{
			// std::cout<<"E of "<<i<<"-th Jet = "<<event.simpleJets2.at(i).p4.E()<<", pT = "<<event.simpleJets2.at(i).p4.Pt()<<std::endl;
			if (event.simpleJets2.at(i).csv>bTagCSV_cut && fabs(event.simpleJets2.at(i).p4.Eta())<2.4 && event.simpleJets2.at(i).p4.Pt()>jetpT_cut) ++nBJets;
		}
				
		if (nJets>0)
		{
			h_Jet1_E->Fill(event.simpleJets2.at(0).p4.E());
			h_Jet1_pT->Fill(event.simpleJets2.at(0).p4.Pt());
			h_Jet1_eta->Fill(event.simpleJets2.at(0).p4.Eta());
			h_Jet1_phi->Fill(event.simpleJets2.at(0).p4.Phi());
			h_Jet1_CSV->Fill(event.simpleJets2.at(0).csv);
			
			// MC Matched
			if (truthMatch(event.simpleJets2.at(0).p4, bZ_gen_p4)) h_Jet1_pT_bZMatched->Fill(event.simpleJets2.at(0).p4.Pt());
			if (truthMatch(event.simpleJets2.at(0).p4, bbZ_gen_p4)) h_Jet1_pT_bbZMatched->Fill(event.simpleJets2.at(0).p4.Pt());
			if (truthMatch(event.simpleJets2.at(0).p4, bH_gen_p4)) h_Jet1_pT_bHMatched->Fill(event.simpleJets2.at(0).p4.Pt());
			if (truthMatch(event.simpleJets2.at(0).p4, bbH_gen_p4)) h_Jet1_pT_bbHMatched->Fill(event.simpleJets2.at(0).p4.Pt());
			h_dR->Fill(event.simpleJets2.at(0).p4.DeltaR(bZ_gen_p4));
			h_dR->Fill(event.simpleJets2.at(0).p4.DeltaR(bbZ_gen_p4));
			h_dR->Fill(event.simpleJets2.at(0).p4.DeltaR(bH_gen_p4));
			h_dR->Fill(event.simpleJets2.at(0).p4.DeltaR(bbH_gen_p4));
			
		}
		if (nJets>1)
		{
			h_Jet2_E->Fill(event.simpleJets2.at(1).p4.E());
			h_Jet2_pT->Fill(event.simpleJets2.at(1).p4.Pt());
			h_Jet2_eta->Fill(event.simpleJets2.at(1).p4.Eta());
			h_Jet2_phi->Fill(event.simpleJets2.at(1).p4.Phi());
			h_Jet2_CSV->Fill(event.simpleJets2.at(1).csv);
			
			// MC Matched
			if (truthMatch(event.simpleJets2.at(1).p4, bZ_gen_p4)) h_Jet2_pT_bZMatched->Fill(event.simpleJets2.at(1).p4.Pt());
			if (truthMatch(event.simpleJets2.at(1).p4, bbZ_gen_p4)) h_Jet2_pT_bbZMatched->Fill(event.simpleJets2.at(1).p4.Pt());
			if (truthMatch(event.simpleJets2.at(1).p4, bH_gen_p4)) h_Jet2_pT_bHMatched->Fill(event.simpleJets2.at(1).p4.Pt());
			if (truthMatch(event.simpleJets2.at(1).p4, bbH_gen_p4)) h_Jet2_pT_bbHMatched->Fill(event.simpleJets2.at(1).p4.Pt());
		}
		if (nJets>2)
		{
			h_Jet3_E->Fill(event.simpleJets2.at(2).p4.E());
			h_Jet3_pT->Fill(event.simpleJets2.at(2).p4.Pt());
			h_Jet3_eta->Fill(event.simpleJets2.at(2).p4.Eta());
			h_Jet3_phi->Fill(event.simpleJets2.at(2).p4.Phi());
			h_Jet3_CSV->Fill(event.simpleJets2.at(2).csv);
			
			// MC Matched
			if (truthMatch(event.simpleJets2.at(2).p4, bZ_gen_p4)) h_Jet3_pT_bZMatched->Fill(event.simpleJets2.at(2).p4.Pt());
			if (truthMatch(event.simpleJets2.at(2).p4, bbZ_gen_p4)) h_Jet3_pT_bbZMatched->Fill(event.simpleJets2.at(2).p4.Pt());
			if (truthMatch(event.simpleJets2.at(2).p4, bH_gen_p4)) h_Jet3_pT_bHMatched->Fill(event.simpleJets2.at(2).p4.Pt());
			if (truthMatch(event.simpleJets2.at(2).p4, bbH_gen_p4)) h_Jet3_pT_bbHMatched->Fill(event.simpleJets2.at(2).p4.Pt());
		}
		if (nJets>3)
		{
			h_Jet4_E->Fill(event.simpleJets2.at(3).p4.E());
			h_Jet4_pT->Fill(event.simpleJets2.at(3).p4.Pt());
			h_Jet4_eta->Fill(event.simpleJets2.at(3).p4.Eta());
			h_Jet4_phi->Fill(event.simpleJets2.at(3).p4.Phi());
			h_Jet4_CSV->Fill(event.simpleJets2.at(3).csv);
			
			// MC Matched
			if (truthMatch(event.simpleJets2.at(3).p4, bZ_gen_p4)) h_Jet4_pT_bZMatched->Fill(event.simpleJets2.at(3).p4.Pt());
			if (truthMatch(event.simpleJets2.at(3).p4, bbZ_gen_p4)) h_Jet4_pT_bbZMatched->Fill(event.simpleJets2.at(3).p4.Pt());
			if (truthMatch(event.simpleJets2.at(3).p4, bH_gen_p4)) h_Jet4_pT_bHMatched->Fill(event.simpleJets2.at(3).p4.Pt());
			if (truthMatch(event.simpleJets2.at(3).p4, bbH_gen_p4)) h_Jet4_pT_bbHMatched->Fill(event.simpleJets2.at(3).p4.Pt());
		}
		
		// Event Selection
		if (nBJets>3)
		{
			bool foundZ=false;
			bool foundH=false;
			unsigned int Zjet1_i, Zjet2_i;
			double Z_peak_best, Z_diff_old=30.;
			TLorentzVector Z_p4_best;
			for (unsigned int i=0; i<nJets; ++i)
			{
				TLorentzVector jet1_p4, jet2_p4;
				if (event.simpleJets2.at(i).csv>bTagCSV_cut && fabs(event.simpleJets2.at(i).p4.Eta())<2.4 && event.simpleJets2.at(i).p4.Pt()>jetpT_cut)
				{
					jet1_p4=event.simpleJets2.at(i).p4;
					for (unsigned int j=0; j<nJets; ++j)
					{
						if (j!=i && event.simpleJets2.at(j).csv>bTagCSV_cut && fabs(event.simpleJets2.at(j).p4.Eta())<2.4 && event.simpleJets2.at(j).p4.Pt()>jetpT_cut)
						{
							jet2_p4=event.simpleJets2.at(j).p4;
							double Z_peak=(jet1_p4+jet2_p4).M();
							h_DiJet_mass->Fill(Z_peak);
							
							// MC match these jets
							if ((truthMatch(jet1_p4, bZ_gen_p4) && truthMatch(jet2_p4, bH_gen_p4)) ||
							    (truthMatch(jet1_p4, bZ_gen_p4) && truthMatch(jet2_p4, bbH_gen_p4)) ||
									(truthMatch(jet1_p4, bbZ_gen_p4) && truthMatch(jet2_p4, bH_gen_p4)) ||
									(truthMatch(jet1_p4, bbZ_gen_p4) && truthMatch(jet2_p4, bbH_gen_p4)) ||
									(truthMatch(jet1_p4, bH_gen_p4) && truthMatch(jet2_p4, bZ_gen_p4)) ||
									(truthMatch(jet1_p4, bH_gen_p4) && truthMatch(jet2_p4, bbZ_gen_p4)) ||
									(truthMatch(jet1_p4, bbH_gen_p4) && truthMatch(jet2_p4, bZ_gen_p4)) ||
									(truthMatch(jet1_p4, bbH_gen_p4) && truthMatch(jet2_p4, bbZ_gen_p4))) h_DiJet_mass_bZbHMatched->Fill(Z_peak);
							
							if ((truthMatch(jet1_p4, bZ_gen_p4) && truthMatch(jet2_p4, bbZ_gen_p4)) || 
							    (truthMatch(jet1_p4, bbZ_gen_p4) && truthMatch(jet2_p4, bZ_gen_p4)))	h_DiJet_mass_bZbZMatched->Fill(Z_peak);
									
							if ((truthMatch(jet1_p4, bH_gen_p4) && truthMatch(jet2_p4, bbH_gen_p4)) ||
									(truthMatch(jet1_p4, bbH_gen_p4) && truthMatch(jet2_p4, bH_gen_p4))) h_DiJet_mass_bHbHMatched->Fill(Z_peak);							
							
							double Z_diff=fabs(Z_peak-Z_mass);
							
							if (Z_diff<Z_diff_old) 
							{
								Zjet1_i=i; 
								Zjet2_i=j; 
								Z_diff_old=Z_diff;
								Z_peak_best=Z_peak;
								Z_p4_best=(jet1_p4+jet2_p4);
								foundZ=true;
							}
						}
					}
				}
			}
			if (foundZ)
			{
				h_DiJet_mass_best->Fill(Z_peak_best);
			  h_Z_E->Fill(Z_p4_best.E());
				h_Z_pT->Fill(Z_p4_best.Pt());
			}
			if (foundZ)
			{
				double H_peak_highest=0.;
				TLorentzVector H_p4_highest;
				for (unsigned int i=0; i<nJets; ++i)
				{
					TLorentzVector jet3_p4, jet4_p4;
					if (i!=Zjet1_i && i!=Zjet2_i && event.simpleJets2.at(i).csv>bTagCSV_cut && fabs(event.simpleJets2.at(i).p4.Eta())<2.4 && event.simpleJets2.at(i).p4.Pt()>jetpT_cut)
					{
						jet3_p4=event.simpleJets2.at(i).p4;
						for (unsigned int j=0; j<nJets; ++j)
						{
							if (j!=Zjet1_i && j!=Zjet2_i && j!=i && event.simpleJets2.at(j).csv>bTagCSV_cut && fabs(event.simpleJets2.at(j).p4.Eta())<2.4 && event.simpleJets2.at(j).p4.Pt()>jetpT_cut)
							{
								jet4_p4=event.simpleJets2.at(j).p4;
								TLorentzVector H_p4=jet3_p4+jet4_p4;
								double dPhi_ZH=Z_p4_best.DeltaPhi(H_p4);
								h_ZH_dPhi->Fill(fabs(dPhi_ZH));
								// if (fabs(dPhi_ZH)>2.8)
								{
								  double H_peak=H_p4.M();
								  h_H_mass->Fill(H_peak);
									
									// MC match these jets
									if ((truthMatch(jet3_p4, bZ_gen_p4) && truthMatch(jet4_p4, bH_gen_p4)) ||
							    (truthMatch(jet3_p4, bZ_gen_p4) && truthMatch(jet4_p4, bbH_gen_p4)) ||
									(truthMatch(jet3_p4, bbZ_gen_p4) && truthMatch(jet4_p4, bH_gen_p4)) ||
									(truthMatch(jet3_p4, bbZ_gen_p4) && truthMatch(jet4_p4, bbH_gen_p4)) ||
									(truthMatch(jet3_p4, bH_gen_p4) && truthMatch(jet4_p4, bZ_gen_p4)) ||
									(truthMatch(jet3_p4, bH_gen_p4) && truthMatch(jet4_p4, bbZ_gen_p4)) ||
									(truthMatch(jet3_p4, bbH_gen_p4) && truthMatch(jet4_p4, bZ_gen_p4)) ||
									(truthMatch(jet3_p4, bbH_gen_p4) && truthMatch(jet4_p4, bbZ_gen_p4))) h_H_mass_bZbHMatched->Fill(H_peak);
																		
									if ((truthMatch(jet3_p4, bH_gen_p4) && truthMatch(jet4_p4, bbH_gen_p4)) ||
									    (truthMatch(jet3_p4, bbH_gen_p4) && truthMatch(jet4_p4, bH_gen_p4))) h_H_mass_bHbHMatched->Fill(H_peak);
											
									if ((truthMatch(jet3_p4, bZ_gen_p4) && truthMatch(jet4_p4, bbZ_gen_p4)) ||
									    (truthMatch(jet3_p4, bbZ_gen_p4) && truthMatch(jet4_p4, bZ_gen_p4))) h_H_mass_bZbZMatched->Fill(H_peak);
									
									if (H_peak>H_peak_highest)
									{
										H_peak_highest=H_peak;
										H_p4_highest=H_p4;
										foundH=true;
									}
								}
							}
						}
					}
				}
				if (foundH)
				{
					h_H_mass_highest->Fill(H_peak_highest);
				}
			}
			
			
		}
		
	}
	
	std::cout<<"Done."<<std::endl;
	return 0;
}
