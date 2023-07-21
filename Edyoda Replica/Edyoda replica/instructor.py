import json
from json import JSONDecodeError


class instructor:
    def __init__(self, userid, password):
        # Initialize the instructor object with the provided user ID and password.
        self.userid = userid
        self.password = password

        # Load instructor data from the JSON file or create an empty dictionary if the file doesn't exist.
        try:
            with open("instructor_info.json", "r") as file:
                self.instructor_data = json.load(file)
        except(FileNotFoundError,JSONDecodeError):
            self.instructor_data = {}

    def check_instructor_details(self):
        # Check if the provided instructor credentials match any stored data.
        # If found, return True and store the corresponding instructor key(s).
        self.l = []
        for key, instructor in self.instructor_data.items():
            if instructor["In_login_details"]["userid"] == self.userid and instructor["In_login_details"]["Password"] == self.password:
                self.l.append(key)
                return True
        return False

    def change_password(self,current_password,new_password):
        # Change the instructor's password if the current password matches.
        # Update the JSON file with the new password.
        for i in self.instructor_data:
            if self.instructor_data[i]["In_login_details"]["Password"] == current_password:
                self.instructor_data[i]["In_login_details"]["Password"] = new_password
                try:
                    with open("instructor_info.json", "w") as file:
                        json.dump(self.instructor_data, file)
                        print("--------Password Changed Succesfully----------")
                except IOError:
                    print("Failed to update password!!")
                return True
        print("Current password is incorrect. Password change failed!!!")
        return False

    def batch_details(self):
        # Display batch details where the instructor is assigned to teach.
        try:
            with open("batches_info.json", "r") as file:
                self.bh_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            self.bh_data = {}

        # Get the course name(s) for which the instructor is assigned.
        for x, y in self.bh_data.items():
            if self.l[0] in y.get("instructor_key", []):
                self.cn = y.get("course_name", [])
        
        # Display the assigned modules for the instructor to teach.
        for a in self.cn:
            c_info = self.bh_data.get(a)
            if c_info:
                print(f"Batch Course Name: {c_info['course_name']}")
        print("------------------------------------------")

        # Get the instructor's data from the JSON file using the instructor key.
        try:
            with open("instructor_info.json", "r") as file:
                self.ik_data = json.load(file)
        except(FileNotFoundError,JSONDecodeError):
            self.ik_data = {}
        
        # Display the assigned modules for the instructor to teach
        for x, y in self.bh_data.items():
            if self.l[0] in y.get("instructor_key", []):
                i_info = self.ik_data.get(self.l[0])
                if i_info:
                    print(f"Assigned Modules for you to teach: {i_info['modules']}\n")
        print("------------------------------------------")
        # Display all modules associated with the batch the instructor is teaching.
        print("---------All Modules in the Batch you are Teaching----------")
        try:
            with open("module_info.json", "r") as file:
                self.mo_data = json.load(file)
        except(FileNotFoundError,JSONDecodeError):
            self.mo_data = {}

        # Get the module keys for the batch the instructor is teaching.
        for m, n in self.bh_data.items():
            if self.l[0] in n.get("instructor_key", []):
                self.mk = n.get("module_key", [])
                
        # Display the details of the modules associated with the batch.
        for i in self.mk:
            mo_info = self.mo_data.get(i)
            if mo_info:
                print(f"Module Name: {mo_info['Module Name']}")
                print(f"Duration: {mo_info['Duration']}")
                print(f"Topics: {mo_info['topiclist']}\n")
        print("------------------------------------------")

        # Display all students in the batch the instructor is teaching.
        print("---------All Studnets in the batch you are Teaching--------")
        try:
            with open("student_info.json", "r") as file:
                self.st_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            self.st_data = {}

        # Get the student keys for the batch the instructor is teaching.
        for c, d in self.bh_data.items():
            if self.l[0] in d.get("instructor_key", []):
                self.sk = d.get("student_key", [])

        # Display the details of the students associated with the batch.
        for e in self.sk:
            bs_info = self.st_data.get(e)
            if bs_info:
                print(f"Student Name : {bs_info['Name']}")
        print("------------------------------------------")

