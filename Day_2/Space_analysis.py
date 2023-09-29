#Example for Polynomial Space Complexity
def generate_lists_of_lists(n):
    table_list=[]
    for num in range(n):#--->n elements
        row=[]
        for i in range(n):#---->n*n elements
            row.append(i)
        table_list.append(row)
    return table_list

print(generate_lists_of_lists(10))