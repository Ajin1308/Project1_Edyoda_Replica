import json
from json import JSONDecodeError
import random

# Create a class for the admin with various functions to manage batches, modules, students, and instructors.
class admin:
    def __init__(self, userid, userpassword):
        # Admin login credentials
        self.id = "admin@123"
        self.password = "password"
        self.userid = userid
        self.userpassword = userpassword
        
    def check_admin_details(self):
        # Check if the provided admin credentials match the stored ones.
        if self.userid == self.id and self.userpassword == self.password:
            return True
        else:
            return False
    
    def change_password(self, new_password):
        self.password = new_password

    def add_batch(self, course, modules, students, instructors):
        # Add a new batch with course details, modules, students, and instructors.
        # Generate a random batch key and store the batch information in a JSON file.
        # If the JSON file doesn't exist, create a new dictionary to store the data.
        batches = {
            "course_name" : course,
            "module_key" : modules,
            "student_key" : students,
            "instructor_key" : instructors
        }

        try:
            with open("batches_info.json", "r") as file:
                    data = json.load(file)
                    self.batch_data = data
        except(FileNotFoundError, JSONDecodeError):
            self.batch_data = {}

        while True:
            batch_key = random.randint(200,350)
            if batch_key not in self.batch_data.keys():
                self.batch_data[batch_key] = batches
                with open("batches_info.json", "w") as file:
                    json.dump(self.batch_data, file)
                break
            else:
                continue

    def remove_batch(self):
        # Remove a batch by entering the batch key.
        # The batch data is stored in a JSON file, and the batch key is used to delete the corresponding entry.
        try:
            with open("batches_info.json", "r") as file:
                self.b_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            self.b_data = {}
        
        print(f"Ongoing Batch Keys: ")
        for u in self.b_data.keys():
            print(u)

        b_key = input("Enter Batches Key to DELETE, separated by space: \n").split()

        for l in b_key:
            if l in self.b_data:
                self.b_data.pop(l)
                with open("batches_info.json", "w") as file:
                    json.dump(self.b_data, file)
                return True
            else:
                return False

    def view_batches(self):
        # View batch details by entering the batch key.
        # Fetch batch information from the JSON file using the provided key and display the details.
        try:
            with open("batches_info.json", "r") as file:
                self.bh_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            self.bh_data = {}

        print(f"Ongoing Batch Keys: ")
        for u in self.bh_data.keys():
            print(u)

        ask = input("Enter Batches Key separated by space: \n").split()
        
        for l in ask:
            info =  self.bh_data.get(l)
            if info:
                print(f"Course Name: {info['course_name']}")
                st_key = info['student_key']
                in_key = info['instructor_key']
        print("---------------------------------")        
        # Fetch student information from the JSON file using the student keys associated with the batch.
        try:
            with open("student_info.json", "r") as file:
                self.st_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            self.st_data = {}

        try:
            with open("instructor_info.json", "r") as file:
                self.in_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            self.in_data = {}

        # Display the details of the students in the batch.
        for i in st_key:
            if st_key[0] in self.st_data:
                st_info = self.st_data.get(i)
                if st_info:
                    print(f"Student Name : {st_info['Name']}")
        print("---------------------------------")

        # Display the details of the instructors associated with the batch.
        for h in in_key:
            if in_key[0] in self.in_data:
                in_info = self.in_data.get(h)
                if in_info:
                    print(f"Instructors: {in_info['Name']}")
        print("---------------------------------")
        
        # The rest of the functions (add_modules, remove_modules, view_modules, add_students, remove_students,
        # add_instructors, remove_instructors, view_instructors) follow a similar pattern, adding, removing, or viewing
        # corresponding data and storing the information in JSON files.
    def add_modules(self,module_name,duration):
        try:
            with open("module_info.json", "r") as file:
                data = json.load(file)
                self.module_data = data
        except (FileNotFoundError, JSONDecodeError):
            self.module_data  = {}

        topic_list = []
        topic_size = int(input("How many topics do you want to add? "))
        for topic in range(topic_size):
            topic_name = input("Topic name: ")
            topic_list.append(topic_name)
        
        module = {
            "Module Name" : module_name,
            "Duration" : duration,
            "topiclist" : topic_list 
        }

        while True:
            module_key = random.randint(1,100)
            if module_key not in self.module_data.keys():
                self.module_data[module_key] = module
                with open("module_info.json", "w") as file:
                    json.dump(self.module_data, file)
                break
            else:
                continue

    def remove_modules(self):
        try:
            with open("module_info.json", "r") as file:
                self.m_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.m_data  = {}

        print("All Module keys:")
        for k ,v in self.m_data.items():
            print(k)

        m = input("Enter Module key seperated by space: ").split()

        for c in m:
            if c in self.m_data:
                self.m_data.pop(c)
                with open("module_info.json", "w") as file:
                    json.dump(self.m_data, file)
                return True
            else:
                return False

    def view_modules(self):
        try:
            with open("module_info.json", "r") as file:
                self.mde_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.mde_data  = {}

        print("All Module keys:")
        for k ,v in self.mde_data.items():
            print(k)
        ask = input("Enter Module key seperated by space: ").split()

        for c in ask:
            mk = self.mde_data.get(c)
            if mk:
                print(f"Module Name: {mk['Module Name']}")
                print(f"Duration: {mk['Duration']}")
                print(f"Topics: {mk['topiclist']}\n")

    def add_students(self, student_name, student_email, course_name):
        students = {
            "Name" : student_name,
            "Email" : student_email,
            "course" : course_name,
            "login_details" : {"userid": student_email, "Password" : student_name + "@edyoda%" }
        }

        try:
            with open("student_info.json", "r") as file:
                data = json.load(file)
                self.student_data = data
        except (FileNotFoundError, JSONDecodeError):
            self.student_data  = {}
        
        while True:
            student_key = random.randint(1,10000)
            if student_key not in self.student_data.keys():
                self.student_data[student_key] = students
                with open("student_info.json", "w") as file:
                    json.dump(self.student_data, file)
                break
            else:
                continue

    def remove_students(self):
        try:
            with open("student_info.json", "r") as file:
                self.s_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.s_data  = {}

        print("All Student keys:")
        for k ,v in self.s_data.items():
            print(k)
        p = input("Enter Student key seperated by space: ").split()

        for s in p:
            if s in self.s_data:
                self.s_data.pop(s)
                with open("student_info.json", "w") as file:
                    json.dump(self.s_data, file)
                return True
            else:
                return False

    def view_students(self):
        try:
            with open("student_info.json", "r") as file:
                self.std_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.std_data  = {}

        print("All Student keys:")
        for k ,v in self.std_data.items():
            print(k)
        ask = input("Enter Student key seperated by space: ").split()

        for s in ask:
            sk = self.std_data.get(s)
            if sk:
                print(f"Name : {sk['Name']}")
                print(f"Email : {sk['Email']}")
                print(f"Course : {sk['course']}")
                print(f"Login details : {sk['login_details']}")
        
    def add_instructors(self, instructor_name, instructor_email, modules_to_teach):
        instructors = {
            "Name" : instructor_name,
            "Email" : instructor_email,
            "modules" : modules_to_teach,
            "In_login_details" : {"userid" : instructor_email, "Password" : instructor_name + "@edyoda#"}
        }

        try:
            with open("instructor_info.json", "r") as file:
                data = json.load(file)
                self.instructor_data = data
        except (FileNotFoundError, JSONDecodeError):
            self.instructor_data  = {}
        
        while True:
            instructor_key = random.randint(1,1000)
            if instructor_key not in self.instructor_data.keys():
                self.instructor_data[instructor_key] = instructors
                with open("instructor_info.json", "w") as file:
                    json.dump(self.instructor_data, file)
                break
            else:
                continue

    def remove_instructors(self):
        try:
            with open("instructor_info.json", "r") as file:
                self.i_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.i_data  = {}

        print("All Instructor keys:")
        for k in self.i_data.keys():
            print(k)
        r = input("Enter Instructor key seperated by space: ").split()

        for f in r:
            if f in self.i_data:
                self.i_data.pop(f)
                with open("instructor_info.json", "w") as file:
                    json.dump(self.i_data, file)
                return True
            else:
                return False

    def view_instructors(self):
        try:
            with open("instructor_info.json", "r") as file:
                self.intr_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.intr_data  = {}

        print("All Instructor keys:")
        for k ,v in self.intr_data.items():
            print(k)
        ask = input("Enter Instructor key seperated by space: ").split()

        for f in ask:
            ik = self.intr_data.get(f)
            if ik:
                print(f"Name : {ik['Name']}")
                print(f"Email : {ik['Email']}")
                print(f"Teaching Modules : {ik['modules']}")
                print(f"Login details : {ik['In_login_details']}")