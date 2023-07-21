import json
from json import JSONDecodeError

class student:
    def __init__(self, userid, password):
        # Initialize the student object with the provided user ID and password.
        self.userid = userid
        self.password = password

        # Load student data from the JSON file or create an empty dictionary if the file doesn't exist.
        try:
            with open("student_info.json", "r") as file:
                self.st_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            self.st_data = {}

        # Load batch data from the JSON file or create an empty dictionary if the file doesn't exist.
        try:
            with open("batches_info.json", "r") as file:
                b = json.load(file)
                self.b_data = b.items()
        except(FileNotFoundError,JSONDecodeError):
            self.b_data = {}

        # Load instructor data from the JSON file or create an empty dictionary if the file doesn't exist.
        try:
            with open("instructor_info.json", "r") as file:
                self.i_data = json.load(file)
        except(FileNotFoundError,JSONDecodeError):
            self.i_data = {}

        # Load module data from the JSON file or create an empty dictionary if the file doesn't exist.
        try:
            with open("module_info.json", "r") as file:
                self.m_data = json.load(file)
        except(FileNotFoundError,JSONDecodeError):
            self.m_data = {}

    def check_student_details(self):
        # Check if the provided student credentials match any stored data.
        # If found, return True and store the corresponding student key(s).
        self.k = []
        for key,student in self.st_data.items():
            if student["login_details"]["userid"] == self.userid and student["login_details"]["Password"] == self.password:
                self.k.append(key)
                return True
        return False
            
    def student_modules(self):
        for m, n in self.b_data:
            if self.k[0] in n.get("student_key", []):
                self.kk = n.get("module_key", [])
        
        # Display the details of the modules associated with the student's batch.
        for i in self.kk:
            m_info = self.m_data.get(i)
            if m_info:
                print(f"Module Name: {m_info['Module Name']}")
                print(f"Duration: {m_info['Duration']}")
                print(f"Topics: {m_info['topiclist']}\n")

    def teachers_alloted(self):
        for x, y in self.b_data:
            if self.k[0] in y.get("student_key", []):
                self.ii = y.get("instructor_key", [])
  
        # Display the details of the instructors assigned to the student's batch.
        for a in self.ii:
            i_info = self.i_data.get(a)
            if i_info:
                print(f"Teacher Name: {i_info['Name']}")
                print(f"Modules: {i_info['modules']}\n")
             
    def batchmates(self):
        for c, d in self.b_data:
            if self.k[0] in d.get("student_key", []):
                self.jj = d.get("student_key", [])

        # Display the names of the batchmates.
        for e in self.jj:
            bm_info = self.st_data.get(e)
            if bm_info:
                print(f"Name : {bm_info['Name']}\n")

    def change_pass(self, c_pass, n_pass):
        # Change the student's password if the current password matches.
        # Update the JSON file with the new password.
        for i in self.st_data:
            if self.st_data[i]["login_details"]["Password"] == c_pass:
                self.st_data[i]["login_details"]["Password"] = n_pass
                try:
                    with open("student_info.json", "w") as file:
                        json.dump(self.st_data, file)
                        print("--------Password Changed Succesfully----------")
                except IOError:
                    print("Failed to update password!!")
                return True
        print("Current password is incorrect. Password change failed!!!")
        return False        