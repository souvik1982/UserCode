#include <TH1F.h>
#include <TROOT.h>
#include <TFile.h>
#include <TLegend.h>
#include <TCanvas.h>
#include <TProfile.h>
#include <iostream>
#include <TStyle.h>
#include <TPaveText.h>
#include <THStack.h>
#include <TF1.h>
#include <TSystem.h>
#include <TGraphErrors.h>

#include <RooRealVar.h>
#include <RooArgList.h>
#include <RooChebychev.h>
#include <RooDataHist.h>
#include <RooExtendPdf.h>
#include <RooWorkspace.h>
#include <RooPlot.h>

double H_mass=125.0;
double mH_diff_cut=40.;
double mH_mean_cut=20.;

double rebin=2;
bool bReg=false;

std::string tags="MMMM"; // MMMM

double r1=15., r2=35.;

TCanvas* comparePlots(TH1F *data, TH1F *qcd, std::string title)
{
  TCanvas *c=new TCanvas(("c"+title).c_str(), "c", 600, 700);
  TPad *p_2=new TPad("p_2", "p_2", 0, 0, 1, 0.3);
  TPad *p_1=new TPad("p_1", "p_1", 0, 0.3, 1, 1);
  p_1->Draw();
  p_2->Draw();
  p_1->cd();
  // p_1->SetLogy();
  qcd->SetTitle((title+"; m_{X} (GeV)").c_str());
  double s=data->Integral(data->FindBin(200.), data->FindBin(1200.))/qcd->Integral(qcd->FindBin(200.), qcd->FindBin(1200.));
  qcd->Scale(s);
  qcd->Draw("HIST");
  data->Draw("Ep9 SAME");
  TLegend *leg=new TLegend(0.5, 0.9, 0.9, 0.7);
  leg->AddEntry(qcd, "Sideband Region");
  leg->AddEntry(data, "Central Region");
  leg->Draw();
  p_2->cd();
  p_2->SetGridy();
  TH1F *h_ratio=(TH1F*)data->Clone("h_ratio");
  h_ratio->SetTitle(("Data/MC Ratio "+title+" ; data/MC").c_str());
  h_ratio->Divide(qcd);                          
  h_ratio->SetMinimum(-1.); h_ratio->SetMaximum(3.);                  
  h_ratio->Draw();                                                    
  qcd->Scale(1./s); 
  p_1->cd(); 
  return c;                           
}

TCanvas* comparePlots2(RooPlot *plot, TH1F *data, TH1F *qcd, std::string title)
{
  TCanvas *c=new TCanvas(("c_RooFit_"+title).c_str(), "c", 600, 700);
  TPad *p_2=new TPad("p_2", "p_2", 0, 0, 1, 0.3);
  TPad *p_1=new TPad("p_1", "p_1", 0, 0.3, 1, 1);
  p_1->Draw();
  p_2->Draw();
  p_1->cd();
  plot->Draw();
  p_2->cd();
  p_2->SetGridy();
  TH1F *h_ratio=(TH1F*)data->Clone("h_ratio");
  h_ratio->SetTitle(("VR/VR-SB Ratio "+title+" ; VR/VR-SB Ratio").c_str());
  h_ratio->Divide(qcd);                          
  h_ratio->SetMinimum(-1.); h_ratio->SetMaximum(3.);                  
  h_ratio->Draw();
  p_1->cd(); 
  return c;                           
}

// 0 = cut (x sigma), 1 = power, 2 = center, 3 = sigma
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

