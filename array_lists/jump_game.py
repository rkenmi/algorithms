def can_jump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) <= 1:
        return True

    jumpable_up_to = 0
    for i in range(0, len(nums)):
        if i > jumpable_up_to:
            break

        start = i
        while nums[start] > 0:
            start += nums[start]
            jumpable_up_to = max(jumpable_up_to, start)
            if start >= len(nums) - 1:
                return True

    return False