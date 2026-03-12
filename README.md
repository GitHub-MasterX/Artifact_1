# Artifact 1 – Behavioral Analysis through System Call Telemetry

## Overview

This artifact explores how program behaviour can be observed and analyzed through __system call telemetry.__
The objective of this experiment is to capture runtime behaviour of processes using _strace_, extract meaningful patterns from the collected system calls, and analyze differences between normal and anomalous execution flows.

System calls represent the __interface between user applications and the operating system kernel__, making them a valuable source of behavioural telemetry for security monitoring and anomaly detection.

---

Objectives

- Capture system call traces from program execution using _strace_.
- Extract structured information from raw syscall logs.
- Identify behavioural patterns in program execution.
- Compare __normal execution vs anomalous execution behaviour__.
- Generate visual representations of execution patterns.

---

## Experimental Setup

Environment

- Linux (Ubuntu)
- Python 3
- _strace_ for syscall tracing

Tools Used

- __strace__ – captures system calls invoked by processes.
- __Python__ – used for parsing syscall logs and generating structured datasets.
- __Matplotlib__ – used to visualize syscall behaviour patterns.

---

## Data Collection

System calls were captured using:

> strace -o trace.log <program>

The output logs contain chronological records of system calls including:

- syscall name
- arguments
- return values
- timestamps

These logs serve as the __raw telemetry source__ for analysis.

---

## Data Processing Pipeline

Raw _strace_ logs are not directly usable for analysis.
A parsing pipeline was developed to convert logs into structured data.

Processing steps:

1. Read raw syscall logs.
2. Extract relevant fields from each entry.
3. Convert extracted data into structured CSV format.
4. Separate traces into different behavioural categories.
5. Prepare datasets for visualization.

---

## Behavioral Analysis

The analysis focuses on identifying differences between:

- __Normal execution behaviour__
- __Unexpected or anomalous syscall sequences__

Key observations include:

- variation in syscall frequency
- differences in syscall sequences
- abnormal interaction with system resources

These behavioural differences can be used as signals for __runtime anomaly detection systems.__

---

# Visualization

Two primary plots were generated:

__Coverage Plot__

Represents the distribution of observed system calls during program execution.

__Mismatch Plot__

Highlights deviations between expected syscall behaviour and observed behaviour.

These visualizations help identify behavioural anomalies in a clear and interpretable way.

---

## Key Insights

- System call telemetry provides a __fine-grained view of program behaviour.__
- Behavioral differences can be detected by analyzing syscall patterns.
- Simple telemetry pipelines can reveal meaningful insights without complex instrumentation.

---

## Reproducibility

Steps to reproduce the experiment:

1. Install required tools (_strace_, Python).
2. Run the target program under _strace_.
3. Parse the generated syscall logs using the provided Python scripts.
4. Generate CSV datasets.
5. Produce the behavioral plots.

---

## Relevance to Security Research

System call telemetry is widely used in:

- anomaly detection systems
- intrusion detection
- sandbox monitoring
- honeypot interaction analysis

This artifact serves as a __foundation for studying system behaviour through low-level telemetry signals.__
