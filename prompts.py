# PROMPT = """
# You are a hiring manager of {company}, and I am applying for a {role} role at {company}, and the following is the job description:

# {job_description}

# I want you to read my resume below and help me improve my resume to fit the job description. Please output it in this format:

# Previous statement: <The statement you have changed>
# Improved statement: <The statement improved by you>

# Here is my resume: {resume}
# """

RESPONSIBILITIES = """
You are an expert resume writer with over 20 years of experience working with job seekers trying to land a role in tech. Highlight the three most important responsibilities in the job description:

{job_description}
"""

TAILOR = """
Based on these 3 most important responsibilities from the job description, please directly modify my resume for this {role} position at {company}. Do not make information up.
Here is my resume: {resume}
"""

DIFFERENCE = """
List out the differences between my original resume and your suggested draft in this format:

Previous statement: <The statement you have changed>
Improved statement: <The statement suggested by you>

Be specific and list out exactly what was changed, down to the exact wording.
"""
