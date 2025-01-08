import pytest


class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out


@pytest.mark.parametrize(
    "operations, expected_outputs",
    [
        ([("push", 1), ("push", 2), ("pop",), ("pop",)], [
         None, None, 1, 2]),  # ID: happy_path_push_pop_multiple
        ([("push", 1), ("peek",), ("pop",)], [None, 1, 1]),
        ([("push", 1), ("empty",), ("push", 2), ("empty",)], [
         None, False, None, False]),  # ID: happy_path_empty_check_non_empty
        ([("empty",)], [True]),  # ID: edge_case_empty_check_initially_empty
        ([("push", 1), ("pop",), ("empty",)], [None, 1, True]),
    ],
)
def test_queue_operations(operations, expected_outputs):
    # Arrange
    queue = MyQueue()

    # Act and Assert
    for operation, expected_output in zip(operations, expected_outputs):
        if operation[0] == "push":
            queue.push(operation[1])
            assert queue.stack_in  # Check if the element is pushed

        elif operation[0] == "pop":
            actual_output = queue.pop()
            assert actual_output == expected_output

        elif operation[0] == "peek":
            actual_output = queue.peek()
            assert actual_output == expected_output

        elif operation[0] == "empty":
            actual_output = queue.empty()
            assert actual_output == expected_output


@pytest.mark.parametrize(
    "operations",
    [
        ([("pop",)]),  # ID: error_case_pop_from_empty
        ([("peek",)]),  # ID: error_case_peek_from_empty
    ],
)
def test_queue_operations_empty_queue(operations):

    # Arrange
    queue = MyQueue()

    # Act and Assert
    for operation in operations:
        if operation[0] == "pop":
            # Expecting an error when popping from empty queue
            with pytest.raises(IndexError):
                queue.pop()
        elif operation[0] == "peek":
            # Expecting an error when peeking into empty queue
            with pytest.raises(IndexError):
                queue.peek()
