#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import os
import yaml


def getConfig():
    basic_path = os.path.abspath(os.pardir)
    config_path = os.path.join(basic_path, "config.yaml")
    return yaml.load(open(config_path))
