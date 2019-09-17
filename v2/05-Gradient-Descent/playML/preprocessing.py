# -*- coding: utf-8 -*-
# @Author : 3zz
# @Time   : 2019/9/15 6:30 下午
# @File   : preprocessing.py
import numpy as np


class StandardScaler:

    def __init__(self):
        self.mean_ = None
        self.scale_ = None

    def fit(self, X):
        """
        根据X获得平均值与方差
        :param X: 训练数据集
        :return: 自身
        """
        self.mean_ = np.array([np.mean(X[:, i]) for i in range(X.shape[1])])
        self.scale_ = np.array([np.std(X[:, i]) for i in range(X.shape[1])])

        return self

    def transform(self, X):
        """
        进行均值方差的归一化处理
        :param X:
        :return:
        """
        assert X.ndim == 2, "the dimension of X must be 2"
        assert self.mean_ is not None and self.scale_ is not None, "must fit before transform"
        assert X.shape[1] == len(self.mean_), "the feature number of X must be equal to mean_ and std_"

        resX = np.empty(shape=X.shape, dtype=float)
        for col in range(X.shape[1]):
            resX[:, col] = (X[:, col] - self.mean_[col]) / self.scale_[col]
        return resX
