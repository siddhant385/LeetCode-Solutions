class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        even_positions = []
        odd_positions = []
    
        for i, num in enumerate(nums):
            if num % 2 == 0:
                even_positions.append(i)
            else:
                odd_positions.append(i)
    
        even_count = len(even_positions)
        odd_count = len(odd_positions)
    
        if abs(even_count - odd_count) > 1:
            return -1
    
        def calculate_moves(start_even):
            total_moves = 0
            for idx, pos in enumerate(even_positions if start_even else odd_positions):
                total_moves += abs(pos - idx * 2)
            return total_moves
    
        if even_count > odd_count:
            return calculate_moves(True)
        elif odd_count > even_count:
            return calculate_moves(False)
        else:
            return min(calculate_moves(True), calculate_moves(False))