double returnCurveSyst(TF1 *h_CR, TF1 *h_SR, double mass)
{
  double err_lo, err_hi;
  if (mass==300) {err_lo=200.; err_hi=700.;}
  else if (mass==400) {err_lo=250.; err_hi=600.;}
  else if (mass==500) {err_lo=300.; err_hi=700.;}
  else if (mass==600) {err_lo=400.; err_hi=800.;}
  else if (mass==700) {err_lo=500.; err_hi=900.;}
  else if (mass==800) {err_lo=600.; err_hi=1000.;}
  double int_mMMMMb_3Tag_CR24=h_CR->Integral(err_lo, err_hi);
  double int_mMMMMb_3Tag_SR=h_SR->Integral(err_lo, err_hi);
  double fracSyst=2.*(int_mMMMMb_3Tag_SR-int_mMMMMb_3Tag_CR24)/(int_mMMMMb_3Tag_CR24+int_mMMMMb_3Tag_SR);
  return fracSyst;
}
/*
double returnCurveSyst2(RevCrystalBall *r_CR, RevCrystalBall *r_SR, double mass)
{
  double err_lo, err_hi;
  if (mass==300) {err_lo=200.; err_hi=700.;}
  else if (mass==400) {err_lo=250.; err_hi=600.;}
  else if (mass==500) {err_lo=300.; err_hi=700.;}
  else if (mass==600) {err_lo=400.; err_hi=800.;}
  else if (mass==700) {err_lo=500.; err_hi=900.;}
  else if (mass==800) {err_lo=600.; err_hi=1000.;}
  double int_mX_CR24=h_CR->Integral(err_lo, err_hi);
  double int_mX_SR=h_SR->Integral(err_lo, err_hi);
  double fracSyst=2.*(int_mMMMMb_3Tag_SR-int_mMMMMb_3Tag_CR24)/(int_mMMMMb_3Tag_CR24+int_mMMMMb_3Tag_SR);
  return fracSyst;
}
*/
void retrieveFitsCR(TF1 *f_CR)
{
  if (rebin==4)
  {
    f_CR->SetParLimits(0, 0.1, 2.0);
    f_CR->SetParLimits(1, 50., 200.);
    f_CR->SetParLimits(2, 300., 500.);
    f_CR->SetParLimits(3, 20., 150.);
    f_CR->SetParLimits(4, 50., 600.);
  }
  if (rebin==2)
  {
    if (bReg==false)
    {
      f_CR->SetParLimits(0, 0.1, 2.0);
      f_CR->SetParLimits(1, 10., 200.); 
      f_CR->SetParLimits(2, 350., 500.);
      f_CR->SetParLimits(3, 45., 150.);
      f_CR->SetParLimits(4, 50., 600.);
    }
    else
    {
      f_CR->SetParLimits(0, 0.1, 2.0);
      f_CR->SetParLimits(1, 10., 60.); 
      f_CR->SetParLimits(2, 300., 500.);
      f_CR->SetParLimits(3, 45., 150.);
      f_CR->SetParLimits(4, 50., 600.);
    } 
  }
  
  // KinFit
  /*
  {
    f_CR->SetParLimits(0, 0.1, 2.0);   
    f_CR->SetParLimits(1, 50., 200.);  
    f_CR->SetParLimits(2, 300., 500.); 
    f_CR->SetParLimits(3, 40., 150.);  
    f_CR->SetParLimits(4, 50., 600.);  
  }
  */
}

void retrieveFitsSR(TF1 *f_SR)
{
  
  if (rebin==4)
  {
    f_SR->SetParLimits(0, 0.1, 2.0);
    f_SR->SetParLimits(1, 50., 200.);
    f_SR->SetParLimits(2, 300., 500.);
    f_SR->SetParLimits(3, 20., 150.);
    f_SR->SetParLimits(4, 50., 600.);
  }
  if (rebin==2)
  {
    if (bReg==false)
    {
      f_SR->SetParLimits(0, 0.1, 2.0);
      f_SR->SetParLimits(1, 50., 200.);
      f_SR->SetParLimits(2, 350., 500.);
      f_SR->SetParLimits(3, 45., 150.);
      f_SR->SetParLimits(4, 50., 600.);
    }
    else
    {
      f_SR->SetParLimits(0, 0.1, 2.0);
      f_SR->SetParLimits(1, 10., 60.);
      f_SR->SetParLimits(2, 350., 500.);
      f_SR->SetParLimits(3, 45., 150.);
      f_SR->SetParLimits(4, 50., 600.);
    }
  }
  
  
  // KinFit
  /*
  {
    f_SR->SetParLimits(0, 0.1, 2.0);   
    f_SR->SetParLimits(1, 50., 200.);  
    f_SR->SetParLimits(2, 300., 500.); 
    f_SR->SetParLimits(3, 40., 150.);  
    f_SR->SetParLimits(4, 50., 600.);  
  }
  */
  
}
  

