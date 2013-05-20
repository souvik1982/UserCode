#include <iostream>

double pi=3.14159265358979;
double e =2.71828182845905;

double factorial(unsigned int f)
{
  double result=1;
  for (unsigned int i=1; i<=f; ++i)
  {
    result=result*i;
  }
  return result;
}

double integral(double b, double sigma, unsigned int i)
{
  double dx=sigma/100.0;
  double numerator=0;
  double denominator=0;
  
  for (double x=0; x<=b+5.*sigma; x+=dx) // go to 5 sigma
  {
    // numerator+=(pow(x, i)/factorial(i))*exp(-x-0.5*pow((x-b)/sigma, 2))*dx;
    numerator+=(TMath::Poisson(x,i))*exp(-0.5*pow((x-b)/sigma, 2))*dx;
    // std::cout<<"b= "<<b<<", sigma = "<<sigma<<", x = "<<x<<", i = "<<i
             // <<", x*e/double(i) = "<<x*e/double(i)<<" pow(x*e/double(i), i) = "<<pow(x*e/double(i), i)
             // << " | exp(-x-0.5*pow((x-b)/sigma, 2)) = "<<exp(-x-0.5*pow((x-b)/sigma, 2))
    //          <<" pow(x/double(i), i) = "<<pow(x/double(i), i)<<", exp(i-x-0.5*pow((x-b)/sigma, 2)) = "<<exp(i-x-0.5*pow((x-b)/sigma, 2))
    //          <<std::endl;
    // numerator+=pow(2*pi*double(i), -0.5)*pow(x*e/double(i), i)*exp(-x-0.5*pow((x-b)/sigma, 2))*dx;
    denominator+=exp(-0.5*pow((x-b)/sigma, 2))*dx;
  }
  
  //return numerator/(pow(2*pi, 0.5)*sigma);
  return numerator/denominator;
}

double sum(double b, double sigma, unsigned int s)
{
  double result=0;
  
  for (unsigned int i=s; i<3*s; ++i) // go to 3*s
  {
    result+=integral(b, sigma, i);
  }
  
  return result;
}

unsigned int returnSigmaInterval(double b, double sigma, double limitintegral=0.6827)
{
  double total=0.;
  unsigned int i=0;
  while (total<limitintegral)
  {
    total+=integral(b, sigma, b+i);
    if (b-i>0)
    {
      total+=integral(b, sigma, b-i);
    }
    else std::cout<<"b-i<0"<<std::endl;
    ++i;
  }
  return i-1;
}

unsigned int returnSigmaLimit(double b, double sigma, unsigned int sstart=100., double limitintegral=3e-7)
{
  double total=0;
  unsigned int i=sstart;
  while (total<limitintegral)
  {
    double temp=integral(b, sigma, i);
    total+=integral(b, sigma, i);
    // std::cout<<"temp = "<<temp<<", total = "<<total<<std::endl;
    --i;
  }
  return i+1;
}
  



double sumPoisson(double b, unsigned int s)
{
  double result=0;
  
  for (unsigned int i=s; i<3*s; ++i)
  {
    // result+=pow(b,i)*exp(-b)/factorial(i);
    result+=TMath::Poisson(b,i);
  }
  
  return result;
}


  

double returnNSigma(double prob)
{
  double x=100.0;
  double dx=1./100.;
  double integral=0.0;
  
  while(integral<prob)
  {
    x-=dx;
    integral+=2.0*exp(-0.5*pow(x, 2))*dx/pow(2.0*pi, 0.5);
    // integral+=exp(-0.5*pow(x, 2))*dx/pow(2.0*pi, 0.5);
  }
  
  return x;
}

