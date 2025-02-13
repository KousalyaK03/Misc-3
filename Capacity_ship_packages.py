# Approach:
# 1. We use **binary search** to determine the minimum ship capacity required to ship all packages within the given days.
# 2. The **minimum capacity** is the weight of the heaviest package (since we must ship it).
# 3. The **maximum capacity** is the sum of all weights (if we ship everything in one day).
# 4. We perform **binary search** between these values to find the smallest capacity that allows shipping within the required days.
# 5. A helper function determines if a given capacity can complete the shipment within the given days.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Step 1: Define the search range
        left, right = max(weights), sum(weights)  # Min capacity = max package, Max capacity = sum of all packages

        def canShip(capacity):
            """Check if we can ship all packages within 'days' using the given capacity."""
            current_weight = 0
            required_days = 1  # Start with 1 day

            for weight in weights:
                if current_weight + weight > capacity:
                    # If adding this package exceeds capacity, start a new day
                    required_days += 1
                    current_weight = 0  # Reset daily weight

                current_weight += weight  # Add package to current day's load

                if required_days > days:
                    return False  # If more than 'days' are needed, return False

            return True  # Successfully shipped within 'days'

        # Step 2: Perform binary search to find the minimum capacity
        while left < right:
            mid = (left + right) // 2  # Test mid capacity
            if canShip(mid):
                right = mid  # Try a smaller capacity
            else:
                left = mid + 1  # Increase capacity

        # Step 3: Return the minimum valid capacity
        return left

# Time Complexity: O(N log M), where:
# - N = number of packages (for checking a given capacity).
# - M = range of possible capacities (sum(weights) - max(weights)).
# - Binary search runs in O(log M), and each check runs in O(N), giving O(N log M).

# Space Complexity: O(1), since we use only a few extra variables.
