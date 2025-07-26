# Sahayak - AI Teaching Assistant for Indian Classrooms

Sahayak is an intelligent multi-agent AI system designed specifically for teachers in multi-grade, low-resource classrooms across India. It provides culturally relevant educational content and explanations in local languages, making teaching more effective and engaging.

## 🌟 Features

### 🤖 Multi-Agent Architecture
- **Coordinator Agent**: Intelligently routes teacher requests to appropriate specialized agents
- **HyperLocal Content Agent**: Creates culturally relevant educational content in local languages
- **Knowledge Base Agent**: Provides simple, analogy-rich explanations for complex concepts

### 🎯 Key Capabilities
- **Content Generation**: Stories, poems, activities, and examples customized for local contexts
- **Multi-language Support**: Hindi, Marathi, Kannada, Tamil, Bengali, and more
- **Grade-appropriate Content**: Tailored for different grade levels (Grade 1-12)
- **Cultural Relevance**: Content adapted to rural, tribal, and urban Indian contexts
- **Interactive Sessions**: Maintains conversation history and context

## 🏗️ Architecture

```
sahayak/
├── main.py                          # Vertex AI deployment configuration
├── interactive.py                   # Interactive CLI interface
├── requirements.txt                 # Python dependencies
├── utils.py                         # Utility functions for session management
└── sahayak_manager/
    ├── __init__.py
    ├── agent.py                     # Root coordinator agent
    ├── prompt.py                    # Main agent prompts
    └── sub_agents/
        ├── hyper_local_content_agent/
        │   ├── agent.py            # Content generation agent
        │   └── prompt.py           # Content generation prompts
        └── knowledge_base_agent/
            ├── agent.py            # Knowledge explanation agent
            └── prompt.py           # Knowledge base prompts
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Cloud Platform account
- Vertex AI API enabled

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sahayak
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud credentials**
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
   ```

4. **Configure environment variables**
   ```bash
   # Create a .env file with your GCP project details
   PROJECT_ID="your-project-id"
   LOCATION="asia-south1"
   STAGING_BUCKET="gs://your-bucket-name"
   ```

### Running the Application

#### Interactive Mode (Recommended for testing)
```bash
python interactive.py
```

#### Deploy to Vertex AI
```bash
python main.py
```

## 📖 Usage Examples

### Content Generation Requests
```
You: Create a story in Marathi about rivers for Grade 4
Sahayak: [Generates a culturally relevant Marathi story about rivers]

You: Make a poem in Hindi to teach subtraction for Grade 2
Sahayak: [Creates a rhyming Hindi poem about subtraction]
```

### Knowledge Questions
```
You: Why do we sweat?
Sahayak: [Provides simple explanation with daily life analogies]

You: Explain photosynthesis in Bengali
Sahayak: [Explains the concept in Bengali with local examples]
```

### Casual Interaction
```
You: Hello
Sahayak: Namaste! How can I help you today?
```

## 🔧 Configuration

### Agent Models
The system uses Google's Gemini 2.0 Flash model by default. You can modify the model in each agent file:

```python
# In agent.py files
model = "gemini-2.0-flash"
# Alternative: model = LiteLlm(model="ollama/gemma3:4b")
```

### Supported Languages
- Hindi (default)
- Marathi
- Kannada
- Tamil
- Bengali
- English
- And more...

### Grade Levels
- Grade 1-12
- Multi-grade classroom support
- Age-appropriate content generation

## 🛠️ Development

### Adding New Agents
1. Create a new directory in `sahayak_manager/sub_agents/`
2. Add `agent.py` and `prompt.py` files
3. Import and add to the root agent's sub_agents list

### Customizing Prompts
Edit the prompt files in each agent directory to modify behavior:
- `sahayak_manager/prompt.py` - Main coordinator logic
- `sahayak_manager/sub_agents/*/prompt.py` - Specialized agent prompts

### Session Management
The system includes utilities for managing conversation history:
- `add_user_query_to_history()` - Track user inputs
- `add_agent_response_to_history()` - Track agent responses
- Session state persistence

## 🌍 Cultural Adaptation

Sahayak is specifically designed for Indian educational contexts:

- **Local Examples**: Uses village life, farming, weather, and daily activities
- **Cultural Sensitivity**: Respects diverse Indian cultures and traditions
- **Language Support**: Native language content creation
- **Grade Appropriateness**: Content tailored to Indian curriculum standards

## 📊 Performance

- **Response Time**: Typically 2-5 seconds for content generation
- **Accuracy**: High-quality, culturally relevant content
- **Scalability**: Built on Google Cloud infrastructure
- **Reliability**: Robust error handling and session management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Cloud Platform for infrastructure
- Vertex AI for agent deployment
- Indian teachers and educators for domain expertise
- Open source community for tools and libraries

## 📞 Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation for common solutions

---

**Sahayak** - Empowering Indian teachers with AI-powered educational assistance. 🌟
