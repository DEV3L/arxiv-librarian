from datetime import datetime

from src.prompts.prompt import (
    get_functions,
    get_prompt,
)


def test_get_prompt():
    current_date = datetime.today().date().isoformat()

    prompt = get_prompt()
    assert isinstance(prompt, str)
    assert current_date in prompt


def test_get_functions():
    functions = get_functions()

    assert len(functions) == 1

    retrieval = functions[0]
    assert retrieval["type"] == "file_search"
