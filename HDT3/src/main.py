import random
import sorts
import timeit

def generatorRandom():
    array = [random.randint(1, 10000) for j in range(10)]
    return array

def run_algorithms():
    numerosAleatorios = generatorRandom()
    ascDescBoolean = False

    start_time = timeit.default_timer()
    sorts.quickSort(numerosAleatorios, 0, len(numerosAleatorios) - 1, ascDescBoolean)
    print("quickSort:", timeit.default_timer() - start_time, "seconds")

    start_time = timeit.default_timer()
    sorts.gnomeSort(numerosAleatorios, ascDescBoolean)
    print("gnomeSort:", timeit.default_timer() - start_time, "seconds")

    start_time = timeit.default_timer()
    sorts.heapSort(numerosAleatorios, ascDescBoolean)
    print("heapSort:", timeit.default_timer() - start_time, "seconds")

    start_time = timeit.default_timer()
    sorts.mergeSort(numerosAleatorios, ascDescBoolean)
    print("mergeSort:", timeit.default_timer() - start_time, "seconds")

    start_time = timeit.default_timer()
    sorts.radixSort(numerosAleatorios, ascDescBoolean)
    print("radixSort:", timeit.default_timer() - start_time, "seconds")

    start_time = timeit.default_timer()
    sorts.selectionSort(numerosAleatorios, ascDescBoolean)
    print("selectionSort:", timeit.default_timer() - start_time, "seconds")

    start_time = timeit.default_timer()
    sorts.shellSort(numerosAleatorios, ascDescBoolean)
    print("shellSort:", timeit.default_timer() - start_time, "seconds")

run_algorithms()