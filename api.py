import os
from openai import OpenAI

def generate_easy_science_mcq():
    # Get the OpenAI API key from environment variables. 
    # It should be stored as an environment variable named 'OPENAI_API_KEY'.
    api_key = os.environ["openmcq"]  
    client = OpenAI(api_key=api_key)
    
    prompt = (
        "Generate an easy science-based multiple-choice question for kids (1st-4th grade). "
        "Format:\nQuestion: <Your question here>\n"
        "A) <Option 1>\nB) <Option 2>\nC) <Option 3>\nD) <Option 4>\n"
        "Answer: <Correct option letter>"
    )
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI that generates multiple-choice science questions for kids."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,  # Keeps responses varied yet accurate
        max_tokens=150,   # Ensures concise output
        top_p=1
    )
    
    return response.choices[0].message.content

# Example usage
mcq_question = generate_easy_science_mcq()
print(mcq_question)