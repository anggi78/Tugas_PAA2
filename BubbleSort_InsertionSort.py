import time


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


# Menghasilkan array dengan elemen acak
arr = [64, 34, 25, 12, 22, 11, 90, 9, 100, 37, 78]

# Mengukur waktu eksekusi Bubble Sort
start_time = time.time()
sorted_arr_bubble = bubble_sort(arr.copy())
end_time = time.time()
bubble_sort_time = end_time - start_time

# Mengukur waktu eksekusi Insertion Sort
start_time = time.time()
sorted_arr_insertion = insertion_sort(arr.copy())
end_time = time.time()
insertion_sort_time = end_time - start_time

# Menampilkan hasil dan perbandingan waktu eksekusi
print("Array awal:", arr)
print("Hasil Bubble Sort:", sorted_arr_bubble)
print("Waktu eksekusi Bubble Sort:", bubble_sort_time)
print("Hasil Insertion Sort:", sorted_arr_insertion)
print("Waktu eksekusi Insertion Sort:", insertion_sort_time)

# Membandingkan keoptimalan algoritma
if bubble_sort_time < insertion_sort_time:
    print("Bubble Sort lebih optimal.")
elif insertion_sort_time < bubble_sort_time:
    print("Insertion Sort lebih optimal.")
else:
    print("Kedua algoritma memiliki kinerja yang sama.")
