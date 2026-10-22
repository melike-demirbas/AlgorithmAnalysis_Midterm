import time
import random
import tracemalloc

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def run_performance_test():
    sizes = [1000, 2000, 5000, 10000]
    
    print("=== BUBBLE SORT PERFORMANS TESTI ===")
    print(f"{'Boyut (n)':<10} | {'Durum':<10} | {'Sure (saniye)':<15} | {'Bellek (KB)':<15}")
    print("-" * 57)

    for size in sizes:
        # 1. Best Case (Zaten Sıralı)
        best_data = list(range(size))
        tracemalloc.start()
        start_time = time.perf_counter()
        bubble_sort(best_data)
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{size:<10} | {'Best':<10} | {end_time - start_time:<15.6f} | {peak / 1024:<15.2f}")

        # 2. Worst Case (Ters Sıralı)
        worst_data = list(range(size, 0, -1))
        tracemalloc.start()
        start_time = time.perf_counter()
        bubble_sort(worst_data)
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{size:<10} | {'Worst':<10} | {end_time - start_time:<15.6f} | {peak / 1024:<15.2f}")

        # 3. Average Case (Rastgele)
        avg_data = [random.randint(0, 10000) for _ in range(size)]
        tracemalloc.start()
        start_time = time.perf_counter()
        bubble_sort(avg_data)
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{size:<10} | {'Average':<10} | {end_time - start_time:<15.6f} | {peak / 1024:<15.2f}")
        print("-" * 57)

if __name__ == "__main__":
    # Önce küçük bir demo ile algoritmanın çalıştığını gösterelim
    demo_arr = [5, 3, 8, 4, 2]
    print("Demo Öncesi:", demo_arr)
    print("Demo Sonrası:", bubble_sort(demo_arr.copy()))
    print("\n")
    
    # Sonra performans testini başlatalım
    run_performance_test()