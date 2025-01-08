import pytest


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


@pytest.mark.parametrize(
    "operations, expected_outputs",
    [
        (
            [("push", 3), ("push", 5), ("getMin",), ("push", 2), ("push", 1),
             ("getMin",), ("pop",), ("getMin",), ("pop",), ("top",)],
            [None, None, 3, None, None, 1, None, 2, None, 2]
        ),  # ID: happy_path_mixed_operations
        ([("push", 1)], [None]),  # ID: edge_case_single_push
        ([("push", 1), ("pop",)], [None, None]),  # ID: edge_case_push_pop
        ([("push", 1), ("top",)], [None, 1]),  # ID: edge_case_push_top
        # ID: edge_case_push_getMin_single_element
        ([("push", 1), ("getMin",)], [None, 1]),
    ],
)
def test_min_stack_operations(operations, expected_outputs):

    # Arrange
    stack = MinStack()

    # Act and Assert
    for operation, expected_output in zip(operations, expected_outputs):
        if operation[0] == "push":

            stack.push(operation[1])
            assert operation[1] in stack.stack

        elif operation[0] == "pop":
            stack.pop()
            if expected_outputs.index(expected_output) + 1 < len(expected_outputs):
                assert len(stack.stack) == len(
                    operations) - (expected_outputs.index(expected_output) + 2)  # Check stack size after pop

        elif operation[0] == "top":
            actual_output = stack.top()
            assert actual_output == expected_output

        elif operation[0] == "getMin":
            actual_output = stack.getMin()
            assert actual_output == expected_output


@pytest.mark.parametrize(
    "operations",
    [
        ([("pop",)]),  # ID: error_case_pop_from_empty
        ([("top",)]),  # ID: error_case_top_from_empty
        ([("getMin",)]),  # ID: error_case_getMin_from_empty
    ],
)
def test_min_stack_operations_empty_stack(operations):

    stack = MinStack()

    for operation in operations:
        if operation[0] == "pop":
            with pytest.raises(IndexError):
                stack.pop()
        elif operation[0] == "top":
            with pytest.raises(IndexError):
                stack.top()
        elif operation[0] == "getMin":
            with pytest.raises(ValueError):
                stack.getMin()