void Significance()
{
  
  unsigned int signal;
  double bg;
  double bg_sigma;
  
  std::string mode="data";
  // data, mc
  std::string decay="Sum";
  // options: KKpi, KsK, pieta, pietaprime, KKpipi0, pipipi, KsKmpipi, pipi0eta, pietaprimerho
  
  if (mode=="mc")
  {
    if (decay=="KKpi")
    {
      signal=15;
      bg=1.048;
      bg_sigma=0.869;
    }
    else if (decay=="KsK")
    {
      signal=4;
      bg=0.849;
      bg_sigma=0.854;
    }
    else if (decay=="pieta")
    {
      signal=3;
      bg=1.4;
      bg_sigma=0.857;
    }
    else if (decay=="pietaprime")
    {
      signal=1;
      bg=0.0;
      bg_sigma=0.6335;
    }
    else if (decay=="KKpipi0")
    {
      signal=7;
      bg=1.703;
      bg_sigma=0.735;
    }
    else if (decay=="pipipi")
    {
      signal=5;
      bg=1.572;
      bg_sigma=0.741;
    }
    else if (decay=="KsKmpipi")
    {
      signal=4;
      bg=1.575;
      bg_sigma=0.654;
    }
    else if (decay=="pipi0eta")
    {
      signal=8;
      bg=2.621;
      bg_sigma=0.630;
    }
    else if (decay=="pietaprimerho")
    {
      signal=4;
      bg=1.835;
      bg_sigma=0.549;
    }
    else if (decay=="Sum")
    {
      signal=51;
      bg=12.603;
      bg_sigma=2.72;
    }
    else if (decay=="Sum_KKpi")
    {
      signal=36;
      bg=11.555;
      bg_sigma=2.379;
    }
    else if (decay=="Sum_pietaprime")
    {
      signal=50;
      bg=12.603;
      bg_sigma=2.357;
    }
    else if (decay=="Sum_pietaprime_pieta")
    {
      signal=46;
      bg=11.203;
      bg_sigma=2.246;
    }
    else if (decay=="Sum_pietaprime_KsKmpipi")
    {
      signal=46;
      bg=11.028;
      bg_sigma=1.947;
    }
    else if (decay=="Sum_pietaprime_pieta_KsKmpipi")
    {
      signal=43;
      bg=9.63;
      bg_sigma=1.78;
    }
    else if (decay=="Sum_pietaprime_pieta_KsKmpipi_KsK")
    {
      signal=39;
      bg=8.779;
      bg_sigma=2.238;
    }
  }
  else if (mode=="data")
  {
    if (decay=="KKpi")
    {
      signal=14;
      bg=1.048;
      bg_sigma=0.869;
    }
    else if (decay=="KsK")
    {
      signal=1;
      bg=0.849;
      bg_sigma=0.854;
    }
    else if (decay=="pieta")
    {
      signal=4;
      bg=1.4;
      bg_sigma=0.857;
    }
    else if (decay=="pietaprime")
    {
      signal=4;
      bg=0.0;
      bg_sigma=0.6335;
    }
    else if (decay=="KKpipi0")
    {
      signal=6;
      bg=1.703;
      bg_sigma=0.735;
    }
    else if (decay=="pipipi")
    {
      signal=7;
      bg=1.572;
      bg_sigma=0.741;
    }
    else if (decay=="KsKmpipi")
    {
      signal=4;
      bg=1.575;
      bg_sigma=0.654;
    }
    else if (decay=="pipi0eta")
    {
      signal=7;
      bg=2.621;
      bg_sigma=0.630;
    }
    else if (decay=="pietaprimerho")
    {
      signal=4;
      bg=1.835;
      bg_sigma=0.549;
    }
    else if (decay=="Sum")
    {
      signal=51;
      bg=12.603;
      // bg_sigma=2.72;
      bg_sigma=4.35;
    }
    else if (decay=="Others")
    {
      signal=37;
      bg=11; //.56;
      bg_sigma=3.61;
    }
  }

  // bg_sigma*=0.75;
  
  double prob=sum(bg, bg_sigma, signal);
  
  std::cout<<"Decay = "<<decay<<std::endl;
  
  std::cout<<"The probability of bg = "<<bg<<"+- bg_sigma = "<<bg_sigma<<" to jump to signal = "<<signal
           <<" is = "<<prob<<std::endl;
           
  std::cout<<"The Poisson prob = "<<sumPoisson(bg, signal)<<std::endl;
  
  std::cout<<"This corresponds to "<<returnNSigma(prob)<<std::endl;
  
  std::cout<<"Prob 1.34e-11 = "<<returnNSigma(1.34e-11)<<std::endl;
           
}
