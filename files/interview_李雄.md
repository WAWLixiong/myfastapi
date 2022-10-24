## 逻辑题
1. E
2. B
3. B
4. E
5. A

## 语言特性
1. 'tim', ['t', 'i', 'm', 'e']
2. [3, 4], [4, 5], [1, 3, 5]
3. 5, [5, 1], [5]
4. {'c'}
5. 1 1 2 3 5
6.
    - 1, 'commit', None {'z': 'merge', 'b': 'clone', 'x': 6, 'y': 7}
    - 1, 2, ('push', 5), {'x': 'pull', 'y': 'checkout'}
7. 
    - [1, 3, 9, 16]
    - [2, 4]
8.
    - 1, 1, 1, '2', '3'
    - 1, 2, 1, '4', '3'
    - 3, 2, 3, '4', '9'
9. '<b><i>hello world</i></b>'
10. 
    - 3 1
    - 3 2


## 计算机网络，操作系统，数据库
1. 3, 4
2. 
    - Cookie存储在客户端
    - Session存储在服务端
3. 
    - 301: 临时转移
    - 302: 永久转移
    - 400: 客户端请求问题
    - 500: 服务端不能正常处理请求
4. 
    - top: 查看进程cpu，内存占用
    - grep: 搜索文本
    - mv: 移动/重命名
    - find: 查找文件
    - du: 查询文件磁盘占用
    - cat: 查看完整文件内容
    - chmod: 修改文件(夹) 权限
    - wc: 监视
    - awk: 文本处理，可以按列查询，
    - crontab: 定时
    - uniq: 去重
    - netstat: 端口占用
    - ps: 进程
    - xargs: 不支持管道的命令通过xargs处理
5. r: 读权限， w: 写权限， x: 执行权限
6.  
    - 进程内开启线程
    - 进程切换比线程切换更耗时
    - 线程共享进程资源
7. 
    - explain: 查询sql的执行计划，可以查看索引情况
    - show processlist: 查询会话及会话任务
8. 单例，工厂，观察者，责任链，装饰， 代理， 命令

## 算法
1. 
    ```python
    a = '2020-05-16 19:20:34|user.login|name=Charles&location=Beijing&device=iPhone'

    def parse(log: str):
        try:
            infos = log.rpartition('|')
            main_info = infos[2]
        except IndexError:
            return {}
        else:
            try:
                kv_strs = main_info.split('&')
                kv_strs = [i.split('=') for i in kv_strs]
                return {i[0]: i[1] for i in kv_strs}
            except IndexError:
                return {}


    if __name__ == '__main__':
        ret = parse(a)
        print(ret)
    ```

2. 
    ```python
    def min_abs(sequence: list):
        if sequence[-1] <= 0:
            return sequence[-1]

        l = 0
        negative_min = float('inf')

        while sequence[l] < 0:
            negative_min = sequence[l]
            l += 1

        if abs(negative_min) < sequence[l]:
            return negative_min
        return sequence[l]


    if __name__ == '__main__':
        a = [-4, -3, -2, 0, 1, 2, 3]
        ret = min_abs(a)
        print(ret)
    ```
    
3. 
    ```python
    from queue import PriorityQueue


    class Solution:

        def __init__(self):
            self.low = PriorityQueue()  # 大顶
            self.high = PriorityQueue()  # 小顶

        def add(self, num):
            self.low.put(-num)
            self.high.put(-self.low.get())
            if self.low.qsize() + 1 < self.high.qsize():
                self.low.put(-self.high.get())

        def find(self):
            return self.high.get()


    if __name__ == '__main__':
        a = [1, 3, 2]
        a = [2, 1, 3, 4, 5, 11, 19]
        a = [1, 5, 2, 9, 8, 0, 6]
        solution = Solution()
        for i in a:
            solution.add(i)

        ret = solution.find()
        print(ret)

    ```


4. 
    ```python
    class Solution:

        def method(self, n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            return self.method(n - 1) + self.method(n - 3)


    if __name__ == '__main__':
        solution = Solution()
        ret = solution.method(4)
        print(ret)
    ```
