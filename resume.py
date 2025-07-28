import json

# JSON string for the resume
resume_json = '''
{
  "name": "Balaji",
  "email": "balaji@email.com",
  "phone": "+91-9876543210",
  "address": "Bangalore, India",
  "education": [
    {
      "degree": "B.Tech",
      "branch": "IT",
      "university": "ABC University",
      "year_of_passing": 2025
    }
  ],
  "skills": ["Python", "C++", "HTML", "Teamwork"],
  "projects": [
    {
      "title": "Library Management System",
      "description": "Created a web app to manage library books and members."
    }
  ],
  "interests": ["Reading", "Watching movies","Travelling"],
  "Are you Working": true
  }
'''

# Convert JSON string to Python dictionary
resume_dict = json.loads(resume_json)

# Print the resume dictionary
print(resume_dict)
