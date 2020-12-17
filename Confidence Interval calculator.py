# Final Data Science assignment 
# Hugo mead - 19419556
# GitHub account 'Hugo-Mead'

import numpy as np
import pandas as pd
# Importing packages for later use

print("This is a calculator to present a 95% confidence interval of your data")
# This tells the user what this program does

def bootstrap_replicate_1d(data, func):
    bs_sample = np.random.choice(data)
    return func(bs_sample)

## This is a single bootsrtap where the data you input is randomly picked out into bs_sample and then is caluclated
## by a function of your choice.

def draw_bs_reps(data, func, size=1):
    bs_replicates = np.empty(size) ### This creates and empty array to put your bootstraps in
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)
    return bs_replicates

## This repeats boostrap_replicate_1d a "size" amount of times
# draw_bs_reps is the simulated number of trials

if __name__ == '__main__':
    fish_data = pd.read_csv('gandhi_et_al_bouts.csv',skiprows=4)
    print("fish_data has been read into the program, skipped the first 4 lines for data convinience")

    # Reads in the data
   
    fish_wt = fish_data[fish_data.genotype == "wt"].bout_length
    mean_wt = np.mean(np.array(fish_wt))
    print("fish_data means have been compiled")
   
    fish_mut = fish_data[fish_data.genotype == "mut"].bout_length
    mean_mut = np.mean(np.array(fish_mut))
    
    # Gets the mean value of fish lengths
    
    bs_reps_wt = draw_bs_reps(fish_wt, np.mean, size=10000)
    bs_reps_mut = draw_bs_reps(fish_mut, np.mean, size=10000) 
    print("fish_data has been bootstrapped 10000 times")

    # Uses the bootstrap function definied earlier to replicate 10000 trials
    
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
    
    # Gets a 95% confidence interval of the data set
    
    print("""
    Wild type zebrafish: mean length = {0:.3f} min., confidence interval = [{1:.1f}, {2:.1f}] min.
    Mutant zebrafish: mean = {3:.3f} min., confidence interval = [{4:.1f}, {5:.1f}] min.
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))
    
    # Gets a 95% confidence interval of data
    
    print("A 95% confidence interval has been placed")
    print("Program is complete")
