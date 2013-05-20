#include <TH1F.h>
#include <TF1.h>
#include <TROOT.h>
#include <TFile.h>
#include <TLegend.h>
#include <TCanvas.h>
#include <iostream>
#include <TStyle.h>
#include <TPaveText.h>
#include <TArrow.h>

int rebin=1;

Double_t crystalBall(Double_t *x, Double_t *par)
{
  Double_t std=(x[0]-par[2])/par[3];
  Double_t A=pow(par[1]/par[0], par[1])*exp(-0.5*pow(par[0], 2));
  Double_t B=par[1]/par[0]-par[0];
  Double_t result=0.;
  
  if (std<par[0]) // Gaussian region
  {
    result=exp(-0.5*pow(std, 2));
  }
  else // Power Law region
  {
    result=A/pow(B+std, par[1]);
  }
  
  result=result*par[4];
  
  return result;
}

void fitSignal(TH1F *h, std::string mass)
{
  RooRealVar *x, *sg_p0, *sg_p1, *sg_p2, *sg_p3;
  
  if (mass=="400")
  {
    // x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    x=new RooRealVar("x", "m_{X} (GeV)", 300., 600.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 1.0, 2.5);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 1., 10.);
    sg_p2=new RooRealVar("sg_p2", "sg_p2", 380., 420.);
    sg_p3=new RooRealVar("sg_p3", "sg_p3", 1., 20.);
  }
  else if (mass=="500")
  {
    x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 1.0, 3.0);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 1., 10.);
    sg_p2=new RooRealVar("sg_p2", "sg_p2", 470., 530.);
    sg_p3=new RooRealVar("sg_p3", "sg_p3", 10., 30.);
  }
  else if (mass=="600")
  {
    x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 1.0, 4.0);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 0.01, 1.);
    sg_p2=new RooRealVar("sg_p2", "sg_p2", 580., 620.);
    sg_p3=new RooRealVar("sg_p3", "sg_p3", 10., 30.);
  }
  else if (mass=="700")
  {
    x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 0.5, 4.0);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 1.0, 4.0);
    sg_p2=new RooRealVar("sg_p2", "sg_p2", 680., 750.);
    sg_p3=new RooRealVar("sg_p3", "sg_p3", 1., 40.);
  }
  else if (mass=="800")
  {
    // x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    x=new RooRealVar("x", "m_{X} (GeV)", 600., 1000.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 1.0, 5.0);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 0.1, 4.0);
    sg_p2=new RooRealVar("sg_p2", "sg_p2", 780., 850.);
    sg_p3=new RooRealVar("sg_p3", "sg_p3", 10., 40.);
  }
  RevCrystalBall signal("signal", "Signal Prediction", *x, *sg_p0, *sg_p1, *sg_p2, *sg_p3);
  RooDataHist signalHistogram("signalHistogram", "Signal Histogram", RooArgList(*x), h);
  signal.fitTo(signalHistogram, RooFit::SumW2Error(kTRUE));
  // Make a fixed RooAbsPdf with the fit parameters
  std::cout<<"sg_p3->getVal() = "<<sg_p3->getVal()<<std::endl;
  RooRealVar signal_p0("signal_p0", "signal_p0", sg_p0->getVal());
  RooRealVar signal_p1("signal_p1", "signal_p1", sg_p1->getVal());
  RooRealVar signal_p2("signal_p2", "signal_p2", sg_p2->getVal());
  RooRealVar signal_p3("signal_p3", "signal_p3", sg_p3->getVal());
  RevCrystalBall signal_fixed("signal", "Signal Prediction Fixed", *x, signal_p0, signal_p1, signal_p2, signal_p3);
  
  
  RooPlot *plot=x->frame();
  signalHistogram.plotOn(plot);
  signal.plotOn(plot);
  TCanvas *c_SignalmX=new TCanvas(("c_SignalmX"+mass).c_str(), ("c_SignalmX"+mass).c_str(), 500, 500);
  plot->Draw();
  c_SignalmX->SaveAs(("c_SignalmX_"+mass+".png").c_str());
  c_SignalmX->SaveAs(("c_SignalmX_"+mass+".root").c_str());
  RooWorkspace *w=new RooWorkspace("HbbHbb");
  // w->import(signal);
  w->import(signal_fixed);
  w->SaveAs(("w_signal_"+mass+".root").c_str());
}

