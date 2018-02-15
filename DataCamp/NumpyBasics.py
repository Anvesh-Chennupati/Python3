positions = ['gk','f','a','d','gk','gk','f','a','d']
heights = [178,125,167,145,188,192,167,188,167]

import numpy as np

np_positions = np.array(positions)
np_heights = np.array(heights)
gk_heights = np.array(np_heights[np_positions=='gk'])
other_height = np.array(np_heights[np_positions!= 'gk'])
gk_mean = np.mean(gk_heights)
other_mean = np.mean(other_height)

if gk_mean > other_mean :
    print('\n Goal Keepers mean height is greater than Other team players')

else :
    print('\n Goal Keepers mean height is not greater than other team players')
