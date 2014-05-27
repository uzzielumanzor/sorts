import time
import random
import math

def generador(cantidad):
    lista = range(cantidad)
    random.shuffle(lista)

    return lista

def buble_sort(alist):
    
    for passnum in range(len(alist)-1,0,-1):
        
        for i in range(passnum):
            
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    
    return alist

def insertion_sort(alist):
    
    for index in range(1,len(alist)):    
        currentvalue = alist[index]
        position = index
        
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
    
    return alist

def selection_sort(alist):

    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        
        for location in range(1,fillslot+1):
            
            if alist[location]>alist[positionOfMax]:
               positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    
    return alist


def merge_sort(alist):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=0
        j=0
        k=0
        
        while i<len(lefthalf) and j<len(righthalf):
        
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
        
            else:
                alist[k]=righthalf[j]
                j=j+1
        
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    return alist


def heap_sort(lst):

  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break

def quick_sort(L, first, last):
    i = first
    j = last    
    pivote = (L[i] + L[j]) / 2

    while i < j:
        while L[i] < pivote:
            i+=1
        while L[j] > pivote:
            j-=1
        if i <= j:
            x = L[j]
            L[j] = L[i]
            L[i] = x
            i+=1
            j-=1

    if first < j:
        L = quick_sort(L, first, j)
    if last > i:
        L = quick_sort(L, i, last)

    return L

def radix_sort( aList ):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1
 
    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range( RADIX )]
 
        for  i in aList:
            tmp = i / placement
            buckets[tmp % RADIX].append( i )
            if maxLength and tmp > 0:
                maxLength = False
 
        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1
 
        placement *= RADIX


def main():
    valores = [10, 100, 1000, 10000]
    buble = []
    insertion = []
    selection = []
    merge = []
    heap = []
    quick = []
    radix = []
    for i in valores:
        for j in xrange(10):
            lista = generador(i)
            print "Tiempo con ", i, " elementos"
            start_time = time.time()
            buble_sort(lista)
            tiempo = time.time() - start_time
            buble.append(tiempo)
            print "bublesort: ", tiempo, "segundos"
    
            start_time = time.time()
            insertion_sort(lista)
            tiempo = time.time() - start_time
            insertion.append(tiempo)
            print "insertionsort: ", tiempo, "segundos"
    
            start_time = time.time()
            selection_sort(lista)
            tiempo = time.time() - start_time
            selection.append(tiempo)
            print "selectionsort: ", tiempo, "segundos"
    
            start_time = time.time()
            merge_sort(lista)
            tiempo = time.time() - start_time
            merge.append(tiempo)
            print "mergesort: ", tiempo, "segundos"
    
            start_time = time.time()
            heap_sort(lista)
            tiempo = time.time() - start_time
            heap.append(tiempo)
            print "heapsort: ", tiempo, "segundos"
    
            start_time = time.time()
            quick_sort(lista, 0, len(lista) - 1)
            tiempo = time.time() - start_time
            quick.append(tiempo)
            print "quicksort: ", tiempo, "segundos"

            start_time = time.time()
            radix_sort(lista)
            tiempo = time.time() - start_time
            radix.append(tiempo)
            print "radixsort: ", tiempo, "segundos"

        print 
        print "promedio bublesort: ", sum(buble)/len(buble)
        print "promedio insertionsort: ", sum(insertion)/len(insertion)
        print "promedio selectionsort: ", sum(selection)/len(selection)
        print "promedio mergesort: ", sum(merge)/len(merge)
        print "promedio heapsort: ", sum(heap)/len(heap)
        print "promedio quicksort: ", sum(quick)/len(quick)
        print "promedio radixsort: ", sum(radix)/len(radix)


if __name__ == "__main__":
    main()
