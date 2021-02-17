import openai
import io
import json
import uuid

### FILE TESTS
def _upload_default_file():
    return openai.File.create(
        file=io.StringIO(json.dumps({"text": "test file data"})),
        purpose="search",
        collection_names=["test1", "test2"],
    )


def test_file_upload_with_multiple_collections():
    result = _upload_default_file()
    assert set(result.collections) == set(["test2", "test1"])
    assert "id" in result


### COLLECTION TESTS
def test_collections_upload():
    file1 = _upload_default_file()
    file2 = _upload_default_file()

    result = openai.Collection.create(
        name=f"ci_{uuid.uuid4().hex}",
        file_ids=[file1.id, file2.id],
    )
    assert set(result.files) == set([file1.id, file2.id])
    assert "id" in result


### COMPLETION TESTS
def test_completions():
    result = openai.Completion.create(prompt="This was a test", n=5, engine="davinci")
    assert len(result.choices) == 5


def test_completions_multiple_prompts():
    result = openai.Completion.create(
        prompt=["This was a test", "This was another test"], n=5, engine="davinci"
    )
    assert len(result.choices) == 10
