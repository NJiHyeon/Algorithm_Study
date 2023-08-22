array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)) :
	# 가장 작은 원소의 인덱스 (첨에는 가장 앞쪽 인덱스라고 가정하고, 다음 조건문을 통해 바뀜)
	min_index = i
	for j in range(i+1, len(array)) :
		if array[min_index] > array[j] :
			min_index = j
	# 스와프
	array[i], array[min_index] = array[min_index], array[i]
print(array)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)) :
	for j in range(i, 0, -1) :
		if array[j] < array[j-1] : 
			array[j], array[j-1] = array[j-1], array[j]
		else :
			break # 하나라도 오른쪽이 크면 계속 볼 필요 없으므로

print(array)