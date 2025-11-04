from typing import Any, Dict

from graph.chains.generation import generation_chain
from graph.state import GraphState


"""---GENERATING FINAL RESPONSE BY USING RETRIEVED DOCUMENTS AND USER QUESTION THROUGH GENERATION CHAIN---"""

def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]

    generation = generation_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}