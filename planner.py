import pandas as pd
import random

# Load the course data from the Excel file
file_path = '/Users/shreyhanlakhina/Dropbox/CWRUplanner/test.csv'
df = pd.read_csv(file_path)

# Initialize lists to store filtered courses based on user preferences
filtered_courses = []

# Function to filter courses based on credit hours
def filter_by_credit_hours(min_credits, max_credits):
    return df[(df['credit_hours'] >= min_credits) & (df['credit_hours'] <= max_credits)]

# Function to filter courses based on category (e.g., 'requirement')
def filter_by_category(category):
    return df[df['category'] == category]

# Function to display the final course schedule
def display_schedule(course_list, num_courses=5):
    print("Your personalized class schedule is as follows:")
    for i in range(num_courses):
        random_course = random.choice(course_list)
        print(f"Course {i+1}: {random_course['course_code']} - {random_course['name']}")
        course_list.remove(random_course)

# Main function to get user input and create the schedule
def create_schedule():
    print("Welcome to your personalized class schedule creator!")
    
    # Simulated user input
    min_credits = 3  # Simulating input for minimum credit hours
    max_credits = 4  # Simulating input for maximum credit hours
    
    # Filter courses based on the user's credit hour preference
    filtered_courses_by_credits = filter_by_credit_hours(min_credits, max_credits)
    
    # Simulated input for course category preference
    category_preference = 'requirement'  # Simulating input for category (e.g., 'requirement')
    
    # Filter courses by category
    filtered_courses_by_category = filter_by_category(category_preference)
    
    # Combine the filters to get the final course list
    filtered_courses = pd.merge(filtered_courses_by_credits, filtered_courses_by_category, how='inner')
    
    if not filtered_courses.empty:
        # Convert the DataFrame to a list of dictionaries for easy access
        course_list = filtered_courses.to_dict('records')
        
        # Display the final schedule with 5 random courses
        display_schedule(course_list, num_courses=5)
    else:
        print("No courses found that match your preferences. Try adjusting the filters.")

# Run the schedule creator
create_schedule()
