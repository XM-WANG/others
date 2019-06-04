# 比较两个txt文件的脚本
写了一个用来比较两个txt文件内容差异的脚本，主要调用的python基本库 [difflib](https://docs.python.org/3/library/difflib.html)。参数给两个txt文件的文件名，脚本会生成一个html文件，保存在result文件夹下。
## 测试
```python
python3 wxm.py -d1=test1.txt -d2=test2.txt
```
