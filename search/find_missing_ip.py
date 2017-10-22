def find_missing_ip(ifs):
    NUM_BUCKET = 1 << 16  # 2 ^ 16
    counter = [0] * NUM_BUCKET
    for x in map(int, ifs):
        # upper_part_x is the index ranging from [0 ... (2^16)-1] that represents the 16 MSBs.
        #   each MSB index can count up to 2^16 times. In total, this is 2^32, which is the max size of a IPv4 address.
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    BUCKET_CAPACITY = 1 << 16  # 2 ^ 16

    candidate_bucket = next(
        i for i, c in enumerate(counter) if c < BUCKET_CAPACITY)

    #  reset stream position to the start
    ifs.seek(0)

    #  bit_vec represents the 16 LSBs, ranging from [0 ... 2^16]. an index with value 0 means it is not recorded yet.
    bit_vec = [0] * BUCKET_CAPACITY
    for x in map(int, ifs):
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            #  we record the 16 LSBs of this ip address using a mask
            lower_part_x = ((1 << 16) - 1) & x
            bit_vec[lower_part_x] = 1

    for i, v in enumerate(bit_vec):
        #  i represents the 16 LSB
        #  v is 0 or 1, if 0 then that means not taken.
        if v == 0:
            #  candidate_bucket represents 0 ... (2^16)-1. Shift it left 16 times to represent the 16 MSB.
            #  Doing OR on the 16 MSB and 16 LSB gets us the 32 bit IPv4 address.
            return (candidate_bucket << 16) | i
