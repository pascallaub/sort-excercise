import random
import time

numbers = [random.randint(1, 1000) for i in range(100)]

def bubblesort(arr):
    n = len(arr)    #Bestimmt die Länge der Liste
    for i in range(n):
        swapped = False #Überprüft ob Tausch schon stattgefunden hat
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #Elemente tauschen
                swapped = True
        if not swapped:
            break   #Beendet wenn kein Tausch notwendig
    return arr

def mergesort(arr):
    if len(arr) <= 1:
        return arr      #Nur ein Element, also sortiert
    
    mid = len(arr) // 2     #Bestimmt die Mitte

    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])   #Teilt die Listen in zwei Hälften

    sorted_list = merge(left_half, right_half)
    return sorted_list

def merge(left, right):
    result = []
    i = j = 0   #Zeiger für die linke und rechte Liste

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print("Unsortierte Liste: ", numbers)

bubblesort(numbers)
print("Bubblesort: ", numbers)
start_time = time.time()
bubblesort(numbers.copy())
print("Bubblesort Laufzeit: ", time.time() - start_time)

sorted_numbers = mergesort(numbers)
print("Mergesort: ", sorted_numbers)
start_time1 = time.time()
mergesort(numbers.copy())
print("Mergesort Laufzeit: ", time.time() - start_time)