"""Text Generation Module.

This module provides text generation capabilities using
various LLM providers.
"""

from typing import Any


class TextGenerator:
    """Handles text generation with multiple LLM providers."""

    def __init__(self, provider: str = "openai", model: str | None = None):
        """Initialize the TextGenerator.

        Args:
            provider: LLM provider (openai, anthropic).
            model: Specific model name.
        """
        self.provider = provider
        self.model = model or self._get_default_model(provider)

    def _get_default_model(self, provider: str) -> str:
        """Get default model for provider.

        Args:
            provider: Provider name.

        Returns:
            Default model name.
        """
        if provider == "openai":
            return "gpt-4"
        elif provider == "anthropic":
            return "claude-3-opus-20240229"
        return "gpt-4"

    def generate(
        self,
        prompt: str,
        max_tokens: int = 1000,
        temperature: float = 0.7
    ) -> str:
        """Generate text from prompt.

        Args:
            prompt: Input prompt.
            max_tokens: Maximum tokens to generate.
            temperature: Sampling temperature.

        Returns:
            Generated text.
        """
        if self.provider == "openai":
            return self._generate_openai(prompt, max_tokens, temperature)
        elif self.provider == "anthropic":
            return self._generate_anthropic(prompt, max_tokens, temperature)
        return "[Generated text placeholder]"

    def _generate_openai(
        self,
        prompt: str,
        max_tokens: int,
        temperature: float
    ) -> str:
        """Generate using OpenAI API.

        Args:
            prompt: Input prompt.
            max_tokens: Max tokens.
            temperature: Temperature.

        Returns:
            Generated text.
        """
        return f"[OpenAI response for: {prompt[:50]}...]"

    def _generate_anthropic(
        self,
        prompt: str,
        max_tokens: int,
        temperature: float
    ) -> str:
        """Generate using Anthropic API.

        Args:
            prompt: Input prompt.
            max_tokens: Max tokens.
            temperature: Temperature.

        Returns:
            Generated text.
        """
        return f"[Anthropic response for: {prompt[:50]}...]"

    def generate_batch(
        self,
        prompts: list[str],
        max_tokens: int = 1000
    ) -> list[str]:
        """Generate text for multiple prompts.

        Args:
            prompts: List of prompts.
            max_tokens: Max tokens per generation.

        Returns:
            List of generated texts.
        """
        return [self.generate(p, max_tokens) for p in prompts]


class StoryGenerator(TextGenerator):
    """Specialized generator for story writing."""

    def __init__(self, provider: str = "openai"):
        """Initialize StoryGenerator.

        Args:
            provider: LLM provider.
        """
        super().__init__(provider)
        self.system_prompt = "You are a creative story writer."

    def generate_story(
        self,
        premise: str,
        length: str = "medium"
    ) -> str:
        """Generate a story from premise.

        Args:
            premise: Story premise.
            length: Length category (short, medium, long).

        Returns:
            Generated story.
        """
        length_map = {
            "short": 500,
            "medium": 1500,
            "long": 3000
        }
        max_tokens = length_map.get(length, 1500)

        prompt = f"Write a story based on this premise: {premise}"
        return self.generate(prompt, max_tokens=max_tokens)


class CodeGenerator(TextGenerator):
    """Specialized generator for code writing."""

    def __init__(self, provider: str = "openai"):
        """Initialize CodeGenerator.

        Args:
            provider: LLM provider.
        """
        super().__init__(provider)
        self.system_prompt = "You are an expert programmer."

    def generate_code(
        self,
        task: str,
        language: str = "python"
    ) -> str:
        """Generate code for a task.

        Args:
            task: Coding task description.
            language: Programming language.

        Returns:
            Generated code.
        """
        prompt = f"Write {language} code that: {task}"
        return self.generate(prompt, max_tokens=2000)


def create_generator(
    provider: str = "openai",
    model: str | None = None
) -> TextGenerator:
    """Factory function to create generator.

    Args:
        provider: LLM provider.
        model: Optional model name.

    Returns:
        TextGenerator instance.
    """
    return TextGenerator(provider=provider, model=model)
