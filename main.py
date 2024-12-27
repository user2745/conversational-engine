from engine.core_engine import CoreEngine
import os

def run_conversational_ai():
    # Initialize the engine
    engine = CoreEngine(max_history_length=50)

    # Load conversation history from a file (if available)
    history_file = "conversation_history.json"
    if os.path.exists(history_file):
        engine.load_history(history_file)

    # Start the interactive session
    print("Welcome to the Conversational AI System!")
    try:
        while True:
            # Capture user input
            query = input("Enter your query ('exit' to quit): ")
            if query.lower() == "exit":
                print("Saving your conversation history...")
                engine.save_history(history_file)
                print("Goodbye!")
                break

            # Process the query using the Core Engine
            response = engine.process_query(query, engine_preference=None)
            print(f"\nAI Response:\n{response}\n")
    finally:
        # Save conversation history to file on exit
        engine.save_history(history_file)

if __name__ == "__main__":
    run_conversational_ai()
