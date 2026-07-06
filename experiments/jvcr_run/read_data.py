import pickle

# 1. 打开文件，用 pickle.load 读
with open('experiment.pkl', 'rb') as f:  # 'rb' = 只读二进制模式
    data = pickle.load(f)

# 2. 看看读出来是啥
print(type(data))  # 先看数据类型：字典？列表？还是某个类的对象？
print(data)        # 直接打印看看内容


