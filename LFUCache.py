#! _*_ encoding=utf-8 _*_

from doublelinklist import DoubleLinkedList,Node

class LFUNode(Node):
	def __init__(self,key,value):
		self.freq = 0
		super(LFUNode,self).__init__(key,value)

class LFUCache(object):
	def __init__(self,capacity):
		self.capacity = capacity
		self.map = {}
		self.freq_map = {}      #key:freq  value:freq duiyingde double link list		
		self.size = 0

	def __update_freq(self,node):
		freq = node.freq
		#shanchu
		node = self.freq_map[freq].remove(node)
		if self.freq_map[freq].size ==0:
			del self.freq_map[freq]
		#gengxin
		freq += 1
		node.freq = freq
		if freq not in self.freq_map:
			self.freq_map[freq] = DoubleLinkedList()
		self.freq_map[freq].append(node)
		

	def get(self,key):
		if key not in self.map:
			return -1
		node = self.map.get(key)
		self.__update_freq(node)
		return node.value

	def put(self,key,value):
		if self.capacity == 0:
			return
		
		#huancun mingzhong
		if key in self.map:
			node = self.map.get(key)
			node.value = value
			self.__update_freq(node)
		else:
			if self.capacity == self.size:
				min freq = min(self.freq_map)
				node = self.freq_map[min_freq].pop()
				del self.map[node.key]
				self.size -= 1
			node = LFUNode(key,value)
			node.freq = 1
			self.map[key] = node
			if node.freq not in self.freq_map:
				self.freq_map[node.freq] = DoubleLinkedList()
			ndoe = self.freq_map[node.freq].append(node)
			self.size += 1
	def print(self):
		for k,v in slef.freq_map.items():
			print('Freq = %d' % k)
			self.freq_map[k].print()	
