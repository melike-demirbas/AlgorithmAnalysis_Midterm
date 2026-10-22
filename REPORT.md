# Sorting Algorithm Analysis — Project Report

**Course:** Algorithm Analysis  
**Lecturer:** Dr. Coşkun Şahin  
**Student Name:** Melike Demirbaş  
**Student Number:** 2322190007  
**Date:** October 2026  

---

## 1. Introduction

This report analyzes two sorting algorithms: **Insertion Sort** and **Bubble Sort**[cite: 9, 10]. For each algorithm, we explain how it works, analyze its time complexity, evaluate CPU and Memory workloads based on custom performance benchmarks, and compare their best use cases[cite: 9].

---

## 2. Insertion Sort

### How It Works

Insertion Sort builds the final sorted array one item at a time. It iterates through the input array, consuming one input element each repetition, and grows a sorted output list by finding the correct position for each element and inserting it there.

```text
INSERTION-SORT(A, n)
    for i = 1 to n-1
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
```

### Example

Sorting `[12, 11, 13, 5, 6]`:

| Step | Action | Result |
|------|--------|--------|
| 1 | `11` is smaller than `12`, insert before `12` | `[11, 12, 13, 5, 6]` |
| 2 | `13` is greater than `12`, leave as is | `[11, 12, 13, 5, 6]` |
| 3 | `5` is smallest, shift everything right | `[5, 11, 12, 13, 6]` |
| 4 | `6` goes after `5`, shift `11, 12, 13` right | `[5, 6, 11, 12, 13]` ✓ |

### Complexity Analysis

**Time Complexity:**

| Case | Time | Explanation |
|------|------|-------------|
| Best | O(n) | Array is already sorted; inner while-loop never executes. |
| Average | O(n²) | Elements are randomly distributed. |
| Worst | O(n²) | Reverse sorted array; every element must be shifted to the beginning. |

**Space Complexity:** O(1) — It is an in-place sorting algorithm.

**Stable:** Yes — It does not change the relative order of elements with equal keys.

### Benchmark Results (CPU and Memory)

*Tested via Python `time` and `tracemalloc` modules.*

| n | Best CPU (s) | Worst CPU (s) | Random CPU (s) | Memory Peak (KB) |
|---|---|---|---|---|
| 1,000 | 0.0005 | 0.1528 | 0.0445 | ~0.06 |
| 2,000 | 0.0006 | 0.3842 | 0.1952 | ~0.00 |
| 5,000 | 0.0015 | 2.6136 | 1.3080 | ~0.00 |
| 10,000| 0.0033 | 10.4712 | 5.2356 | ~0.00 |

> CPU times confirm quadratic O(n²) growth for Worst/Average cases, while Best case stays extremely low (linear). Memory overhead is negligible.

---

## 3. Bubble Sort

### How It Works

Bubble Sort compares **adjacent elements** and swaps them if they are in wrong order[cite: 11]. After each pass, the largest unsorted element "bubbles" to the end[cite: 11]. With the **early-exit optimization**, if no swaps happen in a pass, the array is sorted and we stop[cite: 11].

```text
BUBBLE-SORT(A, n)
    for i = 0 to n-1
        swapped = False
        for j = 0 to n-i-2
            if A[j] > A[j+1]
                swap A[j] and A[j+1]
                swapped = True
        if not swapped
            break
```

### Example

Sorting `[5, 3, 8, 4, 2]`:

| Pass | Comparisons & Swaps | Result |
|------|---------------------|--------|
| 1 | 5↔3, 8↔4, 8↔2 | `[3, 5, 4, 2, 8]` |
| 2 | 5↔4, 5↔2 | `[3, 4, 2, 5, 8]` |
| 3 | 4↔2 | `[3, 2, 4, 5, 8]` |
| 4 | 3↔2 | `[2, 3, 4, 5, 8]` ✓ |

### Complexity Analysis

**Time Complexity:**

| Case | Time | Explanation |
|------|------|-------------|
| Best | O(n) | Already sorted → 1 pass, no swaps, exits early[cite: 11] |
| Average | O(n²) | Roughly half the pairs need swapping[cite: 11] |
| Worst | O(n²) | Reverse sorted → every pair swaps, no early exit[cite: 11] |

**Space Complexity:** O(1) — only uses a few extra variables[cite: 11].

**Stable:** Yes — only swaps adjacent elements when strictly out of order[cite: 11].

### Benchmark Results (CPU and Memory)

*Tested via Python `time` and `tracemalloc` modules.*

| n | Best CPU (s) | Worst CPU (s) | Random CPU (s) | Memory Peak (KB) |
|---|---|---|---|---|
| 1,000 | 0.0062 | 0.3537 | 0.1770 | ~0.09 |
| 2,000 | 0.0003 | 0.5730 | 0.4675 | ~0.00 |
| 5,000 | 0.0008 | 3.5810 | 1.8540 | ~0.00 |

> Bubble sort also demonstrates O(n²) time scaling. Notice that Bubble Sort's worst-case for n=1000 (0.35s) is noticeably slower than Insertion Sort's worst-case (0.15s) due to the higher number of write operations (swaps).

---

## 4. Comparison

| Feature | Insertion Sort | Bubble Sort |
|---|---|---|
| **Best Case** | O(n) | O(n) |
| **Average Case** | O(n²) | O(n²) |
| **Worst Case** | O(n²) | O(n²) |
| **Space Workload**| O(1) | O(1) |
| **Stable** | ✅ Yes | ✅ Yes |
| **Real-world CPU**| **Faster on average** ✅ | Slower due to heavy swaps |

### When to Use Which?

- **Insertion Sort:** Highly recommended for small datasets or data that is already nearly sorted.
- **Bubble Sort:** When data is already nearly sorted, because it can finish in O(n)[cite: 11]. Generally avoided in real-world software due to poor performance compared to Insertion Sort.
- **Neither:** For large data — use Quick Sort, Merge Sort, or Heap Sort instead[cite: 11].

---

## 5. Conclusion

Both algorithms operate with an O(n²) time complexity on average, making them unsuitable for massive datasets[cite: 11]. However, both algorithms are highly memory-efficient (O(1) space). Between the two, Insertion Sort is definitively the better algorithm for practical use, as demonstrated by the benchmark test times showing significantly lower CPU workloads for average and worst-case scenarios.

---

## 6. References

1. Dr. Coşkun Şahin, Algorithm Analysis Midterm Assignment Sheet, Istanbul Esenyurt University, 2026.
2. Cormen, T. H. et al. *Introduction to Algorithms* (4th ed.). MIT Press, 2022[cite: 11].

---

## 7. AI Usage Statement

"Gemini 1.5 Pro was used in the Code Generation, Documentation, and Report Writing section of this product[cite: 9]. The tool was utilized via the prompt 'Help create sorting algorithm implementations, benchmark tests for CPU and memory, and format the project report for the Algorithm Analysis course assignment' for the purpose of code generation, algorithm analysis, documentation, and text structuring[cite: 9]. The output generated has been reviewed and verified by me for technical accuracy, safety, and originality[cite: 9]. I bear full responsibility for the work[cite: 9]."