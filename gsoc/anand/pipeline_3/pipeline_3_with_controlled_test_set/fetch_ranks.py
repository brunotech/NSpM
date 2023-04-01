from tqdm import tqdm
import numpy as np

def fetch_ranks(filename='../utility/wikidata.rank'):
    """
    The function loads rank from a supplied position.
    """
    sub = open(filename,'r').readlines()
    print("Loading Rankings")
    return {val.split('\t')[0]: float(val.split('\t')[1]) for val in tqdm(sub)}

if __name__ == "__main__":
    fetch_ranks()

