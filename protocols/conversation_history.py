from collections import deque
import json

class ConversationHistory:
    """
    A self-updating protocol for managing conversation history.
    """
    def __init__(self, max_length=50):
        """
        Initialize conversation history with a maximum length.
        """
        self.history = deque(maxlen=max_length)

    def add_exchange(self, role, content):
        """
        Add a new message to the conversation history.
        
        Parameters:
        - role: "user" or "assistant"
        - content: The message content
        """
        self.history.append({"role": role, "content": content})
        print(f"Updated conversation history: {self.history}")  # Debugging


    def get_recent(self, n=5):
        """
        Retrieve the most recent `n` exchanges.
        
        Parameters:
        - n: Number of exchanges to retrieve
        Returns:
        - List of recent exchanges
        """
        return list(self.history)[-n:]

    def serialize(self):
        """
        Serialize the history into a JSON-compatible format.
        
        Returns:
        - List of conversation history
        """
        return list(self.history)

    def load_from_file(self, filepath):
        """
        Load history from a JSON file.
        
        Parameters:
        - filepath: Path to the JSON file
        """
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                self.history = deque(data, maxlen=self.history.maxlen)
        except Exception as e:
            print(f"Error loading conversation history: {e}")

    def save_to_file(self, filepath):
        """
        Save history to a JSON file.
        """
        try:
            print(f"Saving history to {filepath}...")  # Debugging
            with open(filepath, "w") as f:
                json.dump(self.serialize(), f, indent=4)
            print(f"History successfully saved: {self.serialize()}")  # Debugging
        except Exception as e:
            print(f"Error saving conversation history: {e}")
