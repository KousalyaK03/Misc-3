# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach:
# 1. First, count the total number of nodes in the linked list.
# 2. Reverse nodes in groups of `k` while keeping track of the previous and next pointers.
# 3. If there are fewer than `k` nodes left, leave them unchanged.
# 4. Use iterative reversal to achieve O(1) space complexity.
# 5. Connect the reversed segments properly to maintain the list structure.

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Count the total number of nodes
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        total_nodes = count_nodes(head)
        dummy = ListNode(0)  # Dummy node to help manage head changes
        dummy.next = head
        prev_group = dummy  # Previous group's last node
        current = head

        # Step 2: Reverse nodes in groups of k
        while total_nodes >= k:
            prev = None
            tail = current  # The tail of the reversed group (will become the last node after reversal)

            # Reverse k nodes
            for _ in range(k):
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            # Step 3: Connect reversed group properly
            prev_group.next = prev  # Connect previous group's end to new group's start
            tail.next = current  # Connect the last node of the reversed group to the next part
            prev_group = tail  # Move prev_group pointer to the end of the current group

            # Reduce total_nodes count by k
            total_nodes -= k

        return dummy.next  # The new head of the list

# Time Complexity: O(N), where N is the number of nodes in the linked list.
# - Each node is visited and reversed once.

# Space Complexity: O(1), since we only use a few extra pointers for in-place reversal.
