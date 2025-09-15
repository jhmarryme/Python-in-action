import inspect  # 新增：导入inspect模块获取类的模块信息
import time
import tracemalloc
from typing import List, Type, Any


def run_performance_test(
        solution_classes: List[Type],
        method_name: str,
        test_params: List[Any],  # 已支持任意类型参数列表
        report_title: str = "函数性能测试报告"
) -> str:  # 返回类型为str（Markdown报告内容）
    """通用性能测试框架（支持类方法测试）"""
    results = []

    # 为每个解决方案类创建实例并获取测试方法
    functions = []
    for cls in solution_classes:
        instance = cls()
        method = getattr(instance, method_name)
        # 包装方法以保留类名作为标识 - 修改lambda参数名避免冲突
        wrapped_method = lambda n, captured_method=method: captured_method(n)

        # 获取类的模块名并提取文件名作为前缀
        module_name = inspect.getmodule(cls).__name__.split('.')[-1]
        wrapped_method.__name__ = f"{module_name}.{cls.__name__}.{method_name}"

        functions.append(wrapped_method)

    for func in functions:
        for n in test_params:
            tracemalloc.start()
            snapshot_before = tracemalloc.take_snapshot()

            start_time = time.perf_counter()
            result = func(n)
            duration = time.perf_counter() - start_time

            snapshot_after = tracemalloc.take_snapshot()
            tracemalloc.stop()
            top_stats = snapshot_after.compare_to(snapshot_before, 'lineno')
            memory_used = sum(stat.size_diff for stat in top_stats) / (1024 * 1024)

            results.append({
                "function": func.__name__,
                "param": n,
                "result": result,
                "duration": duration,
                "memory_used": memory_used
            })

    # 输出格式化控制台表格
    print_console_report(results, report_title, test_params)

    # 输出Markdown格式报告文本
    print("\n" + "=" * 30 + " Markdown报告 " + "=" * 30)
    report = generate_markdown_report(results, report_title, test_params)
    print(report)
    print("=" * 70 + "\n")
    return report


def print_console_report(
        results: List[dict],
        title: str,
        test_params: List[Any]  # 修改为 List[Any] 支持任意参数类型
) -> None:
    """在控制台输出格式化的性能测试表格"""
    print(f"\n{title:=^50}")
    print("\n===== 测试环境 =====")
    print(f"测试时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # 优化1：安全显示参数范围（移除 min/max 依赖）
    try:
        # 尝试获取范围（仅对可比较类型有效）
        param_range = f"{min(test_params)} ~ {max(test_params)}"
    except (TypeError, ValueError):
        # 对复杂类型参数显示样本数量
        param_range = f"共 {len(test_params)} 个样本参数"
    print(f"参数范围: {param_range}")

    print("\n===== 性能对比结果 =====")
    # 优化2：参数列改用字符串格式化，支持任意类型
    print(f"{'函数名称':<25} {'输入参数':<20} {'计算结果':<10} {'运行时间(秒)':<14} {'内存使用(MB)':<12}")
    print("-" * 85)
    for item in sorted(results, key=lambda x: (x["function"], str(x["param"]))):
        print(
            f"{item['function']:<25} {str(item['param']):<20} {item['result']:<10} {item['duration']:.6f} {' ':<6} {item['memory_used']:.4f}")


# 新增：恢复Markdown报告生成函数（仅返回字符串，不写入文件）
def generate_markdown_report(
        results: List[dict],
        title: str,
        test_params: List[Any]  # 修改为 List[Any] 支持任意参数类型
) -> str:
    """生成Markdown格式报告字符串"""
    md = f"# {title}\n\n"
    md += "## 测试环境\n"
    md += f"- 测试时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"

    # 优化1：安全显示参数范围（同控制台报告逻辑）
    try:
        param_range = f"{min(test_params)} ~ {max(test_params)}"
    except (TypeError, ValueError):
        param_range = f"共 {len(test_params)} 个样本参数"
    md += f"- 测试参数范围: {param_range}\n\n"

    md += "## 性能对比结果\n"
    md += "| 函数名称 | 输入参数 | 计算结果 | 运行时间(秒) | 内存使用(MB) |\n"
    md += "|----------|----------|----------|--------------|--------------|\n"

    # 修复：统一使用字符串格式化，修复代码顺序
    for item in sorted(results, key=lambda x: (x["function"], str(x["param"]))):
        # 优化2：参数显示改用字符串格式，支持任意类型
        md += "| {function} | {param} | {result} | {duration:.6f} | {memory_used:.4f} |\n".format(
            function=item["function"],
            param=str(item["param"]),  # 转为字符串避免格式化错误
            result=item["result"],
            duration=item["duration"],
            memory_used=item["memory_used"]
        )

    return md
