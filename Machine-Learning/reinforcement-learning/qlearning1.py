import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("MountainCar-v0")

# valid values for LEARNING_RATE and DISCOUNT are [0,1]
LEARNING_RATE = 0.1
DISCOUNT = 0.95         # measure of how important is future reward vs current reward 

#EPISODES = 25000
#SHOW_EVERY = 2000   # show us a status update every 2000 episodes
EPISODES = 4000
SHOW_EVERY = 500   # show us a status update every 500 episodes

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)               # number of possible actions

# our discrete observation space size
#DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
DISCRETE_OS_SIZE = [40] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

print(discrete_os_win_size)
# [0.09 0.007]
# means that the size of the "bucket" for first dimension is 0.09
#            and size of the "bucket" for second dimension is 0.007
# We do this so the number of combinations (1st and 2nd dimensions) is manageable

# Introduce a degree of randomness; epsilon indicates how much "exploring" we want to do along the way
epsilon = 0.1   # range is [0,1]
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES // 2    # integer division

epsilon_decay_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)

# initialize the Q table
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))     # since our reward starts at -1.0, range [-2,0] seems reasonable
print(q_table.shape)

# Add per-episode rewards
ep_rewards = []
aggr_ep_rewards = {'ep': [], 'avg': [], 'min': [], 'max': []}
# ep is episode (x-axis value)
# avg is 'trailing' average
# min is worst performance
# max is best performance


# We need to convert the continuous state that we get back from env.reset and env.step
# to a discrete state. Here is a helper function:
def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))



for episode in range(EPISODES):
    episode_reward = 0
    if episode % SHOW_EVERY == 0:
        print(episode)
        render = True
    else:
        render = False

    discrete_state = get_discrete_state(env.reset())

    """
    print(discrete_state)
    # Print our starting values of the q_table (these are random based on our np.random.uniform)
    print(q_table[discrete_state])  # we can look up this discrete_state in the q_table (because discrete_state is a tuple)
    print(np.argmax(q_table[discrete_state]))   # gives us the *index* of the max value element
    """

    done = False
    while not done:
        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])         # do actions in the usual way
        else:
            action = np.random.randint(0, env.action_space.n)   # random action

        new_state, reward, done, _ = env.step(action)
        episode_reward += reward
        #print(reward, new_state)    # reward starts at -1.0 and becomes 0.0 when we reach the flag
        new_discrete_state = get_discrete_state(new_state)
        if render:
            env.render()
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action, )]
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state+(action, )] = new_q      # update our q_table based on the results of the action we took
        elif new_state[0] >= env.goal_position:
            print(f"We made it on episode {episode}")
            q_table[discrete_state+(action, )] = 0

        discrete_state = new_discrete_state

    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

    ep_rewards.append(episode_reward)

    if not episode % SHOW_EVERY:
        average_reward = sum(ep_rewards[-SHOW_EVERY:])/len(ep_rewards[-SHOW_EVERY:])
        aggr_ep_rewards['ep'].append(episode)
        aggr_ep_rewards['avg'].append(average_reward)
        aggr_ep_rewards['min'].append(min(ep_rewards[-SHOW_EVERY:]))
        aggr_ep_rewards['max'].append(max(ep_rewards[-SHOW_EVERY:]))
        print(f"Episode: {episode}  avg: {average_reward}  min: {min(ep_rewards[-SHOW_EVERY:])}  max: {max(ep_rewards[-SHOW_EVERY:])}")

    if episode % 10 == 0:
        np.save(f"qtables/{episode}-qtable.npy", q_table)

env.close()

plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label="avg")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label="min")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label="max")
plt.legend(loc=4)
plt.show()




# FORMULA:
#
# Qnew(s,a) = (1-alpha) * Q(s,a) + alpha * ( r + gamma * maxQ(s',a) )
#
# (s,a) is actually (s , a )   and    s' is s
#                     t   t                  t+1
#
# alpha : learning rate
# r : reward
# gamma : discount factor
# maxQ(s    , a) : estimate of optimal future value
#       t+1
# ( r + gamma * maxQ(s',a) ) : learned value


