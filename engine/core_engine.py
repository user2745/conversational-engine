from protocols.conversation_history import ConversationHistory
from modules.openai import query_openai
from modules.ollama import query_ollama
import os


class CoreEngine:
    def __init__(self, max_history_length=50):
        # Initialize conversation history
        self.conversation = ConversationHistory(max_length=max_history_length)

    def process_query(self, query, engine_preference=None):
        """
        Process a query using either OpenAI, Ollama, or both engines.
        """
        try:
            # Step 1: Add user query to the history
            self.conversation.add_exchange("user", query)

            # Step 2: Decide which engine(s) to use
            if engine_preference == "openai":
                response = query_openai(query)
            elif engine_preference == "ollama":
                response = query_ollama(query)
            else:
                # Default: Use both engines and merge responses
                response_openai = query_openai(query)
                response_ollama = query_ollama(query)
                response = self.merge_responses(response_openai, response_ollama)

            # Step 3: Add assistant response to the history
            self.conversation.add_exchange("assistant", response)

            # Step 4: Return the response
            return response
        except Exception as e:
            return f"Core Engine Error: {e}"

    @staticmethod
    def merge_responses(openai_response, ollama_response):
        """
        Combine responses from OpenAI and Ollama into a single enhanced output.
        """
        if openai_response == ollama_response:
            return openai_response
        return f"{openai_response} Additionally, Ollama noted: {ollama_response}"

    def save_history(self, file_path):
        """
        Save conversation history to a file.
        """
        self.conversation.save_to_file(file_path)

    def load_history(self, file_path):
        """
        Load conversation history from a file.
        """
        if os.path.exists(file_path):
            self.conversation.load_from_file(file_path)
            print("Loaded previous conversation history.")
