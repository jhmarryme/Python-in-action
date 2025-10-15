在本教程中，将使用 Agent Development Kit (ADK) 为一个简单的天气查询智能体补齐“可重复、可度量”的评估能力。你将学习如何准备测试用例、配置评估指标，并通过 Web、CLI 与 pytest 运行评估与调试。

参考文档：[Why Evaluate Agents | ADK Docs](https://google.github.io/adk-docs/evaluate/)

### 目录结构

```
 tutorials/evaluate/
   __init__.py                    # 导出 root_agent，便于 CLI/pytest 发现
   agent.py                       # 智能体与工具定义
   run.py                         # 本地交互运行验证
   tests/
     simple_weather.test.json     # 单 Session 测试文件（轻量评估）
   hello_weather_eval_set_001.evalset.json  # 批量评估用 Evalset 文件
   test_config.json               # 评估阈值配置（可选）
   test_programmatic_eval.py      # 使用 pytest 的程序化评估
   note.md                        # 本文档
```

### 0. 准备评估（目标与成功标准）
在自动化评估之前，明确：
- **成功定义**：什么结果算“通过”？例如：伦敦天气查询需调用 `get_weather`，最终文案需包含“多云 15°C”。
- **关键任务**：智能体必须完成的核心步骤是什么？例如：意图识别 → 工具调用 → 结果复述。
- **指标选择**：关注轨迹一致性、回答质量，还是两者兼顾？

这些约定将指导你如何编写“测试文件”/Evalset 与设定阈值，保证评估贴近真实目标。

### 1. 评估什么：Trajectory 与 Final Response

- **Trajectory（工具轨迹与工具使用）**：比较期望 vs 实际工具调用序列。
  - 常见口径：
    - Exact match：必须与期望完全一致。
    - In-order：顺序正确，允许多余步骤。
    - Any-order：包含期望步骤即可，顺序不限。
    - Precision/Recall：衡量预测的相关性与覆盖率。
    - 单工具使用检查：是否包含某个关键工具调用。
- **Final Response（最终自然语言回答）**：与参考答案做相似度比较（默认 ROUGE）。

### 2. 指标与默认阈值（Evaluation Criteria）

- `tool_trajectory_avg_score`：工具使用与期望匹配的平均分。
- `response_match_score`：最终回答与参考答案的相似度。

默认阈值（若未配置）：
- `tool_trajectory_avg_score = 1.0`
- `response_match_score = 0.8`

自定义阈值示例：

**文件:** `tutorials/evaluate/test_config.json`
```json
{ "criteria": { "tool_trajectory_avg_score": 1.0, "response_match_score": 0.8 } }
```

### 3. 定义工具与智能体

**文件:** `tutorials/evaluate/agent.py`
```python
# ... existing code ...
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = 'openai/qwen2.5-72b-instruct'

def get_weather(city: str) -> dict:
    """获取指定城市的当前天气报告。"""
    # 省略实现...

root_agent = Agent(
    name="evaluate_weather_agent",
    model=LiteLlm(model=AGENT_MODEL),
    description="用于演示 ADK 评估的简单天气智能体。",
    instruction=(
        "用户询问特定城市天气时，必须使用 'get_weather' 工具；"
        "若工具返回 error，礼貌反馈未知；若 success，清晰给出 report；"
        "仅在明确城市时调用工具。"
    ),
    tools=[get_weather],
)
# ... existing code ...
```
- 提示：在 docstring 与 instruction 中明确“何时调用工具/如何处理失败”，有助于提升轨迹达标率。

### 4. 运行与调试（Runner / Web Trace）

**文件:** `tutorials/evaluate/run.py`
- 本地运行：
```
python -m tutorials.evaluate.run
```
- Web UI（Eval 与 Trace）：
```
adk web /home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/evaluate
```
- Trace 视图说明：蓝色行代表产生事件；点击可查看底部详情，包含四个面板：
  - Event：原始事件数据
  - Request：模型请求
  - Response：模型响应
  - Graph：工具调用与逻辑流程图

### 5. 使用“测试文件”的轻量评估（单 Session）

**文件:** `tutorials/evaluate/tests/simple_weather.test.json`
```json
{
  "name": "simple_weather_session",
  "turns": [
    {
      "user": "What's the weather in London?",
      "expected_tool_use": [
        { "tool_name": "get_weather", "args": { "city": "London" } }
      ],
      "reference": "伦敦多云，温度为 15°C。"
    }
  ],
  "session_input": { "app_name": "evaluate_tutorial_app", "user_id": "user_eval_root", "state": {} }
}
```
- 在 Web UI 的 Eval 标签页：
  1) 选中智能体，交互生成会话；2) 进入 Eval 标签，创建/选择 evalset；3) “Add current session” 保存；
  4) 点击 Run Evaluation，使用滑杆配置阈值并启动；5) 失败项支持 Expected vs Actual 对比。

