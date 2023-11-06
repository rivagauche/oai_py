# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RunCreateParams",
    "Tool",
    "ToolAssistantToolsCode",
    "ToolAssistantToolsRetrieval",
    "ToolAssistantToolsFunction",
    "ToolAssistantToolsFunctionFunction",
]


class RunCreateParams(TypedDict, total=False):
    assistant_id: Required[str]
    """
    The ID of the
    [Assistant](https://platform.openai.com/docs/api-reference/assistants) to use to
    execute this Run.
    """

    instructions: Optional[str]
    """Override the default system message of the Assistant.

    This is useful for modifying the behavior on a per-run basis.
    """

    metadata: Optional[object]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format. Keys can be a maximum of 64 characters long and values can be
    a maxium of 512 characters long.
    """

    model: Optional[str]
    """
    The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to
    be used to execute this Run. If a value is provided here, it will override the
    model associated with the Assistant. If not, the model associated with the
    Assistant will be used.
    """

    tools: Optional[List[Tool]]
    """Override the tools the Assistant can use for this Run.

    This is useful for modifying the behavior on a per-run basis.
    """


class ToolAssistantToolsCode(TypedDict, total=False):
    type: Required[Literal["code_interpreter"]]
    """The type of tool being defined: `code_interpreter`"""


class ToolAssistantToolsRetrieval(TypedDict, total=False):
    type: Required[Literal["retreival"]]
    """The type of tool being defined: `retreival`"""


class ToolAssistantToolsFunctionFunction(TypedDict, total=False):
    description: Required[str]
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    parameters: Required[Dict[str, object]]
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](https://platform.openai.com/docs/guides/gpt/function-calling)
    for examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    To describe a function that accepts no parameters, provide the value
    `{"type": "object", "properties": {}}`.
    """


class ToolAssistantToolsFunction(TypedDict, total=False):
    function: Required[ToolAssistantToolsFunctionFunction]
    """The function definition."""

    type: Required[Literal["function"]]
    """The type of tool being defined: `function`"""


Tool = Union[ToolAssistantToolsCode, ToolAssistantToolsRetrieval, ToolAssistantToolsFunction]
