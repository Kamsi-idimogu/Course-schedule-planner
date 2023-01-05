from CourseScheduleTester import CourseScheduleTester
from CourseSchedulePlanner import CourseSchedulePlanner


#Test case 1
#basic course schedule with no prerequisites
def test_1():
    schedule_planner = CourseSchedulePlanner(5)

    input_file = open('test_files/test_input_1.txt', 'r')

    for line in input_file:
        course, prereq = get_course_and_prerequisite(line)

        schedule_planner.course_prereqs[course] = prereq
        prereq = set(prereq)

        schedule_planner.build_adjecency_list(prereq, course)

    input_file.close()

    schedule_planner.build_schedule()
    schedule_planner.scheduler()

    tester = CourseScheduleTester(schedule_planner.schedule[0], "Semester 1: ['CS101', 'CS121', 'CS150']")
    tester.test()


#Test case 2
#course schedule with more than five courses 
def test_2():
    schedule_planner = CourseSchedulePlanner(5)

    input_file = open('test_files/test_input_2.txt', 'r')

    for line in input_file:
        course, prereq = get_course_and_prerequisite(line)

        schedule_planner.course_prereqs[course] = prereq
        prereq = set(prereq)

        schedule_planner.build_adjecency_list(prereq, course)

    input_file.close()

    schedule_planner.build_schedule()
    schedule_planner.scheduler()

    semester1 = CourseScheduleTester(schedule_planner.schedule[0], "Semester 1: ['CS101', 'CS121', 'CS150', 'CS171', 'CS201']")
    semester2 = CourseScheduleTester(schedule_planner.schedule[1], "Semester 2: ['ELE200', 'MATH140']")

    semester1.test()
    semester2.test()


#Test case 3.1
#course schedule with prerequisites
def test_3_1():
    schedule_planner = CourseSchedulePlanner(5)

    input_file = open('test_files/test_input_3.txt', 'r')

    for line in input_file:
        course, prereq = get_course_and_prerequisite(line)

        schedule_planner.course_prereqs[course] = prereq
        prereq = set(prereq)

        schedule_planner.build_adjecency_list(prereq, course)

    input_file.close()

    schedule_planner.build_schedule()
    schedule_planner.scheduler()

    semester1 = CourseScheduleTester(schedule_planner.schedule[0], "Semester 1: ['CS100', 'CS101', 'CS121', 'CS171', 'MATH140']")
    semester2 = CourseScheduleTester(schedule_planner.schedule[1], "Semester 2: ['CS150']")
    semester3 = CourseScheduleTester(schedule_planner.schedule[2], "Semester 3: ['CS180']")

    semester1.test()
    semester2.test()
    semester3.test()


#Test case 3.2
#course schedule with prerequisites
def test_3_2():
    schedule_planner = CourseSchedulePlanner(5)

    input_file = open('test_files/test_input_4.txt', 'r')

    for line in input_file:
        course, prereq = get_course_and_prerequisite(line)

        schedule_planner.course_prereqs[course] = prereq
        prereq = set(prereq)

        schedule_planner.build_adjecency_list(prereq, course)

    input_file.close()

    schedule_planner.build_schedule()
    schedule_planner.scheduler()

    semester1 = CourseScheduleTester(schedule_planner.schedule[0], "Semester 1: ['CS101']")
    semester2 = CourseScheduleTester(schedule_planner.schedule[1], "Semester 2: ['CS110', 'CS111']")
    semester3 = CourseScheduleTester(schedule_planner.schedule[2], "Semester 3: ['CS121']")

    semester1.test()
    semester2.test()
    semester3.test()


#Test case 4
#course schedule with multiple semesters and courses with miltiple prerequisites
def test_4():
    schedule_planner = CourseSchedulePlanner(5)

    input_file = open('test_files/test_input_5.txt', 'r')

    for line in input_file:
        course, prereq = get_course_and_prerequisite(line)

        schedule_planner.course_prereqs[course] = prereq
        prereq = set(prereq)

        schedule_planner.build_adjecency_list(prereq, course)

    input_file.close()

    schedule_planner.build_schedule()
    schedule_planner.scheduler()

    semester1 = CourseScheduleTester(schedule_planner.schedule[0], "Semester 1: ['CS101']")
    semester2 = CourseScheduleTester(schedule_planner.schedule[1], "Semester 2: ['CS110', 'CS111']")
    semester3 = CourseScheduleTester(schedule_planner.schedule[2], "Semester 3: ['CS121']")
    semester4 = CourseScheduleTester(schedule_planner.schedule[3], "Semester 4: ['CS150', 'CS171']")

    semester1.test()
    semester2.test()
    semester3.test()
    semester4.test()


def get_course_and_prerequisite(input_str):
    input_str = input_str[:-1]
    course_and_prereq = input_str.split(': ')
    course = course_and_prereq[0]

    if len(course_and_prereq) == 1:
        prerequisite = []
    else:
        prerequisite = course_and_prereq[-1].split(', ')
    
    return course, prerequisite