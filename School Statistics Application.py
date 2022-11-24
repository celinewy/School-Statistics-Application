# school_data.py
# Celine Yeung, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Import data here
data_2020_2021 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)
data_2019_2020 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)
data_2018_2019 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)

# Hint: Create a dictionary for all school names and codes
school_code_name_dictionary = {"Centennial High School": 1224,
                                "Robert Thirsk School": 1679,
                                "Louise Dean School": 9626,
                                "Queen Elizabeth High School": 9806,
                                "Forest Lawn High School": 9813,
                                "Crescent Heights High School": 9815,
                                "Western Canada High School": 9816,
                                "Central Memorial High School": 9823,
                                "James Fowler High School": 9825,
                                "Ernest Manning High School": 9826,
                                "William Aberhart High School": 9829,
                                "National Sport School": 9830,
                                "Henry Wise Wood High School": 9836,
                                "Bowness High School": 9847,
                                "Lord Beaverbrook High School": 9850,
                                "Jack James High School": 9856,
                                "Sir Winston Churchill High School": 9857,
                                "Dr. E. P. Scarlett High School": 9858,
                                "John G Diefenbaker High School": 9860,
                                "Lester B. Pearson High School": 9865}

# Hint: Create a list of school codes to help with index look-up in arrays
school_codes_list = list(school_code_name_dictionary.values()) #Make a list of the school codes which are the values in the dictionary
school_names_list = list(school_code_name_dictionary.keys()) #Make a list of the school names which are the keys in the dictionary   

# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    print('Array data for 2020 - 2021:\n', data_2020_2021)
    print('Array data for 2019 - 2020:\n', data_2019_2020)
    print('Array data for 2018 - 2019:\n', data_2018_2019)
    
    
    # Add request for user input here
    i = 0
    while i == 0: #Loop until the user inputs a valid school name or code 
        user_input = input('Please enter the high school name or school code: ')
        if user_input.isdigit() == True: #Check if the string input is all numbers 
            user_input = int(user_input) #Make string input into an integer 
            if user_input not in school_codes_list: #Check if code is not the school codes list
                print('You must enter a valid school name or code.')    
            else: #If the code is in school codes list, increment by one to get out of the while loop
                i += 1
        elif user_input not in school_names_list: #Check if the string input is in the schools name list
                print('You must enter a valid school name or code.')
        else: #If the string is in the schools name list, increment by one to get out of the while loop
            i += 1
    
    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    if type(user_input) == str: #If user input is the school name
        #Find the index of the user input in the school names list, use that index to find the element in the schools codes list and save it to the variable  
        school_code = school_codes_list[school_names_list.index(user_input)]
        #Create an instance by passing the user input for the attribute name and the school code for the attribute code
        school_info = School(user_input, school_code)
    
    else: #If user input is the school code
        #Find the index of the users input in the school codes list, use that index to find the element in the schools name list and save it to the variable  
        school_name = school_names_list[school_codes_list.index(user_input)]
        #Create an instance by passing the school name for the attribute name and the user input for the attribute code
        school_info = School(school_name, user_input)

    School.print_all_stats(school_info) #Call the class School method to print the requested school statistics
  
    # Add data processing and plotting here
    index = school_codes_list.index(school_info.code) #The index number of the code in the school codes list

    '''For the users specified school, found the mean enrollment of each grade throughout the school years by summing the number 
    of students in that grade for each school year (from 2019-2021) and floor dividing it by 3 to round down. Found the school in the data 
    set using the index of the code in the school codes list (row index). Then, got the specific value for that grade using the column
    the grade is in in the csv file, starting from 0 (column index).'''
    mean_grade_10 = int((data_2018_2019[index][1] + data_2019_2020[index][1] + data_2020_2021[index][1]) // 3)
    print('Mean enrollment for Grade 10:', (mean_grade_10))
    mean_grade_11 = int((data_2018_2019[index][2] + data_2019_2020[index][2] + data_2020_2021[index][2]) // 3)
    print('Mean enrollment for Grade 11:', (mean_grade_11))
    mean_grade_12 = int((data_2018_2019[index][3] + data_2019_2020[index][3] + data_2020_2021[index][3]) // 3)
    print('Mean enrollment for Grade 12:', (mean_grade_12))

    '''For the users specified school, got the total graduated of the past 3 years by summing the number of grade 12 students for each
    school year. Found the school in each data set using the index of the code in the school codes list (row index) and got the grade 12 
    value using the column index (3) for each school year.'''
    total_graduated = int((data_2018_2019[index][3] + data_2019_2020[index][3] + data_2020_2021[index][3]))
    print('Total number of students who graduated in the past three years:', total_graduated)
    
    plt.figure(1) #To show figure 1 at the same time as figure 2
    position_on_graph = [1, 2, 3] #Tick locations for figure 1 and figure 2
    grades = [10, 11, 12] #Labels for tick locations in figure 1 
    '''Each plot is for each school year (for the specificed school):
    x-cordinates: tick positions that will be labelled from grade 10 to 12,
    y-cordinates: number of students in each grade from 10 to 12'''
    plt.plot(position_on_graph, data_2018_2019[index][1:], 'ro', label='2021 Enrollment') 
    plt.plot(position_on_graph, data_2019_2020[index][1:], 'go', label='2020 Enrollment')
    plt.plot(position_on_graph, data_2020_2021[index][1:], 'bo', label='2019 Enrollment')
    plt.xticks(position_on_graph, grades) 
    plt.legend(shadow=True, loc='upper left') 
    plt.title('Grade Enrollment by Year')
    plt.xlabel("Grade Level", fontsize=8.0)
    plt.ylabel("Number of Students", fontsize=8.0)

    #Bonus
    enrollment_years = [2019, 2020, 2021] #Labels for each tick in figure 2
    #List composed of the number of students in grade 10 for each school year of the specified school
    grade_10_stats = [data_2018_2019[index][1], data_2019_2020[index][1], data_2020_2021[index][1]] 
    #List composed of the number of students in grade 11 for each school year of the specified school
    grade_11_stats = [data_2018_2019[index][2], data_2019_2020[index][2], data_2020_2021[index][2]] 
    #List composed of the number of students in grade 12 for each school year of the specified school
    grade_12_stats = [data_2018_2019[index][3], data_2019_2020[index][3], data_2020_2021[index][3]]

    '''For the specific school, each subplot:
    x-cordinates: tick positions that will be labelled from 2019 to 2021
    y-cordinates: number of students in the grade in each school year'''
    plt.figure(2) #To show figure 2 at the same time as figure 1 
    plt.subplot(3,1,1) #Subplot 1
    plt.plot(position_on_graph, grade_10_stats,'y:', label='Grade 10')
    plt.xticks(position_on_graph, enrollment_years, fontsize=8.0)
    plt.legend(shadow=True, loc='upper right')
    plt.title('Enrollment by Grade')
    plt.xlabel('Enrollment Year', fontsize=8.0)
    plt.ylabel('Number of Students', fontsize=8.0)

    plt.subplot(3,1,2) #Subplot 2
    plt.plot(position_on_graph, grade_11_stats,'m:', label='Grade 11')
    plt.xticks(position_on_graph, enrollment_years, fontsize=8.0)
    plt.legend(shadow=True, loc='upper right')
    plt.xlabel('Enrollment Year', fontsize=8.0)
    plt.ylabel('Number of Students', fontsize=8.0)

    plt.subplot(3,1,3) #Subplot 3
    plt.plot(position_on_graph, grade_12_stats,'c:', label='Grade 12')
    plt.xticks(position_on_graph, enrollment_years, fontsize=8.0)
    plt.legend(shadow=True, loc='upper right')
    plt.xlabel('Enrollment Year', fontsize=8.0)
    plt.ylabel('Number of Students', fontsize=8.0)
    plt.show()



# Do not modify the code below
if __name__ == '__main__':
    main()