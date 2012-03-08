int ZbbHbbDistributionsArranger()
{
	std::string H_string="H_110";
	
	TFile *file;
	if (H_string=="H_110") file=new TFile("../bin/distributions_H_110.root");
	if (H_string=="H_130") file=new TFile("../bin/distributions_H_130.root");
        if (H_string=="H_150") file=new TFile("../bin/distributions_H_150.root");


        TH1I *h_nJets=(TH1I*)gDirectory->Get("h_nJets");
	TH1F *h_dR=(TH1F*)gDirectory->Get("h_dR");
	TH1F *h_Jet1_E=(TH1F*)gDirectory->Get("h_Jet1_E");
	TH1F *h_Jet1_pT=(TH1F*)gDirectory->Get("h_Jet1_pT");
	TH1F *h_Jet1_eta=(TH1F*)gDirectory->Get("h_Jet1_eta");
	TH1F *h_Jet1_phi=(TH1F*)gDirectory->Get("h_Jet1_phi");
	TH1F *h_Jet1_CSV=(TH1F*)gDirectory->Get("h_Jet1_CSV");
	TH1F *h_Jet1_pT_bZMatched=(TH1F*)gDirectory->Get("h_Jet1_pT_bZMatched"); h_Jet1_pT_bZMatched->SetLineColor(kBlue);
	TH1F *h_Jet1_pT_bbZMatched=(TH1F*)gDirectory->Get("h_Jet1_pT_bbZMatched"); h_Jet1_pT_bbZMatched->SetLineColor(kGreen);
	TH1F *h_Jet1_pT_bHMatched=(TH1F*)gDirectory->Get("h_Jet1_pT_bHMatched"); h_Jet1_pT_bHMatched->SetLineColor(kRed);
	TH1F *h_Jet1_pT_bbHMatched=(TH1F*)gDirectory->Get("h_Jet1_pT_bbHMatched"); h_Jet1_pT_bbHMatched->SetLineColor(kMagenta);
	
	TH1F *h_Jet2_E=(TH1F*)gDirectory->Get("h_Jet2_E");
	TH1F *h_Jet2_pT=(TH1F*)gDirectory->Get("h_Jet2_pT");
	TH1F *h_Jet2_eta=(TH1F*)gDirectory->Get("h_Jet2_eta");
	TH1F *h_Jet2_phi=(TH1F*)gDirectory->Get("h_Jet2_phi");
	TH1F *h_Jet2_CSV=(TH1F*)gDirectory->Get("h_Jet2_CSV");
	TH1F *h_Jet2_pT_bZMatched=(TH1F*)gDirectory->Get("h_Jet2_pT_bZMatched"); h_Jet2_pT_bZMatched->SetLineColor(kBlue);
	TH1F *h_Jet2_pT_bbZMatched=(TH1F*)gDirectory->Get("h_Jet2_pT_bbZMatched"); h_Jet2_pT_bbZMatched->SetLineColor(kGreen);
	TH1F *h_Jet2_pT_bHMatched=(TH1F*)gDirectory->Get("h_Jet2_pT_bHMatched"); h_Jet2_pT_bHMatched->SetLineColor(kRed);
	TH1F *h_Jet2_pT_bbHMatched=(TH1F*)gDirectory->Get("h_Jet2_pT_bbHMatched"); h_Jet2_pT_bbHMatched->SetLineColor(kMagenta);
	
	TH1F *h_Jet3_E=(TH1F*)gDirectory->Get("h_Jet3_E");
	TH1F *h_Jet3_pT=(TH1F*)gDirectory->Get("h_Jet3_pT");
	TH1F *h_Jet3_eta=(TH1F*)gDirectory->Get("h_Jet3_eta");
	TH1F *h_Jet3_phi=(TH1F*)gDirectory->Get("h_Jet3_phi");
	TH1F *h_Jet3_CSV=(TH1F*)gDirectory->Get("h_Jet3_CSV");
	TH1F *h_Jet3_pT_bZMatched=(TH1F*)gDirectory->Get("h_Jet3_pT_bZMatched"); h_Jet3_pT_bZMatched->SetLineColor(kBlue);
	TH1F *h_Jet3_pT_bbZMatched=(TH1F*)gDirectory->Get("h_Jet3_pT_bbZMatched"); h_Jet3_pT_bbZMatched->SetLineColor(kGreen);
	TH1F *h_Jet3_pT_bHMatched=(TH1F*)gDirectory->Get("h_Jet3_pT_bHMatched"); h_Jet3_pT_bHMatched->SetLineColor(kRed);
	TH1F *h_Jet3_pT_bbHMatched=(TH1F*)gDirectory->Get("h_Jet3_pT_bbHMatched"); h_Jet3_pT_bbHMatched->SetLineColor(kMagenta);
	
	TH1F *h_Jet4_E=(TH1F*)gDirectory->Get("h_Jet4_E");
	TH1F *h_Jet4_pT=(TH1F*)gDirectory->Get("h_Jet4_pT");
	TH1F *h_Jet4_eta=(TH1F*)gDirectory->Get("h_Jet4_eta");
	TH1F *h_Jet4_phi=(TH1F*)gDirectory->Get("h_Jet4_phi");
	TH1F *h_Jet4_CSV=(TH1F*)gDirectory->Get("h_Jet4_CSV");
	TH1F *h_Jet4_pT_bZMatched=(TH1F*)gDirectory->Get("h_Jet4_pT_bZMatched"); h_Jet4_pT_bZMatched->SetLineColor(kBlue);
	TH1F *h_Jet4_pT_bbZMatched=(TH1F*)gDirectory->Get("h_Jet4_pT_bbZMatched"); h_Jet4_pT_bbZMatched->SetLineColor(kGreen);
	TH1F *h_Jet4_pT_bHMatched=(TH1F*)gDirectory->Get("h_Jet4_pT_bHMatched"); h_Jet4_pT_bHMatched->SetLineColor(kRed);
	TH1F *h_Jet4_pT_bbHMatched=(TH1F*)gDirectory->Get("h_Jet4_pT_bbHMatched"); h_Jet4_pT_bbHMatched->SetLineColor(kMagenta);
	
  TH1F *h_DiJet_mass=(TH1F*)gDirectory->Get("h_DiJet_mass");
	TH1F *h_DiJet_mass_best=(TH1F*)gDirectory->Get("h_DiJet_mass_best");
	TH1F *h_DiJet_mass_bZbHMatched=(TH1F*)gDirectory->Get("h_DiJet_mass_bZbHMatched"); h_DiJet_mass_bZbHMatched->SetFillColor(kCyan);
	TH1F *h_DiJet_mass_bHbHMatched=(TH1F*)gDirectory->Get("h_DiJet_mass_bHbHMatched"); h_DiJet_mass_bHbHMatched->SetFillColor(kBlue);
	TH1F *h_DiJet_mass_bZbZMatched=(TH1F*)gDirectory->Get("h_DiJet_mass_bZbZMatched"); h_DiJet_mass_bZbZMatched->SetFillColor(kGreen);
	TH1F *h_Z_E=(TH1F*)gDirectory->Get("h_Z_E");
	TH1F *h_Z_pT=(TH1F*)gDirectory->Get("h_Z_pT");
	
	TH1F *h_H_mass=(TH1F*)gDirectory->Get("h_H_mass");
	TH1F *h_H_mass_bZbHMatched=(TH1F*)gDirectory->Get("h_H_mass_bZbHMatched"); h_H_mass_bZbHMatched->SetFillColor(kCyan);
	TH1F *h_H_mass_bZbZMatched=(TH1F*)gDirectory->Get("h_H_mass_bZbZMatched"); h_H_mass_bZbZMatched->SetFillColor(kGreen);
	TH1F *h_H_mass_bHbHMatched=(TH1F*)gDirectory->Get("h_H_mass_bHbHMatched"); h_H_mass_bHbHMatched->SetFillColor(kBlue);
	
	gROOT->SetStyle("Plain");
	TLegend *leg;
	
	TCanvas *c_nJets=new TCanvas("c_nJets");
	h_nJets->Draw();
	c_nJets->SaveAs(("h_nJets_"+H_string+".png").c_str());
	
	TCanvas *c_dR=new TCanvas("c_dR");
	h_dR->Draw();
	c_dR->SaveAs(("h_dR_"+H_string+".png").c_str());
	
	TCanvas *c_Jet1_E=new TCanvas("c_Jet1_E");
	h_Jet1_E->Draw();
	c_Jet1_E->SaveAs(("h_Jet1_E_"+H_string+".png").c_str());
	
	TCanvas *c_Jet1_pT=new TCanvas("c_Jet1_pT");
	h_Jet1_pT->Draw();
	h_Jet1_pT_bZMatched->Draw("SAME");
	h_Jet1_pT_bbZMatched->Draw("SAME");
	h_Jet1_pT_bHMatched->Draw("SAME");
	h_Jet1_pT_bbHMatched->Draw("SAME");
	TLegend *leg=new TLegend(0.7, 0.7, 0.85, 0.85);
	leg->AddEntry(h_Jet1_pT, "Unmatched");
	leg->AddEntry(h_Jet1_pT_bZMatched, "Matched to b(Z)");
	leg->AddEntry(h_Jet1_pT_bbZMatched, "Matched to #bar{b}(Z)");
	leg->AddEntry(h_Jet1_pT_bHMatched, "Matched to b(H)");
	leg->AddEntry(h_Jet1_pT_bbHMatched, "Matched to #bar{b}(H)");
	leg->Draw();
	c_Jet1_pT->SaveAs(("h_Jet1_pT_"+H_string+".png").c_str());
	
	TCanvas *c_Jet1_eta=new TCanvas("c_Jet1_eta");
	h_Jet1_eta->Draw();
  c_Jet1_eta->SaveAs(("h_Jet1_eta_"+H_string+".png").c_str());
	
	TCanvas *c_Jet1_phi=new TCanvas("c_Jet1_phi");
	h_Jet1_phi->Draw();
	c_Jet1_phi->SaveAs(("h_Jet1_phi_"+H_string+".png").c_str());
	
	TCanvas *c_Jet1_CSV=new TCanvas("c_Jet1_CSV");
	h_Jet1_CSV->Draw();
	c_Jet1_CSV->SaveAs(("h_Jet1_CSV_"+H_string+".png").c_str());
	
	TCanvas *c_Jet2_E=new TCanvas("c_Jet2_E");
	h_Jet2_E->Draw();
	c_Jet2_E->SaveAs(("h_Jet2_E_"+H_string+".png").c_str());
	
	TCanvas *c_Jet2_pT=new TCanvas("c_Jet2_pT");
	h_Jet2_pT->Draw();
	h_Jet2_pT_bZMatched->Draw("SAME");
	h_Jet2_pT_bbZMatched->Draw("SAME");
	h_Jet2_pT_bHMatched->Draw("SAME");
	h_Jet2_pT_bbHMatched->Draw("SAME");
	TLegend *leg=new TLegend(0.7, 0.7, 0.85, 0.85);
	leg->AddEntry(h_Jet2_pT, "Unmatched");
	leg->AddEntry(h_Jet2_pT_bZMatched, "Matched to b(Z)");
	leg->AddEntry(h_Jet2_pT_bbZMatched, "Matched to #bar{b}(Z)");
	leg->AddEntry(h_Jet2_pT_bHMatched, "Matched to b(H)");
	leg->AddEntry(h_Jet2_pT_bbHMatched, "Matched to #bar{b}(H)");
	leg->Draw();
	c_Jet2_pT->SaveAs(("h_Jet2_pT_"+H_string+".png").c_str());
	
	TCanvas *c_Jet2_eta=new TCanvas("c_Jet2_eta");
	h_Jet2_eta->Draw();
  c_Jet2_eta->SaveAs(("h_Jet2_eta_"+H_string+".png").c_str());
	
	TCanvas *c_Jet2_phi=new TCanvas("c_Jet2_phi");
	h_Jet2_phi->Draw();
	c_Jet2_phi->SaveAs(("h_Jet2_phi_"+H_string+".png").c_str());
	
	TCanvas *c_Jet2_CSV=new TCanvas("c_Jet2_CSV");
	h_Jet2_CSV->Draw();
	c_Jet2_CSV->SaveAs(("h_Jet2_CSV_"+H_string+".png").c_str());
	
	TCanvas *c_Jet3_E=new TCanvas("c_Jet3_E");
	h_Jet3_E->Draw();
	c_Jet3_E->SaveAs(("h_Jet3_E_"+H_string+".png").c_str());
	
	TCanvas *c_Jet3_pT=new TCanvas("c_Jet3_pT");
	h_Jet3_pT->Draw();
	h_Jet3_pT_bZMatched->Draw("SAME");
	h_Jet3_pT_bbZMatched->Draw("SAME");
	h_Jet3_pT_bHMatched->Draw("SAME");
	h_Jet3_pT_bbHMatched->Draw("SAME");
	TLegend *leg=new TLegend(0.7, 0.7, 0.85, 0.85);
	leg->AddEntry(h_Jet3_pT, "Unmatched");
	leg->AddEntry(h_Jet3_pT_bZMatched, "Matched to b(Z)");
	leg->AddEntry(h_Jet3_pT_bbZMatched, "Matched to #bar{b}(Z)");
	leg->AddEntry(h_Jet3_pT_bHMatched, "Matched to b(H)");
	leg->AddEntry(h_Jet3_pT_bbHMatched, "Matched to #bar{b}(H)");
	leg->Draw();
	c_Jet3_pT->SaveAs(("h_Jet3_pT_"+H_string+".png").c_str());
	
	TCanvas *c_Jet3_eta=new TCanvas("c_Jet3_eta");
	h_Jet3_eta->Draw();
  c_Jet3_eta->SaveAs(("h_Jet3_eta_"+H_string+".png").c_str());
	
	TCanvas *c_Jet3_phi=new TCanvas("c_Jet3_phi");
	h_Jet3_phi->Draw();
	c_Jet3_phi->SaveAs(("h_Jet3_phi_"+H_string+".png").c_str());
	
	TCanvas *c_Jet3_CSV=new TCanvas("c_Jet3_CSV");
	h_Jet3_CSV->Draw();
	c_Jet3_CSV->SaveAs(("h_Jet3_CSV_"+H_string+".png").c_str());
	
	TCanvas *c_Jet4_E=new TCanvas("c_Jet4_E");
	h_Jet4_E->Draw();
	c_Jet4_E->SaveAs(("h_Jet4_E_"+H_string+".png").c_str());
	
	TCanvas *c_Jet4_pT=new TCanvas("c_Jet4_pT");
	h_Jet4_pT->Draw();
	h_Jet4_pT_bZMatched->Draw("SAME");
	h_Jet4_pT_bbZMatched->Draw("SAME");
	h_Jet4_pT_bHMatched->Draw("SAME");
	h_Jet4_pT_bbHMatched->Draw("SAME");
	TLegend *leg=new TLegend(0.7, 0.7, 0.85, 0.85);
	leg->AddEntry(h_Jet4_pT, "Unmatched");
	leg->AddEntry(h_Jet4_pT_bZMatched, "Matched to b(Z)");
	leg->AddEntry(h_Jet4_pT_bbZMatched, "Matched to #bar{b}(Z)");
	leg->AddEntry(h_Jet4_pT_bHMatched, "Matched to b(H)");
	leg->AddEntry(h_Jet4_pT_bbHMatched, "Matched to #bar{b}(H)");
	leg->Draw();
	c_Jet4_pT->SaveAs(("h_Jet4_pT_"+H_string+".png").c_str());
	
	TCanvas *c_Jet4_eta=new TCanvas("c_Jet4_eta");
	h_Jet4_eta->Draw();
  c_Jet4_eta->SaveAs(("h_Jet4_eta_"+H_string+".png").c_str());
	
	TCanvas *c_Jet4_phi=new TCanvas("c_Jet4_phi");
	h_Jet4_phi->Draw();
	c_Jet4_phi->SaveAs(("h_Jet4_phi_"+H_string+".png").c_str());
	
	TCanvas *c_Jet4_CSV=new TCanvas("c_Jet4_CSV");
	h_Jet4_CSV->Draw();
	c_Jet4_CSV->SaveAs(("h_Jet4_CSV_"+H_string+".png").c_str());
	
  TCanvas *c_DiJet_mass=new TCanvas("c_DiJet_mass");
	THStack *s_DiJet_mass=new THStack("s_DiJet_mass", "Di-bJet Mass");
	s_DiJet_mass->Add(h_DiJet_mass_bZbHMatched);
	s_DiJet_mass->Add(h_DiJet_mass_bHbHMatched);
	s_DiJet_mass->Add(h_DiJet_mass_bZbZMatched);
	h_DiJet_mass->Draw();
	s_DiJet_mass->Draw("SAME");
	leg=new TLegend(0.7, 0.7, 0.85, 0.85);
	leg->AddEntry(h_DiJet_mass_bZbHMatched, "b(Z)b(H)");
	leg->AddEntry(h_DiJet_mass_bHbHMatched, "b(H)b(H)");
	leg->AddEntry(h_DiJet_mass_bZbZMatched, "b(Z)b(Z)");
	leg->Draw();
	c_DiJet_mass->SaveAs(("h_DiJet_mass_"+H_string+".png").c_str());
	
	TCanvas *c_DiJet_mass_best=new TCanvas("c_DiJet_mass_best");
	h_DiJet_mass_best->Draw();
	c_DiJet_mass_best->SaveAs(("h_DiJet_mass_best_"+H_string+".png").c_str());
	
	TCanvas *c_Z_E=new TCanvas("c_Z_E");
	h_Z_E->Draw();
	c_Z_E->SaveAs(("h_Z_E_"+H_string+".png").c_str());
	
	TCanvas *c_Z_pT=new TCanvas("c_Z_pT");
	h_Z_pT->Draw();
	c_Z_pT->SaveAs(("h_Z_pT_"+H_string+".png").c_str());
	
	TCanvas *c_H_mass=new TCanvas("c_H_mass");
	THStack *s_H_mass=new THStack("s_H_mass", "H mass");
	s_H_mass->Add(h_H_mass_bZbHMatched);
	s_H_mass->Add(h_H_mass_bZbZMatched);
	s_H_mass->Add(h_H_mass_bHbHMatched);
	h_H_mass->Draw();
	s_H_mass->Draw("SAME");
	leg=new TLegend(0.7, 0.7, 0.85, 0.85);
	leg->AddEntry(h_H_mass_bZbHMatched, "b(Z)b(H)");
	leg->AddEntry(h_H_mass_bZbZMatched, "b(Z)b(Z)");
	leg->AddEntry(h_H_mass_bHbHMatched, "b(H)b(H)");
	leg->Draw();
	c_H_mass->SaveAs(("h_H_mass_"+H_string+".png").c_str());
	
}
