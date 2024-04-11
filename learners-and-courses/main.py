import json

def find_courses_completed_by_single_learner(data):
    # Create a dictionary to store the number of learners who have completed each course
    course_learners = {}
    for learner, courses in data.items():
        for course in courses:
            if course in course_learners:
                course_learners[course].add(learner)
            else:
                course_learners[course] = {learner}
    
    # Filter out courses completed by only one learner
    single_learner_courses = [course for course, learners in course_learners.items() if len(learners) == 1]
    
    return single_learner_courses

# Read data from JSON file
with open("data.json", "r") as file:
    input_data = json.load(file)

# Call the function with the input data
output = find_courses_completed_by_single_learner(input_data)
print(output)
