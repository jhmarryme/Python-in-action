import asyncio
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义一个异步生成器函数
async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)  # 模拟异步操作
        yield i

# 定义一个异步函数来使用异步生成器
async def main():
    async for num in async_generator():
        logging.info("received num: %s", num)

# 运行异步函数
logging.info("start")
asyncio.run(main())
logging.info("end")