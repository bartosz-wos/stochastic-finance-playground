#pragma once

#include <cstdint>
#include <array>
#include <new>
#include <numbers>
#include <cmath>

namespace quant_math{

  constexpr double nCr(uint32_t n, uint32_t k) noexcept{
    if(k > n) [[unlikely]] return 0.0;
    if(k * 2 > n) k = n - k;
    if(k == 0 || k == n) [[unlikely]] return 1.0;

    double res = 1.0;
    for(uint32_t i = 1; i <= k; ++i)
      res = res * (n - i + 1) / i;

    return res;
  }

  constexpr double fast_pow(double base, uint32_t exp) noexcept{
    double ret = 1.0;

    while(exp){
      if(exp & 1)
        ret *= base;
      base *= base;
      exp >>= 1;
    }

    return ret;
  }

  constexpr double binomial_pmf(uint32_t n, uint32_t k, double p) noexcept{
    if(k > n) [[unlikely]] return 0.0;
    if(p == 0.0) return (k == 0) ? 1.0 : 0.0;
    if(p == 1.0) return (k == n) ? 1.0 : 0.0;
    return fast_pow(p, k) * fast_pow(1.0 - p, n - k) * nCr(n, k);
  }

  constexpr double approx_ln_factorial(double n) noexcept{
    if(n < 2.0) return 0.0;
    return n * std::log(n) - n + 0.5 * std::log(2.0 * std::numbers::pi * n) + 1 / (12.0 * n) - 1 / (360.0 * n * n * n);
  }

  inline double binomial_pmf_large(uint32_t n, uint32_t k, double p) noexcept{
    if(k > n) [[unlikely]] return 0.0;
    if(p == 0.0) return (k == 0) ? 1.0 : 0.0;
    if(p == 1.0) return (k == n) ? 1.0 : 0.0;
    return std::exp(approx_ln_factorial(n) - approx_ln_factorial(k) - approx_ln_factorial(n - k) + k * std::log(p) + (n - k) * std::log(1.0 - p));
  }

  template <size_t maxN>
  class alignas(std::hardware_destructive_interference_size) BinomialLUT{
  public:
    explicit BinomialLUT(double p) : p_(p){
      for(size_t n = 0; n < maxN; ++n)
        for(size_t k = 0; k <= n; ++k){
          if(n > 0 && k > 0)
            data_[n * maxN + k] = data_[(n - 1) * maxN + k - 1] * p + data_[(n - 1) * maxN + k] * (1 - p);
          else
            data_[n * maxN + k] = binomial_pmf(n, k, p);
        }
    }

    inline double get(uint32_t n, uint32_t k) const noexcept{
      return data_[n * maxN + k];
    }

  private:
    double p_;
    std::array<double, maxN * maxN> data_{};
  };
}
