import openai

def gpt_query(prompt, model="text-davinci-003", max_tokens=100):
    """
    Function to interact with GPT API.
    
    Args:
    prompt (str): The prompt to send to the model.
    model (str, optional): The model to use. Defaults to "text-davinci-003".
    max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 100.
    
    Returns:
    str: The response from the model.
    """
    openai.api_key = "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"  # Replace with your actual API key

    response = openai.completions.create(
        model=model,
        prompt=prompt,
        max_tokens=max_tokens
    )
    
    return response.choices[0].text.strip()

# Example usage
example_prompt = "Translate 'Hello World' into Spanish."
response = gpt_query(example_prompt)
print("Prompt:", example_prompt)
print("Response:", response)
