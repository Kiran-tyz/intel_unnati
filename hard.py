import random
from hard_questions import hard_questions 

def generate_easy_mcq():
    question_data = random.choice(hard_questions)
    question = question_data["question"]
    options = question_data["options"].copy() 
    random.shuffle(options) 
    answer = question_data["answer"]
    
    return {
        "question": question,
        "options": options,
        "correct_answer": answer
    }

if __name__ == "__main__":  
    mcq = generate_easy_mcq()
    print("Question:", mcq["question"])
    for i, option in enumerate(mcq["options"], 1):
        print(f"{i}. {option}")
    print("Answer:", mcq["correct_answer"])  
