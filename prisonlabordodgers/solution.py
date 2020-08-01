def solution(x, y):
  matrix = [x,y]  
  all_values = [y for x in matrix for y in x]  
  unique_values = list(set(all_values))  
  matched_values = [x for x in unique_values if all_values.count(x) % 2 == 0]  
  missing_values = [x for x in unique_values if x not in matched_values ]  
  return missing_values[0]
