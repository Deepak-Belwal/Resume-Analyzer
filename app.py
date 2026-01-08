# BASIC REQUIRED DATA
jobs_skills = {
    "Data Analyst": ["SQL", "Excel", "Python"],
    "Web Developer": ["HTML", "CSS", "JavaScript"],
    "Project Manager": ["Leadership", "Communication", "Agile"],
    "Developer": []
}

for job,skills in jobs_skills.items():
    jobs_skills[job] = [x.lower() for x in skills] #Lowercasing skills in the dictionary to remove case sensitivity during comparison
skill_set = [] #Creating a list of skills to get all the required skills in one place which helps during text extraction
for x in jobs_skills.values():
    for y in x:
        if y not in skill_set:
            skill_set.append(y)

# PROJECT FUNCTION SECTION

# Skill Extraction Function
def extract_skills(input_text):
    text = input_text.lower().translate(str.maketrans(",:.;/?|[]{}()","             ")) #Removing punctuations before tokenization 
    input_tokens = text.split() #Whitespace tokenization
    input_skills = set([]) #Use a set to avoid duplicates
    for x in input_tokens: #Extract skills from 
        if x in skill_set:
            input_skills.add(x)
    unique_skills = list(input_skills) #Converted to list for readability
    return unique_skills

# Skill Comparison and Matching Function
def check_skills(person_skills,jobs):
    person_skills_lower = [x.lower() for x in person_skills] #Lowercasing skill for comparison
    suitability = 0
    best_job = ""
    for role, skills in jobs.items():
        match = 0
        for ps in person_skills_lower:
            if ps in skills:
                match = match + 1 #Counting number of matched skills to calculate suitability
        if not skills:
            continue
        if (match/len(skills))*100 > suitability: #Comparing suitability percentage to get best suitability
            suitability = (match/len(skills))*100 #Updating suitability and best job conditionally
            best_job = role
    if suitability==0:
        print("Found no job role suitable for the candidate.") #Edge case handling
    else:
        print(f"The candidate is most suitable for: {best_job}, and his suitability is: {suitability:.2f}%")


# MAIN EXECUTION BLOCK

# Input Text
print("Enter resume text:- ")
input_text = input()

p_skills = extract_skills(input_text)
if p_skills == []: #Edge case handling
    print("No required skills were found in the resume text!")
else:
    print(p_skills)
    check_skills(p_skills,jobs_skills)