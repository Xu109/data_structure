"""
Author:  Mr.Xu
Create:  2020/7/8 11:42
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""


class heap:
    def __init__(self):
        self.data_list = []

    def print_heap(self):
        for i in range(len(self.data_list)):
            print(self.data_list[i], end=" ")


    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        '''
        交换两个索引对应的值
        :param index_a:
        :type index_a:
        :param index_b:
        :type index_b:
        :return:
        :rtype:
        '''
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data: int):
        self.data_list.append(data)  # 把一个新元素放到末尾
        curr_index = len(self.data_list) - 1
        curr_parent_index = self.get_parent_index(curr_index)
        while curr_parent_index is not None and self.data_list[curr_parent_index] < self.data_list[curr_index]:
            self.swap(curr_index, curr_parent_index)
            curr_index = curr_parent_index
            curr_parent_index = self.get_parent_index(curr_parent_index)

    def heapify(self, index):
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2 * index + 1 <= total_index and self.data_list[2 * index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.data_list[2 * index + 2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index

    def pop(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return remove_data

if __name__ == '__main__':
    h = heap()
    for i in range(10):
        h.insert(i + 1)
    print("堆为:", h.data_list)
    for i in range(10):
        print(h.pop(), end=" ")