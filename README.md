# agents powered by Local LLMs

## Custom Ollama Model

* [Customizing Ollama Models using Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md)
* to create custom Ollama model using the Modelfile run the following command:

    ```bash
    ollama create agent -f Modelfile
    ```
* Create a virtualenv
    ```bash
    pip install - r requirements.txt
    # setup jira secrets in https://github.com/shreyaskarnik/agents-demo/blob/main/agents.py#L16-L18
    # make sure you input the correct project_key and num_weeks parameters in https://github.com/shreyaskarnik/agents-demo/blob/main/main.py#L9
    python main.py
    # the crew should now be starting
    ```
* Accompanying blog post can be found at <https://kshreyas.dev/post/ai-agents/>
