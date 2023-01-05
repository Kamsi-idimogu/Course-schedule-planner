import sys
from io import StringIO

class CourseScheduleTester:

    def __init__(self, input_str, expected_output_str):
        self.input_str = input_str
        self.expected_output_str = expected_output_str
    
    def test(self):
        # Capture stdout
        stdout_ = sys.stdout
        sys.stdout = StringIO()

        # Call the code to build the course schedule
        exec(self.input_str)

        # Get the output of the code
        output_str = sys.stdout.getvalue()

        # Reset stdout
        sys.stdout = stdout_

        # Compare the expected output and the actual output
        assert self.expected_output_str == output_str