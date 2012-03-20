Double_t f_eff(Double_t *x, Double_t *par)
{
  return (1./(1.+exp(-par[0]*(x[0]-par[1]))))*par[2];
}

int METEfficiencyArranger()
{
	TFile *file;
	file=new TFile("Distributions.root");
	
	TH1F *h_L1ETM=(TH1F*)gDirectory->Get("h_L1ETM");
	TH1F *h_CaloMET=(TH1F*)gDirectory->Get("h_CaloMET");
	TH1F *h_PFMHT=(TH1F*)gDirectory->Get("h_PFMHT");
	TH1F *h_CaloJet1_pT=(TH1F*)gDirectory->Get("h_CaloJet1_pT");
	TH1F *h_CaloJet2_pT=(TH1F*)gDirectory->Get("h_CaloJet2_pT");
	TH1F *h_PFJet1_pT=(TH1F*)gDirectory->Get("h_PFJet1_pT");
	TH1F *h_PFJet2_pT=(TH1F*)gDirectory->Get("h_PFJet2_pT");
	TH1F *h_mindPhi=(TH1F*)gDirectory->Get("h_mindPhi");
	
	TH1F *h_CaloMET80wrtPFMHT_num=(TH1F*)gDirectory->Get("h_CaloMET80wrtPFMHT_num"); h_CaloMET80wrtPFMHT_num->Rebin(10);
	TH1F *h_CaloMET80wrtPFMHT_den=(TH1F*)gDirectory->Get("h_CaloMET80wrtPFMHT_den"); h_CaloMET80wrtPFMHT_den->Rebin(10);
	
	TH1F *h_L1ETM36wrtCaloMET_num=(TH1F*)gDirectory->Get("h_L1ETM36wrtCaloMET_num"); h_L1ETM36wrtCaloMET_num->Rebin(10);
	TH1F *h_L1ETM36wrtCaloMET_den=(TH1F*)gDirectory->Get("h_L1ETM36wrtCaloMET_den"); h_L1ETM36wrtCaloMET_den->Rebin(10);
	
	TGraphAsymmErrors *g_CaloMET80wrtPFMHT=new TGraphAsymmErrors(h_CaloMET80wrtPFMHT_num, h_CaloMET80wrtPFMHT_den, "cp"); g_CaloMET80wrtPFMHT->SetTitle("(L1ETM36 && CaloMET80) Response w.r.t. HLT PFMHT; HLT PFMHT (GeV); Efficiency"); 
	TGraphAsymmErrors *g_L1ETM36wrtCaloMET=new TGraphAsymmErrors(h_L1ETM36wrtCaloMET_num, h_L1ETM36wrtCaloMET_den, "cp");
	
	gROOT->SetStyle("Plain");
	
	TCanvas *c_L1ETM=new TCanvas("c_L1ETM");
	h_L1ETM->Draw();
	c_L1ETM->SaveAs("c_L1ETM.png");
	
	TCanvas *c_CaloMET=new TCanvas("c_CaloMET");
	h_CaloMET->Draw();
	c_CaloMET->SaveAs("c_CaloMET.png");
	
	TCanvas *c_PFMHT=new TCanvas("c_PFMHT");
	h_PFMHT->Draw();
	c_PFMHT->SaveAs("c_PFMHT.png");
	
	TCanvas *c_CaloJet_pT=new TCanvas("c_CaloJet_pT");
	h_CaloJet2_pT->SetLineColor(kBlue); h_CaloJet2_pT->Draw();
	h_CaloJet1_pT->SetLineColor(kRed); h_CaloJet1_pT->Draw("SAME");
	c_CaloJet_pT->SaveAs("c_CaloJet_pT.png");
	
	TCanvas *c_PFJet_pT=new TCanvas("c_PFJet_pT");
	h_PFJet2_pT->SetLineColor(kBlue); h_PFJet2_pT->Draw();
	h_PFJet1_pT->SetLineColor(kRed); h_PFJet1_pT->Draw("SAME");
	c_PFJet_pT->SaveAs("c_PFJet_pT.png");
	
	TCanvas *c_mindPhi=new TCanvas("c_mindPhi");
	h_mindPhi->Draw();
	c_mindPhi->SaveAs("c_mindPhi.png");
	
	TCanvas *c_CaloMET80wrtPFMHT=new TCanvas("c_CaloMET80wrtPFMHT");
	g_CaloMET80wrtPFMHT->Draw("AP");
	f_CaloMET80wrtPFMHT=new TF1("f_CaloMET80wrtPFMHT", f_eff, 20., 400., 3);
  f_CaloMET80wrtPFMHT->SetParLimits(0, 0., 2.);
  f_CaloMET80wrtPFMHT->SetParLimits(1, 50., 90.);
  f_CaloMET80wrtPFMHT->FixParameter(2, 1.);
	g_CaloMET80wrtPFMHT->Fit(f_CaloMET80wrtPFMHT, "REMS");
	
	
	c_CaloMET80wrtPFMHT->SaveAs("c_CaloMET80wrtPFMHT.png");
	
	TCanvas *c_L1ETM36wrtCaloMET=new TCanvas("c_L1ETM36wrtCaloMET");
	g_L1ETM36wrtCaloMET->Draw("AP");
	c_L1ETM36wrtCaloMET->SaveAs("c_L1ETM36wrtCaloMET.png");
	
}
	
