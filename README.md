# Artifact 1 – Behavioral Analysis through System Call Telemetry

## Overview

In this artifact we are going to explore how behavior varies across different execution conditions of processes by observing and analyzing their __syscall telemetry__.

The objective of this experiment is to capture runtime behavior of processes using _strace_, extract meaningful patterns from the collected system calls, and analyze differences between normal and anomalous execution flows.

For the artifact the goal is to make a minimal program to capture the syscalls for normal, CPU, memory and IO, then we are going to compare the syscall traces from normal execution with those under CPU, memory and IO stress conditions. 
These three are used to as they represent the primary system resources, while other metrics are typically derived from them

---

## Objectives

- Capture system call traces from program execution using _strace_.
- Extract structured information from raw syscall logs.
- Identify behavioral patterns from syscall distribution.
- Compare __normal execution vs anomalous execution behavior__.
---

## Experimental Setup

Environment

- Linux (Ubuntu)
- Python 3
- _strace_ for syscall tracing

Tools Used

- __strace__ – captures system calls invoked by processes.
- __Python__ – used for parsing syscall logs and generating structured datasets.
---

## Data Collection

System calls were captured using:

> strace -o trace.log <program>

The output logs contain time-ordered records of system calls including:

- syscall name
- arguments
- return values
- timestamps

These logs serve as the __raw telemetry source__ for analysis.

Anomalous conditions were simulated by executing programs under CPU, memory and IO stress while capturing syscall traces.

---

## Data Processing Pipeline

Raw _strace_ logs are not directly usable for analysis.
A parsing pipeline was developed to convert logs into structured data.

Processing steps:

1. Read raw syscall logs.
2. Extract relevant fields from each entry.
3. Convert extracted data into structured CSV format.
4. Separate traces into different behavioral categories.

---

## Behavioral Analysis

The analysis focuses on identifying differences between:

- __Normal execution behavior__
- __Unexpected or anomalous syscall behavior__

Key observations include:

- variations in syscall frequency
- differences in syscall distributions
- abnormal interaction with system resources

These behavioral differences can be used as signals for __runtime anomaly detection systems.__

---

## Key Insights

- System call telemetry provides a __fine-grained view of program behavior.__
- Behavioral differences can be detected through variations in syscall distributions.
- Simple telemetry pipelines can reveal meaningful insights without complex instrumentation.

---

## Reproducibility

Steps to reproduce the experiment:

1. Install required tools (_strace_, Python).
2. Run the target program under _strace_.
3. Parse the generated syscall logs using the provided Python scripts.
4. Generate CSV datasets.

---

## Relevance to Security Research

System call telemetry is widely used in:

- anomaly detection systems
- intrusion detection
- sandbox monitoring
- honeypot interaction analysis

This artifact serves as a __foundation for studying system behavior through low-level telemetry signals.__

This forms a baseline for higher-level behavioral modeling in later stages.
