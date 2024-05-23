# # # s1 = set([1,2,3,4,5,2,3,3])
# # # print(s1)]

s1 = {1,2,3,4,5,6,2,2}
print(s1)

# # # add value to a set
# # s1.add(9)

# # # using update to add 
# # s1.update([7,8])

# # # removing values in a set
# # s1.remove(4)

# # # KeyError
# # # s1.remove(10)

# # # using discard to remove
# # s1.discard(8)

# # print(s1)

# s1 = {1,2,3}
# s2 = {2,3,4}
# s3 = {3,4,5}

# # values which are common    intersection
# s4 = s1.intersection(s2)
# s4 = s1.intersection(s2,s3)

# # unique values    difference
# s4 = s1.difference(s2)
# s4 = s2.difference(s1)

# s4 = s2.difference(s1,s3)
# s4 = s3.difference(s1,s2)

# # unique values both ways    symmetric_differences

# s4 = s1.symmetric_difference(s2)

# print(s4)

# l1 = [1,2,2,3,4,1,2,4]
# l2 = set(l1)
# print(l2)

# employees = ['Corey','Jim','Steven','April','Judy','Jenn','John']
# gym_members = ['April','John','Corey']
# developers = ['Judy','Corey','Steven','Jane','April']

# result = set(gym_members).intersection(developers,employees)
# result = set(gym_members).difference(developers)
# result = set(gym_members).symmetric_difference(developers)
# print(result)

# if 'Corey' in developers:
#     print('\n\nFound!')

# set1 = {1,2,3,4,5,6}
# print(set1)
# print(dir(set1))