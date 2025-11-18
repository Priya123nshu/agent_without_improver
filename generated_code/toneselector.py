```python
from typing import Any, Dict
from langgraph import Node
from EmailContextAnalyzer import EmailContextAnalyzer

class ToneSelector(Node):
    def __init__(self, analyzer: EmailContextAnalyzer):
        super().__init__()
        self.analyzer = analyzer

    def select_tone(self, context_analysis: Dict[str, Any]) -> str:
        """
        Selects the appropriate tone for the email based on context analysis.

        Args:
            context_analysis (Dict[str, Any]): The analysis result containing context details.

        Returns:
            str: The selected tone for the email (e.g., 'formal', 'informal', 'persuasive').
        """
        tone = self.analyze_context(context_analysis)
        return tone

    def analyze_context(self, context_analysis: Dict[str, Any]) -> str:
        """
        Analyzes the context and determines the tone.

        Args:
            context_analysis (Dict[str, Any]): The analysis result containing context details.

        Returns:
            str: The determined tone.
        """
        # Example logic, this can be more sophisticated based on actual analysis
        if context_analysis.get('urgency', False):
            return 'persuasive'
        elif context_analysis.get('audience_type') == 'professional':
            return 'formal'
        else:
            return 'informal'

    def run(self, context_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the tone selection process.

        Args:
            context_analysis (Dict[str, Any]): The analysis result containing context details.

        Returns:
            Dict[str, Any]: Contains 'selected_tone' as the output.
        """
        selected_tone = self.select_tone(context_analysis)
        return {'selected_tone': selected_tone}
```