// Original Author:  Souvik Das
//         Created:  Wed Nov 30 16:51:14 CST 2011

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"

class TriggerSignal : public edm::EDAnalyzer {
   public:
      explicit TriggerSignal(const edm::ParameterSet&);
      ~TriggerSignal();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      edm::InputTag triggerResults_;
      std::map<std::string, int> hltMap_;
};


TriggerSignal::TriggerSignal(const edm::ParameterSet& iConfig)
{
  triggerResults_=iConfig.getUntrackedParameter<edm::InputTag>("TriggerResults");
}

TriggerSignal::~TriggerSignal()
{
}

void TriggerSignal::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  Handle<TriggerResults> triggerResults;
  if (!iEvent.getByLabel(triggerResults_, triggerResults))
  {
    std::cout<<"TriggerResults requested does not exist"<<std::endl;
    return;
  }
  iEvent.getByLabel(triggerResults_, triggerResults);
  const edm::TriggerNames &trigNames=iEvent.triggerNames(*triggerResults);
  for (size_t i=0; i<triggerResults->size(); ++i)
  {
    std::string trigName=trigNames.triggerName(i);
    int accept=triggerResults->accept(i);
    // if (hltMap_.find(trigName)==hltMap_.end())
    // {
    //   hltMap_[trigName]=accept;
    // }
    // else
    // {
    //  hltMap_[trigName]+=accept;
    // }
    hltMap_[trigName]+=accept;
  }
  
}


// ------------ method called once each job just before starting event loop  ------------
void 
TriggerSignal::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerSignal::endJob() 
{
  for (std::map<std::string, int>::iterator iMap=hltMap_.begin(); iMap!=hltMap_.end(); ++iMap)
  {
    std::cout<<iMap->first<<", "<<iMap->second<<std::endl;
  }
}

// ------------ method called when starting to processes a run  ------------
void 
TriggerSignal::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
TriggerSignal::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
TriggerSignal::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
TriggerSignal::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerSignal::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerSignal);
