#include "PhysicsTools/KinFitter/interface/TFitConstraintM.h"
#include "PhysicsTools/KinFitter/interface/TFitParticleEtEtaPhi.h"
#include "PhysicsTools/KinFitter/interface/TFitParticleEt.h"
#include "PhysicsTools/KinFitter/interface/TKinFitter.h"
#include "PhysicsTools/KinFitter/interface/TFitConstraintEp.h"
#include "TLorentzVector.h"

#include <iostream>

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
// Modified version of the ExampleEtEtaPhi2CFit.C macro from CMS AN 2005/025.
// Jet error parametrization from CMS AN 2005/005.
//
// To run this macro in a root session do:
// root [0] gSystem->Load("libPhysicsToolsKinFitter.so");
// root [1] .x PhysicsTools/KinFitter/test/kinFit4b.C+
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
namespace H4b
{
double deltaPhi(double phi1,double phi2)
  {
    double result = phi1 - phi2;
    while (result > TMath::Pi()) result -= 2*TMath::Pi();
    while (result <= -TMath::Pi()) result += 2*TMath::Pi();
    return result;
  }

double deltaR(double eta1,double phi1,double eta2,double phi2)
    {
      double deta = eta1 - eta2;
      double dphi = deltaPhi(phi1, phi2);
      return TMath::Sqrt(deta*deta + dphi*dphi);
    }



Double_t ErrEt(Float_t Et, Float_t Eta) {
  Double_t InvPerr2, a, b, c;
  if(fabs(Eta) < 1.4){
    a = 5.6;
    b = 1.25;
    c = 0.033;
  }
  else{
    a = 4.8;
    b = 0.89;
    c = 0.043;
  }
  InvPerr2 = (a * a) + (b * b) * Et + (c * c) * Et * Et;
  return InvPerr2;
}

Double_t ErrEta(Float_t Et, Float_t Eta) {
  Double_t InvPerr2, a, b, c;
  if(fabs(Eta) < 1.4){
    a = 1.215;
    b = 0.037;
    c = 7.941 * 0.0001;
  }
  else{
    a = 1.773;
    b = 0.034;
    c = 3.56 * 0.0001;
  }
 InvPerr2 = a/(Et * Et) + b/Et + c;
 
return InvPerr2;
}

Double_t ErrPhi(Float_t Et, Float_t Eta) {
  Double_t InvPerr2, a, b, c;
  if(fabs(Eta) < 1.4){
    a = 6.65;
    b = 0.04;
    c = 8.49 * 0.00001;
  }
  else{
    a = 2.908;
    b = 0.021;
    c = 2.59 * 0.0001;
  }
 InvPerr2 = a/(Et * Et) + b/Et + c;
return InvPerr2;
}


float chi2(TLorentzVector v1, TLorentzVector v2){

 float result = -1;

  TMatrixD m1(3,3);
  TMatrixD m2(3,3);
  m1.Zero();
  m2.Zero();
  
  //In this example the covariant matrix depends on the transverse energy and eta of the jets
  m1(0,0) = ErrEt (v1.Et(), v1.Eta()); // et
  m1(1,1) = ErrEta(v1.Et(), v1.Eta()); // eta
  m1(2,2) = ErrPhi(v1.Et(), v1.Eta()); // phi
  m2(0,0) = ErrEt (v2.Et(), v2.Eta()); // et
  m2(1,1) = ErrEta(v2.Et(), v2.Eta()); // eta
  m2(2,2) = ErrPhi(v2.Et(), v2.Eta()); // phi
  TFitParticleEtEtaPhi *jet1 = new TFitParticleEtEtaPhi( "Jet1", "Jet1", &v1, &m1 );
  TFitParticleEtEtaPhi *jet2 = new TFitParticleEtEtaPhi( "Jet2", "Jet2", &v2, &m2 );

  //vec1 and vec2 must make a W boson
  TFitConstraintM *mCons1 = new TFitConstraintM( "WMassConstraint", "WMass-Constraint", 0, 0 , 126);
  mCons1->addParticles1( jet1, jet2 );

  //Definition of the fitter
  //Add three measured particles(jets)
  //Add two constraints
  TKinFitter* fitter = new TKinFitter("fitter", "fitter");
  fitter->addMeasParticle( jet1 );
  fitter->addMeasParticle( jet2 );
  fitter->addConstraint( mCons1 );

  //Set convergence criteria
  fitter->setMaxNbIter( 30 );
  fitter->setMaxDeltaS( 1e-2 );
  fitter->setMaxF( 1e-1 );
  fitter->setVerbosity(1);

  //Perform the fit
  //std::cout << "Performing kinematic fit..." << std::endl;
  fitter->fit();

  result = fitter->getS(); 

  delete jet1;
  delete jet2;
  delete mCons1;
  delete fitter;

	return result;

}

TLorentzVector Xchi2(TLorentzVector &v11, TLorentzVector &v22,TLorentzVector &v33, TLorentzVector &v44, double & chi2, double mass){

  TLorentzVector v1 = v11;
  TLorentzVector v2 = v22;
  TLorentzVector v3 = v33;
  TLorentzVector v4 = v44;
 
  TMatrixD m1(3,3);
  TMatrixD m2(3,3);
  TMatrixD m3(3,3);
  TMatrixD m4(3,3);
  TMatrixD mm1(3,3);
  TMatrixD mm2(3,3);
  TMatrixD mm3(3,3);
  TMatrixD mm4(3,3);
  mm1.Zero();
  mm2.Zero();
  mm3.Zero();
  mm4.Zero();
  m1.Zero();
  m2.Zero();
  m3.Zero();
  m4.Zero();
  //In this example the covariant matrix depends on the transverse energy and eta of the jets
  m1(0,0) = ErrEt (v1.Et(), v1.Eta()); // et
  mm1(0,0) = ErrEt (v1.Et(), v1.Eta()); // et
  m1(1,1) = ErrEta(v1.Et(), v1.Eta()); // eta
  m1(2,2) = ErrPhi(v1.Et(), v1.Eta()); // phi
  m2(0,0) = ErrEt (v2.Et(), v2.Eta()); // et
  mm2(0,0) = ErrEt (v2.Et(), v2.Eta()); // et
  m2(1,1) = ErrEta(v2.Et(), v2.Eta()); // eta
  m2(2,2) = ErrPhi(v2.Et(), v2.Eta()); // phi
  m3(0,0) = ErrEt (v3.Et(), v3.Eta()); // et
  mm3(0,0) = ErrEt (v3.Et(), v3.Eta()); // et
  m3(1,1) = ErrEta(v3.Et(), v3.Eta()); // eta
  m3(2,2) = ErrPhi(v3.Et(), v3.Eta()); // phi
  m4(0,0) = ErrEt (v4.Et(), v4.Eta()); // et
  mm4(0,0) = ErrEt (v4.Et(), v4.Eta()); // et
  m4(1,1) = ErrEta(v4.Et(), v4.Eta()); // eta
  m4(2,2) = ErrPhi(v4.Et(), v4.Eta()); // phi   
  
  TFitParticleEt *jet1 = new TFitParticleEt( "Jet1", "Jet1", &v1, &mm1 );
  TFitParticleEt *jet2 = new TFitParticleEt( "Jet2", "Jet2", &v2, &mm2 );
  TFitParticleEt *jet3 = new TFitParticleEt( "Jet3", "Jet3", &v3, &mm3 );
  TFitParticleEt *jet4 = new TFitParticleEt( "Jet4", "Jet4", &v4, &mm4 );

	//vec1 and vec2 must make a W boson
  TFitConstraintM *mCons1 = new TFitConstraintM( "WMassConstraint", "WMass-Constraint", 0, 0 , mass);
  mCons1->addParticles1( jet1, jet2 );
	
  TFitConstraintM *mCons2 = new TFitConstraintM( "W2MassConstraint", "W2Mass-Constraint", 0, 0 , mass);
  mCons2->addParticles1( jet3, jet4 );

//Definition of the fitter
  TKinFitter* fitter = new TKinFitter("fitter", "fitter");
  fitter->addMeasParticle( jet1 );
  fitter->addMeasParticle( jet2 );
  fitter->addConstraint( mCons1 );
  fitter->addMeasParticle( jet3 );
  fitter->addMeasParticle( jet4 );
  fitter->addConstraint( mCons2 );	
//  fitter->addConstraint( mCons3 );

//  fitter->addConstraint( mCons4 );	

  //Set convergence criteria
  fitter->setMaxNbIter( 30 );
  fitter->setMaxDeltaS( 1e-2 );
  fitter->setMaxF( 1e-1 );
  fitter->setVerbosity(3);

  //Perform the fit
  //std::cout << "Performing kinematic fit..." << std::endl;
  fitter->fit();

  chi2  = fitter->getS();

  const TLorentzVector* jet1F;
  const TLorentzVector* jet2F;
  const TLorentzVector* jet3F;
  const TLorentzVector* jet4F;

  jet1F=fitter->get4Vec(0);
  jet2F=fitter->get4Vec(1);
  jet3F=fitter->get4Vec(2);
  jet4F=fitter->get4Vec(3);

  TLorentzVector H1, H2;
  v11= *jet1F;
  v22= *jet2F;
  v33= *jet3F;
  v44= *jet4F;

  H1 = (*jet1F)+(*jet2F);
  H2 = (*jet3F)+(*jet4F);

  delete jet1;
  delete jet2;
  delete jet3;
  delete jet4;
  delete mCons1;
  delete mCons2;
  delete fitter;


        return (H1+H2);

	}
}

