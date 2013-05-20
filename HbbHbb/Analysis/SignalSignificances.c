#include <TROOT.h>

#include "/Users/souvik/CommonAnalysisTools/Significance.c"
#include "/Users/souvik/HbbHbb/Analysis/Significance_Kinematic.c"

void SignalSignificances()
{
  std::vector<double> signal(6);
  std::vector<double> bg(6);
  std::vector<double> bg_error(6);
  
  double xsec[6], xsecNeg1[6], xsecPos1[6], xsecNeg2[6], xsecPos2[6];
  double mass[6]={300, 400, 500, 600, 700, 800};
  
  Significance_Kinematic("Histograms_glugluToX300ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root", signal.at(0), bg.at(0), bg_error.at(0));
  Significance_Kinematic("Histograms_glugluToX400ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root", signal.at(1), bg.at(1), bg_error.at(1));
  Significance_Kinematic("Histograms_glugluToX500ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root", signal.at(2), bg.at(2), bg_error.at(2));
  Significance_Kinematic("Histograms_glugluToX600ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root", signal.at(3), bg.at(3), bg_error.at(3));
  Significance_Kinematic("Histograms_glugluToX700ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root", signal.at(4), bg.at(4), bg_error.at(4));
  Significance_Kinematic("Histograms_glugluToX800ToHHTobbbb_8TeV_width1MeV_FASTSIM_PU.root", signal.at(5), bg.at(5), bg_error.at(5));
  /*
  Significance_Kinematic("Histograms_glugluToX300ToHHTobbbb_8TeV_FASTSIM_PU_Signal_2.root", signal.at(0), bg.at(0), bg_error.at(0));
  Significance_Kinematic("Histograms_glugluToX400ToHHTobbbb_8TeV_FASTSIM_PU_Signal_2.root", signal.at(1), bg.at(1), bg_error.at(1));
  Significance_Kinematic("Histograms_glugluToX500ToHHTobbbb_8TeV_FASTSIM_PU_Signal_2.root", signal.at(2), bg.at(2), bg_error.at(2));
  Significance_Kinematic("Histograms_glugluToX600ToHHTobbbb_8TeV_FASTSIM_PU_Signal_2.root", signal.at(3), bg.at(3), bg_error.at(3));
  Significance_Kinematic("Histograms_glugluToX700ToHHTobbbb_8TeV_FASTSIM_PU_Signal_2.root", signal.at(4), bg.at(4), bg_error.at(4));
  Significance_Kinematic("Histograms_glugluToX800ToHHTobbbb_8TeV_FASTSIM_PU_Signal_2.root", signal.at(5), bg.at(5), bg_error.at(5));
  */
  // Figure out, given the background yield and uncertainty, how much signal corresponds to 5 sigma
  // What is the p-value of 5 sigma? 3e-7
  
  /*
  for (double s=135; s<=140; s+=1)
  {
    double prob=sum(bg.at(0), bg_error.at(0), bg.at(0)+s);
    std::cout<<"bg = "<<bg.at(0)<<", bg_error = "<<bg_error.at(0)<<", s = "<<s<<", prob = "<<prob<<std::endl;
  }
  */
  /*
  for (unsigned int i=0; i<signal.size(); ++i)
  {
    std::cout<<"i = "<<i<<", signal = "<<signal.at(i)<<", bg = "<<bg.at(i)<<", bg_error = "<<bg_error.at(i)<<std::endl;
    
    
    double yield=signal.at(i)+bg.at(i);
    double prob=sum(bg.at(i), bg_error.at(i), yield);
    // double prob=sumPoisson(bg.at(i), yield);
    double sigma=returnNSigma(prob);
    
    std::cout<<", prob = "<<prob<<", sigma = "<<sigma<<std::endl;
    
    std::cout<<" === "<<std::endl;
    
  }
  */
  /*
  for (unsigned int i=0; i<signal.size(); ++i)
  {
    // Without PU
    // xsec[i]=65./signal.at(i); // TTTT
    // xsec[i]=186./signal.at(i); // MMMM
    // xsec[i]=140./signal.at(i); // TMTM
    
    // With PU
    // xsec[i]=78./signal.at(i); // TTTT
    // xsec[i]=255./signal.at(i); // MMMM
    // xsec[i]=191./signal.at(i); // TMTM
    
    // With PU, syst=20%
    // xsec[i]=54./signal.at(i); // TTTT
    xsec[i]=186./signal.at(i); // MMMM
    // xsec[i]=136./signal.at(i); // TMTM
  }
  */
  
  // Print out +-1 sigma and +-2 sigma bars around the central x-section value
  for (unsigned int i=0; i<signal.size(); ++i)
  {
    bg_error.at(i)=bg.at(i)*0.20;
    std::cout<<"i = "<<i<<", signal = "<<signal.at(i)<<", bg = "<<bg.at(i)<<", bg_error = "<<bg_error.at(i)<<std::endl;
    
    double signallimit=double(returnSigmaLimit(bg.at(i), bg_error.at(i), 400.));
    xsec[i]=(signallimit-bg.at(i))/signal.at(i);
    std::cout<<"Mass point "<<i<<" needs yield = "<<signallimit<<", thus minimum signal x-sec*Br = "<<xsec[i]<<std::endl;
    
    // Find +-1 sigma limit
    unsigned int sigma1=returnSigmaInterval(bg.at(i), bg_error.at(i), 0.6827);
    unsigned int sigma2=returnSigmaInterval(bg.at(i), bg_error.at(i), 0.9545);
    xsecPos1[i]=sigma1/signal.at(i);
    xsecNeg1[i]=sigma1/signal.at(i);
    xsecPos2[i]=sigma2/signal.at(i);
    xsecNeg2[i]=sigma2/signal.at(i);
    std::cout<<"sigma1 = "<<sigma1<<", xsec 1 sigma width = "<<xsecPos1[i]<<", xsec 2 sigma width = "<<xsecPos2[i]<<std::endl;
  }
  
  TGraph *g_xsec=new TGraph(6, mass, xsec);
  g_xsec->SetTitle("Minimum x-sec of signal required for 5.0 #sigma observation significance; m_{X} (GeV); #sigma(X) #times Br(X#rightarrowH(b#bar{b}) H(b#bar{b})) (pb)");
  g_xsec->SetLineWidth(2);
  g_xsec->SetLineStyle(2);
  TGraphAsymmErrors *g_xsec_1sigma=new TGraphAsymmErrors(6, mass, xsec, 0, 0, xsecNeg1, xsecPos1);
  g_xsec_1sigma->SetLineColor(kGreen);
  g_xsec_1sigma->SetFillColor(kGreen);
  TGraphAsymmErrors *g_xsec_2sigma=new TGraphAsymmErrors(6, mass, xsec, 0, 0, xsecNeg2, xsecPos2);
  g_xsec_2sigma->SetLineColor(kYellow);
  g_xsec_2sigma->SetFillColor(kYellow);
  TCanvas *c_xsec=new TCanvas("c_xsec", "c_xsec", 1000, 700);
  c_xsec->SetLogy();
  g_xsec->SetMaximum(1000.); g_xsec->SetMinimum(0.1);
  g_xsec->Draw("AL*");
  g_xsec_2sigma->Draw("3");
  g_xsec_1sigma->Draw("3");
  g_xsec->Draw("L*");
  TLegend *leg=new TLegend(0.45, 0.5, 0.9, 0.9);
  leg->SetFillStyle(0);
  leg->AddEntry((TObject*)0, "CMS Experiment", "");
  leg->AddEntry((TObject*)0, "#sqrt{s} = 8 TeV, L = 13.24 fb^{-1}", "");
  leg->AddEntry((TObject*)0, "X#rightarrowH(b#bar{b}) H(b#bar{b})", "");
  leg->AddEntry((TObject*)0, "Jet Tagging: MMMM", "");
  leg->AddEntry(g_xsec, "Expected Limit", "LP");
  leg->AddEntry(g_xsec_1sigma, "Expected #pm 1 #sigma");
  leg->AddEntry(g_xsec_2sigma, "Expected #pm 2 #sigma");
  leg->Draw();
  c_xsec->SaveAs("minxSec.png");
  
  TFile *outFile=new TFile("Histogram_xsec.root", "RECREATE");
  g_xsec->Write("g_xsec");
  g_xsec_1sigma->Write("g_xsec_1sigma");
  g_xsec_2sigma->Write("g_xsec_2sigma");
  // outFile->Write();
  outFile->Close();
  
  
}
  
