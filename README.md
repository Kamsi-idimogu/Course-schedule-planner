# Course Schedule Planner

This project generates a course schedule based on the given user inputs. The schedule is grouped by semester and has a default maximum of five courses per semester.

## Requirements
* Python 3.x

# Getting Started
1. Clone or download the repository
2. Navigate to the repository in a terminal
3. Run the following command:
	```sh
	python main.py
	```
4. Enter a course and its prerequisites in the format:
	> CourseName: List of prerequisites separated by comma and space
	
	Courses with no prerequisites are entered in the format:
	> CourseName
	
	When you are finished, enter 'q' to quit

	## Example
	**Input:**
	```sh
	Enter a course and it's prerequisites (enter `q` when finished)> CS101
	Enter a course and it's prerequisites (enter `q` when finished)> CS110: CS101
	Enter a course and it's prerequisites (enter `q` when finished)> CS111: CS101
	Enter a course and it's prerequisites (enter `q` when finished)> CS121: CS110, CS111
	Enter a course and it's prerequisites (enter `q` when finished)> q
	```
	
	**Output:**
	```sh
	GENERATED COURSE SCHEDULE =>
	{
	Semester 1: ['CS101']
	Semester 2: ['CS110', 'CS111']
	Semester 3: ['CS121']
	}
	```

## Contributions
Contributions to this project are welcomed! If you have an idea for a new feature or have found a bug, please create a new issue in the repository.