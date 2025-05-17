sum_str = lambda a, b : a + b
sum_num = lambda a, b, c : a + b + c
sum_list = lambda l : sum(l)
count_str = lambda st, coof : st.count(coof)

print(sum_str("hello", " world"))
print(sum_num(1, 3, 5))
print(sum_list([1,2,3,4,5]))
print(count_str("hello", 'l'))
