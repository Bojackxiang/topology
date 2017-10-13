# Initialization
list = ['Z', 'B']
new_list = sorted(list)


print(new_list)






# 读文件
topo = "topology.txt"
with open(topo) as file:
    point_list = []
    topo = file.readlines()
    #building matrix
    for element in topo:
        first_c = element.split(" ")[0]
        if first_c not in point_list:
            point_list.append(first_c)
        second_c = element.split(" ")[1]
        if second_c not in point_list:
            point_list.append(second_c)
    sorted(point_list)
    length = len(point_list)
    topology_matrix = [[0 for i in range(length)] for i in range(length)]























