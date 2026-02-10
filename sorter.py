def bubblesort(nums):
	n = len(nums)

	for i in range(n): # precisa iterar toda a lista
		swapped = False

		for j in range(n-i-1): # para nao gerar indexError
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
				swapped = True

		if not swapped: # se nao houveram trocas, esta ordenado
			break
	return nums

print(bubblesort([2,3,1,5,4]))