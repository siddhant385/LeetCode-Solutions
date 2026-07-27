class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        x_val_to_max_y = {}
        for i in range(n):
            current_x = x[i]
            current_y = y[i]
            if current_x not in x_val_to_max_y or current_y > x_val_to_max_y[current_x]:
                
                x_val_to_max_y[current_x] = current_y
        if len(x_val_to_max_y) < 3:
            return -1
        sorted_max_y_values = sorted(x_val_to_max_y.values(), reverse=True)        
        max_sum = sorted_max_y_values[0] + sorted_max_y_values[1] + sorted_max_y_values[2]
        
        return max_sum
