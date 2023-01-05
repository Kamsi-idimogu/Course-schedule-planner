from collections import defaultdict, deque

class CourseSchedulePlanner:

    def __init__(self, max_course):
        self.courses = set()
        self.in_degree_list = defaultdict(int)
        self.adjList = defaultdict(set)
        self.ordered_courses = []
        self.can_build_graph = False
        self.course_prereqs = {}
        self.schedule = []
        self.max_course_per_semester = max_course


    def isEmpty(input_string):
        return input_string.isspace() or input_string == ''


    def build_adjecency_list(self, prerequisites, current_course):
        for course in prerequisites:
            if self.adjList.get(course) is None:
                self.adjList[course] = { current_course }
                self.in_degree_list[current_course] += 1
            else:
                if current_course not in self.adjList[course]:
                    self.in_degree_list[current_course] += 1

                self.adjList.get(course).add(current_course)
            
            self.courses.add(course)
        
        self.courses.add(current_course)


    def build_schedule(self):
        queue = deque()

        for course in self.courses:
            #Add all courses that have no prerequisites first
            if self.in_degree_list[course] is 0:
                queue.append(course)

        covered_courses = 0

        #Initialize the list of courses to be taken in order
        self.ordered_courses = []

        while queue:
            course = queue.popleft()
            self.ordered_courses.append(course)
            covered_courses += 1

            if course in self.adjList:
                for postrequisite in self.adjList.get(course):
                    self.in_degree_list[postrequisite] -= 1

                    if self.in_degree_list[postrequisite] is 0:
                        queue.append(postrequisite)

        if covered_courses is not len(self.courses):
            print('\nBuild Schedule Failed: Courses can not be taken based on prequisites')
        else:
            self.can_build_graph = True


    #Checks if a course has any prerequisites
    def has_prerequisites(self, course):
        return course in self.course_prereqs and self.course_prereqs[course]


    #Gets a list of courses that have no prerequisites
    def get_safe_courses(self, taken_courses):
        courses = []
        for course in self.courses:
            if course not in self.course_prereqs:
                self.course_prereqs[course] = []

            if not self.has_prerequisites(course) and course not in taken_courses:
                courses.append(course)
        return courses


    #Gets a list of courses that can be taken in the current semester
    def get_current_semester_courses(self, taken_courses):
        courses = []
        for course in self.course_prereqs:
            can_take_course = True
            for prereq in self.course_prereqs[course]:
                if prereq not in taken_courses:
                    can_take_course = False
                    break
            
            if can_take_course and course not in taken_courses:
                courses.append(course)

        return courses

    
    def scheduler(self):
        if not self.can_build_graph:
            print('Unable to display schedule because `build schedule` failed')
            return

        #Initialize a set of taken courses
        taken_courses = set()

        # Initialize semester counter
        semester = 1

        while True:
            #Get courses that have no prerequisites
            no_prerequisite_courses = self.get_safe_courses(taken_courses)

            #Get courses that can be taken this semester
            current_courses = self.get_current_semester_courses(taken_courses)

            #Merge current courses and courses without prerequisites, 
            current_courses = list(set(current_courses + no_prerequisite_courses)) #To remove duplicates

            current_courses.sort()

            self.schedule.append(f'Semester {semester}: {current_courses[:self.max_course_per_semester]}')
            
            taken_courses = taken_courses.union(current_courses[:self.max_course_per_semester])

            semester += 1

            #Check if all course have been taken
            if len(taken_courses) is len(self.courses):
                break

    def display_generated_schedule(self):
        self.scheduler()

        if self.can_build_graph:
            # Build course schedule
            print('\nGENERATED COURSE SCHEDULE => \n{')

            for semester in self.schedule:
                print(semester)

            print('}')

    
