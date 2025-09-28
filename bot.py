import streamlit.st
from transformers import logging
logging.set_verbosity_error()  # Only show errors, hide info/warnings

from knowledge_base import KnowledgeBase
from websearch import WebSearch
from retriever import Retriever

# -------------------------------
# Main Q&A Bot
# -------------------------------
class QABot:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.search = WebSearch()
        self.retriever = Retriever()
        self.history = []

    def ask(self, query: str):
        """
        Process user query -> check KB -> search web -> rank results.
        """
        # Step 1: Check Knowledge Base
        kb_answer = self.kb.get_answer(query)
        if kb_answer:
            self.history.append((query, kb_answer))
            return kb_answer

        # Step 2: Web Search
        urls = self.search.get_top_links(query)
        summaries = []
        for url in urls:
            summary = self.search.fetch_and_summarize(url)
            if summary:
                summaries.append(summary)

        if not summaries:
            return "Sorry, I couldn't find relevant information."

        # Step 3: Rank using embeddings
        best_answer = self.retriever.rank_summaries(query, summaries)

        # Step 4: Save in history
        self.history.append((query, best_answer))
        return best_answer

    def show_history(self):
        return self.history
