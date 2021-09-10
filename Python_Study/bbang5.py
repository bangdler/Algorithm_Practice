assigned_list = [1, 2, 3]
assigned_list[0:1] = [10, 20]
print(sum(assigned_list))

b_list = assigned_list
c_list = assigned_list[:]

assigned_list[2:4] = [5, 6, 7]
c_list.append(7)

print(b_list)
print(c_list)

d_list = b_list + c_list
print(d_list)

b_list.append(c_list)
print(b_list)

print(d_list == b_list)

d_list.append(2)
d_list.pop()
print(d_list)