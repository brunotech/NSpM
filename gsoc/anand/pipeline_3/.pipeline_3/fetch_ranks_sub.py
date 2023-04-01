from tqdm import tqdm
import numpy as np

def fetch_ranks(filename='part-r-00000'):
    sub = open(filename,'r').readlines()
    print("Loading Rankings")
    return {
        val.split('\t')[0]
        .strip()[1:-1]
        .strip(): float(val.split('\t')[-2].split('"')[1])
        for val in tqdm(sub)
    }

if __name__ == "__main__":
    fetch_ranks()

