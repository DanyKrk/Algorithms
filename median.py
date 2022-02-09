def median(heap_max, heap_min):
  n_min = len(heap_min)
  n_max = len(heap_max)
  if n_min == n_max:
    median = (heap_max[0] + heap_min[0])/2
    heap_max[0], heap_max[n_max - 1] = heap_max[n_max - 1], heap_max[0]
    heapify_max(heap_max, 0)
    #usuwam ostatni element heap_max, np.: heap_max.pop(n_max-1)
    heap_min[0], heap_min[n_min - 1] = heap_min[n_min -1], heap_min[0]
    heapify_min(heap_min, 0)
    #usuwam ostatni element heap_min
    return median
  elif n_min < n_max:
    median = heap_max[0]
    heap_max[0], heap_max[n_max - 1] = heap_max[n_max - 1], heap_max[0]
    #usuwam ostatni element heap_max
    heapify_max(heap_max, 0)
    return median
  else:
    median - heap_min[0]
    heap_min[0], heap_min[n_min - 1] = heap_min[n_min -1], heap_min[0]
    #usuwam ostatni element heap_min
    heapify_min(heap_min, 0)
    return median

def _insert(heap_max, heap_min, elem):
  if elem <= heap_max[0]:
    if len(heap_max) <= len(heap_min):
      insert(heap_max, elem)
    else:
      temp = heap_max[0]
      heap_max[0] = elem
      heapify(heap_max, 0)
      insert(heap_min, temp)
  else:
    if len(heap_min) <= len(heap_max):
      insert(heap_min, elem)
    else:
      temp = heap_min[0]
      heap_min[0] = elem
      heapify(heap_min, 0)
      insert(heap_max, temp)