import pytest

from google.adk.evaluation.agent_evaluator import AgentEvaluator


@pytest.mark.asyncio
async def test_programmatic_eval_with_evalset():
    await AgentEvaluator.evaluate(
        agent_module="tutorials.evaluate",  # 根级 agent 模块
        eval_dataset_file_path_or_dir="/home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/evaluate/hello_weather_eval_set_001.evalset.json",
        config_file_path="/home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/evaluate/test_config.json",
    )
