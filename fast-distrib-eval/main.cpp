#include <iostream>
#include "distrib-eval.hpp"

int main(){
  auto val = quant_math::binomial_pmf(40, 7, 0.5);
  auto distrib = quant_math::BinomialLUT<100>{0.5};
  std::cout << val << '\n';
  std::cout << distrib.get(40, 7) << '\n';
  std::cout << quant_math::binomial_pmf_large(40, 7, 0.5) << '\n';
}
