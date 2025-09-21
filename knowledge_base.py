# -------------------------------
# Knowledge Base (Offline Memory)
# -------------------------------

class KnowledgeBase:
    def __init__(self):
        self.data = {
            "hello": "Hi there! How can I help you?",
            "who are you": "I am a simple Q&A bot built using Python and Hugging Face.",
            "what is ai": "AI stands for Artificial Intelligence, the simulation of human intelligence in machines."
        }

    def get_answer(self, query: str):
        """
        Check if the query matches anything in our offline KB.
        """
        for key, value in self.data.items():
            if key in query.lower():
                return value
        return None
