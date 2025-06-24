SYNTHETIC SCIENTIFIC WORKFLOWS
#Workflows

This folder contains the code of synthetic scientific workflows similar to the ones used to validate the effectivenes of the methods used to slect and allocate resources withihn a Volunteer Edge-Cloud (VEC) environment. 

* Synthetic 1: A PGen Genomic Variation Workflow

This repository includes a synthetic Python workflow that simulates a large-scale genomic variation analysis pipeline inspired by PGen. The workflow consists of 10 modular stages representing typical steps in variant discovery and annotation pipelines, such as quality control, adapter trimming, read alignment, duplicate marking, base quality recalibration, variant calling, variant filtration, variant annotation, copy number variation (CNV) analysis, and results integration/reporting. Each stage is implemented as a separate function, with configurable parameters for simulated execution time, CPU core usage (1–8), and memory requirement (1–10 GB). This design allows users to benchmark, test, or demonstrate workflow orchestration and resource management in a controlled environment, without requiring real genomic data or software dependencies.

* Synthetic 2: A RNA-Seq Analysis Workflow

The repository also provides a synthetic Python workflow that mimics a typical RNA-Seq analysis pipeline. This workflow features 4 key stages: quality control, read alignment, quantification, and differential expression analysis. Each stage is implemented as an independent function and can be configured for execution time, CPU usage (1–5), and memory requirement (1–10 GB). This lightweight simulation is ideal for educational purposes, workflow prototyping, or testing resource allocation strategies in RNA-Seq data analysis, without the need for actual sequencing data or bioinformatics tools.

Both workflows are modular, easy to extend, and suitable for learning, demonstration, or workflow development in computational genomics contexts.
