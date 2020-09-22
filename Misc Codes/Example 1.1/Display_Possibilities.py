import numpy as np
from itertools import product as counter
Avg_reward=0
n=0


for COIN in counter([0,1],repeat=5): #Generates all possibile combinations of a vector of 0,1 of length 'repeat'
	r=1 #the reward to be obtained after a toss
	Tot_Reward=0 #the sum of all rewards obtained in 'repeat' number of tosses
	reward_sequence=[] #array to store the rewards we got as the coin was being tossed
	first_head=True 
	after_first_head=False
	Yn=0
	toss_index=0
	for toss in COIN:
		if (toss==1 and first_head): #if we get heads
			after_first_head=True
			first_head=False
			r=1
		elif after_first_head:
			if toss==0:
				r=2*r
			else:
				r=2*r
			after_first_head=False
		elif toss==1:
			r=2*r #if r!=0 else 1  #reward is 2 times the earlier reward. If r is 0, make it 1(initial reward)				
		else:
			r=r
			next_head=False
		if toss_index>1:
			Yn=r
		Yn=(2**toss)*Yn
		toss_index+=1
		Tot_Reward=r+Tot_Reward   #Summing up the rewards
		reward_sequence.append(r)
	y=0
	index=0
	for rr,x in zip(reward_sequence,COIN):
		if index>1:
			y=rr
		y=(2**x)*y
		index+=1
	Avg_reward=(Tot_Reward+Avg_reward*n)/(n+1)
	print("Coin toss: ",COIN," Reward sequence ", reward_sequence," Total reward is ",Tot_Reward, y)
	n=n+1 #Counter to hold how many experiment trials have occured
import fractions
print("Average of all rewards obtained is", Avg_reward, "or",fractions.Fraction(Avg_reward))
print(Yn)



