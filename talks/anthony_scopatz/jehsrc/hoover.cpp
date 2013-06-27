#include "hoover.h"

using namespace hoover;

double A::power(int n){
  int i = 1;
  double val = a;
  while (i < n){val *= a;i++;};
  return val;
};
