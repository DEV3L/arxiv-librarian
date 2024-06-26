from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.clients.openai_api import OpenAIClient, build_openai_client


@patch("src.clients.openai_api.OpenAI")
def test_build_openai_client(mock_openai):
    client = build_openai_client()

    assert client is mock_openai.return_value

    mock_openai.assert_called_once_with(timeout=45)


class TestOpenAIClient(TestCase):
    client: OpenAIClient

    mock_open_ai: MagicMock

    def setUp(self):
        self.mock_open_ai = MagicMock()

        self.client = OpenAIClient(self.mock_open_ai)

    def test_threads_create(self):
        messages = [{"content": "Hello", "role": "system"}]

        self.client.threads_create(messages)

        self.mock_open_ai.beta.threads.create.assert_called_once_with(messages=messages)

    def test_messages_list(self):
        thread_id = "thread_id"

        self.client.messages_list(thread_id)

        self.mock_open_ai.beta.threads.messages.list.assert_called_once_with(thread_id)

    def test_messages_create(self):
        thread_id = "thread_id"
        content = "Hello"
        role = "user"

        self.client.messages_create(thread_id, content, role)

        self.mock_open_ai.beta.threads.messages.create.assert_called_once_with(
            thread_id=thread_id, content=content, role=role
        )

    def test_runs_create(self):
        thread_id = "thread_id"
        assistant_id = "assistant_id"

        self.client.runs_create(thread_id, assistant_id)

        self.mock_open_ai.beta.threads.runs.create.assert_called_once_with(
            thread_id=thread_id, assistant_id=assistant_id
        )

    def test_runs_retrieve(self):
        run_id = "run_id"
        thread_id = "thread_id"

        self.client.runs_retrieve(run_id, thread_id)

        self.mock_open_ai.beta.threads.runs.retrieve.assert_called_once_with(run_id, thread_id=thread_id)

    def test_assistants_list(self):
        self.client.assistants_list()

        self.mock_open_ai.beta.assistants.list.assert_called_once()

    def test_assistants_create(self):
        name = "assistant_name"
        instructions = "instructions"
        tools = [{"tool_name": "tool"}]
        vector_store_ids = ["vector_store_id"]

        self.client.assistants_create(name, instructions, vector_store_ids, tools)

        self.mock_open_ai.beta.assistants.create.assert_called_once_with(
            name=name,
            instructions=instructions,
            model="gpt-4-turbo",
            tool_resources={"file_search": {"vector_store_ids": vector_store_ids}},
            tools=tools,
        )

    def test_assistants_delete(self):
        assistant_id = "assistant_id"

        self.client.assistants_delete(assistant_id)

        self.mock_open_ai.beta.assistants.delete.assert_called_once_with(assistant_id)

    def test_files_list(self):
        files = self.client.files_list()

        self.mock_open_ai.files.list.assert_called_once()
        assert files == self.mock_open_ai.files.list.return_value

    def test_files_create(self):
        file = MagicMock()
        purpose = "purpose"

        self.client.files_create(file, purpose)

        self.mock_open_ai.files.create.assert_called_once_with(file=file, purpose=purpose)

    def test_files_delete(self):
        file_id = "file_id"

        self.client.files_delete(file_id)

        self.mock_open_ai.files.delete.assert_called_once_with(file_id)

    def test_vector_stores_list(self):
        vector_stores = self.client.vector_stores_list()

        self.mock_open_ai.beta.vector_stores.list.assert_called_once()
        assert vector_stores == self.mock_open_ai.beta.vector_stores.list.return_value

    def test_vector_stores_retrieve(self):
        vector_store_id = "vector_store_id"

        vector_store = self.client.vector_stores_retrieve(vector_store_id)

        self.mock_open_ai.beta.vector_stores.retrieve.assert_called_once_with(vector_store_id)
        assert vector_store == self.mock_open_ai.beta.vector_stores.retrieve.return_value

    @patch("src.clients.openai_api.time")
    def test_vector_stores_create(self, mock_time):
        file_ids = ["file_id"]
        name = "vector_store_name"
        self.mock_open_ai.beta.vector_stores.retrieve.side_effect = [
            MagicMock(status="pending"),
            MagicMock(status="completed"),
        ]

        self.client.vector_stores_create(name, file_ids)

        self.mock_open_ai.beta.vector_stores.create.assert_called_once_with(name=name, file_ids=file_ids)
        assert mock_time.sleep.call_count == 1

    def test_vector_stores_delete(self):
        vector_store_id = "vector_store_id"

        self.client.vector_stores_delete(vector_store_id)

        self.mock_open_ai.beta.vector_stores.delete.assert_called_once_with(vector_store_id)
