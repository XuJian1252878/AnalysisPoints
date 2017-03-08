#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import numpy as np
from generate.data import generate_target_point, generate_sample_points
import codecs


__EUCLIDEAN_DISTANCE = 0


def load_target_point():
    """
    从文件中读取目标point，将来可能需要计算离该点最近的点的信息
    :return:
    """
    target_point = np.loadtxt('./point.txt')
    return target_point


def calc_euclidean_distance(vector_1, vector_2):
    """
    计算两个向量之间的欧式距离
    :param vector_1:
    :param vector_2:
    :return:
    """
    distance = np.linalg.norm(vector_1 - vector_2)
    return distance


def find_nearest_points(top_n=10, distance_method=__EUCLIDEAN_DISTANCE):
    """
    返回距离目标点最近的top_n个点
    :param top_n:
    :return:
    """
    target_point, tpoint_path = generate_target_point()  # 读入目标点数据
    points, points_path = generate_sample_points()  # 根据配置文件生成随机点列表

    nearest_points = {}
    # for point in points:
    for index in xrange(0, len(points)):
        if distance_method == __EUCLIDEAN_DISTANCE:
            distance = calc_euclidean_distance(target_point, points[index])
            print distance
            nearest_points[index] = distance

    nearest_points = sorted(nearest_points.items(), key=lambda item: item[1], reverse=False)

    result_points = np.zeros(points[0].size)
    for item in nearest_points:
        nearest_point = points[item[0]]
        result_points = np.vstack((nearest_point, result_points))

    # 将最近点的信息写入文件中
    path = './nearest-' + points_path.split('/')[-1]
    np.savetxt(path, result_points[0: -1], fmt='%10.5f', newline='\n')

    # 写入最近点的下标信息
    with codecs.open('./info-' + points_path.split('/')[-1], 'wb', 'utf-8') as output_file:
        for item in nearest_points:
            output_file.write('\t'.join([str(ele) for ele in item]) + '\n')
    return nearest_points[0: top_n], result_points[0: -1]


if __name__ == '__main__':
    print find_nearest_points()
