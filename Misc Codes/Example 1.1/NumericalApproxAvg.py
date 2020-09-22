import numpy as np
from scipy.stats import bernoulli
def generate_trials(p,n):
	X=[]
	for _ in range(n):
		x=bernoulli.rvs(p) #Generate a 1 or a 0 with probability p
		X.append(x)		   #Save that 1 or 0 in X
	X=np.asarray(X)		   #Convert it to a numpy array from python list
	return X

Avg_reward=0
for n in range(2048):
	COIN=generate_trials(0.5,10)#Generates a bernoulli trial of 10 coin tosses
	r=0 #the reward to be obtained after a toss
	Tot_Reward=0 #the sum of all rewards obtained in 'repeat' number of tosses
	reward_sequence=[] #array to store the rewards we got as the coin was being tossed
	for toss in COIN:
		if toss==1: #if we get heads
			r=2*r if r!=0 else 1  #reward is 2 times the earlier reward. If r is 0, make it 1(initial reward)
		else:
			r=r 				  #Else keep giving the same reward
		Tot_Reward=r+Tot_Reward   #Summing up the rewards
		reward_sequence.append(r) 
	Avg_reward=(Tot_Reward+Avg_reward*n)/(n+1)
	print("Coin toss: ",COIN," Reward sequence ", reward_sequence," Total reward is ",Tot_Reward)
print("Average of all rewards obtained is ", Avg_reward)