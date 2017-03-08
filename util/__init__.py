#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import json
import codecs


def load_config():
    """
    读取项目的配置文件
    :return: 配置文件的json对象
    """
    with codecs.open('../config.json', 'rb', 'utf-8') as config_file:
        config_data = json.load(config_file)
        return config_data


if __name__ == '__main__':
    print load_config()
