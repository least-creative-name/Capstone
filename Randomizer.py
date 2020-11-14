import random

def randomise_uniform_float(min_max , num_variants):
    result = []
    min_val = min_max[0]
    max_val = min_max[1]
    for i in range(num_variants):
        result.append(random.uniform(min_val, max_val))
    return result

def return_ranges_list(rangelist , num_variants):
    result = []
    length = len(rangelist)
    num_copies = num_variants // length
    fixup = num_variants % length
    for i in range(num_copies):
        result+=rangelist
    result+=rangelist[0:fixup]
    return result 

def randomise_uniform_int(min_max , num_variants):
    result = []
    min_val = min_max[0]
    max_val = min_max[1]
    for i in range(num_variants):
        result.append(random.randrange(min_val, max_val))
    return result

def randomise_rand_and_range(problems , num_variants):
    for problem in problems:
        for rand in problem.rands:
            rand.set_value(randomise_uniform_int([rand.get_min(),rand.get_max()] , num_variants))
        for ranges in problem.ranges:
            ranges.set_value(return_ranges_list(ranges.get_values() , num_variants))
    return problems

