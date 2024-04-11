import json

def most_common_next_course(session_data):
    next_course_counts = {}  # Create a dictionary to store the count of occurrences of next courses for each course

    # Iterate through each study session
    for session in session_data:
        # Iterate through each course in the study session
        for i in range(len(session) - 1):
            current_course = session[i]
            next_course = session[i + 1]

            # Increase the count of next_course for current_course
            if current_course in next_course_counts:
                if next_course in next_course_counts[current_course]:
                    next_course_counts[current_course][next_course] += 1
                else:
                    next_course_counts[current_course][next_course] = 1
            else:
                next_course_counts[current_course] = {next_course: 1}

    # Find the most common next course for each course
    most_common_next = {}
    for current_course, next_courses in next_course_counts.items():
        most_common_next[current_course] = max(next_courses, key=next_courses.get)

    return most_common_next

# Read input from file
with open("data.json", "r") as file:
    session_data = json.load(file)

# Call the function and print the result
print(most_common_next_course(session_data))
