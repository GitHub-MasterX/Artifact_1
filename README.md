# Syscall Sequence Window Analysis

## Motivation
Evaluate how syscall sequence window size (k) impacts anomaly sensitivity under stress.

## Method
- Collect syscall traces using straces
- Generate k-length syscall windows
- Compare unique sequence overlap between normal and stressed execution

## Experiments
- CPU stress
- I/O stress
- Memory stress
- k={3,5,7,9,11}

## Results
See results/results.csv

## How to Run
1. Collect traces
2. Run parsing script
3. Run evalution script
