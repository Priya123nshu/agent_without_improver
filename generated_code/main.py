# Auto-generated LangGraph Orchestrator
from langgraph.graph import StateGraph, END
from typing import Dict, Any

graph = StateGraph()
from emailcontextanalyzer import EmailContextAnalyzer
graph.add_node("EmailContextAnalyzer", EmailContextAnalyzer)
from toneselector import ToneSelector
graph.add_node("ToneSelector", ToneSelector)
from contentgenerator import ContentGenerator
graph.add_node("ContentGenerator", ContentGenerator)
from subjectlinecreator import SubjectLineCreator
graph.add_node("SubjectLineCreator", SubjectLineCreator)
from emailcomposer import EmailComposer
graph.add_node("EmailComposer", EmailComposer)
from emailvalidator import EmailValidator
graph.add_node("EmailValidator", EmailValidator)
from emaildispatcher import EmailDispatcher
graph.add_node("EmailDispatcher", EmailDispatcher)
graph.add_edge("EmailContextAnalyzer", "ToneSelector")
graph.add_edge("ToneSelector", "ContentGenerator")
graph.add_edge("ContentGenerator", "SubjectLineCreator")
graph.add_edge("SubjectLineCreator", "EmailComposer")
graph.add_edge("EmailComposer", "EmailValidator")
graph.add_edge("EmailValidator", "EmailDispatcher")
graph.set_entry_point("EmailContextAnalyzer")
graph.add_edge("EmailDispatcher", END)

if __name__ == '__main__':
    result = graph.run({'input': 'start'})
    print(result)