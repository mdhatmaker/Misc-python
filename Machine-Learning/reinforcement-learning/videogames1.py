import tensorflow as tf
import numpy as np
import retro

from skimage import transform   # help us to preprocess the frames
from skimage.color import rgb2gray  # help us to gray our frames

import matplotlib.pyplot as plt     # display graphs

from collections import deque       # ordered collection with ends

import random

import warnings
warnings.filterwarnings('ignore')

### https://romsmania.cc/roms/atari-2600

# Create our environment
#env = retro.make(game='SpaceInvaders-Atari2600')
#env = retro.make(game='Airstriker-Genesis')
env = retro.make(game='Breakout-Atari2600')

print("The size of our frame is: ", env.observation_space)
print("The action size is : ", env.action_space.n)

# Here we create an hot encoded version of our actions
# possible_actions = [[1,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0]...]
possible_actions = np.array(np.identity(env.action_space.n, dtype=int).tolist())

# '-Nes', '-Genesis', '-Snes', '-GameBoy', '-Genesis', '-Sms', '-Atari2600'
games = retro.data.list_games(inttype=retro.data.Integrations.ALL)
for g in games:
    if g.endswith('-Atari2600'): print(g)

