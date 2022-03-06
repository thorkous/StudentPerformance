import requests

endpoint = "http://127.0.0.1:8000/api/"
# post_response = requests.post(endpoint, json={'name' : 'koustubh', 'email':'koustubh@gmail.com','parent_name':'Shilpi', 'adhar' : '123455'})
# get_response = requests.get(endpoint+"getstudent", json = {'id' : '1'})
# post_subject = requests.post(endpoint+"savesubject",json ={'name':'chem','description':'chemistry is a good subject'})
# get_subjects = requests.get(endpoint+"getsubjects")
# save_subject_marks = requests.post(endpoint+"savemarks", json = {'subject_id':'1', 'student_id':'1','student_marks':'90'})
get_subject_marks = requests.get(endpoint + "getmarks", json={'subject_id': '1', 'student_id': '1'})
