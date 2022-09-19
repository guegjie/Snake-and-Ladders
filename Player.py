import Window
#ihioh

class Player:
    def __init__(self, name="player", position=1, colour="blue", size=[10,10]):
        self.Position = position
        self.Colour = colour

    def draw(self, window):
        print(self.binary_search(window.Positions, 0, len(window.Postions), self.Position))
    
    def binary_search(self, arr, low, high, x):
 
        # Check base case
        if high >= low:
 
            mid = (high + low) // 2
 
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
 
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)
 
            # Else the element can only be present in right subarray
            else:
                return binary_search(arr, mid + 1, high, x)
 
        else:
            # Element is not present in the array
            return -1