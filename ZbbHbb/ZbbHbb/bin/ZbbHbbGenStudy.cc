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

int main(int argc, char* argv[])
{
  // load framework libraries
  gSystem->Load("libFWCoreFWLite");
  AutoLibraryLoader::enable();
  
  double pi=3.14159265358979;
	
	fwlite::TFileService outFile=fwlite::TFileService("genPlots.root");
	TH1F *h_Z_E=outFile.make<TH1F>("h_Z_E", "Z energy; E (GeV)", 200, 0., 1000.);
	TH1F *h_Z_pT=outFile.make<TH1F>("h_Z_pT", "Z p_T; p_T (GeV)", 200, 0., 1000.);
	TH1F *h_Z_phi=outFile.make<TH1F>("h_Z_phi", "Z #phi; #phi", 200, -pi, pi);
	TH1F *h_Z_eta=outFile.make<TH1F>("h_Z_eta", "Z #eta; #eta", 200, -5, 5);
	TH1F *h_Z_mass=outFile.make<TH1F>("h_Z_mass", "Z mass; mass (GeV)", 200, 0., 200.);
	TH1F *h_H_E=outFile.make<TH1F>("h_H_E", "H energy; E (GeV)", 200, 0., 1000.);
	TH1F *h_H_pT=outFile.make<TH1F>("h_H_pT", "H p_T; p_T (GeV)", 200, 0., 1000.);
	TH1F *h_H_phi=outFile.make<TH1F>("h_H_phi", "H #phi; #phi", 200, -pi, pi);
	TH1F *h_H_eta=outFile.make<TH1F>("h_H_eta", "H #eta; #eta", 200, -5, 5);
	TH1F *h_H_mass=outFile.make<TH1F>("h_H_mass", "H mass; mass (GeV)", 200, 0., 200.);
	TH1F *h_bZ_E=outFile.make<TH1F>("h_bZ_E", "b from Z energy; E (GeV)", 200, 0., 1000.);
	TH1F *h_bbZ_E=outFile.make<TH1F>("h_bbZ_E", "b' from Z energy; E (GeV)", 200, 0., 1000.);
	TH1F *h_bH_E=outFile.make<TH1F>("h_bH_E", "b from H energy; E (GeV)", 200, 0., 1000.);
	TH1F *h_bH_eta=outFile.make<TH1F>("h_bH_eta", "b #eta; #eta", 200, -10., 10.);
	TH1F *h_bbH_E=outFile.make<TH1F>("h_bbH_E", "b' from H energy; E (GeV)", 200, 0., 1000.);
	TH1F *h_bbH_eta=outFile.make<TH1F>("h_bbH_eta", "b' #eta; #eta", 200, -10., 10.);
	TH1F *h_ZH_theta=outFile.make<TH1F>("h_ZH_theta", "#theta(Z,H)", 100, 0, pi);
	TH1F *h_ZH_dR=outFile.make<TH1F>("h_ZH_dR", "#DeltaR(Z,H)", 100, 0, 10.);
	TH1F *h_ZH_dPhi=outFile.make<TH1F>("h_ZH_dPhi", "#Delta#Phi(Z,H)", 100, -pi, pi);
	TH1F *h_ZH_dEta=outFile.make<TH1F>("h_ZH_dEta", "#Delta#Eta(Z,H)", 100, -10., 10.);
	TH1F *h_DiJet_mass=outFile.make<TH1F>("h_DiJet_mass", "DiJet mass", 100, 0., 500.);
	
	std::vector<std::string> inFilenames;
	inFilenames.push_back("file:/uscms_data/d2/souvik/ZbbHbb/SignalEvents/H_110/PAT_H_110.edm.root");
	
	fwlite::ChainEvent event(inFilenames);
	for (event.toBegin(); !event.atEnd(); ++event)
	{
	  fwlite::Handle<VHbbEventAuxInfo> vhbbAuxHandle;
		vhbbAuxHandle.getByLabel(event, "HbbAnalyzerNew");
		const VHbbEventAuxInfo & aux = *vhbbAuxHandle.product();
		/*
		std::cout<<"#b = "<<aux.mcB.size()<<std::endl;
		std::cout<<"#b' = "<<aux.mcBbar.size()<<std::endl;
		std::cout<<"#H = "<<aux.mcH.size()<<std::endl;		
		std::cout<<"#Z = "<<aux.mcZ.size()<<std::endl;
		*/
		TLorentzVector Z_p4, H_p4, bZ_p4, bbZ_p4, bH_p4, bbH_p4;
		double Z_mass;
		for (unsigned int i=0; i<aux.mcZ.size(); ++i)
		{
			/*
			std::cout<<"Z status = "<<aux.mcZ.at(i).status<<std::endl;
			std::cout<<"Z E = "<<aux.mcZ.at(i).p4.E()<<std::endl;
			for (unsigned int j=0; j<aux.mcZ.at(i).dauid.size(); ++j)
			{
				std::cout<<"Z dauid = "<<aux.mcZ.at(i).dauid.at(j)<<std::endl;
			}
			*/
			if (aux.mcZ.at(i).dauid.size()==2)
			{
				if (aux.mcZ.at(i).dauid.at(0)==-5 && aux.mcZ.at(i).dauid.at(1)==5)
				{
					Z_p4=aux.mcZ.at(i).p4;
					bbZ_p4=aux.mcZ.at(i).dauFourMomentum.at(0);
					bZ_p4=aux.mcZ.at(i).dauFourMomentum.at(1);
					Z_mass=(bbZ_p4+bZ_p4).M();
				}
			}
		}
		double H_mass;
		for (unsigned int i=0; i<aux.mcH.size(); ++i)
		{
			/*
			std::cout<<"Higgs status = "<<aux.mcH.at(i).status<<std::endl;
			std::cout<<"Higgs E = "<<aux.mcH.at(i).p4.E()<<std::endl;
			for (unsigned int j=0; j<aux.mcH.at(i).dauid.size(); ++j)
			{
				std::cout<<"H dauid = "<<aux.mcH.at(i).dauid.at(j)<<std::endl;
			}
			*/
			if (aux.mcH.at(i).dauid.size()==2)
			{
				if (aux.mcH.at(i).dauid.at(0)==5 && aux.mcH.at(i).dauid.at(1)==-5)
				{
					H_p4=aux.mcH.at(i).p4;
					bH_p4=aux.mcH.at(i).dauFourMomentum.at(0);
					bbH_p4=aux.mcH.at(i).dauFourMomentum.at(1);
					H_mass=(bH_p4+bbH_p4).M();
				}
			}
		}
		
		fwlite::Handle<VHbbEvent> vhbbHandle;
		vhbbHandle.getByLabel(event, "HbbAnalyzerNew");
		const VHbbEvent &event=*vhbbHandle.product();
		
		TLorentzVector jet1_p4, jet2_p4;
		double jet1_csv, jet2_csv;
		for (unsigned int i=0; i<event.simpleJets2.size(); ++i)
		{
			jet1_p4=event.simpleJets2.at(i).p4;
			jet1_csv=event.simpleJets2.at(i).csv;
			if (jet1_csv>0.5 && jet1_p4.Eta()>-2.4 && jet1_p4.Eta()<2.4)
			{
				for (unsigned int j=0; j<event.simpleJets2.size(); ++j)
				{
					if (i!=j)
					{
						jet2_p4=event.simpleJets2.at(j).p4;
						jet2_csv=event.simpleJets2.at(j).csv;
						if (jet2_csv>0.5 && jet2_p4.Eta()>-2.4 && jet2_p4.Eta()<2.4)
						{
						 double mass=(jet1_p4+jet2_p4).M();
						 double pT=(jet1_p4+jet2_p4).Pt();
						 if (pT>150.) h_DiJet_mass->Fill(mass);
						}
					}
				}
			}
		}
		
		
		h_Z_E->Fill(Z_p4.E());
		h_Z_pT->Fill(Z_p4.Pt());
		h_Z_phi->Fill(Z_p4.Phi());
		h_Z_eta->Fill(Z_p4.Eta());
		h_Z_mass->Fill(Z_mass);
		h_H_E->Fill(H_p4.E());
		h_H_pT->Fill(H_p4.Pt());
		h_H_phi->Fill(H_p4.Phi());
		h_H_eta->Fill(H_p4.Eta());
		h_H_mass->Fill(H_mass);
		h_bZ_E->Fill(bZ_p4.E());
		h_bbZ_E->Fill(bbZ_p4.E());
		h_bH_E->Fill(bH_p4.E());
		h_bH_eta->Fill(bH_p4.Eta());
		h_bbH_E->Fill(bbH_p4.E());
		h_bbH_eta->Fill(bbH_p4.Eta());
		h_ZH_theta->Fill(Z_p4.Angle(H_p4.Vect()));
		h_ZH_dR->Fill(Z_p4.DeltaR(H_p4));
		h_ZH_dPhi->Fill(Z_p4.DeltaPhi(H_p4));
		h_ZH_dEta->Fill(Z_p4.Eta()-H_p4.Eta());
		
		
		// std::cout<<"==="<<std::endl;
		
	}
	
	std::cout<<"Done."<<std::endl;
	return 0;
}
