import gradio as gr
import random
import numpy as np
import pandas as pd

class AIRecruitmentSystem:
    def __init__(self):
        self.skills = {
            'programming': ['Python', 'Java', 'JavaScript'],
            'frameworks': ['React', 'Django', 'Spring'],
            'cloud': ['AWS', 'Azure', 'GCP']
        }
        self.job_roles = [
            'Software Engineer', 
            'Data Scientist', 
            'Cloud Architect', 
            'Full Stack Developer'
        ]

    def generate_sample_resume(self, job_role):
        """Generate a sample resume based on job role"""
        resume_templates = {
            'Software Engineer': """
            John Doe
            Senior Software Developer

            Professional Summary:
            - 5+ years of experience in full-stack development
            - Expert in Python, JavaScript, and React
            - Strong background in building scalable web applications

            Technical Skills:
            - Programming Languages: Python, JavaScript, TypeScript
            - Frameworks: React, Django, Express.js
            - Databases: PostgreSQL, MongoDB
            - Cloud: AWS, Docker, Kubernetes
            """,
            'Data Scientist': """
            Jane Smith
            Data Science Professional

            Professional Summary:
            - 4+ years of experience in machine learning and data analysis
            - Expertise in Python, statistical modeling, and AI
            - Proven track record of delivering actionable insights

            Technical Skills:
            - Programming Languages: Python, R
            - Data Tools: Pandas, NumPy, Scikit-learn
            - Machine Learning: TensorFlow, PyTorch
            - Cloud: GCP, Azure Machine Learning
            """,
            'Cloud Architect': """
            Michael Johnson
            Cloud Solutions Architect

            Professional Summary:
            - 6+ years of cloud infrastructure design
            - Expert in multi-cloud strategies and migration
            - Strong background in enterprise cloud solutions

            Technical Skills:
            - Cloud Platforms: AWS, Azure, GCP
            - Infrastructure as Code: Terraform, CloudFormation
            - Containerization: Kubernetes, Docker
            - Networking: SDN, Cloud Security
            """,
            'Full Stack Developer': """
            Sarah Williams
            Full Stack Web Developer

            Professional Summary:
            - 4+ years of full-stack development experience
            - Proficient in modern web technologies
            - Strong focus on responsive and efficient web applications

            Technical Skills:
            - Frontend: React, Vue.js, HTML5, CSS3
            - Backend: Node.js, Django, Express
            - Databases: MySQL, MongoDB
            - Cloud: Heroku, AWS
            """
        }
        return resume_templates.get(job_role, "No resume template available")

    def generate_sample_interview_response(self, skill, job_role):
        """Generate a sample interview response"""
        responses = {
            ('Python', 'Software Engineer'): """
            As a Python developer, I approach complex problems by first breaking them down into smaller, manageable components. 
            In my previous role, I developed a microservices architecture using Django and Flask, which improved our application's 
            scalability and reduced deployment time by 40%. I'm particularly passionate about writing clean, maintainable code 
            and using design patterns like dependency injection to create more modular software solutions.
            """,
            ('Java', 'Software Engineer'): """
            My approach to Java development focuses on creating robust, efficient solutions. In my last project, I implemented 
            a high-performance caching mechanism using Spring Boot that reduced database query times by 60%. I'm experienced 
            in implementing microservices, using design patterns, and ensuring code quality through comprehensive unit and 
            integration testing.
            """,
            ('Python', 'Data Scientist'): """
            As a data scientist, I leverage Python's powerful libraries to derive meaningful insights. In my recent project, 
            I developed a machine learning model using TensorFlow and Scikit-learn that predicted customer churn with 85% accuracy. 
            I'm skilled in data preprocessing, feature engineering, and translating complex statistical models into actionable 
            business recommendations.
            """,
            ('AWS', 'Cloud Architect'): """
            My cloud architecture strategy revolves around creating scalable, secure, and cost-effective solutions. I've 
            successfully migrated monolithic applications to microservices on AWS, utilizing services like ECS, Lambda, and 
            API Gateway. My approach involves comprehensive cost analysis, performance optimization, and implementing 
            robust security measures using IAM and network segmentation.
            """
        }
        return responses.get((skill, job_role), "Generic interview response about technical expertise")

    def skills_matcher(self, resume, job_role):
        """Match candidate skills to job requirements"""
        match_score = random.uniform(70, 95)
        
        feedback = f"""
        Job Role: {job_role}
        Match Score: {match_score:.2f}%
        
        Analysis:
        - Technical Skills Alignment: {random.uniform(7.0, 9.5):.1f}/10
        - Problem-Solving Potential: {random.uniform(7.0, 9.5):.1f}/10
        - Communication Skills: {random.uniform(7.0, 9.5):.1f}/10
        """
        
        return feedback, match_score

    def interview_simulation(self, candidate_response, skill):
        """Simulate AI-driven interview assessment"""
        technical_score = random.uniform(7.0, 9.5)
        communication_score = random.uniform(7.0, 9.5)
        problem_solving_score = random.uniform(7.0, 9.5)
        
        overall_score = (technical_score + communication_score + problem_solving_score) / 3
        
        feedback = f"""
        Skill Assessed: {skill}
        
        Interview Performance:
        - Technical Depth: {technical_score:.1f}/10
        - Communication: {communication_score:.1f}/10
        - Problem-Solving: {problem_solving_score:.1f}/10
        
        Overall Score: {overall_score:.1f}/10
        
        Recommendation: {
            'Hire' if overall_score >= 8 else 
            'Second Interview' if overall_score >= 7 else 
            'Not Recommended'
        }
        """
        
        return feedback, overall_score

def create_recruitment_interface():
    system = AIRecruitmentSystem()

    def process_recruitment(resume, job_role, candidate_response, skill):
        # Skill Matching Stage
        skills_feedback, match_score = system.skills_matcher(resume, job_role)
        
        # Interview Simulation Stage
        interview_feedback, interview_score = system.interview_simulation(candidate_response, skill)
        
        # Final Decision
        final_decision = f"""
        🤖 AI Recruitment System Report 🤖

        {skills_feedback}

        {interview_feedback}

        Final Weighted Score: {(match_score * 0.4 + interview_score * 0.6):.2f}/100
        """
        
        return final_decision

    # Prepare initial values
    initial_job_role = 'Software Engineer'
    initial_skill = 'Python'
    initial_resume = system.generate_sample_resume(initial_job_role)
    initial_response = system.generate_sample_interview_response(initial_skill, initial_job_role)

    # Gradio Interface
    demo = gr.Interface(
        fn=process_recruitment,
        inputs=[
            gr.Textbox(label="Resume Content", value=initial_resume),
            gr.Dropdown(system.job_roles, label="Job Role", value=initial_job_role),
            gr.Textbox(label="Candidate Interview Response", value=initial_response),
            gr.Dropdown(system.skills['programming'], label="Primary Skill", value=initial_skill)
        ],
        outputs=gr.Textbox(label="Recruitment Assessment"),
        title="🚀 AI Recruitment Assistant",
        description="Automated candidate assessment and matching system"
    )
    
    return demo

def main():
    demo = create_recruitment_interface()
    demo.launch(share=True)

if __name__ == "__main__":
    main()