void BackgroundPrediction_Kinematic()
{

  gROOT->SetStyle("Plain");
  gStyle->SetOptStat(000000000);
  
  if (bReg) tags=tags+"_bReg";
  
  const unsigned int nPoints=4;
  double mass[nPoints]={90., 107.5, 142.5, 160.};
  double n_SB[nPoints], n_SR[nPoints];
  double ratio[nPoints];
  double errorsY[nPoints], errorsX[nPoints];
  
  // === MMMM/b ===
  TFile *f_MMMM_b=new TFile((tags+"/b/Histograms_8TeVData2012BCD_Skim.root").c_str());
  TH1F *h_mX_CR2_b=(TH1F*)f_MMMM_b->Get("h_mX_CR2");
  TH1F *h_mX_CR4_b=(TH1F*)f_MMMM_b->Get("h_mX_CR4");
  TH1F *h_mX_SR_b=(TH1F*)f_MMMM_b->Get("h_mX_SR");
  n_SB[0]=(h_mX_CR2_b->GetSumOfWeights()+h_mX_CR4_b->GetSumOfWeights());
  n_SR[0]=h_mX_SR_b->GetSumOfWeights();
  
  // === MMMM/d ===
  TFile *f_MMMM_d=new TFile((tags+"/d/Histograms_8TeVData2012BCD_Skim.root").c_str());
  TH1F *h_mX_CR2_d=(TH1F*)f_MMMM_d->Get("h_mX_CR2");
  TH1F *h_mX_CR4_d=(TH1F*)f_MMMM_d->Get("h_mX_CR4");
  TH1F *h_mX_SR_d=(TH1F*)f_MMMM_d->Get("h_mX_SR");
  n_SB[1]=(h_mX_CR2_d->GetSumOfWeights()+h_mX_CR4_d->GetSumOfWeights());
  n_SR[1]=h_mX_SR_d->GetSumOfWeights();
  
  // === MMMM/e ===
  TFile *f_MMMM_e=new TFile((tags+"/e/Histograms_8TeVData2012BCD_Skim.root").c_str());
  TH1F *h_mX_CR2_e=(TH1F*)f_MMMM_e->Get("h_mX_CR2");
  TH1F *h_mX_CR4_e=(TH1F*)f_MMMM_e->Get("h_mX_CR4");
  TH1F *h_mX_SR_e=(TH1F*)f_MMMM_e->Get("h_mX_SR");
  n_SB[2]=(h_mX_CR2_e->GetSumOfWeights()+h_mX_CR4_e->GetSumOfWeights());
  n_SR[2]=h_mX_SR_e->GetSumOfWeights();
  
  // === MMMM/c ===
  TFile *f_MMMM_c=new TFile((tags+"/c/Histograms_8TeVData2012BCD_Skim.root").c_str());
  TH1F *h_mX_CR2_c=(TH1F*)f_MMMM_c->Get("h_mX_CR2");
  TH1F *h_mX_CR4_c=(TH1F*)f_MMMM_c->Get("h_mX_CR4");
  TH1F *h_mX_SR_c=(TH1F*)f_MMMM_c->Get("h_mX_SR");
  n_SB[3]=(h_mX_CR2_c->GetSumOfWeights()+h_mX_CR4_c->GetSumOfWeights());
  n_SR[3]=h_mX_SR_c->GetSumOfWeights();
  
  for (unsigned int i=0; i<nPoints; ++i)
  {
    ratio[i]=n_SR[i]/n_SB[i];
    errorsY[i]=ratio[i]*pow(1./n_SR[i]+1./n_SB[i], 0.5);
    errorsX[i]=0.;
  }
  
  TGraphErrors *g_ratio=new TGraphErrors(nPoints, mass, ratio, errorsX, errorsY);
  g_ratio->SetTitle("SR/SB ratio");
  TCanvas *c_ratio=new TCanvas("c_ratio", "c_ratio", 700, 700);
  g_ratio->SetMinimum(0.); g_ratio->SetMaximum(1.);
  g_ratio->Draw("A*");
  TF1 *f_ratio=new TF1("f_ratio", "pol1");
  g_ratio->Fit(f_ratio);
  c_ratio->SaveAs(("c_ratio_"+tags+".png").c_str());
  
  double ratioAt125=f_ratio->Eval(125.);
  double errorAt125=(errorsY[0]+errorsY[1]+errorsY[2]+errorsY[3])/4.;
  std::cout<<"ratioAt125 = "<<ratioAt125<<" +- "<<errorAt125<<std::endl;
  
  /*
  // === MMMM/a ===
  TFile *f_MMMM_a=new TFile((tags+"/a/Histograms_8TeVData2012BCD_Skim.root").c_str());
  TH1F *h_mX_CR2_a=(TH1F*)f_MMMM_a->Get("h_mX_CR2");
  TH1F *h_mX_CR4_a=(TH1F*)f_MMMM_a->Get("h_mX_CR4");
  n_SB_125=(h_mX_CR2_a->GetSumOfWeights()+h_mX_CR4_a->GetSumOfWeights());
  n_SR_125=n_SB_125*ratioAt125;
  n_SR_125_error=n_SB_125*errorAt125;
  std::cout<<"n_SR_125 Prediction = "<<n_SR_125<<" +- "<<n_SR_125_error<<std::endl;
  */
  
  std::cout<<" = MMMM b ======================================== "<<std::endl;
  TFile *data_8TeVData2012_MMMMb=new TFile((tags+"/b_KinFit/Histograms_8TeVData2012BCD_Skim.root").c_str());
  TH1F *h_mMMMMb_3Tag_CR2=(TH1F*)data_8TeVData2012_MMMMb->Get("h_mX_CR2");
  TH1F *h_mMMMMb_3Tag_CR4=(TH1F*)data_8TeVData2012_MMMMb->Get("h_mX_CR4");
  TH1F *h_mMMMMb_3Tag_SR=(TH1F*)data_8TeVData2012_MMMMb->Get("h_mX_SR");
  double bS=h_mMMMMb_3Tag_SR->Integral(h_mMMMMb_3Tag_SR->FindBin(250.), h_mMMMMb_3Tag_SR->FindBin(1100.));
  std::cout<<"Number of events in MMMM b signal region = "<<bS<<std::endl;
  TH1F *h_mMMMMb_3Tag_CR24=(TH1F*)h_mMMMMb_3Tag_CR2->Clone("h_mX_CR24");
  h_mMMMMb_3Tag_CR24->Add(h_mMMMMb_3Tag_CR4);
  h_mMMMMb_3Tag_CR24->Rebin(rebin);
  h_mMMMMb_3Tag_SR->Rebin(rebin);
  h_mMMMMb_3Tag_CR24->SetLineColor(kRed);
  h_mMMMMb_3Tag_SR->SetLineColor(kBlue);
  double bC=h_mMMMMb_3Tag_CR24->Integral(h_mMMMMb_3Tag_CR24->FindBin(250.), h_mMMMMb_3Tag_CR24->FindBin(1100.));
  std::cout<<"bC = "<<bC<<", bS = "<<bS<<std::endl;
  // Fit both MMMMb curves to Crystal Balls and compute Kolmogorov
  h_mMMMMb_3Tag_CR24->SetMaximum(h_mMMMMb_3Tag_CR24->GetMaximum()*1.3);
  h_mMMMMb_3Tag_CR24->GetXaxis()->SetRangeUser(250, 1100);
  h_mMMMMb_3Tag_SR->GetXaxis()->SetRangeUser(250, 1100);
  h_mMMMMb_3Tag_CR24->SetTitle(("Kinematic Extrapolation in "+tags+" Validation Region; m_{X} GeV").c_str());
  h_mMMMMb_3Tag_SR->Scale(bC/bS);
  TCanvas *c_mMMMMb=comparePlots(h_mMMMMb_3Tag_SR, h_mMMMMb_3Tag_CR24, "Kinematic Extrapolation in "+tags+" Validation Region of Data; m_{X} GeV");
  TF1 *f_mMMMMb_3Tag_CR24=new TF1("f_mMMMMb_3Tag_CR24", crystalBall, 300., 1000., 5);
  f_mMMMMb_3Tag_CR24->SetLineWidth(2);
  f_mMMMMb_3Tag_CR24->SetLineColor(kRed);
  retrieveFitsCR(f_mMMMMb_3Tag_CR24);
  h_mMMMMb_3Tag_CR24->Fit(f_mMMMMb_3Tag_CR24, "REFMN");
  std::cout<<"CR Fit (red) has GetChisquare() = "<<f_mMMMMb_3Tag_CR24->GetChisquare()<<std::endl;
  std::cout<<"CR Fit (red) has GetNDF() = "<<f_mMMMMb_3Tag_CR24->GetNDF()<<std::endl;
  TF1 *f_mMMMMb_3Tag_SR=new TF1("f_mMMMMb_3Tag_SR", crystalBall, 300., 1000., 5);
  f_mMMMMb_3Tag_SR->SetLineWidth(2);
  f_mMMMMb_3Tag_SR->SetLineColor(kBlue);
  retrieveFitsSR(f_mMMMMb_3Tag_SR);
  h_mMMMMb_3Tag_SR->Fit(f_mMMMMb_3Tag_SR, "REFMN");
  std::cout<<"SR Fit (black) has GetChisquare() = "<<f_mMMMMb_3Tag_SR->GetChisquare()<<std::endl;
  std::cout<<"SR Fit (black) has GetNDF() = "<<f_mMMMMb_3Tag_SR->GetNDF()<<std::endl;
  h_mMMMMb_3Tag_CR24->Draw("Ep9");
  f_mMMMMb_3Tag_CR24->Draw("SAME");
  h_mMMMMb_3Tag_SR->Draw("Ep9 SAME");
  f_mMMMMb_3Tag_SR->Draw("SAME");
  c_mMMMMb->SaveAs(("c_compareData_"+tags+"_VR.png").c_str());
  double ks_MMMMb=h_mMMMMb_3Tag_CR24->KolmogorovTest(h_mMMMMb_3Tag_SR);
  std::cout<<"MMMM Validation in b region, KS = "<<ks_MMMMb<<std::endl;
  std::cout<<" ====================================================== "<<std::endl;
  
  // Do the fits using RooFit
  gSystem->Load("PDFs/RevCrystalBall_cxx.so");
  RooRealVar mX("mX", "m_{X} (GeV)", 300., 1100.);
  // bC
  RooRealVar bC_p0("bC_p0", "bC_p0", 0.1, 1.0);
  // RooRealVar bC_p1("bC_p1", "bC_p1", 100., 150.);
  RooRealVar bC_p1("bC_p1", "bC_p1", 1., 10.);
  RooRealVar bC_p2("bC_p2", "bC_p2", 390., 500.);
  RooRealVar bC_p3("bC_p3", "bC_p3", 50., 100.);
  RevCrystalBall bC_fit("bC_fit", "bC Fit", mX, bC_p0, bC_p1, bC_p2, bC_p3);
  RooDataHist bC_data("bC_data", "bC Data", RooArgList(mX), h_mMMMMb_3Tag_CR24);
  bC_fit.fitTo(bC_data);
  RooPlot *bC_plot=mX.frame();
  bC_data.plotOn(bC_plot, RooFit::MarkerColor(kRed));
  bC_fit.plotOn(bC_plot, RooFit::LineColor(kRed));
  // bS
  RooRealVar bS_p0("bS_p0", "bS_p0", 0.1, 1.0);
  // RooRealVar bS_p1("bS_p1", "bS_p1", 100., 150.);
  RooRealVar bS_p1("bS_p1", "bS_p1", 1., 10.);
  RooRealVar bS_p2("bS_p2", "bS_p2", 390., 500.);
  RooRealVar bS_p3("bS_p3", "bS_p3", 50., 100.);
  RevCrystalBall bS_fit("bS_fit", "bS Fit", mX, bS_p0, bS_p1, bS_p2, bS_p3);
  RooDataHist bS_data("bS_data", "bS Data", RooArgList(mX), h_mMMMMb_3Tag_SR);
  bS_fit.fitTo(bS_data);
  bS_data.plotOn(bC_plot, RooFit::MarkerColor(kBlue));
  bS_fit.plotOn(bC_plot, RooFit::LineColor(kBlue));
  TCanvas *c_bC=comparePlots2(bC_plot, h_mMMMMb_3Tag_SR, h_mMMMMb_3Tag_CR24, "Kinematic Extrapolation in "+tags+" Validation Region of Data; m_{X} GeV");
  c_bC->SaveAs(("c_compareData_"+tags+"_VR_RooFit.png").c_str());
  
  /*
  TH1F *h_fracSyst=new TH1F("h_fracSyst", "Fractional Difference between Predicted Shapes from Control Region; m_{X} GeV", 100., 0., 2000.);
  h_fracSyst->Rebin(rebin);
  h_fracSyst->GetXaxis()->SetRangeUser(0, 1200.);
  for (int i=1; i<=h_fracSyst->GetNbinsX(); ++i)
  {
    double SB=h_mMMMMb_3Tag_CR24->GetBinContent(i);
    double SR=h_mMMMMb_3Tag_SR->GetBinContent(i);
    double frac=2.*(SR-SB)/(SR+SB);
    // std::cout<<"SR = "<<SR<<", SB = "<<SB<<", frac = "<<frac<<std::endl;
    if (SR!=0 && SB!=0) h_fracSyst->SetBinContent(i, frac);
  }
  TCanvas *c_fracSyst=new TCanvas("c_fracSyst", "c_fracSyst", 500, 500);
  h_fracSyst->Draw("E");
  c_fracSyst->SaveAs(("c_fracSyst_"+tags+".png").c_str());
  */
  
  // Fractional Systematic Uncertainty computed from the difference in the integral between the two functions in the 400-800 GeV region
  std::cout<<" 300 GeV fractional systematic = "<<fabs(returnCurveSyst(f_mMMMMb_3Tag_CR24, f_mMMMMb_3Tag_SR, 300))+1.<<std::endl;
  std::cout<<" 400 GeV fractional systematic = "<<fabs(returnCurveSyst(f_mMMMMb_3Tag_CR24, f_mMMMMb_3Tag_SR, 400))+1.<<std::endl;
  std::cout<<" 500 GeV fractional systematic = "<<fabs(returnCurveSyst(f_mMMMMb_3Tag_CR24, f_mMMMMb_3Tag_SR, 500))+1.<<std::endl;
  std::cout<<" 600 GeV fractional systematic = "<<fabs(returnCurveSyst(f_mMMMMb_3Tag_CR24, f_mMMMMb_3Tag_SR, 600))+1.<<std::endl;
  std::cout<<" 700 GeV fractional systematic = "<<fabs(returnCurveSyst(f_mMMMMb_3Tag_CR24, f_mMMMMb_3Tag_SR, 700))+1.<<std::endl;
  std::cout<<" 800 GeV fractional systematic = "<<fabs(returnCurveSyst(f_mMMMMb_3Tag_CR24, f_mMMMMb_3Tag_SR, 800))+1.<<std::endl;
  
  std::cout<<" = MMMM Background Prediction ==== "<<std::endl;
  TFile *data_8TeVData2012_MMMMa=new TFile((tags+"/a_KinFit/Histograms_8TeVData2012BCD_Skim.root").c_str());
  TH1F *h_mMMMMa_3Tag_CR2=(TH1F*)data_8TeVData2012_MMMMa->Get("h_mX_CR2");
  TH1F *h_mMMMMa_3Tag_CR4=(TH1F*)data_8TeVData2012_MMMMa->Get("h_mX_CR4");
  TH1F *h_mMMMMa_3Tag_CR24=(TH1F*)h_mMMMMa_3Tag_CR2->Clone("h_mX_CR24");
  h_mMMMMa_3Tag_CR24->Add(h_mMMMMa_3Tag_CR4);
  h_mMMMMa_3Tag_CR24->Rebin(rebin);
  h_mMMMMa_3Tag_CR24->SetLineColor(kBlack);
  TH1F *h_mMMMMa_3Tag_SR_Prediction=(TH1F*)h_mMMMMa_3Tag_CR24->Clone("h_mMMMMa_3Tag_SR_Prediction");
  double aC=h_mMMMMa_3Tag_CR24->GetSumOfWeights();
  // Get the scale of the prediction right
  std::cout<<"bS/bC = "<<bS/bC<<std::endl;
  std::cout<<"ratioAt125 = "<<ratioAt125<<", +- "<<errorAt125<<" (fract unc.) = "<<1.+errorAt125/ratioAt125<<std::endl;
  h_mMMMMa_3Tag_SR_Prediction->Scale(ratioAt125);
  std::cout<<"Number of predicted events = "<<h_mMMMMa_3Tag_SR_Prediction->GetSumOfWeights()<<std::endl;
  /*
  TCanvas *c_MMMMa=new TCanvas("c_MMMMa", "Background Prediction", 500, 500);
  h_mMMMMa_3Tag_SR_Prediction->GetXaxis()->SetRangeUser(200, 1200);
  h_mMMMMa_3Tag_SR_Prediction->SetMaximum(52.);
  h_mMMMMa_3Tag_SR_Prediction->SetTitle("mX background prediction shape in MMMM");
  // h_mMMMMa_3Tag_SR_Prediction->Draw("Ep9");
  TF1 *f_mMMMMa_3Tag_SR_Prediction=new TF1("f_mMMMMa_3Tag_SR_Prediction", crystalBall, 250., 1100., 5);
  f_mMMMMa_3Tag_SR_Prediction->SetLineColor(kBlue);
  f_mMMMMa_3Tag_SR_Prediction->SetLineWidth(2);
  f_mMMMMa_3Tag_SR_Prediction->SetParLimits(0, 0.1, 2.0);
  f_mMMMMa_3Tag_SR_Prediction->SetParLimits(1, 10., 200.);
  f_mMMMMa_3Tag_SR_Prediction->SetParLimits(2, 400., 600.);
  f_mMMMMa_3Tag_SR_Prediction->SetParLimits(3, 20., 150.);
  f_mMMMMa_3Tag_SR_Prediction->SetParLimits(4, 20., 200.);
  h_mMMMMa_3Tag_SR_Prediction->Fit(f_mMMMMa_3Tag_SR_Prediction, "REFM");
  TH1F *h_mMMMMa_3Tag_SR_Prediction_systUp=(TH1F*)h_mMMMMa_3Tag_SR_Prediction->Clone("h_mMMMMa_3Tag_SR_Prediction_systUp");
  TH1F *h_mMMMMa_3Tag_SR_Prediction_systDown=(TH1F*)h_mMMMMa_3Tag_SR_Prediction->Clone("h_mMMMMa_3Tag_SR_Prediction_systDown");
  for (int i=1; i<=h_mMMMMa_3Tag_SR_Prediction->GetNbinsX(); ++i)
  {
    double binContent=h_mMMMMa_3Tag_SR_Prediction->GetBinContent(i);
    double fracSyst=fabs(h_fracSyst->GetBinContent(i));
    std::cout<<"fracSyst = "<<fracSyst<<std::endl;
    h_mMMMMa_3Tag_SR_Prediction_systUp->SetBinContent(i, binContent*(1.+fracSyst));
    h_mMMMMa_3Tag_SR_Prediction_systDown->SetBinContent(i, binContent*(1.-fracSyst));
  }
  h_mMMMMa_3Tag_SR_Prediction_systUp->SetLineColor(kOrange);
  h_mMMMMa_3Tag_SR_Prediction_systDown->SetLineColor(kRed);
  h_mMMMMa_3Tag_SR_Prediction_systUp->Draw("HIST");
  h_mMMMMa_3Tag_SR_Prediction_systDown->Draw("HIST SAME");
  h_mMMMMa_3Tag_SR_Prediction->Draw("E1P SAME");
  c_MMMMa->SaveAs((tags+"_BackgroundPrediction.png").c_str());
  
  std::cout<<"MMMM # events in VR-SB region = "<<bC<<std::endl;
  std::cout<<"MMMM # events in VR region = "<<bS<<std::endl;
  std::cout<<"MMMM # events in CR region = "<<aC<<std::endl;
  std::cout<<"MMMM # projected events in SR region = "<<aC*bS/bC<<std::endl;
  std::cout<<"MMMM prediction histogram contains "<<h_mMMMMa_3Tag_SR_Prediction->GetSumOfWeights()<<" events"<<std::endl;
  
  // Write out background prediction shape into a ROOT file
  TF1 *f_BackgroundPDF=(TF1*)f_mMMMMa_3Tag_SR_Prediction->Clone("f_BackgroundPDF");
  f_BackgroundPDF->SetTitle("Background Prediction PDF");
  double integral=f_BackgroundPDF->Integral(300., 1100.);
  double norm=f_BackgroundPDF->GetParameter(4);
  std::cout<<"Integral(250., 1100.) = "<<integral<<", and norm = "<<norm<<std::endl;
  f_BackgroundPDF->SetParameter(4, norm/integral);
  TFile *outFile=new TFile("SignalBackgroundData.root", "RECREATE");
  f_BackgroundPDF->Write();
  outFile->Close();
  */
  
  // RooFit fit to background prediction
  gSystem->Load("/Users/souvik/HbbHbb/Analysis/PDFs/RevCrystalBall_cxx.so");
  RooRealVar x("x", "m_{X} (GeV)", 300., 1100.);
  RooRealVar bg_p0("bg_p0", "bg_p0", 0.1, 0.5);
  RooRealVar bg_p1("bg_p1", "bg_p1", 1., 20.);
  RooRealVar bg_p2("bg_p2", "bg_p2", 420., 520.);
  RooRealVar bg_p3("bg_p3", "bg_p3", 30., 90.);
  RevCrystalBall bg("bg", "Background Prediction PDF", x, bg_p0, bg_p1, bg_p2, bg_p3);
  RooDataHist pred("pred", "Prediction from SB", RooArgList(x), h_mMMMMa_3Tag_SR_Prediction);
  bg.fitTo(pred);
  RooRealVar bg_norm("bg_norm", "bg_norm", 0.1, 100.);
  RooExtendPdf background("background", "Background Prediction PDF with ext", bg, bg_norm);
  RooPlot *plot=x.frame();
  pred.plotOn(plot);
  bg.plotOn(plot);
  TCanvas *c_rooFit=new TCanvas("c_rooFit", "c_rooFit", 500, 500);
  plot->Draw();
  c_rooFit->SaveAs("c_rooFit_bg.png"); 
  
  // Write a new background function with same parameters
  RooRealVar background_p0("background_p0", "background_p0", bg_p0.getVal());
  RooRealVar background_p1("background_p1", "background_p1", bg_p1.getVal());
  RooRealVar background_p2("background_p2", "background_p2", bg_p2.getVal());
  RooRealVar background_p3("background_p3", "background_p3", bg_p3.getVal());
  RevCrystalBall bg_fixed("bg_fixed", "Background Prediction Fixed", x, background_p0, background_p1, background_p2, background_p3);
  RooExtendPdf background_fixed("background", "Background Prediction PDF with ext", bg_fixed, bg_norm);
  
  RooWorkspace *w=new RooWorkspace("HbbHbb");
  w->import(background_fixed);
  w->SaveAs("w_background.root");
  
}
  
  
  
