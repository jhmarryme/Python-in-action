"""
# 题目2：Linux路径模拟（pwd与cd操作）
## 问题描述
在Linux系统中，路径管理依赖`pwd`（显示当前工作目录）和`cd`（切换工作目录）两种基础操作。现需编写程序，模拟这两种操作的执行过程，根据输入的操作序列，输出每次`pwd`操作对应的当前工作目录路径。

### 核心规则
1. **初始路径**：程序启动时，当前工作目录默认为根目录 `/`。
2. **操作类型**：仅支持两种操作，无其他非法操作：
   - `pwd`：输出当前工作目录的完整路径。
   - `cd xx`：切换工作目录，其中`xx`为目标路径，格式固定为`./dir/`（一定以`./`开头、以`/`结尾），具体规则如下：
     - 路径中的`.`表示“当前目录”，切换后路径不变（如`cd ./`等价于不切换）。
     - 路径中的`..`表示“上一级目录”，若当前目录为根目录，执行`cd ./../`后仍保持根目录。
     - 路径中的非`.`、非`..`部分为合法目录名（不含空格），切换时需将该目录添加到当前路径的层级中。
3. **路径输出格式**：
   - 根目录输出为 `/`。
   - 非根目录输出需以 `/` 开头、以 `/` 结尾，层级间用 `/` 分隔（如`/home/test/`）。


## 输入格式
1. 第一行输入一个整数 `n`（`1 ≤ n ≤ 100`），表示后续输入的操作总条数。
2. 接下来 `n` 行，每行输入一个操作，仅为以下两种形式之一：
   - 单独的 `pwd` 字符串。
   - `cd xx` 格式的字符串（`xx` 为目标路径，符合`./dir/`格式，目录合法且不含空格，`dir`可为目录名、`..`，若`dir`为空则路径为`./`）。


## 输出格式
每遇到一次 `pwd` 操作，就输出一行当前工作目录的完整路径，路径格式需严格遵循核心规则中的“路径输出格式”要求。


## 输入示例
```
9
pwd
cd ./home/test/
pwd
cd ./
pwd
cd ./../
pwd
cd ./../../../../
pwd
```

## 输出示例
```
/
/home/test/
/home/test/
/home/
/
```


## 解题思路提示
1. 用数组（列表）存储当前路径的层级结构（如`/home/test/`对应数组`['home', 'test']`），根目录对应空数组。
2. 处理`cd`操作时：
   - 将目标路径按 `/` 分割（如`./home/test/`分割后得到`['.', 'home', 'test', '']`）。
   - 遍历分割后的每个部分：遇到`.`跳过，遇到`..`且数组非空则删除最后一个元素，遇到非空非特殊字符则添加到数组。
3. 处理`pwd`操作时：
   - 若数组为空（根目录），直接输出 `/`。
   - 若数组非空，拼接成`/` + 数组元素用`/`连接 + `/`的格式（如`['home','test']`拼接为`/home/test/`）。
"""


def run_tests(func, test_cases):
    """通用测试执行器"""
    passed = 0
    total = len(test_cases)
    print(f"开始测试，共 {total} 个测试用例\n")

    for case_idx, (input_ops, expected_outputs) in enumerate(test_cases, 1):
        try:
            result = func(input_ops)
            if result == expected_outputs:
                passed += 1
                print(f"测试用例 {case_idx}: ✅ 通过")
            else:
                print(f"测试用例 {case_idx}: ❌ 失败")
                print(f"  输入操作: {input_ops}")
                print(f"  预期输出: {expected_outputs}")
                print(f"  实际输出: {result}")
        except Exception as e:
            print(f"测试用例 {case_idx}: ⚠️ 异常")
            print(f"  输入操作: {input_ops}")
            print(f"  错误信息: {str(e)}")
        finally:
            print("-" * 80)

    print(f"\n测试总结: {passed}/{total} 用例通过")
    print("🎉 全部通过！" if passed == total else "💡 请根据失败信息修正代码")


def simulate_linux_path(operations: list[str]):
    paths, res = list(), list()
    paths.append("/")

    def pwd():
        res.append("".join(paths))

    def cd(source_path: str):
        for path in source_path.split('/'):
            if path == '.' or path == '/' or path == '':
                pass
            elif path == '..':
                if len(paths) > 1:
                    paths.pop()
            else:
                paths.append(path + '/')

    for path in operations[1::]:
        if path.startswith('pwd'):
            pwd()
        if path.startswith('cd'):
            cd(path.split('cd')[1].strip())
    return res


# 测试用例设计（覆盖各种场景）
test_cases = [
    # 测试用例1: 题目示例
    (
        [
            '9',
            'pwd',
            'cd ./home/test/',
            'pwd',
            'cd ./',
            'pwd',
            'cd ./../',
            'pwd',
            'cd ./../../../../',
            'pwd'
        ],
        ['/', '/home/test/', '/home/test/', '/home/', '/']
    ),

    # 测试用例2: 根目录下cd ..（边界情况）
    (
        [
            '3',
            'pwd',
            'cd ./../',
            'pwd'
        ],
        ['/', '/']
    ),

    # 测试用例3: 多级目录切换
    (
        [
            '6',
            'pwd',
            'cd ./a/',
            'cd ./b/',
            'cd ./c/',
            'pwd',
            'cd ../../',
            'pwd'
        ],
        ['/', '/a/b/c/', '/a/']
    ),

    # 测试用例4: 连续切换和返回
    (
        [
            '5',
            'cd ./x/',
            'cd ./y/',
            'cd ../z/',
            'pwd',
            'cd ../../../',
            'pwd'
        ],
        ['/x/z/', '/']
    ),

    # 测试用例5: 仅pwd操作
    (
        [
            '2',
            'pwd',
            'pwd'
        ],
        ['/', '/']
    ),

    # 测试用例6: 复杂路径（含多个.和..）
    (
        [
            '4',
            'cd ./dir1/./dir2/../dir3/',
            'pwd',
            'cd ../.././dir4/',
            'pwd'
        ],
        ['/dir1/dir3/', '/dir4/']
    )
]

if __name__ == "__main__":
    run_tests(simulate_linux_path, test_cases)
