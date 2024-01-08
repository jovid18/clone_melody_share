import random

def generate_lotto_numbers():
    """Generate a random set of 6 unique lotto numbers between 1 and 45"""
    return sorted(random.sample(range(1, 46), 6))
