'''
1. 生成随机数列
2. 接受seed数,size in turple format
3. 写成log，log放在"logs/"下面
4. bash执行5次
'''
import numpy as np
import os
import argparse


def mkdir():
    current_folder = os.getcwd()
    if os.path.exists(current_folder + "/logs/"):
        pass
    else:
        os.makedirs(current_folder + "/logs/")


def workload(num, msg):
    current_folder = os.getcwd()
    name = "log" + num + ".txt"
    fpath = current_folder + "/logs/" + name
    with open(fpath, "a") as f:
        f.write(msg)


def gen_rand(sd, x, y):
    np.random.seed(sd)
    result = np.random.rand(x, y)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=str, default='0')
    parser.add_argument('-s', '--seed', type=int, default='100')
    parser.add_argument('-x', type=int, default='0')
    parser.add_argument('-y', type=int, default='0')
    args = parser.parse_args()

    mkdir()
    result = gen_rand(args.seed, args.x, args.y)
    workload(args.number, "\n" + str(result))
