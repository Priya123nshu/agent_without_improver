from langgraph import Node
from typing import Dict, Any

class EmailComposer(Node):
    def __init__(self, subject_line_creator: Any, content_generator: Any) -> None:
        """
        Initialize the EmailComposer with dependencies.

        Args:
            subject_line_creator: An instance of SubjectLineCreator.
            content_generator: An instance of ContentGenerator.
        """
        super().__init__()
        self.subject_line_creator = subject_line_creator
        self.content_generator = content_generator

    def compile_email(self, subject_line: str, email_body: str) -> str:
        """
        Compiles the email components into a complete email format.

        Args:
            subject_line (str): The subject line of the email.
            email_body (str): The body content of the email.

        Returns:
            str: The complete formatted email.
        """
        complete_email = f"Subject: {subject_line}\n\n{email_body}"
        return complete_email

    def run(self, inputs: Dict[str, str]) -> Dict[str, str]:
        """
        Run the email composition process.

        Args:
            inputs (Dict[str, str]): A dictionary containing 'subject_line' and 'email_body'.

        Returns:
            Dict[str, str]: A dictionary containing the 'complete_email'.
        """
        subject_line = self.subject_line_creator.create_subject_line(inputs['subject_line'])
        email_body = self.content_generator.generate_content(inputs['email_body'])
        complete_email = self.compile_email(subject_line, email_body)
        return {'complete_email': complete_email}