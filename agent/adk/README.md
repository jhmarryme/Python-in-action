

2. **创建并激活虚拟环境（推荐）：**
**创建：**
```shell
uv venv 
```

**激活（在每个新终端会话中执行）：**
- macOS / Linux：
    ```bash
    source .venv/bin/activate
    ```
- Windows（命令提示符）：
    ```bash
    .venv\Scripts\activate.bat
    ```
- Windows（PowerShell）：
    ```ps1
    .venv\Scripts\Activate.ps1
    ```
（你的终端提示符前应该会出现 `(.venv)`）

3. **安装依赖项：**
    安装 ADK 和 LiteLLM（用于多模型支持）。
```shell
uv pip install litellm --index-url https://pypi.tuna.tsinghua.edu.cn/simple
uv pip install google-adk --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```