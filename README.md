
---

# Conversational Engine

This module powers conversational interactions, supporting queries, context-based responses, and integration with AI models like OpenAI and Ollama. It is designed for modularity and scalability, allowing seamless embedding into a generic intelligence framework or running as a standalone service.

## Features
- **Multimodal Input Support**: Accepts text input from the console, APIs, voice (via STT modules), and internal NOVA subsystems.
- **AI Model Integration**: Combines OpenAI and Ollama responses to generate enriched outputs.
- **Context-Aware**: Leverages user and system contexts for more personalized and relevant interactions.
- **Conversation History**: Tracks and persists conversation exchanges for continuity across sessions.

---

## How It Works
1. **Input Handling**: Captures user queries from multiple sources and preprocesses them with context enrichment.
2. **Core Engine Processing**:
   - Routes the query to the preferred AI engine (OpenAI, Ollama, or both).
   - Combines responses if both engines are used.
3. **Output Generation**: Returns a structured and meaningful response to the user or calling subsystem.
4. **Conversation History**: Stores exchanges for reference and future interactions.

---

## File Structure
```plaintext
.
├── engine/
│   ├── core_engine.py         # Main processing logic for queries
├── modules/
│       ├── openai.py          # Integration with OpenAI
│       ├── ollama.py          # Integration with Ollama
├── protocols/
│   ├── conversation_history.py # Tracks and saves conversational exchanges
├── main.py                    # Entry point for running the engine
├── README.md                  # Description of the project
└── requirements.txt           # Required Python libraries
```

---

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- API keys for OpenAI
- Ollama server on localhost

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/user2745/conversational-engine.git
   cd conversational-engine
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
1. Set your API keys in the environment variables:
   ```bash
   export OPENAI_API_KEY="your-openai-key"
   ```
2. (Optional) Customize conversation history settings in `conversation_history.py`.

---

## Usage

### Standalone Mode
Run the module directly for command-line interaction:
```bash
python main.py
```
---

## Future Enhancements
- Add support for multimodal inputs (text + voice + images).
- Optimize AI engine combination logic for faster responses.
- Implement more robust error handling and fallback mechanisms.

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bug fixes, enhancements, or ideas.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
