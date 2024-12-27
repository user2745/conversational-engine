from openai import OpenAI
client = OpenAI()
model = "gpt-4o-mini"
max_tokens = 150
temperature = 0.7
top_p = 1



def query_openai(prompt):

    # Query the OpenAI API
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            response_format={
                "type": "text"
            },
            temperature=temperature,
            max_completion_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=0,
            presence_penalty=0,
        );
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error querying OpenAI: {e}"