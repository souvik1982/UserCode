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
#include <iostream>
#include <fstream>

int rebin=1;
ofstream outfile;

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
  RooRealVar *x, *sg_p0, *sg_p1;
  
  if (mass=="400")
  {
    // x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    x=new RooRealVar("x", "m_{X} (GeV)", 300., 600.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 380., 420.);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 1., 20.);
  }
  else if (mass=="500")
  {
    // x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    x=new RooRealVar("x", "m_{X} (GeV)", 300., 700.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 470., 530.);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 10., 30.);
  }
  else if (mass=="600")
  {
    // x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    x=new RooRealVar("x", "m_{X} (GeV)", 400., 800.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 580., 620.);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 10., 30.);
  }
  else if (mass=="700")
  {
    // x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    x=new RooRealVar("x", "m_{X} (GeV)", 500., 900.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 680., 750.);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 10., 40.);
  }
  else if (mass=="800")
  {
    // x=new RooRealVar("x", "m_{X} (GeV)", 300., 1100.);
    x=new RooRealVar("x", "m_{X} (GeV)", 600., 1000.);
    sg_p0=new RooRealVar("sg_p0", "sg_p0", 780., 850.);
    sg_p1=new RooRealVar("sg_p1", "sg_p1", 10., 40.);
  }
  RooGaussian signal("signal", "Signal Prediction", *x, *sg_p0, *sg_p1);
  RooDataHist signalHistogram("signalHistogram", "Signal Histogram", RooArgList(*x), h);
  std::cout<<" ======================= "<<std::endl;
  std::cout<<" === FITTING mH = "<<mass<<" GeV === "<<std::endl;
  std::cout<<" ======================= "<<std::endl;
  signal.fitTo(signalHistogram, RooFit::SumW2Error(kTRUE));
  std::cout<<" ======================= "<<std::endl;
  std::cout<<" ======================= "<<std::endl;
  std::cout<<" ======================= "<<std::endl;
  // Make a fixed RooAbsPdf with the fit parameters
  RooRealVar signal_p0("signal_p0", "signal_p0", sg_p0->getVal());
  RooRealVar signal_p1("signal_p1", "signal_p1", sg_p1->getVal());
  RooGaussian signal_fixed("signal", "Signal Prediction Fixed", *x, signal_p0, signal_p1);
  
  RooPlot *plot=x->frame();
  signalHistogram.plotOn(plot);
  signal.plotOn(plot);
  TCanvas *c_SignalmX=new TCanvas(("c_SignalmX"+mass).c_str(), ("c_SignalmX"+mass).c_str(), 500, 500);
  plot->Draw();
  c_SignalmX->SaveAs(("c_SignalmX_"+mass+".png").c_str());
  c_SignalmX->SaveAs(("c_SignalmX_"+mass+".root").c_str());
  // c_SignalmX->SetLogy();
  RooWorkspace *w=new RooWorkspace("HbbHbb");
  // w->import(signal);
  w->import(signal_fixed);
  w->SaveAs(("w_signal_"+mass+"_Gaussian.root").c_str());
  
  outfile<<"<tr>"<<std::endl;
  outfile<<" <td>"<<std::endl;
  outfile<<"  <img src=\""<<("c_SignalmX_"+mass+".png").c_str()<<"\"/> <br/>"<<std::endl;
  outfile<<"  mean = "<<sg_p0->getVal()<<" +- "<<sg_p0->getError()<<" GeV <br/>"<<std::endl;
  outfile<<"  sigma = "<<sg_p1->getVal()<<" +- "<<sg_p1->getError()<<" GeV <br/>"<<std::endl;
  outfile<<" </td>"<<std::endl;
  outfile<<"</tr>"<<std::endl;
}


int SignalShapeFit_Gaussian()
{
  double chisq, ndf, chisq_ndf;
  double nSignal=0;
  
  gROOT->SetStyle("Plain");
  gStyle->SetOptStat(000000000);
  
  // Calculate nSignal events given production cross section, branching fractions and efficiency
  double nSignal_init=100000.;
  double totalLumi=13241.968; // /pb
  double prodXsec_1=1.; // pb
  
  // Write out to an HTML file
  outfile.open("SignalShapeFit_Gaussian.html");
  outfile<<"<html>"<<std::endl;
  outfile<<"<head>"<<std::endl;
  // outfile<<"<base href=\"https://cmslpcweb.fnal.gov/uscms_data/souvik/SignalShape_GaussianFits\" target=\"_blank\">"<<std::endl;
  outfile<<"</head>"<<std::endl;
  outfile<<"<body>"<<std::endl;
  outfile<<"<h1> Signal Shape with Gaussian Fits </h1>"<<std::endl;
  outfile<<"<table border='1'>"<<std::endl;
  
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
  outfile<<"<tr>"<<std::endl;
  fitSignal(h_mjjjj_3Tag_SR_400, "400");

  TFile *glugluToX500=new TFile("Histograms_glugluToX500ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX500ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_500=(TH1F*)glugluToX500->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_500->SetTitle("m_{X} Peak in Signal MC (m_{X}=500 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_500->Rebin(rebin);
  h_mjjjj_3Tag_SR_500->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_500->Scale(totalLumi*prodXsec_1/nSignal_init);
  fitSignal(h_mjjjj_3Tag_SR_500, "500");
  
  TFile *glugluToX600=new TFile("Histograms_glugluToX600ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX600ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_600=(TH1F*)glugluToX600->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_600->SetTitle("m_{X} Peak in Signal MC (m_{X}=600 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_600->Rebin(rebin);
  h_mjjjj_3Tag_SR_600->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_600->Scale(totalLumi*prodXsec_1/nSignal_init);
  fitSignal(h_mjjjj_3Tag_SR_600, "600");
 
  TFile *glugluToX700=new TFile("Histograms_glugluToX700ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX700ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU_Signal_2.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_700=(TH1F*)glugluToX700->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_700->SetTitle("m_{X} Peak in Signal MC (m_{X}=700 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_700->Rebin(rebin);
  h_mjjjj_3Tag_SR_700->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_700->Scale(totalLumi*prodXsec_1/nSignal_init);
  fitSignal(h_mjjjj_3Tag_SR_700, "700");

  TFile *glugluToX800=new TFile("Histograms_glugluToX800ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root");
  std::cout<<"Opened Histograms_glugluToX800ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root"<<std::endl;
  TH1F *h_mjjjj_3Tag_SR_800=(TH1F*)glugluToX800->Get("h_mX_SR");
  h_mjjjj_3Tag_SR_800->SetTitle("m_{X} Peak in Signal MC (m_{X}=800 GeV); m_{X} (GeV)");
  h_mjjjj_3Tag_SR_800->Rebin(rebin);
  h_mjjjj_3Tag_SR_800->SetMaximum(850.);
  h_mjjjj_3Tag_SR_800->GetXaxis()->SetRangeUser(0, 1200);
  h_mjjjj_3Tag_SR_800->Scale(totalLumi*prodXsec_1/nSignal_init);
  fitSignal(h_mjjjj_3Tag_SR_800, "800");
  
  outfile<<"</table>"<<std::endl;
  outfile<<"</body>"<<std::endl;
  outfile<<"</html>"<<std::endl;
  outfile.close();

  return 0;
}
  
                                                     
