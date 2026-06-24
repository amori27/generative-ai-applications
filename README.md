# Generative AI Applications

Production-ready generative AI applications including text generation, image generation, and LLM integration using OpenAI, Anthropic, and open-source models.

## Description

A comprehensive toolkit for building generative AI applications featuring large language model integration, text generation pipelines, prompt engineering utilities, and image generation capabilities with Stable Diffusion.

## Skills & Technologies

- Python 3.9+
- OpenAI API
- Anthropic Claude
- LangChain
- Stable Diffusion
- Hugging Face Transformers
- Text Generation
- Image Generation

## Installation

```bash
git clone https://github.com/AmirAsaad/generative-ai-applications.git
cd generative-ai-applications
pip install -r requirements.txt
```

## Usage

### Text Generation

```python
from src.text_generator import TextGenerator

generator = TextGenerator(provider="openai")
output = generator.generate("Write a short story about AI")
```

### Image Generation

```python
from src.image_generator import ImageGenerator

img_gen = ImageGenerator()
img_gen.generate("A futuristic city at sunset")
```

## Project Structure

```
generative-ai-applications/
├── src/
│   ├── text_generator.py      # Text generation
│   ├── image_generator.py     # Image generation
│   ├── llm_client.py          # LLM clients
│   └── prompts.py             # Prompt management
├── requirements.txt
└── README.md
```

## References

- [OpenAI API](https://platform.openai.com/docs/)
- [Anthropic Claude](https://docs.anthropic.com/)
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)

## License

MIT License
