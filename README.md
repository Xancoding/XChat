# Run 
## Requirement 
1. Python 3.8

## Before Start 
### In folder "XChat"
1. Install python libs
    ```
    pip install -r requirements.txt
    ```
2. Config 

    In `src/config.py`, config `API_KEY` and `USE_PROXY`
   ```python
   # OpenAI API_KEY
   API_KEY = "YOUR_OPENAI_API_KEY"

   # 是否使用代理
   USE_PROXY = True
   ```

## Start
```shell
cd src
python main.py
```