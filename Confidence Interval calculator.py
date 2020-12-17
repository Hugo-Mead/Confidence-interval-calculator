import numpy as np
import pandas as pd
# Importing packages for later use

print("This is a calculator to present a 95% confidence interval of your data")
# This tells the user what this program does


def bootstrap_replicate_1d(data, func):
    bs_sample = np.random.choice(data)
    return func(bs_sample)
## This is a single bootsrap where the data you input is randomly picked out into bs_sample and then is caluclated
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
   
    fish_wt = fish_data[fish_data.genotype == "wt"].bout_length
    mean_wt = np.mean(np.array(fish_wt))
    
    fish_mut = fish_data[fish_data.genotype == "mut"].bout_length
    mean_mut = np.mean(np.array(fish_mut))
   
    bs_reps_wt = draw_bs_reps(fish_wt, np.mean, size=10000)
    bs_reps_mut = draw_bs_reps(fish_mut, np.mean, size=10000)
    
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
    
    print("""
    Wild type zebrafish: mean length = {0:.3f} min., confidence interval = [{1:.1f}, {2:.1f}] min.
    Mutant zebrafish: mean = {3:.3f} min., confidence interval = [{4:.1f}, {5:.1f}] min.
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))

# If program is imported then this condition will return as false and you will manually have to call each function. 
# But if it isn't then main will guide you through each function as intended.
    


#def main():
 #   
  #  data = get_data()
   # read_data = collect_data(data)
    #means = get_averages(read_data)
   # CI = get_CI(means)
    #get_BootStraps(CI)
# Main() is the entry point for the program and guides the program from each definition to another.

#def get_data():
 #   data_frame = input(print("Input your data as a csv file here"))
  #  data_frame
   # return data_frame
# get_data simply takes the dataframe that the user inputs
    
#def collect_data(data):
 #   mod_data_frame = pd.read_csv(data, skiprows=4)
  #  print("Reading dataframe\nData has been read")
   # mod_data_frame
    #return(mod_data_frame)
# Reads in the data
    
#def get_averages(read_data):
 #   fish_wt = fish_data[fish_data.genotype == "wt"].bout_length
  #  mean_wt = np.mean(np.array(fish_wt))
    #mean_wt
#
 #   fish_mut = fish_data[fish_data.genotype == "mut"].bout_length
  #  mean_mut = np.mean(np.array(fish_mut))
   # mean_mut
# Gets the mean value of fish lengths

#def get_CI(means):
 #   conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
  #  conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
# Gets a 95% confidence interval of data
    
#def get_BootStraps():
 #   draw_bs_reps()
# Uses pre defined bootstrap function to replicate data
