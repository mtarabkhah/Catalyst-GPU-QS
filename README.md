# Catalyst-GPU-QS

I am benchmarking quantum circuits using Catalyst on a GPU. However, the speedup over CPU execution seems unexpectedly low.

## Problem

I’ve implemented a sample GHZ circuit with 26 qubits as a reference, comparing performance between CPU and GPU executions. Despite the expectation of significant GPU acceleration, the observed speedup is limited.

## Benchmark Results

Here are some sample execution times for a 26-qubit GHZ circuit:

- **GHZ1** (using `lightning.qubit` on CPU):  
  *Execution time*: 2.6811 seconds
- **GHZ2** (using `lightning.gpu` on GPU):  
  *Execution time*: 0.5751 seconds

This results in a **4.66x speedup** with the GPU version, which seems relatively low for GPU acceleration.

For comparison, running this quantum circuit in **Qiskit** yielded the following:

- GPU execution in Qiskit was **~760x faster** than the CPU version.
- While Catalyst showed better CPU performance than Qiskit, its GPU performance lagged behind.

## Additional Note

P.S. I have not used for loops in the creation of the circuits, as I am using code to automatically generate the circuits based on a provided list of gates. I assume this should not affect the performance.