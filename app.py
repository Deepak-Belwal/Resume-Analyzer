jobs_skills = {
    "Data Analyst": ["SQL", "Excel", "Python"],
    "Web Developer": ["HTML", "CSS", "JavaScript"],
    "Project Manager": ["Leadership", "Communication", "Agile"]
}
for job,skills in jobs_skills.items():
    jobs_skills[job] = [x.lower() for x in skills]

p_skills = ["SQL", "Excel", "leadership", "HTML","css"]

def check_skills(person_skills,jobs):
    person_skills_lower = [x.lower() for x in person_skills]
    suitability = 0
    best_job = ""
    for role, skills in jobs.items():
        match = 0
        for ps in person_skills_lower:
            if ps in skills:
                match = match + 1
        if (match/len(skills))*100 > suitability:
            suitability = (match/len(skills))*100
            best_job = role
    if suitability==0:
        print("Found no job role suitable for the candidate.")
    else:
        print(f"The candidate is most suitable for: {best_job}, and his suitability is: {suitability:.2f}%")


check_skills(p_skills,jobs_skills)