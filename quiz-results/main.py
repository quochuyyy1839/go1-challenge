import json

# Define a function to find the index of the easiest question based on correct answers and learner responses
def easiest_question(correct_answers, learner_responses):
    # Determine the total number of questions
    num_questions = len(correct_answers)
    # Initialize a list to store the count of correct responses for each question
    correct_counts = [0] * num_questions
    
    # Iterate through each learner's response
    for response in learner_responses:
        # Iterate through each question and its corresponding answer in the response
        for i, answer in enumerate(response):
            # Check if the answer matches the correct answer for the question
            if answer == correct_answers[i]:
                # If the answer is correct, increment the count of correct responses for that question
                correct_counts[i] += 1
    
    # Find the index of the question with the maximum count of correct responses
    easiest_index = correct_counts.index(max(correct_counts))
    
    # Return a string indicating the index of the easiest question
    return f"The easiest question is index {easiest_index}"

# Read data from JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Get correct_answers and learner_responses from the JSON data
correct_answers = data["correct_answers"]
learner_responses = data["learner_responses"]

# Call the function with data from the JSON file and print the result
print(easiest_question(correct_answers, learner_responses))
