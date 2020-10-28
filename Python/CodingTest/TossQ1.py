answer = []
user_input = input()
data, target_value = user_input.split('/')
data = input(data)
print(type(data))
print(target_value)

# 해당 값 찾기


# def find_data(data, key):
# 	for i in range(len(data)):
# 		if data[i]["pk"] == key:
# 			if data[i]["is_active"] == False:
# 				return False
# 			if data[i]["parent"] != None:
# 				answer.append(data[i]["value"])
# 				find_data(data, data[i]["parent"])


# def get_summary(data, target_value):
# 	answer.append(target_value)

# 	find_p = 0
# 	# tartget_value 값 찾기
# 	for d_idx in range(len(data)):
# 		# 찾은 경우
# 		if data[d_idx]["value"] == target_value:
# 			find_p = d_idx
# 			break

# 	if find_data(data, find_p) == None:
# 		print('>'.join(reversed(answer)))
# 	else:
# 		print("INACTIVE")


# get_summary(data, target_value)
