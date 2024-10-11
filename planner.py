import pandas as pd
import random

# Load the CSV file
df = pd.read_csv('/Users/shreyhanlakhina/Dropbox/CWRUplanner/test.csv')

# Function to process the course selection based on the category format
def pick_courses(df, category, num_pick=None):
    if num_pick:
        return df[df['category'] == category].sample(n=num_pick)
    return df[df['category'] == category]

# Select all required courses
required_courses = pick_courses(df, 'requirement')

# Process the categories that require picking specific numbers of courses
# Example: pick 1 from each of these categories
calc2_pick1 = pick_courses(df, 'calc2_pick1', 1)
linearalgebra_pick1 = pick_courses(df, 'linearalgebra_pick1', 1)
calc3_pick1 = pick_courses(df, 'calc3_pick1', 1)
stats_pick1 = pick_courses(df, 'stats_pick1', 1)
security_pick1 = pick_courses(df, 'security_pick1', 1)

# Process categories that require picking a range of courses (e.g., pick 4 to 6 courses)
csdsgroup1_pick = pick_courses(df, 'csdsgroup1_pick4:6', random.randint(4, 6))
csdsgroup2_pick = pick_courses(df, 'csdsgroup2_pick0:2', random.randint(0, 2))

# Combine all selected courses
final_schedule = pd.concat([
    required_courses,
    calc2_pick1,
    linearalgebra_pick1,
    calc3_pick1,
    stats_pick1,
    security_pick1,
    csdsgroup1_pick,
    csdsgroup2_pick
])

# Display the final list of chosen courses
print("Final Course Schedule:")
print(final_schedule[['course_code', 'name']])
