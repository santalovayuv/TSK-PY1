def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    if index == None:
        index = -1
    if index >= 0:
        list1 = list_[:index]
        list2 = list_[index+1:]
        return list1 + list2
    elif index < 0:
        list1 = list_[::-1]
        index = index * (-1) - 1
        list2 = list1[:index]
        list3 = list1[index+1:]
        list4 = list2 + list3
        return list4[::-1]


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]