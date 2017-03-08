__功能__

计算随机生成的目标点与随机生成的取样点 距离最近的top_n个取样点。

__config.json说明__

1. 参数意义：
> point_count: 需要随机生成点的数量

> dimensions: 需要生成点的维度

> min_coordinate_num: 每个数据点坐标的最小值

> max_coordinate_num: 每个数据点坐标的最大值

> coordinate_num_format: 每个数据点坐标的数据格式, 0为小数格式，1为整数格式


__程序运行__:
1. 配置更好config.json文件
3. 运行 analysis/distance.py 之前，修改main中的代码：
```python
if __name__ == '__main__':
    print find_nearest_points(top_n=10, distance_method=__EUCLIDEAN_DISTANCE)
```
其中 top_n 表示需要求出距离2步中得出的最近top_n个点， distance_method 参数暂时不用设置，现在只支持欧式距离

4. 生成的结果文件位于 analysis/文件夹下，info-yy-mm-dd-HH-MM-SS-points.txt 保存的是最近点的下标以及具体的距离值：
```text
下标  距离值
66	355.966108019
12	379.03663753
34	401.662931081
82	404.689850171
38	409.78346215
93	416.533845118
94	416.652975138
43	416.746263606
```
nearest-yy-mm-dd-HH-MM-SS-points.txt 保存的是最近点的具体下标：
```text
 271.45039   11.35356  222.76524   49.37754  110.38732
 271.45039   11.35356  222.76524   49.37754  110.38732
  271.45039   11.35356  222.76524   49.37754  110.38732
```

5. data文件夹下保存生成的随机点信息，文件名为 yy-mm-dd-HH-MM-SS-points.txt；该文件夹下target-points.txt文件中为随机生成的目标点信息。