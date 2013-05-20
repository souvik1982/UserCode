#include <TH1F.h>
#include <TH2F.h>
#include <TROOT.h>
#include <TFile.h>
#include <TTree.h>
#include <TSystem.h>
#include <TChain.h>
#include <TLorentzVector.h>
#include <TLegend.h>
#include <TCanvas.h>
#include <TProfile.h>
#include <iostream>
#include <TFractionFitter.h>
#include <TStyle.h>
#include <TPaveText.h>
#include <THStack.h>
#include <TArrow.h>
#include <TColor.h>
#include <sstream>

std::string tostr(float t)
{
  std::ostringstream os; 
  os<<t; 
  return os.str(); 
}

TLegend* twoStatBoxes(TH1F* h1, TH1F* h2)
{
  TLegend *leg=new TLegend(0.6, 0.6, 0.9, 0.9);
  double wherepeak=(h2->GetMean())/(h2->GetXaxis()->GetXmax());
  // std::cout<<"wherepeak = "<<wherepeak<<std::endl;
  if (wherepeak>0.63) leg=new TLegend(0.1, 0.9, 0.4, 0.6);
  leg->AddEntry(h1, "Before regression");
  leg->AddEntry((TObject*)0, ("mean="+tostr(h1->GetMean())).c_str(), "");
  leg->AddEntry((TObject*)0, ("rms="+tostr(h1->GetRMS())).c_str(), "");
  leg->AddEntry((TObject*)0, "", "");
  leg->AddEntry(h2, "After regression");
  leg->AddEntry((TObject*)0, ("mean="+tostr(h2->GetMean())).c_str(), "");
  leg->AddEntry((TObject*)0, ("rms="+tostr(h2->GetRMS())).c_str(), "");
  leg->SetFillColor(10);
  return leg;
}

