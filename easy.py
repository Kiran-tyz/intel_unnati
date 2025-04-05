
import random
from easy_questions import easy_questions  # Importing the list from the other file

# Function to generate a random MCQ
def generate_easy_mcq():
    question_data = random.choice(easy_questions)
    question = question_data["question"]
    options = question_data["options"].copy()  # Copy to avoid modifying original list
    random.shuffle(options)  # Shuffle options
    answer = question_data["answer"]
    
    return {
        "question": question,
        "options": options,
        "correct_answer": answer
    }

# Example usage
if __name__ == "__main__":  # Correct name check
    mcq = generate_easy_mcq()
    print("Question:", mcq["question"])
    for i, option in enumerate(mcq["options"], 1):
        print(f"{i}. {option}")
    print("Answer:", mcq["correct_answer"])  # Optional: Hide in UI
