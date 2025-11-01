def radix_base(values_to_sort, base):
    if not values_to_sort or base < 2:
        raise ValueError()

    for val in values_to_sort:
        if not isinstance(val, int) or val < 0:
            raise ValueError()

    max_val = max(values_to_sort)

    exponent = 1

    new_list = values_to_sort[:]

    while max_val // exponent > 0:
        buckets = [[] for _ in range(base)]

        for val in new_list:
            digit = (val // exponent) % base
            buckets[digit].append(val)

        new_list = [num for bucket in buckets for num in bucket]

        exponent *= base

    return new_list


# print(radix_base([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1, 8900, 992], 2))

# print(divmod(192, 10))
