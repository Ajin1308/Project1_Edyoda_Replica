import json
from admin import admin
from students import student
from instructor import instructor


# This is the main script that connects all other files (admin.py, students.py, instructor.py). 

print("----------------------Welcome to Edyoda----------------------")
while True:
    choice = int(input("Enter 1. Login as Admin\nEnter 2. Login as Instructor\nEnter 3. Login as Student\n0. Exit\n"))
    if choice == 1:
        admid = input("Enter your UserID: ")
        admpassword = input("Enter your Password: ")
        adm = admin(admid,admpassword)
        check = adm.check_admin_details()
        if check:
            print("--------------Successfully logged in---------------")
            while True:
                choi = int(input("1. Add new Module\n2. View Module\n3. Delete Module\n4. Add new Batch\n5. View Ongoing Batch details\n6. Delete Batch\n7. Add Instructors\n8. View Instructors\n9. Delete Instructor\n10. Add Students\n11. View Students\n12. Delete Students\n13. Change your password\n0. Logout\n"))
                if choi == 1:
                    module_name = input("Module name: ")
                    duration = input("Duration: ")
                    adm.add_modules(module_name, duration)
                    print("--------------Module Added Succesfully---------------")
                if choi == 2:
                    print("-----------------------------------------")
                    adm.view_modules()
                    print("-----------------------------------------")
                if choi == 3:
                    g = adm.remove_modules()
                    if g:
                        print("------Module Deleted Succesfully------")
                    else:
                        print("---------Error!!!!--------")
                if choi == 4:
                    c = input("Course Name: ")
                    print("--------Add Modules to the Course--------")
                    print("Enter Module key separated by space\n")
                    f = open("module_info.json","r")
                    cnt = json.load(f)
                    m_keys = list(cnt.keys())
                    for key in m_keys:
                        m_name = cnt[key]["Module Name"]
                        print(f"Module Key: {key} ----> Module Name: {m_name}")
                    f.close()
                    m = input().split()
                    print("--------Add Teachers to the Course--------")
                    print("Enter Instructor key separated by space\n")
                    j = open("instructor_info.json", "r")
                    cnt2 = json.load(j)
                    i_keys = list(cnt2.keys())
                    for key in i_keys:
                        i_name = cnt2[key]["modules"]
                        print(f"Instructor Key: {key} -----> Teaching Modules: {i_name}")
                    j.close()
                    n = input().split()
                    print("--------Add Students to the Course--------")
                    print("Enter Students key separated by space\n")
                    l = open("student_info.json", "r")
                    cnt3 = json.load(l)
                    s_keys = list(cnt3.keys())
                    for key in s_keys:
                        s_name = cnt3[key]["course"]
                        print(f"Student Key: {key} -----> Student Course: {s_name}")
                    l.close()
                    k = input().split()
                    adm.add_batch(c, m, k, n)
                    print("---------Batch Added Successfully---------")
                if choi == 5:
                    print("-----------------------------------------")
                    adm.view_batches()
                if choi == 6:
                    a = adm.remove_batch()
                    if a:
                        print("------Batch Deleted Succesfully------")
                    else:
                        print("---------Error!!!!--------")
                if choi == 7:
                    instructor_name = input("Instructor Name: ")
                    instructor_email = input("Instructor Email: ")
                    instructor_modules  = input("Type modules taken by instructor separated by space: ").split()
                    adm.add_instructors(instructor_name, instructor_email, instructor_modules)
                    print("----------Instructor Enrolled Successfully----------")
                if choi == 8:
                    print("-----------------------------------------")
                    adm.view_instructors()
                    print("-----------------------------------------")
                if choi == 9:
                    v = adm.remove_instructors()
                    if v:
                        print("------Instructor Deleted Succesfully------")
                    else:
                        print("---------Error!!!!--------")
                if choi == 10:
                    student_name = input("Student Name: ")
                    student_email = input("Student Email: ")
                    course_name = input("Student Course: ")
                    adm.add_students(student_name, student_email, course_name)
                    print("-----------Student Enrolled Succesfully------------")
                if choi == 11:
                    print("-----------------------------------------")
                    adm.view_students()
                    print("-----------------------------------------")
                if choi == 12:
                    p = adm.remove_students()
                    if p:
                        print("------Student Deleted Succesfully------")
                    else:
                        print("---------Error!!!!--------")
                if choi == 13:
                    new = input("Enter new Password")
                    adm.change_password(new)
                    print("---------Password Changed Successfully--------")
                if choi == 0:
                    break
        else:
            print("------------Credentials doesnt match-------------")
    
    if choice == 2:
        intrid = input("Enter your UserID: ")
        intrpassword = input("Enter your Password: ")
        intr = instructor(intrid, intrpassword)
        chek = intr.check_instructor_details()
        if chek:
            print("--------------Successfully logged in---------------")
            while True:
                ch = int(input("1. Change Password\n2. Assigned Batch details\n0. Logout\n"))
                if ch == 1:
                    c_p = input("Current password: ")
                    n_p = input("New password: ")
                    intr.change_password(c_p, n_p)
                if ch == 2:
                    intr.batch_details()
                if ch == 0:
                    break

    if choice == 3:
        stdid = input("Enter your UserID: ")
        stdpassword = input("Enter your Password: ")
        std = student(stdid, stdpassword)
        chk = std.check_student_details()
        if chk:
            print("--------------Successfully logged in---------------")
            f = open("student_info.json", "r")
            d = json.load(f)
            for i in d.values():
                if i["login_details"]["Password"] == stdpassword:
                    print(f"Course Name: {i['course']}")
            f.close()
            while True:
                ch = int(input("1. Your Modules\n2. Your Instructors\n3. Quizes and Assignments\n4. Batchmates\n5. Change Pasword\n6. Logout\n"))
                if ch == 1:
                    std.student_modules()
                if ch == 2:
                    std.teachers_alloted()
                if ch == 4:
                    std.batchmates()
                if ch == 5:
                    q = input("Current Password: ")
                    w = input("New Password: ")
                    std.change_pass(q, w)
                if ch == 6:
                    break
        else:
            print("------------Credentials doesn't match-------------")

    if choice == 0:
        break