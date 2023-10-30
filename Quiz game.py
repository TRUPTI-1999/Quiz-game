Questions = [
    "In which year did India gain independence from British rule?",
    "What is the capital city of India?",
    "Who was the first Prime Minister of India?",
    "Which animal is known as the 'ship of the desert'?",
    "Which planet in the solar system is the hottest?",
    "Which word means the same as 'tiny'?"
]  # You can make Any Questions and Answers

Options = [
    ["A. 1974", "B. 1847", "C. 1947", "D. 1948"],
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Bangalore"],
    ["A. Indira Gandhi", "B. Jawaharlal Nehru", "C. Rajiv Gandhi", "D. Sardar Patel"],
    ["A. Camel", "B. Elephant", "C. Horse", "D. Tiger"],
    ["A. Mercury", "B. Mars", "C. Earth", "D. Venus"],
    ["A. Huge", "B. Fast", "C. Small", "D. Strong"]
]
Answers = ["C", "B", "B", "A", "D", "C"]

score = 0

for i in range(len(Questions)):
    print("______________________ ")
    print(Questions[i])
    
    for option in Options[i]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
if guess == Answers[     i       ]:
        print("Correct!")
        score += 1
else:
        print(f"Wrong! The correct answer is {Answers[i]}")

print("\nQuiz complete!")
print("Your score is:",score /len(Questions))

