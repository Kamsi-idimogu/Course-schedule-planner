from CourseSchedulePlanner import CourseSchedulePlanner

print('\nThe Course Schedule Planner creates a schedule for you based on the given course data\n')
print('Courses are inputted in the format:\n\'CourseName: List of prerequisites for the course seperated by comma and space\'')
print(' Example-> CS150: CS101, CS121, MATH140')
print(' Example of course with no prerequisites-> CS101\n')


#Initialize course schedule planner with the max number of courses per semester
schedulePlanner = CourseSchedulePlanner(5)

def isEmpty(input_string):
    return input_string.isspace() or input_string == ''

while (query := input('Enter a course and it\'s prerequisites (enter `q` when finished)> ')) != 'q':
    if query == '':
        continue

    try:
        course_and_prerequites = query.split(': ', 1)
    except ValueError:
        print('Error occured split failed')
        continue
    if ':' in course_and_prerequites[-1] or isEmpty(course_and_prerequites[0]):
        print('invalid input, please try again')
        continue

    try:
        prerequisites = course_and_prerequites[-1].split(', ')
    except ValueError:
        print('Error occured split failed')
        continue
    if isEmpty(prerequisites[0]):
        print('invalid input, please try again')
        continue

    if prerequisites == course_and_prerequites:
        prerequisites = []
        schedulePlanner.course_prereqs[course_and_prerequites[0]] = prerequisites
    else:
        schedulePlanner.course_prereqs[course_and_prerequites[0]] = prerequisites
        prerequisites = set(prerequisites)

    #Build adjecency list
    schedulePlanner.build_adjecency_list(prerequisites, course_and_prerequites[0])

if not schedulePlanner.courses:
    print('\nNo courses were added\n')
    exit()

schedulePlanner.build_schedule()

schedulePlanner.display_generated_schedule()
