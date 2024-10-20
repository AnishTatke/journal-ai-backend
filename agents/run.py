from uagents import Bureau

from protocols.broadcast_protocol import broadcast_protocol

from InterviewCoordinatorAgent import interview_coordinator
from QuestionGeneratorAgent import question_generator

question_generator.include(broadcast_protocol)

bureau = Bureau(
    port=8000,
    endpoint=['http://localhost:8000/submit']
)
bureau.add(question_generator)
bureau.add(interview_coordinator)

if __name__ == "__main__":
    bureau.run()