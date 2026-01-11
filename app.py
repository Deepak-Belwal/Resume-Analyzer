#TRY THIS RESUME INPUT TEXT AS TEST INPUT
"""
+91 7906170826 
Deepak Belwal
GitHub 
LeetCode
deepak.belwal.1105@gmail.com 
Education
LinkedIn 
Graphic Era Hill University
Bachelor of Technology in Computer Science — 8.06 CGPA
Sainik School Ghorakhal
Intermediate — 61%
Projects
July 2023– Present
Uttarakhand
July 2023
Nainital, Uttarakhand
Public Sanitation and Complaint Logging System — Python, HTML, CSS, JavaScript, Socket.IO,
Leaflet.js, MongoDB
Oct 2025
• Built a Complaint Portal where users can submit complaints with their location on a map using Leaflet.js.
• Integrated with SocketIO for real time updates and designed a lightweight python backend.
• Added a Chatbot to ease up the process of registering complaints.
Process Scheduling Analyzer — Node.js, Express, TypeScript, SKLearn, MediaPipe
Aug 2025
• Built an Analyzer webapp that takes user input to provide the calculated and visualization with gantt chart.
• Connected the frontend with an Express backend that provided comparisons and a connection to ML model as well.
• Further enhanced it by integrating a ML model to recommend the best algorithm possible.
Forest Fire Prediction System — Python, Gradio, ML
• Implemented a system to predict the occurance of forest fires based on older data of the region.
• Added a regression model as well to predict the intensity of fire if it has a chance to occur.
• Integrated with a simple yet reliable Gradio frontend to get user input.
Skills
Oct 2024
Programming: C, C++, Python, Java, JavaScript
Tech Stack: HTML, CSS, Tailwind, React.js, MySQL, Git, GitHub
ML/AI Tools: CNN, Mediapipe
Experience
WeCode Coding Club
Member
July 2024– Present
Graphic Era Hill University
• Attended various sessions and workshops for personal improvement while solving leetcode problems with other
members.
• Participated in various coding challenges, thus improving my average solving time for problems on leetcode.
Relevant Coursework
•Data Structures and Algorithms
•Database Management
•Operating System
•Natural Language Processing
Achievements / Extracurricular
•Computer Networking
•Machine Learning
• Participated in various hackathons at college level and secured second position once.
• Solved 200+ coding challenges on LeetCode and GeeksForGeeks.
• Coordinated and managed various events in college.
"""











# BASIC REQUIRED DATA
jobs_skills = {
    "Data Analyst": ["SQL", "Excel", "Python"],
    "Web Developer": ["HTML", "CSS", "JavaScript"],
    "Project Manager": ["Leadership", "Communication", "Agile"],
    "Developer": []
}

for job,skills in jobs_skills.items():
    jobs_skills[job] = [x.lower() for x in skills] #Lowercasing skills in the dictionary to remove case sensitivity during comparison
skill_set = set() #Creating a set(Only uniqueness matters, order does not) of skills to get all the required skills in one place which helps during text extraction
for skills in jobs_skills.values():
    skill_set.update(skills)




# PROJECT FUNCTION SECTION

# Skill Extraction Function
def extract_skills(input_text):
    """
    Function to extract unique skills from the inputted resume text.
    
    Parameters:
    input text (string) : Resume input to the system as a single string.

    Returns:
    A list of unique skills found in the resume text.
    """
    text = input_text.lower().translate(str.maketrans(",:.;/?|[]{}()","             ")) #Removing punctuations before tokenization 
    input_tokens = text.split() #Whitespace tokenization
    input_skills = set() #Use a set to avoid duplicates
    for x in input_tokens: #Extract skills from 
        if x in skill_set:
            input_skills.add(x)
    unique_skills = list(input_skills) #Converted to list for readability
    return unique_skills

# Skill Comparison and Matching Function
def check_skills(person_skills,jobs):
    """
    Function to match and find suitabile job of a candidate along with his or her suitability percentage.
    
    Parameters:
    person_skills (list) : List of a candidate's unique skills.
    jobs (dict) : Dictionary containing available roles as key and list of required skills as values.

    Returns:
    Dictionary containing Candidate's Skills, Suitable Job, Suitability Percentage, Matched Skills and Remaining Skills.
    -1 when no skills of a person match with the requirements.
    """
    person_skills_lower = [x.lower() for x in person_skills] #Lowercasing skill for comparison
    suitability = 0
    best_job = ""
    matched_skills = []
    for role, skills in jobs.items():
        match = 0
        matched_skills_temp = []
        for ps in person_skills_lower:
            if ps in skills:
                matched_skills_temp.append(ps)
                match += 1 #Counting number of matched skills to calculate suitability
        if not skills: #Skip empty skill sets as they'll always provide 0 suitability
            continue
        if (match/len(skills))*100 > suitability: #Comparing suitability percentage to get best suitability
            suitability = (match/len(skills))*100 #Updating suitability and best job conditionally
            best_job = role
            matched_skills = matched_skills_temp
    if suitability==0:
        return -1
    else:
        unmatched_skills = [] #List of unmatched skills
        if best_job:
            for skills in jobs[best_job]: #Logic to store unmatched skills
                if skills not in matched_skills:
                    unmatched_skills.append(skills)
        return { #Return dictionary of Required Values
        "Candidate_Skills" : person_skills, "Suitable_Job" : best_job, "Suitability" : suitability, "matching_skills" : matched_skills, "remaining_skills" : unmatched_skills}



# FLASK BLOCK
from flask import Flask, request, jsonify, render_template
import json
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods = ["POST"])
def analyze_resume():

    raw_data = request.get_data(as_text=True)

    if not raw_data:
        return jsonify({"ERROR": "Empty request body"}), 400
    try:
        data = json.loads(raw_data)
    except Exception:
        return jsonify({"ERROR": "Invalid JSON payload"}), 400

    if not data or "text" not in data:
        return jsonify({"ERROR" : "Resume text not provided."}), 400
    resume_text = data["text"]
    skills = extract_skills(resume_text)

    if not skills:
        return jsonify({"SORRY":"No relevant skills found."}),200
    result = check_skills(skills, jobs_skills)
    
    if result == -1:
        return jsonify({"SORRY":"No suitable job role found."}),200
    
    return jsonify(result),200

if __name__ == "__main__":
    app.run(debug = True)
