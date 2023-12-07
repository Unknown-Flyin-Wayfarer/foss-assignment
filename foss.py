def max_area(height):
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        h_left, h_right = height[left], height[right]
        width = right - left
        min_height = min(h_left, h_right)

        current_water = width * min_height
        max_water = max(max_water, current_water)

        # Move pointers towards each other
        if h_left < h_right:
            left += 1
        else:
            right -= 1

    return max_water
height = [1,8,6,2,5,4,8,3,7]
result = max_area(height)
print(result)