int DisplayBJetRegression()
{
  std::vector<std::string> masses;
  masses.push_back("300");
  masses.push_back("400");
  masses.push_back("500");
  masses.push_back("600");
  masses.push_back("700");
  masses.push_back("800");
  
  std::vector<int> colors;
  colors.push_back(kOrange);
  colors.push_back(kRed);
  colors.push_back(kMagenta);
  colors.push_back(kBlue);
  colors.push_back(kCyan);
  colors.push_back(kGreen);
  
  gROOT->SetStyle("Plain");
  gStyle->SetOptStat(000000000);
  gStyle->SetPalette(1);
  
  for (unsigned int i=1; i<masses.size(); ++i)
  {
  
    // First the regression quality plots
    TFile *file_qual=new TFile(("MMMM/Histograms_RegmX"+masses.at(i)+"_glugluToX"+masses.at(i)+"ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_MMMM.root").c_str());
    TH2F *h_RegGenpT_pT_1_b=(TH2F*)file_qual->Get("h_RegGenpT_pT_1_b");
    TH2F *h_RegGenpT_pT_2_b=(TH2F*)file_qual->Get("h_RegGenpT_pT_2_b");
    TH2F *h_RegGenpT_pT_3_b=(TH2F*)file_qual->Get("h_RegGenpT_pT_3_b");
    TH2F *h_RegGenpT_pT_4_b=(TH2F*)file_qual->Get("h_RegGenpT_pT_4_b");
    TH2F *h_RecoGenpT_pT_1_b=(TH2F*)file_qual->Get("h_RecoGenpT_pT_1_b");
    TH2F *h_RecoGenpT_pT_2_b=(TH2F*)file_qual->Get("h_RecoGenpT_pT_2_b");
    TH2F *h_RecoGenpT_pT_3_b=(TH2F*)file_qual->Get("h_RecoGenpT_pT_3_b");
    TH2F *h_RecoGenpT_pT_4_b=(TH2F*)file_qual->Get("h_RecoGenpT_pT_4_b");
    TProfile *p_RegGenpT_pT_1_b=h_RegGenpT_pT_1_b->ProfileX();
    TProfile *p_RegGenpT_pT_2_b=h_RegGenpT_pT_2_b->ProfileX();
    TProfile *p_RegGenpT_pT_3_b=h_RegGenpT_pT_3_b->ProfileX();
    TProfile *p_RegGenpT_pT_4_b=h_RegGenpT_pT_4_b->ProfileX();
    TProfile *p_RecoGenpT_pT_1_b=h_RecoGenpT_pT_1_b->ProfileX();
    TProfile *p_RecoGenpT_pT_2_b=h_RecoGenpT_pT_2_b->ProfileX();
    TProfile *p_RecoGenpT_pT_3_b=h_RecoGenpT_pT_3_b->ProfileX();
    TProfile *p_RecoGenpT_pT_4_b=h_RecoGenpT_pT_4_b->ProfileX();
    TFile *fileAll_qual=new TFile(("MMMM/Histograms_RegmXAll_glugluToX"+masses.at(i)+"ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_MMMM.root").c_str());
    TH2F *h_RegGenpT_pT_1_b_mXAll=(TH2F*)fileAll_qual->Get("h_RegGenpT_pT_1_b");
    TH2F *h_RegGenpT_pT_2_b_mXAll=(TH2F*)fileAll_qual->Get("h_RegGenpT_pT_2_b");
    TH2F *h_RegGenpT_pT_3_b_mXAll=(TH2F*)fileAll_qual->Get("h_RegGenpT_pT_3_b");
    TH2F *h_RegGenpT_pT_4_b_mXAll=(TH2F*)fileAll_qual->Get("h_RegGenpT_pT_4_b");
    TProfile *p_RegGenpT_pT_1_b_mXAll=h_RegGenpT_pT_1_b_mXAll->ProfileX();
    TProfile *p_RegGenpT_pT_2_b_mXAll=h_RegGenpT_pT_2_b_mXAll->ProfileX();
    TProfile *p_RegGenpT_pT_3_b_mXAll=h_RegGenpT_pT_3_b_mXAll->ProfileX();
    TProfile *p_RegGenpT_pT_4_b_mXAll=h_RegGenpT_pT_4_b_mXAll->ProfileX();
    // Reg-Gen
    TCanvas *c_RegGenpT_pT_1_b=new TCanvas("RegGenpT_pT_1_b", "RegGenpT_pT_1_b", 700, 700);
    h_RegGenpT_pT_1_b->Draw("colz");
    p_RegGenpT_pT_1_b->SetLineColor(kBlack); p_RegGenpT_pT_1_b->SetLineWidth(3); p_RegGenpT_pT_1_b->Draw("same");
    c_RegGenpT_pT_1_b->SaveAs(("c_RegGenpT_pT_1_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RegGenpT_pT_2_b=new TCanvas("RegGenpT_pT_2_b", "RegGenpT_pT_2_b", 700, 700);
    h_RegGenpT_pT_2_b->Draw("colz");
    p_RegGenpT_pT_2_b->SetLineColor(kBlack); p_RegGenpT_pT_2_b->SetLineWidth(3); p_RegGenpT_pT_2_b->Draw("same");
    c_RegGenpT_pT_2_b->SaveAs(("c_RegGenpT_pT_2_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RegGenpT_pT_3_b=new TCanvas("RegGenpT_pT_3_b", "RegGenpT_pT_3_b", 700, 700);
    h_RegGenpT_pT_3_b->Draw("colz");
    p_RegGenpT_pT_3_b->SetLineColor(kBlack); p_RegGenpT_pT_3_b->SetLineWidth(3); p_RegGenpT_pT_3_b->Draw("same");
    c_RegGenpT_pT_3_b->SaveAs(("c_RegGenpT_pT_3_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RegGenpT_pT_4_b=new TCanvas("RegGenpT_pT_4_b", "RegGenpT_pT_4_b", 700, 700);
    h_RegGenpT_pT_4_b->Draw("colz");
    p_RegGenpT_pT_4_b->SetLineColor(kBlack); p_RegGenpT_pT_4_b->SetLineWidth(3); p_RegGenpT_pT_4_b->Draw("same");
    c_RegGenpT_pT_4_b->SaveAs(("c_RegGenpT_pT_4_b_mX"+masses.at(i)+".png").c_str());
    // RegmXAll-Gen
    TCanvas *c_RegGenpT_pT_1_b_mXAll=new TCanvas("RegGenpT_pT_1_b_mXAll", "RegGenpT_pT_1_b_mXAll", 700, 700);
    h_RegGenpT_pT_1_b_mXAll->Draw("colz");
    p_RegGenpT_pT_1_b_mXAll->SetLineColor(kBlack); p_RegGenpT_pT_1_b_mXAll->SetLineWidth(3); p_RegGenpT_pT_1_b_mXAll->Draw("same");
    c_RegGenpT_pT_1_b_mXAll->SaveAs(("c_RegmXAllGenpT_pT_1_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RegGenpT_pT_2_b_mXAll=new TCanvas("RegGenpT_pT_2_b_mXAll", "RegGenpT_pT_2_b_mXAll", 700, 700);
    h_RegGenpT_pT_2_b_mXAll->Draw("colz");
    p_RegGenpT_pT_2_b_mXAll->SetLineColor(kBlack); p_RegGenpT_pT_2_b_mXAll->SetLineWidth(3); p_RegGenpT_pT_2_b_mXAll->Draw("same");
    c_RegGenpT_pT_2_b_mXAll->SaveAs(("c_RegmXAllGenpT_pT_2_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RegGenpT_pT_3_b_mXAll=new TCanvas("RegGenpT_pT_3_b_mXAll", "RegGenpT_pT_3_b_mXAll", 700, 700);
    h_RegGenpT_pT_3_b_mXAll->Draw("colz");
    p_RegGenpT_pT_3_b_mXAll->SetLineColor(kBlack); p_RegGenpT_pT_3_b_mXAll->SetLineWidth(3); p_RegGenpT_pT_3_b_mXAll->Draw("same");
    c_RegGenpT_pT_3_b_mXAll->SaveAs(("c_RegmXAllGenpT_pT_3_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RegGenpT_pT_4_b_mXAll=new TCanvas("RegGenpT_pT_4_b_mXAll", "RegGenpT_pT_4_b_mXAll", 700, 700);
    h_RegGenpT_pT_4_b_mXAll->Draw("colz");
    p_RegGenpT_pT_4_b_mXAll->SetLineColor(kBlack); p_RegGenpT_pT_4_b_mXAll->SetLineWidth(3); p_RegGenpT_pT_4_b_mXAll->Draw("same");
    c_RegGenpT_pT_4_b_mXAll->SaveAs(("c_RegmXAllGenpT_pT_4_b_mX"+masses.at(i)+".png").c_str());
    // Reco-Gen
    TCanvas *c_RecoGenpT_pT_1_b=new TCanvas("RecoGenpT_pT_1_b", "RecoGenpT_pT_1_b", 700, 700);
    h_RecoGenpT_pT_1_b->Draw("colz");
    p_RecoGenpT_pT_1_b->SetLineColor(kBlack); p_RecoGenpT_pT_1_b->SetLineWidth(3); p_RecoGenpT_pT_1_b->Draw("same");
    c_RecoGenpT_pT_1_b->SaveAs(("c_RecoGenpT_pT_1_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RecoGenpT_pT_2_b=new TCanvas("RecoGenpT_pT_2_b", "RecoGenpT_pT_2_b", 700, 700);
    h_RecoGenpT_pT_2_b->Draw("colz");
    p_RecoGenpT_pT_2_b->SetLineColor(kBlack); p_RecoGenpT_pT_2_b->SetLineWidth(3); p_RecoGenpT_pT_2_b->Draw("same");
    c_RecoGenpT_pT_2_b->SaveAs(("c_RecoGenpT_pT_2_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RecoGenpT_pT_3_b=new TCanvas("RecoGenpT_pT_3_b", "RecoGenpT_pT_3_b", 700, 700);
    h_RecoGenpT_pT_3_b->Draw("colz");
    p_RecoGenpT_pT_3_b->SetLineColor(kBlack); p_RecoGenpT_pT_3_b->SetLineWidth(3); p_RecoGenpT_pT_3_b->Draw("same");
    c_RecoGenpT_pT_3_b->SaveAs(("c_RecoGenpT_pT_3_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_RecoGenpT_pT_4_b=new TCanvas("RecoGenpT_pT_4_b", "RecoGenpT_pT_4_b", 700, 700);
    h_RecoGenpT_pT_4_b->Draw("colz");
    p_RecoGenpT_pT_4_b->SetLineColor(kBlack); p_RecoGenpT_pT_4_b->SetLineWidth(3); p_RecoGenpT_pT_4_b->Draw("same");
    c_RecoGenpT_pT_4_b->SaveAs(("c_RecoGenpT_pT_4_b_mX"+masses.at(i)+".png").c_str());
    
    // Reg-Reco
    TH2F *h_diffpT_pT_1_b=(TH2F*)fileAll_qual->Get("h_diffpT_pT_1_b"); h_diffpT_pT_1_b->SetYTitle("(reg pT - reco pT)/reco pT");
    TH2F *h_diffpT_pT_2_b=(TH2F*)fileAll_qual->Get("h_diffpT_pT_2_b"); h_diffpT_pT_2_b->SetYTitle("(reg pT - reco pT)/reco pT");
    TH2F *h_diffpT_pT_3_b=(TH2F*)fileAll_qual->Get("h_diffpT_pT_3_b"); h_diffpT_pT_3_b->SetYTitle("(reg pT - reco pT)/reco pT");
    TH2F *h_diffpT_pT_4_b=(TH2F*)fileAll_qual->Get("h_diffpT_pT_4_b"); h_diffpT_pT_4_b->SetYTitle("(reg pT - reco pT)/reco pT");
    TProfile *p_diffpT_pT_1_b=h_diffpT_pT_1_b->ProfileX(); p_diffpT_pT_1_b->SetLineWidth(3);
    TProfile *p_diffpT_pT_2_b=h_diffpT_pT_2_b->ProfileX(); p_diffpT_pT_2_b->SetLineWidth(3);
    TProfile *p_diffpT_pT_3_b=h_diffpT_pT_3_b->ProfileX(); p_diffpT_pT_3_b->SetLineWidth(3);
    TProfile *p_diffpT_pT_4_b=h_diffpT_pT_4_b->ProfileX(); p_diffpT_pT_4_b->SetLineWidth(3);
    TCanvas *c_diffpT_pT_1_b=new TCanvas("c_diffpT_pT_1_b", "c_diffpT_pT_1_b", 700, 700);
    h_diffpT_pT_1_b->Draw("colz");
    p_diffpT_pT_1_b->Draw("same");
    c_diffpT_pT_1_b->SaveAs(("c_diffpT_pT_1_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_diffpT_pT_2_b=new TCanvas("c_diffpT_pT_2_b", "c_diffpT_pT_2_b", 700, 700);
    h_diffpT_pT_2_b->Draw("colz");
    p_diffpT_pT_2_b->Draw("same");
    c_diffpT_pT_2_b->SaveAs(("c_diffpT_pT_2_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_diffpT_pT_3_b=new TCanvas("c_diffpT_pT_3_b", "c_diffpT_pT_3_b", 700, 700);
    h_diffpT_pT_3_b->Draw("colz");
    p_diffpT_pT_3_b->Draw("same");
    c_diffpT_pT_3_b->SaveAs(("c_diffpT_pT_3_b_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_diffpT_pT_4_b=new TCanvas("c_diffpT_pT_4_b", "c_diffpT_pT_4_b", 700, 700);
    h_diffpT_pT_4_b->Draw("colz");
    p_diffpT_pT_4_b->Draw("same");
    c_diffpT_pT_4_b->SaveAs(("c_diffpT_pT_4_b_mX"+masses.at(i)+".png").c_str());
    
    
    // Now, H masses right after kinematic selection + randomization
    TH1F *h_H1_mass=(TH1F*)file_qual->Get("h_H1_mass");
    TCanvas *c_H1_mass=new TCanvas("c_H1_mass", "c_H1_mass", 700, 700);
    h_H1_mass->SetLineColor(kRed); h_H1_mass->SetLineWidth(2);
    h_H1_mass->Draw();
    c_H1_mass->SaveAs(("c_H1_mass_mX"+masses.at(i)+".png").c_str());
    
    // H masses after b-jet regression
    TH1F *h_H1_mass_reg=(TH1F*)file_qual->Get("h_H1_mass_reg");
    TCanvas *c_H1_mass_reg=new TCanvas("c_H1_mass_reg", "c_H1_mass_reg", 700, 700);
    h_H1_mass_reg->SetLineColor(kRed); h_H1_mass_reg->SetLineWidth(2); h_H1_mass_reg->SetLineStyle(9); h_H1_mass_reg->Draw();
    h_H1_mass->SetLineColor(kRed); h_H1_mass->SetLineWidth(2); h_H1_mass->Draw("SAME");
    twoStatBoxes(h_H1_mass, h_H1_mass_reg)->Draw();
    c_H1_mass_reg->SaveAs(("c_H1_mass_reg_mX"+masses.at(i)+".png").c_str());
    
    TH1F *h_H1_mass_reg_mXAll=(TH1F*)fileAll_qual->Get("h_H1_mass_reg");
    TCanvas *c_H1_mass_reg_mXAll=new TCanvas("c_H1_mass_reg_mXAll", "c_H1_mass_reg_mXAll", 700, 700);
    h_H1_mass_reg_mXAll->SetLineColor(kRed); h_H1_mass_reg_mXAll->SetLineWidth(2); h_H1_mass_reg_mXAll->SetLineStyle(9); h_H1_mass_reg_mXAll->Draw();
    h_H1_mass->SetLineColor(kRed); h_H1_mass->SetLineWidth(2); h_H1_mass->Draw("SAME");
    twoStatBoxes(h_H1_mass, h_H1_mass_reg_mXAll)->Draw();
    c_H1_mass_reg_mXAll->SaveAs(("c_H1_mass_reg_mXAll"+masses.at(i)+".png").c_str());
    
    // H masses after b-jet regression, after b-tagging
    TFile *file=new TFile(("MMMM/Histograms_glugluToX"+masses.at(i)+"ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_MMMM.root").c_str());
    TH1F *h_H1_mass_bTagged=(TH1F*)file->Get("h_H1_mass_bTagged");
    TH1F *h_H1_mass_bTagged_reg=(TH1F*)file_qual->Get("h_H1_mass_bTagged");
    TH1F *h_H1_mass_bTagged_regmXAll=(TH1F*)fileAll_qual->Get("h_H1_mass_bTagged");
    h_H1_mass_bTagged->SetLineColor(kRed); h_H1_mass_bTagged->SetLineWidth(2);
    h_H1_mass_bTagged_reg->SetLineColor(kRed); h_H1_mass_bTagged_reg->SetLineWidth(2); h_H1_mass_bTagged_reg->SetLineStyle(9);
    h_H1_mass_bTagged_regmXAll->SetLineColor(kRed); h_H1_mass_bTagged_regmXAll->SetLineWidth(2); h_H1_mass_bTagged_regmXAll->SetLineStyle(9);
    TCanvas *c_H1_mass_bTagged=new TCanvas("c_H1_mass_bTagged", "c_H1_mass_bTagged", 700, 700);
    h_H1_mass_bTagged->Draw();
    c_H1_mass_bTagged->SaveAs(("c_H1_mass_bTagged_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_H1_mass_bTagged_reg=new TCanvas("c_H1_mass_bTagged_reg", "c_H1_mass_bTagged_reg", 700, 700);
    h_H1_mass_bTagged_reg->Draw();
    h_H1_mass_bTagged->Draw("SAME");
    twoStatBoxes(h_H1_mass_bTagged, h_H1_mass_bTagged_reg)->Draw();
    c_H1_mass_bTagged_reg->SaveAs(("c_H1_mass_bTagged_reg_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_H1_mass_bTagged_regmXAll=new TCanvas("c_H1_mass_bTagged_regmXAll", "c_H1_mass_bTagged_regmXAll", 700, 700);
    h_H1_mass_bTagged_regmXAll->Draw();
    h_H1_mass_bTagged->Draw("SAME");
    twoStatBoxes(h_H1_mass_bTagged, h_H1_mass_bTagged_regmXAll)->Draw();
    c_H1_mass_bTagged_regmXAll->SaveAs(("c_H1_mass_bTagged_regmXAll_mX"+masses.at(i)+".png").c_str());
    
    // X masses after kinematic selection + randomization
    TH1F *h_X_mass=(TH1F*)file->Get("h_X_mass");
    TH1F *h_X_mass_reg=(TH1F*)file_qual->Get("h_X_mass");
    TH1F *h_X_mass_regmXAll=(TH1F*)fileAll_qual->Get("h_X_mass");
    h_X_mass->SetLineColor(kBlue); h_X_mass->SetLineWidth(2);
    h_X_mass_reg->SetLineColor(kBlue); h_X_mass_reg->SetLineWidth(2); h_X_mass_reg->SetLineStyle(9);
    h_X_mass_regmXAll->SetLineColor(kBlue); h_X_mass_regmXAll->SetLineWidth(2); h_X_mass_regmXAll->SetLineStyle(9);
    TCanvas *c_X_mass=new TCanvas("c_X_mass", "c_X_mass", 700, 700);
    h_X_mass->Draw();
    c_X_mass->SaveAs(("c_X_mass_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_X_mass_reg=new TCanvas("c_X_mass_reg", "c_X_mass_reg", 700, 700);
    h_X_mass_reg->Draw();
    h_X_mass->Draw("same");
    twoStatBoxes(h_X_mass, h_X_mass_reg)->Draw();
    c_X_mass_reg->SaveAs(("c_X_mass_reg_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_X_mass_regmXAll=new TCanvas("c_X_mass_regmXAll", "c_X_mass_regmXAll", 700, 700);
    h_X_mass_regmXAll->Draw();
    h_X_mass->Draw("same");
    twoStatBoxes(h_X_mass, h_X_mass_regmXAll)->Draw();
    c_X_mass_regmXAll->SaveAs(("c_X_mass_regmXAll_mX"+masses.at(i)+".png").c_str());
    
    // X masses after kinematic selection + randomization
    TH1F *h_X_mass_bTagged=(TH1F*)file->Get("h_X_mass_bTagged");
    TH1F *h_X_mass_bTagged_reg=(TH1F*)file_qual->Get("h_X_mass_bTagged");
    TH1F *h_X_mass_bTagged_regmXAll=(TH1F*)fileAll_qual->Get("h_X_mass_bTagged");
    h_X_mass_bTagged->SetLineColor(kBlue); h_X_mass_bTagged->SetLineWidth(2);
    h_X_mass_bTagged_reg->SetLineColor(kBlue); h_X_mass_bTagged_reg->SetLineWidth(2); h_X_mass_bTagged_reg->SetLineStyle(9);
    h_X_mass_bTagged_regmXAll->SetLineColor(kBlue); h_X_mass_bTagged_regmXAll->SetLineWidth(2); h_X_mass_bTagged_regmXAll->SetLineStyle(9);
    TCanvas *c_X_mass_bTagged=new TCanvas("c_X_mass_bTagged", "c_X_mass_bTagged", 700, 700);
    h_X_mass_bTagged->Draw();
    c_X_mass_bTagged->SaveAs(("c_X_mass_bTagged_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_X_mass_bTagged_reg=new TCanvas("c_X_mass_bTagged_reg", "c_X_mass_bTagged_reg", 700, 700);
    h_X_mass_bTagged_reg->Draw();
    h_X_mass_bTagged->Draw("same");
    twoStatBoxes(h_X_mass_bTagged, h_X_mass_bTagged_reg)->Draw();
    c_X_mass_bTagged_reg->SaveAs(("c_X_mass_bTagged_reg_mX"+masses.at(i)+".png").c_str());
    TCanvas *c_X_mass_bTagged_regmXAll=new TCanvas("c_X_mass_bTagged_regmXAll", "c_X_mass_bTagged_regmXAll", 700, 700);
    h_X_mass_bTagged_regmXAll->Draw();
    h_X_mass_bTagged->Draw("same");
    twoStatBoxes(h_X_mass_bTagged, h_X_mass_bTagged_regmXAll)->Draw();
    c_X_mass_bTagged_regmXAll->SaveAs(("c_X_mass_bTagged_regmXAll_mX"+masses.at(i)+".png").c_str());
    
  }
  
  // Data
  TFile *file_DATA=new TFile("MMMM/Histograms_8TeVData2012BCD_SkimV10_MMMM.root");
  TFile *file_reg_DATA=new TFile("MMMM/Histograms_RegmXAll_8TeVData2012BCD_SkimV10_MMMM.root");
  
  //Regression quality plots
  TH2F *h_diffpT_pT_1_b_DATA=(TH2F*)file_reg_DATA->Get("h_diffpT_pT_1_b"); h_diffpT_pT_1_b_DATA->SetYTitle("(reg pT - reco pT)/reco pT");
  TH2F *h_diffpT_pT_2_b_DATA=(TH2F*)file_reg_DATA->Get("h_diffpT_pT_2_b"); h_diffpT_pT_2_b_DATA->SetYTitle("(reg pT - reco pT)/reco pT");
  TH2F *h_diffpT_pT_3_b_DATA=(TH2F*)file_reg_DATA->Get("h_diffpT_pT_3_b"); h_diffpT_pT_3_b_DATA->SetYTitle("(reg pT - reco pT)/reco pT");
  TH2F *h_diffpT_pT_4_b_DATA=(TH2F*)file_reg_DATA->Get("h_diffpT_pT_4_b"); h_diffpT_pT_4_b_DATA->SetYTitle("(reg pT - reco pT)/reco pT");
  TProfile *p_diffpT_pT_1_b_DATA=h_diffpT_pT_1_b_DATA->ProfileX();
  TProfile *p_diffpT_pT_2_b_DATA=h_diffpT_pT_2_b_DATA->ProfileX();
  TProfile *p_diffpT_pT_3_b_DATA=h_diffpT_pT_3_b_DATA->ProfileX();
  TProfile *p_diffpT_pT_4_b_DATA=h_diffpT_pT_4_b_DATA->ProfileX();
  TCanvas *c_diffpT_pT_1_b_DATA=new TCanvas("c_diffpT_pT_1_b_DATA", "c_diffpT_pT_1_b_DATA", 700, 700);
  h_diffpT_pT_1_b_DATA->Draw("colz");
  p_diffpT_pT_1_b_DATA->SetLineWidth(3); p_diffpT_pT_1_b_DATA->Draw("same");
  c_diffpT_pT_1_b_DATA->SaveAs("c_diffpT_pT_1_b_DATA.png");
  TCanvas *c_diffpT_pT_2_b_DATA=new TCanvas("c_diffpT_pT_2_b_DATA", "c_diffpT_pT_2_b_DATA", 700, 700);
  h_diffpT_pT_2_b_DATA->Draw("colz");
  p_diffpT_pT_2_b_DATA->SetLineWidth(3); p_diffpT_pT_2_b_DATA->Draw("same");
  c_diffpT_pT_2_b_DATA->SaveAs("c_diffpT_pT_2_b_DATA.png");
  TCanvas *c_diffpT_pT_3_b_DATA=new TCanvas("c_diffpT_pT_3_b_DATA", "c_diffpT_pT_3_b_DATA", 700, 700);
  h_diffpT_pT_3_b_DATA->Draw("colz");
  p_diffpT_pT_3_b_DATA->SetLineWidth(3); p_diffpT_pT_3_b_DATA->Draw("same");
  c_diffpT_pT_3_b_DATA->SaveAs("c_diffpT_pT_3_b_DATA.png");
  TCanvas *c_diffpT_pT_4_b_DATA=new TCanvas("c_diffpT_pT_4_b_DATA", "c_diffpT_pT_4_b_DATA", 700, 700);
  h_diffpT_pT_4_b_DATA->Draw("colz");
  p_diffpT_pT_4_b_DATA->SetLineWidth(3); p_diffpT_pT_4_b_DATA->Draw("same");
  c_diffpT_pT_4_b_DATA->SaveAs("c_diffpT_pT_4_b_DATA.png");
  
  // H mass right after kinematic selection and randomization, and then regression
  TH1F *h_H1_mass_DATA=(TH1F*)file_reg_DATA->Get("h_H1_mass");
  TH1F *h_H1_mass_reg_DATA=(TH1F*)file_reg_DATA->Get("h_H1_mass_reg");
  h_H1_mass_DATA->SetLineColor(kRed); h_H1_mass_DATA->SetLineWidth(2);
  h_H1_mass_reg_DATA->SetLineColor(kRed); h_H1_mass_reg_DATA->SetLineWidth(2); h_H1_mass_reg_DATA->SetLineStyle(7);
  TCanvas *c_H1_mass_DATA=new TCanvas("c_H1_mass_DATA", "c_H1_mass_DATA", 700, 700);
  h_H1_mass_DATA->Draw();
  h_H1_mass_reg_DATA->Draw("SAME");
  twoStatBoxes(h_H1_mass_DATA, h_H1_mass_reg_DATA)->Draw();
  c_H1_mass_DATA->SaveAs("c_H1_mass_DATA.png");
  
  // H mass after kinematic selection, randomization, regression and then b-tagging
  TH1F *h_H1_mass_bTagged_reg_DATA=(TH1F*)file_reg_DATA->Get("h_H1_mass_bTagged"); h_H1_mass_bTagged_reg_DATA->Rebin(2);
  TH1F *h_H1_mass_bTagged_DATA=(TH1F*)file_DATA->Get("h_H1_mass_bTagged"); h_H1_mass_bTagged_DATA->Rebin(2);
  h_H1_mass_bTagged_reg_DATA->SetLineColor(kRed); h_H1_mass_bTagged_reg_DATA->SetLineWidth(2); h_H1_mass_bTagged_reg_DATA->SetLineStyle(7);
  h_H1_mass_bTagged_DATA->SetLineColor(kRed); h_H1_mass_bTagged_DATA->SetLineWidth(2);
  TCanvas *c_H1_mass_bTagged_DATA=new TCanvas("H1_mass_bTagged_DATA", "H1_mass_bTagged_DATA", 700, 700);
  h_H1_mass_bTagged_DATA->Draw();
  h_H1_mass_bTagged_reg_DATA->Draw("SAME");
  twoStatBoxes(h_H1_mass_bTagged_DATA, h_H1_mass_bTagged_reg_DATA)->Draw();
  c_H1_mass_bTagged_DATA->SaveAs("c_H1_mass_bTagged_DATA.png");
  
  
  // X mass right after kinematic selection and randomization, and then regression
  TH1F *h_X_mass_DATA=(TH1F*)file_DATA->Get("h_X_mass");
  TH1F *h_X_mass_reg_DATA=(TH1F*)file_reg_DATA->Get("h_X_mass");
  TH1F *h_X_mass_bTagged_DATA=(TH1F*)file_DATA->Get("h_X_mass_bTagged"); h_X_mass_bTagged_DATA->Rebin(2);
  TH1F *h_X_mass_bTagged_reg_DATA=(TH1F*)file_reg_DATA->Get("h_X_mass_bTagged"); h_X_mass_bTagged_reg_DATA->Rebin(2);
  h_X_mass_DATA->SetLineColor(kBlue); h_X_mass_DATA->SetLineWidth(2);
  h_X_mass_reg_DATA->SetLineColor(kBlue); h_X_mass_reg_DATA->SetLineWidth(2); h_X_mass_reg_DATA->SetLineStyle(7);
  h_X_mass_bTagged_DATA->SetLineColor(kBlue); h_X_mass_bTagged_DATA->SetLineWidth(2);
  h_X_mass_bTagged_reg_DATA->SetLineColor(kBlue); h_X_mass_bTagged_reg_DATA->SetLineWidth(2); h_X_mass_bTagged_reg_DATA->SetLineStyle(7);
  TCanvas *c_X_mass_DATA=new TCanvas("c_X_mass_DATA", "c_X_mass_DATA", 700, 700);
  h_X_mass_DATA->Draw();
  h_X_mass_reg_DATA->Draw("SAME");
  twoStatBoxes(h_X_mass_DATA, h_X_mass_reg_DATA)->Draw();
  c_X_mass_DATA->SaveAs("c_X_mass_DATA.png");
  TCanvas *c_X_mass_bTagged_DATA=new TCanvas("c_X_mass_bTagged_DATA", "c_X_mass_bTagged_DATA", 700, 700);
  h_X_mass_bTagged_DATA->Draw();
  h_X_mass_bTagged_reg_DATA->Draw("SAME");
  twoStatBoxes(h_X_mass_bTagged_DATA, h_X_mass_bTagged_reg_DATA)->Draw();
  c_X_mass_bTagged_DATA->SaveAs("c_X_mass_bTagged_DATA.png");
  
  
  /*
  for (unsigned int i=0; i<masses.size(); ++i)
  {
    TFile *nom=new TFile(("MMMM_a/Histograms_glugluToX"+masses.at(i)+"ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_Signal_2.root").c_str());
    TH1F *h_H1_mass_nom=(TH1F*)nom->Get("h_H1_mass");
  
    TFile *reg=new TFile(("MMMM_bReg_a/Histograms_glugluToX"+masses.at(i)+"ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_Signal_2.root").c_str());
    TH1F *h_H1_mass_reg=(TH1F*)reg->Get("h_H1_mass");
    
    h_H1_mass_nom->SetLineColor(kRed); h_H1_mass_nom->SetLineWidth(2); h_H1_mass_nom->SetLineStyle(9); 
    h_H1_mass_reg->SetLineColor(kRed); h_H1_mass_reg->SetLineWidth(2); h_H1_mass_reg->SetTitle("Higgs Mass");
  
    TCanvas *c_H_mass=new TCanvas(("c_H_mass"+masses.at(i)).c_str(), "c_H_mass", 700, 700);
    h_H1_mass_reg->Draw();
    h_H1_mass_nom->Draw("SAME");
    double nom_mean=h_H1_mass_nom->GetMean();
    double nom_rms=h_H1_mass_nom->GetRMS();
    double reg_mean=h_H1_mass_reg->GetMean();
    double reg_rms=h_H1_mass_reg->GetRMS();
    TLegend *leg=new TLegend(0.6, 0.6, 0.9, 0.9);
    leg->AddEntry((TObject*)0, ("m_{X} = "+(masses.at(i))+" GeV").c_str(), "");
    leg->AddEntry((TObject*)0, "", "");
    leg->AddEntry(h_H1_mass_nom, "Nominal m_{H}");
    leg->AddEntry((TObject*)0, ("mean = "+tostr(nom_mean)).c_str(), "");
    leg->AddEntry((TObject*)0, ("rms = "+tostr(nom_rms)).c_str(), "");
    leg->AddEntry((TObject*)0, "", "");
    leg->AddEntry(h_H1_mass_reg, "b-jet Regressed m_{H}");
    leg->AddEntry((TObject*)0, ("mean = "+tostr(reg_mean)).c_str(), "");
    leg->AddEntry((TObject*)0, ("rms = "+tostr(reg_rms)).c_str(), "");
    leg->Draw();
    c_H_mass->SaveAs(("c_bRegImprovement_"+masses.at(i)+".png").c_str());
    
  }
  */
  return 0;
}
  
