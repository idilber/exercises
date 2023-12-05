def median(lst):
  new_list = sorted(lst)
  if len(new_list) %2 == 0:
    mid = len(new_list)/2 -1
    mid_2 = len(new_list)/2
    avrg = (new_list[mid] + new_list[mid_2]) / 2
    return avrg
  else:
    index = len(new_list)//2
    return new_list[index]
  
median([1,2,3,4,5,6,7])
