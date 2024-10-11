import pandas as pd
import random

# Load the CSV file
df = pd.read_csv('/Users/shreyhanlakhina/Dropbox/CWRUplanner/test.csv')

# Function to process the course selection based on the category format
def pick_courses(df, category, num_pick=None):
    available_courses = df[df['category'] == category]
    if num_pick and len(available_courses) >= num_pick:
        return available_courses.sample(n=num_pick)
    elif num_pick:
        print(f"Not enough courses in {category}, returning all available courses")
        return available_courses
    return available_courses


# Select all required courses
required_courses = pick_courses(df, 'requirement')

# Process the categories that require picking specific numbers of courses
# Example: pick 1 from each of these categories
calc2_pick1 = pick_courses(df, 'calc2_pick1', 1)
linearalgebra_pick1 = pick_courses(df, 'linearalgebra_pick1', 1)
calc3_pick1 = pick_courses(df, 'calc3_pick1', 1)
stats_pick1 = pick_courses(df, 'stats_pick1', 1)
security_pick1 = pick_courses(df, 'security_pick1', 1)
brearea1 = pick_courses(df, 'brarea1_pick2', 2)
brearea2 = pick_courses(df, 'brarea2_pick2', 2)
brearea3 = pick_courses(df, 'brarea3_pick2', 2)
brearea4 = pick_courses(df, 'brarea4_pick2', 2)

# Process categories that require picking a range of courses (e.g., pick 4 to 6 courses)
gr1 = random.randint(4, 6)
gr2 = 6-gr1
csdsgroup1_pick = pick_courses(df, 'csdsgroup1_pick4:6', gr1)
csdsgroup2_pick = pick_courses(df, 'csdsgroup2_pick0:2', gr2)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

# Combine all selected courses
final_schedule = pd.concat([
    required_courses,
    calc2_pick1,
    linearalgebra_pick1,
    calc3_pick1,
    stats_pick1,
    brearea1,
    brearea2,
    brearea3,
    brearea4,
    security_pick1,
    csdsgroup1_pick,
    csdsgroup2_pick
])

# Display the final list of chosen courses
print("Final Course Schedule:")
print(final_schedule[['course_code', 'name']])
