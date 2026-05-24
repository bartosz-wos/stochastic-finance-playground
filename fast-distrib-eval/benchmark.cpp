#include <benchmark/benchmark.h>
#include "distrib-eval.hpp"

static void BM_CompileTime(benchmark::State& state){
	for(auto _ : state)
		benchmark::DoNotOptimize(quant_math::binomial_pmf(40, 7, 0.5));
}
BENCHMARK(BM_CompileTime);

static void BM_LUT_FastPath(benchmark::State& state){
	quant_math::BinomialLUT<100> lut{0.5};
	uint32_t n = 40, k = 7;

	for(auto _ : state){
		benchmark::DoNotOptimize(n);
		benchmark::DoNotOptimize(k);
		benchmark::DoNotOptimize(lut.get(n, k));
		benchmark::ClobberMemory();
	}
}
BENCHMARK(BM_LUT_FastPath);

static void BM_SlowPath_Large(benchmark::State& state){
	uint32_t n = 40, k = 7;

	for(auto _ : state){
		benchmark::DoNotOptimize(n);
                benchmark::DoNotOptimize(k);
		benchmark::DoNotOptimize(quant_math::binomial_pmf_large(n, k, 0.5));
		benchmark::ClobberMemory();
	}
}
BENCHMARK(BM_SlowPath_Large);

static void BM_FastPath_Large(benchmark::State& state){
	uint32_t n = 40, k = 7;

        for(auto _ : state){
                benchmark::DoNotOptimize(n);
                benchmark::DoNotOptimize(k);
                benchmark::DoNotOptimize(quant_math::approx_binomial_pmf_large(n, k, 0.5));
                benchmark::ClobberMemory();
        }

}
BENCHMARK(BM_FastPath_Large);

BENCHMARK_MAIN();