### 6. 使用 Evalset 的批量评估（CLI）

**文件:** `tutorials/evaluate/hello_weather_eval_set_001.evalset.json`

- 运行：
```bash
adk eval \
  /home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/evaluate \
  /home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/evaluate/hello_weather_eval_set_001.evalset.json \
  --config_file_path=/home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/evaluate/test_config.json \
  --print_detailed_results
```
- 仅运行指定 eval 名称：
```bash
adk eval \
  /home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/evaluate \
  /home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/evaluate/hello_weather_eval_set_001.evalset.json:eval_weather_london,eval_weather_tokyo
```
- 参数说明（与官网一致）：
  - `AGENT_MODULE_FILE_PATH`：包含名为 `agent` 模块且内含 `root_agent` 的包路径（本教程已在 `__init__.py` 重导出）。
  - `EVAL_SET_FILE_PATH`：可为单文件或多个文件；冒号后可跟 eval 名称列表进行过滤。
  - `--config_file_path`：自定义评估阈值配置路径。
  - `--print_detailed_results`：在控制台打印更详细的结果。

### 7. 使用 pytest 的程序化评估（CI/CD）

**文件:** `tutorials/evaluate/test_programmatic_eval.py`
```bash
cd /home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials
pytest tutorials/evaluate/test_programmatic_eval.py -q
```
- 可选：若需指定初始 Session 状态，可在文件中存储并通过 `AgentEvaluator.evaluate` 传入（参考官网示例）。

### 8. 扩展示例（更多用例）

为更全面覆盖场景，可在 evalset 中加入：
- 错误城市（期望工具返回 error 且回答礼貌说明未知）。
- 城市同义词/大小写变体（验证标准化处理）。
- 非天气意图（不应调用工具，回答应得体）。

已在下方扩充 evalset（见“文件”章节）。

### 9. 常见问题与排查

- 工具未被调用：
  - 强化 instruction 中“何时调用工具”；
  - 检查工具 docstring 是否清楚；
  - 查看 Trace 的 Graph 面板，确认决策分支。
- 回答与参考差异大：
  - 先提升轨迹达标（确保用了正确工具）；
  - 适度调整 `response_match_score`；
  - 收紧或优化 `instruction` 以减少冗余扩写。
- CLI 无法找到 `root_agent`：
  - 确认 `evaluate/__init__.py` 导出了 `root_agent`；
  - CLI 的第一个参数路径指向包含 `agent` 模块的包目录。

---

### 总结
- 覆盖测试文件（轻量）、Evalset+CLI（批量）、pytest（程序化）三大路径。
- Eval 与 Trace 提供强可视化支撑：配置阈值、查看 Expected vs Actual、定位轨迹差异。
- 建议先以严格轨迹保障流程正确性，再优化回答相似度。

更多细节请参考：[ADK Evaluate 文档](https://google.github.io/adk-docs/evaluate/)。
