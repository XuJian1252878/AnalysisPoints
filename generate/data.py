#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from util import load_config
import numpy as np
import datetime


__COORDINATE_NUM_FORMAT_INT = 1  # 坐标点为整数格式
__COORDINATE_NUM_FORMAT_FLOAT = 0  # 坐标点为小数格式

# COORDINATE_NUM_FORMAT = {
#     0: __COORDINATE_NUM_FORMAT_FLOAT,
#     1: __COORDINATE_NUM_FORMAT_INT
# }


def generate_target_point():
    """
    根据配置文件，生成目标点信息
    :return:
    """
    point = __generate_points(1)
    point_path = '../data/target-point.txt'
    np.savetxt(point_path, point, fmt='%10.5f', newline='\n')
    print point
    return point, point_path


def generate_sample_points():
    """
    根据配置文件信息，生成随机的数据点
    :return:
    """
    points = __generate_points()
    # 保存多维随机点数据
    cur_timestamp_str = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    points_path = "../data/" + cur_timestamp_str + "-points.txt"
    np.savetxt(points_path, points, fmt='%10.5f', newline='\n')
    print points
    # 返回点坐标的数组信息、保存路径
    return points, points_path


def __generate_points(point_count=None):
    """
    根据配置文件信息，生成合适的点坐标
    :return:
    """
    config = load_config()
    if point_count is None:
        point_count = config["point_count"]  # 需要生成的数据点个数
    dimensions = config["dimensions"]  # 需要生成的每一个数据点的维度
    min_coordinate_num = config["min_coordinate_num"]  # 每个数据点坐标的最小值
    max_coordinate_num = config["max_coordinate_num"]  # 每个数据点坐标的最大值
    coordinate_num_format = config["coordinate_num_format"]  # 每个数据点坐标的数据格式

    points = None
    # 生成多维随机点数据
    if coordinate_num_format == __COORDINATE_NUM_FORMAT_FLOAT:
        points = (max_coordinate_num - min_coordinate_num) * np.random.random_sample((point_count, dimensions)) \
                 + min_coordinate_num
    elif coordinate_num_format == __COORDINATE_NUM_FORMAT_INT:
        points = np.random.randint(min_coordinate_num, max_coordinate_num, size=[point_count, dimensions])
    return points


if __name__ == '__main__':
    __generate_points()
