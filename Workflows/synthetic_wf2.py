import multiprocessing as mp
import time

# Define stage configurations: (description, time_per_read, num_cores, memory_gb)
STAGE_CONFIGS = [
    # 1. Quality Control
    {
        "name": "Quality Control",
        "desc": "Assess and filter raw sequencing reads for quality (e.g., FastQC, adapter trimming).",
        "time_per_read": 0.000006,
        "num_cores": 1,
        "memory_gb": 2
    },
    # 2. Read Alignment
    {
        "name": "Read Alignment",
        "desc": "Align reads to the reference genome or transcriptome (e.g., STAR, HISAT2).",
        "time_per_read": 0.000009,
        "num_cores": 2,
        "memory_gb": 4
    },
    # 3. Quantification
    {
        "name": "Quantification",
        "desc": "Count reads mapped to genes or transcripts (e.g., featureCounts, Salmon).",
        "time_per_read": 0.000007,
        "num_cores": 5,
        "memory_gb": 3
    },
    # 4. Differential Expression Analysis
    {
        "name": "Differential Expression",
        "desc": "Identify genes with significant expression changes (e.g., DESeq2, edgeR).",
        "time_per_read": 0.000005,
        "num_cores": 1,
        "memory_gb": 2
    }
]

def run_stage(stage, num_reads):
    print(f"\nStage: {stage['name']}")
    print(f"Description: {stage['desc']}")
    print(f"Simulating {num_reads} reads | Cores: {stage['num_cores']} | Memory: {stage['memory_gb']} GB | Time/read: {stage['time_per_read']}s")
    start = time.time()
    with mp.Pool(stage['num_cores']) as pool:
        pool.map(lambda _: time.sleep(stage['time_per_read']), range(num_reads))
    elapsed = time.time() - start
    print(f"Completed {stage['name']} in {elapsed:.2f} seconds. (Simulated)")
    return elapsed

def synthetic_rnaseq_workflow(num_reads=1000000):
    total_time = 0
    print("Starting Synthetic RNA-Seq Workflow (4 Stages)\n")
    for stage in STAGE_CONFIGS:
        elapsed = run_stage(stage, num_reads)
        total_time += elapsed
    print(f"\nTotal workflow time: {total_time:.2f} seconds. (Simulated)")
    return total_time

if __name__ == "__main__":
    synthetic_rnaseq_workflow()
