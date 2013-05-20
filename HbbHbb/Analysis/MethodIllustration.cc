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
#include <TArc.h>

double H_mass=125.0;
double mH_diff_cut=40.;
double mH_mean_cut=20.;
double marg=0.9*mH_mean_cut;

double mx1=H_mass-(5./3.)*mH_mean_cut;
double mx2=H_mass-mH_mean_cut;
double mx3=H_mass+mH_mean_cut;
double mx4=H_mass+(5./3.)*mH_mean_cut;

double my1=H_mass-(5./3.)*mH_mean_cut;
double my2=H_mass-mH_mean_cut;
double my3=H_mass+mH_mean_cut;
double my4=H_mass+(5./3.)*mH_mean_cut;

double rebin=2;

double r1=15., r2=35.;

int fit=1; // 0 = Fit 2&4, 1 = Fit 1, 24, 3

double Normalize(TH1* h)
{
  double nEntries=h->GetSumOfWeights();
  h->Scale(1./nEntries);
  return nEntries;
}

void drawRegion(double H_mass, double r1, double r2, std::string sr, std::string cr)
{
  TArc *circle1=new TArc(H_mass, H_mass, r1); circle1->SetLineWidth(2); circle1->SetLineColor(kBlue); circle1->SetFillStyle(0); circle1->Draw();
  TArc *circle2=new TArc(H_mass, H_mass, r2, 90., 180.); circle2->SetLineWidth(2); circle2->SetNoEdges(); circle2->SetLineColor(kRed); circle2->SetFillStyle(0); circle2->Draw();
  TArc *circle3=new TArc(H_mass, H_mass, r2, 270., 360.); circle3->SetLineWidth(3); circle3->SetNoEdges(); circle3->SetLineColor(kRed); circle3->SetFillStyle(0); circle3->Draw();
  TLine *line1=new TLine(H_mass-r2, H_mass, H_mass-r1, H_mass); line1->SetLineWidth(2); line1->SetLineColor(kRed); line1->Draw();
  TLine *line2=new TLine(H_mass+r2, H_mass, H_mass+r1, H_mass); line2->SetLineWidth(2); line2->SetLineColor(kRed); line2->Draw();
  TLine *line3=new TLine(H_mass, H_mass-r2, H_mass, H_mass-r1); line3->SetLineWidth(2); line3->SetLineColor(kRed); line3->Draw();
  TLine *line4=new TLine(H_mass, H_mass+r2, H_mass, H_mass+r1); line4->SetLineWidth(2); line4->SetLineColor(kRed); line4->Draw();
  TArrow *arrow1=new TArrow(H_mass, H_mass+r2*5, H_mass, H_mass, 0.02); arrow1->SetLineWidth(2); arrow1->SetLineColor(kBlue); arrow1->Draw();
  TPaveText *mod1=new TPaveText(H_mass-marg, H_mass+r2*5-marg, H_mass+marg, H_mass+r2*5+marg);
  mod1->SetBorderSize(0); mod1->SetFillColor(0); mod1->AddText(sr.c_str()); mod1->SetLineColor(kBlue); mod1->Draw("ARC");
  TArrow *arrow2_1=new TArrow(H_mass+r2*4., H_mass, H_mass-r2/2., H_mass+r2/2., 0.02); arrow2_1->SetLineWidth(2); arrow2_1->SetLineColor(kRed);     
  TArrow *arrow2_2=new TArrow(H_mass+r2*4., H_mass, H_mass+r2/2., H_mass-r2/2., 0.02); arrow2_2->SetLineWidth(2); arrow2_2->SetLineColor(kRed);
  TLine *arrow2_3=new TLine(H_mass+r2*4., H_mass, H_mass+r2*5., H_mass); arrow2_3->SetLineWidth(2); arrow2_3->SetLineColor(kRed);
  arrow2_1->Draw(); arrow2_2->Draw(); arrow2_3->Draw();
  TPaveText *mod2=new TPaveText(H_mass+r2*5.-marg, H_mass+marg, H_mass+r2*5.+marg, H_mass-marg);
  mod2->SetBorderSize(0); mod2->SetFillColor(0); mod2->AddText(cr.c_str()); mod2->SetLineColor(kRed); mod2->Draw("ARC");
  
}

void MethodIllustration()
{
  gROOT->SetStyle("Plain");
  gStyle->SetOptStat(000000000);
  
  TFile *data_8TeVData2012=new TFile("Histograms_8TeVData2012BCD_Skim.root");
  std::cout<<"Opened Histograms_8TeVData2012BCD_Data_2.root"<<std::endl;
  
  TH2F *h_mH_mH_3Tag_data=(TH2F*)data_8TeVData2012->Get("h_mH_mH");
  
  TCanvas *c_mH_mH_3Tag=new TCanvas("c_mH_mH_3Tag", "c_mH_mH_3Tag", 700, 700);
  h_mH_mH_3Tag_data->SetTitle("mH1 vs mH2 for Data; mH1 (GeV); mH2 (GeV)");
  h_mH_mH_3Tag_data->Draw("box");
  drawRegion(125., 15., 35., "SR", "SB");
  drawRegion(90., 15., 35., "VR", "VR-SB");
  // drawRegion(160., 15., 35., "CR2", "CR2-SB");
  TLegend *leg=new TLegend(0.45, 0.75, 0.9, 0.9);
  leg->SetFillStyle(0);
  leg->AddEntry((TObject*)0, "SR: Signal Region", "");
  leg->AddEntry((TObject*)0, "SB: Sideband", "");
  leg->AddEntry((TObject*)0, "VR: Control Region ", "");
  leg->AddEntry((TObject*)0, "VR-SB: Control Region  Sideband", "");
  // leg->AddEntry((TObject*)0, "CR2: Control Region 2", "");
  // leg->AddEntry((TObject*)0, "CR2-SB: Control Region 2 Sideband", ""); 
  leg->Draw();
  c_mH_mH_3Tag->SaveAs("Illustration_nTag_data.png");
  
  // Signal MC
  TFile *signal_8TeVData2012=new TFile("Histograms_glugluToX600ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX600ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_Signal_2.root"<<std::endl;
  
  TH2F *h_mH_mH_3Tag_signal=(TH2F*)signal_8TeVData2012->Get("h_mH_mH");
  
  TCanvas *c_mH_mH_3Tag_signal=new TCanvas("c_mH_mH_3Tag_signal", "c_mH_mH_3Tag_signal", 700, 700);
  h_mH_mH_3Tag_signal->SetTitle("mH1 vs mH2 for Signal mX=600 GeV; mH1 (GeV); mH2 (GeV)");
  h_mH_mH_3Tag_signal->Draw("box");
  drawRegion(125., 15., 35., "SR", "SB");
  drawRegion(90., 15., 35., "VR", "VR-SB");
  // drawRegion(160., 15., 35., "CR2", "CR2-SB");
  leg->Draw();
  c_mH_mH_3Tag_signal->SaveAs("Illustration_nTag_signal.png");
  
  
}
    
  
  