int SignalShapeFit()
{
  double chisq, ndf, chisq_ndf;
  double nSignal=0;
  
  gROOT->SetStyle("Plain");
  gStyle->SetOptStat(000000000);
  gSystem->Load("../../PDFs/RevCrystalBall_cxx.so");
  
  // Calculate nSignal events given production cross section, branching fractions and efficiency
  double nSignal_init=100000.;
  double totalLumi=13241.968; // /pb
  double prodXsec_1=1.; // pb
/*
  TFile *glugluToX300=new TFile("Histograms_glugluToX300ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX300ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_Signal_2.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_300=(TH1F*)glugluToX300->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_300->SetTitle("Reconstructed m_{X} in Signal MC (m_{X}=300 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_300->Rebin(rebin);
  h_mjjjj_3Tag_SR_300->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_300->Scale(totalLumi*prodXsec_1/nSignal_init);
  TCanvas *c_mjjjj_3Tag_SR_300=new TCanvas("c_mjjjj_3Tag_SR_300", "c_mjjjj_3Tag_SR_300", 500, 500);
  h_mjjjj_3Tag_SR_300->Draw();
  c_mjjjj_3Tag_SR_300->SaveAs("c_mjjjj_3Tag_SR_300.png");

  TFile *glugluToX400=new TFile("Histograms_glugluToX400ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX400ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_Signal_2.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_400=(TH1F*)glugluToX400->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_400->SetTitle("m_{X} Peak in Signal MC (m_{X}=400 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_400->Rebin(rebin);
  h_mjjjj_3Tag_SR_400->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_400->Scale(totalLumi*prodXsec_1/nSignal_init);
  TCanvas *c_mjjjj_3Tag_SR_400=new TCanvas("c_mjjjj_3Tag_SR_400", "c_mjjjj_3Tag_SR_400", 500, 500);
  h_mjjjj_3Tag_SR_400->Draw();
  h_mjjjj_3Tag_SR_400->SetMaximum(h_mjjjj_3Tag_SR_400->GetMaximum()*1.4);
  TF1 *f_mjjjj_3Tag_SR_400=new TF1("f_mjjjj_3Tag_SR_400", crystalBall, 250., 1100., 5);
  f_mjjjj_3Tag_SR_400->SetLineWidth(0);
  f_mjjjj_3Tag_SR_400->SetParLimits(0, 0.1, 2.0);
  f_mjjjj_3Tag_SR_400->SetParLimits(1, 1., 20.);
  f_mjjjj_3Tag_SR_400->SetParLimits(2, 380., 420.);
  f_mjjjj_3Tag_SR_400->SetParLimits(3, 10., 30.);
  f_mjjjj_3Tag_SR_400->SetParLimits(4, 15., 30.);
  h_mjjjj_3Tag_SR_400->Fit(f_mjjjj_3Tag_SR_400, "REFMN");
  f_mjjjj_3Tag_SR_400->Draw("SAME");
  chisq=f_mjjjj_3Tag_SR_400->GetChisquare();
  ndf=f_mjjjj_3Tag_SR_400->GetNDF();
  chisq_ndf=chisq/ndf;
  nSignal=h_mjjjj_3Tag_SR_400->GetSumOfWeights();
  std::cout<<"chi^2 = "<<chisq<<", ndf = "<<ndf<<", chi^2/ndf = "<<chisq_ndf<<std::endl;
  std::cout<<"nSignal = "<<nSignal<<std::endl;
  c_mjjjj_3Tag_SR_400->SaveAs("c_mjjjj_3Tag_SR_400.png");
  fitSignal(h_mjjjj_3Tag_SR_400, "400");

  TFile *glugluToX500=new TFile("Histograms_glugluToX500ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX500ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_500=(TH1F*)glugluToX500->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_500->SetTitle("m_{X} Peak in Signal MC (m_{X}=500 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_500->Rebin(rebin);
  h_mjjjj_3Tag_SR_500->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_500->Scale(totalLumi*prodXsec_1/nSignal_init);
  TCanvas *c_mjjjj_3Tag_SR_500=new TCanvas("c_mjjjj_3Tag_SR_500", "c_mjjjj_3Tag_SR_500", 500, 500);
  h_mjjjj_3Tag_SR_500->Draw();
  TF1 *f_mjjjj_3Tag_SR_500=new TF1("f_mjjjj_3Tag_SR_500", crystalBall, 250., 1100., 5);
  f_mjjjj_3Tag_SR_500->SetLineWidth(0);
  f_mjjjj_3Tag_SR_500->SetParLimits(0, 0.1, 3.0);
  f_mjjjj_3Tag_SR_500->SetParLimits(1, 0.1, 1.);
  f_mjjjj_3Tag_SR_500->SetParLimits(2, 470., 530.);
  f_mjjjj_3Tag_SR_500->SetParLimits(3, 10., 30.);
  f_mjjjj_3Tag_SR_500->SetParLimits(4, 60., 80.);
  h_mjjjj_3Tag_SR_500->Fit(f_mjjjj_3Tag_SR_500, "REFMN");
  f_mjjjj_3Tag_SR_500->Draw("SAME");
  chisq=f_mjjjj_3Tag_SR_500->GetChisquare();
  ndf=f_mjjjj_3Tag_SR_500->GetNDF();
  chisq_ndf=chisq/ndf;
  nSignal=h_mjjjj_3Tag_SR_500->GetSumOfWeights();
  std::cout<<"chi^2 = "<<chisq<<", ndf = "<<ndf<<", chi^2/ndf = "<<chisq_ndf<<std::endl;
  std::cout<<"nSignal = "<<nSignal<<std::endl;
  c_mjjjj_3Tag_SR_500->SaveAs("c_mjjjj_3Tag_SR_500.png");
  fitSignal(h_mjjjj_3Tag_SR_500, "500");
  
  TFile *glugluToX600=new TFile("Histograms_glugluToX600ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX600ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_600=(TH1F*)glugluToX600->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_600->SetTitle("m_{X} Peak in Signal MC (m_{X}=600 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_600->Rebin(rebin);
  h_mjjjj_3Tag_SR_600->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_600->Scale(totalLumi*prodXsec_1/nSignal_init);
  TCanvas *c_mjjjj_3Tag_SR_600=new TCanvas("c_mjjjj_3Tag_SR_600", "c_mjjjj_3Tag_SR_600", 500, 500);
  h_mjjjj_3Tag_SR_600->Draw();
  TF1 *f_mjjjj_3Tag_SR_600=new TF1("f_mjjjj_3Tag_SR_600", crystalBall, 250., 800., 5);
  f_mjjjj_3Tag_SR_600->SetLineWidth(0);
  f_mjjjj_3Tag_SR_600->SetParLimits(0, 1.0, 4.0);
  f_mjjjj_3Tag_SR_600->SetParLimits(1, 0.01, 1.0);
  f_mjjjj_3Tag_SR_600->SetParLimits(2, 580., 620.);
  f_mjjjj_3Tag_SR_600->SetParLimits(3, 10., 40.);
  f_mjjjj_3Tag_SR_600->SetParLimits(4, 80., 90.);
  h_mjjjj_3Tag_SR_600->Fit(f_mjjjj_3Tag_SR_600, "REFMN");
  f_mjjjj_3Tag_SR_600->Draw("SAME");
  chisq=f_mjjjj_3Tag_SR_600->GetChisquare();
  ndf=f_mjjjj_3Tag_SR_600->GetNDF();
  chisq_ndf=chisq/ndf;
  nSignal=h_mjjjj_3Tag_SR_600->GetSumOfWeights();
  std::cout<<"chi^2 = "<<chisq<<", ndf = "<<ndf<<", chi^2/ndf = "<<chisq_ndf<<std::endl;
  std::cout<<"nSignal = "<<nSignal<<std::endl;
  c_mjjjj_3Tag_SR_600->SaveAs("c_mjjjj_3Tag_SR_600.png");
  fitSignal(h_mjjjj_3Tag_SR_600, "600");
  
  TFile *glugluToX700=new TFile("Histograms_glugluToX700ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX700ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_Signal_2.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_700=(TH1F*)glugluToX700->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_700->SetTitle("m_{X} Peak in Signal MC (m_{X}=700 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_700->Rebin(rebin);
  h_mjjjj_3Tag_SR_700->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_700->Scale(totalLumi*prodXsec_1/nSignal_init);
  TCanvas *c_mjjjj_3Tag_SR_700=new TCanvas("c_mjjjj_3Tag_SR_700", "c_mjjjj_3Tag_SR_700", 500, 500);
  h_mjjjj_3Tag_SR_700->Draw();
  TF1 *f_mjjjj_3Tag_SR_700=new TF1("f_mjjjj_3Tag_SR_700", crystalBall, 250., 1100., 5);
  f_mjjjj_3Tag_SR_700->SetLineWidth(0);
  f_mjjjj_3Tag_SR_700->SetParLimits(0, 0.1, 4.0);
  f_mjjjj_3Tag_SR_700->SetParLimits(1, 1.0, 3.0.);
  f_mjjjj_3Tag_SR_700->SetParLimits(2, 690., 720.);
  f_mjjjj_3Tag_SR_700->SetParLimits(3, 25., 50.);
  f_mjjjj_3Tag_SR_700->SetParLimits(4, 90., 110.);
  h_mjjjj_3Tag_SR_700->Fit(f_mjjjj_3Tag_SR_700, "REFMN");
  f_mjjjj_3Tag_SR_700->Draw("SAME");
  chisq=f_mjjjj_3Tag_SR_700->GetChisquare();
  ndf=f_mjjjj_3Tag_SR_700->GetNDF();
  chisq_ndf=chisq/ndf;
  nSignal=h_mjjjj_3Tag_SR_700->GetSumOfWeights();
  std::cout<<"chi^2 = "<<chisq<<", ndf = "<<ndf<<", chi^2/ndf = "<<chisq_ndf<<std::endl;
  std::cout<<"nSignal = "<<nSignal<<std::endl;
  c_mjjjj_3Tag_SR_700->SaveAs("c_mjjjj_3Tag_SR_700.png");
  fitSignal(h_mjjjj_3Tag_SR_700, "700");
*/
  TFile *glugluToX800=new TFile("Histograms_glugluToX800ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX800ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_800=(TH1F*)glugluToX800->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_800->SetTitle("m_{X} Peak in Signal MC (m_{X}=800 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_800->Rebin(rebin);
  h_mjjjj_3Tag_SR_800->SetMaximum(850.);
  h_mjjjj_3Tag_SR_800->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_800->Scale(totalLumi*prodXsec_1/nSignal_init);
  TCanvas *c_mjjjj_3Tag_SR_800=new TCanvas("c_mjjjj_3Tag_SR_800", "c_mjjjj_3Tag_SR_800", 500, 500);
  h_mjjjj_3Tag_SR_800->Draw();
  TF1 *f_mjjjj_3Tag_SR_800=new TF1("f_mjjjj_3Tag_SR_800", crystalBall, 250., 1100., 5);
  f_mjjjj_3Tag_SR_800->SetLineWidth(0);
  f_mjjjj_3Tag_SR_800->SetParLimits(0, 2.0, 5.0);
  f_mjjjj_3Tag_SR_800->SetParLimits(1, 0.1, 1.0);
  f_mjjjj_3Tag_SR_800->SetParLimits(2, 750., 850.);
  f_mjjjj_3Tag_SR_800->SetParLimits(3, 20., 70.);
  f_mjjjj_3Tag_SR_800->SetParLimits(4, 90., 120.);
  h_mjjjj_3Tag_SR_800->Fit(f_mjjjj_3Tag_SR_800, "REFMN");
  f_mjjjj_3Tag_SR_800->Draw("SAME");
  chisq=f_mjjjj_3Tag_SR_800->GetChisquare();
  ndf=f_mjjjj_3Tag_SR_800->GetNDF();
  chisq_ndf=chisq/ndf;
  nSignal=h_mjjjj_3Tag_SR_800->GetSumOfWeights();
  std::cout<<"chi^2 = "<<chisq<<", ndf = "<<ndf<<", chi^2/ndf = "<<chisq_ndf<<std::endl;
  std::cout<<"nSignal = "<<nSignal<<std::endl;c_mjjjj_3Tag_SR_800->SaveAs("c_mjjjj_3Tag_SR_800.png");
  fitSignal(h_mjjjj_3Tag_SR_800, "800");

  return 0;
}
  
                                                     
