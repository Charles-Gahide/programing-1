# write your code here
from math import ceil 
def internet_costs(duration_in_seconds,cost_per_block):
    block_duration=360
    blocks_amount=ceil(duration_in_seconds/block_duration)
    return(blocks_amount*cost_per_block)
    
    
    