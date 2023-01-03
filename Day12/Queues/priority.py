class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])
	def isEmpty(self):
		return len(self.queue) == 0

	def insert(self, data): # 12
		self.queue.append(data) # [12,1,14,7]

	def delete(self):
		try: 
			max_val = 0
			for i in range(len(self.queue)): # [12,1,14,7]
				if self.queue[i]  > self.queue[max_val]: # self.queue[2] > self.queue[0]
														#  14 > 12 
					max_val = i #i=2 , max_val=2
			item = self.queue[max_val] # self.queue[2] 
			del self.queue[max_val] #self.queue[2]  --> [12,1,7]
			return item
		except IndexError:
			print()
			exit()


myQueue = PriorityQueue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(7)
print(myQueue)	 # [12,1,14,7]	
myQueue.delete() # --> It will delete the value with highest priority / highest value
print(myQueue)	# [12,1,7]