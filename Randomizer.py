import random

def randomise_uniform_float(min_max , num_variants):
    result = []
    min_val = min_max[0]
    max_val = min_max[1]
    for i in range(num_variants):
        result.append(random.uniform(min_val, max_val))
    return result

def randomise_uniform_int(min_max , num_variants):
    result = []
    min_val = min_max[0]
    max_val = min_max[1]
    for i in range(num_variants):
        result.append(random.randrange(min_val, max_val))
    return result

def randomise_rand_and_range(problems , num_variants):
    min_max = []
    min_max.append(1)
    min_max.append(7)
    randomise_uniform_int(min_max , num_variants) 
    return None

