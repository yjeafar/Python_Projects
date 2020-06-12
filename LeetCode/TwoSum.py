class sol: 
	def twoSum():
		nums = [7,1,5,7] 
		target = 14  
		# listDict = { }
		# indexList = []
		# count = 0
		# for num in range(len(nums)):
		# 	listDict[num] = nums[num]            
		# 	if count > 0:
		# 			for numVal in range(len(nums))[:num]:
		# 				if listDict[numVal] + listDict[num] == target:
		# 					indexList.extend([numVal, num])
		# 					return indexList
		# 	count += 1

		# print(indexList)

		h = {}
		for i, num in enumerate(nums): # Enumerate prints all values in the list, i is index, num is val
			n = target - num # target - value in list
			if n not in h:
				h[num] = i
			else:
				return [h[n], i]

	print(twoSum())
