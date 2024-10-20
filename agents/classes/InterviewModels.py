from uagents import Model

class InterviewRequest(Model):
    resume_content: str
    job_description: str
    custom_prompt: str | None

class InterviewResponse(Model):
    question: str
