'''


(EmployeeDetails)   (Skills)       (ProjectInfo)       (Certification)       (TeamHandling)
        \             |                 |                      |                     /
         \____________|_________________|______________________|____________________/
                                   ↓
                               TechLead




'''

class EmployeeDetails:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def show_employee(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


class Skills:
    def __init__(self, skills):
        self.skills = skills

    def show_skills(self):
        print(f"Skills: {', '.join(self.skills)}")


class ProjectInfo:
    def __init__(self, project_name, deadline):
        self.project_name = project_name
        self.deadline = deadline

    def show_project(self):
        print(f"Project: {self.project_name}, Deadline: {self.deadline}")


class Certification:
    def __init__(self, certificates):
        self.certificates = certificates

    def show_certifications(self):
        print(f"Certifications: {', '.join(self.certificates)}")


class TeamHandling:
    def __init__(self, team_size):
        self.team_size = team_size

    def show_team(self):
        print(f"Team Size: {self.team_size}")


# === Final class using multiple inheritance ===
class TechLead(EmployeeDetails, Skills, ProjectInfo, Certification, TeamHandling):
    def __init__(self, emp_id, name, skills, project_name, deadline, certificates, team_size):
        EmployeeDetails.__init__(self, emp_id, name)
        Skills.__init__(self, skills)
        ProjectInfo.__init__(self, project_name, deadline)
        Certification.__init__(self, certificates)
        TeamHandling.__init__(self, team_size)

    def show_full_profile(self):
        print("\n--- Tech Lead Profile ---")
        self.show_employee()
        self.show_skills()
        self.show_project()
        self.show_certifications()
        self.show_team()
lead = TechLead(
    emp_id="TL567",
    name="Niharika Sharma",
    skills=["Python", "Django", "DevOps"],
    project_name="ERP Automation",
    deadline="2025-09-30",
    certificates=["AWS", "Scrum Master"],
    team_size=8
)

lead.show_full_profile()
