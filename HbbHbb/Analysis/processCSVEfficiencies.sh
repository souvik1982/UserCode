date1=$(date +"%s")
root -l -b -q 'CSVEfficiencies.cc++("QCDHT250To500_V5", "QCDHT500To1000_V5", "QCDHT1000ToInf_V5", "PUWeight_QCD250To500.root", "PUWeight_QCD500To1000.root", "PUWeight_QCD1000ToInf.root")' 
date2=$(date +"%s")
diff=$(($date2-$date1))
echo "$(($diff / 60)) minutes and $(($diff % 60)) seconds elapsed."
say "$(($diff / 60)) minutes and $(($diff % 60)) seconds elapsed."
