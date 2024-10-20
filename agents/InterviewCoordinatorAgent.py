from uagents import Agent, Context

from protocols.broadcast_protocol import broadcast_protocol
from classes.BroadcastExample import BroadcastExampleRequest, BroadcastExampleResponse
from classes.InterviewModels import InterviewRequest, InterviewResponse




interview_coordinator = Agent('InterviewCoordinatorAgent')

@interview_coordinator.on_event('startup')
async def on_startup(ctx: Context):
    ctx.logger.info(f'Interview Coordinator Agent started {interview_coordinator.address}')

@interview_coordinator.on_interval(period=2.0)
async def check_for_content(ctx: Context):
    status_list = await ctx.broadcast(broadcast_protocol.digest, message=BroadcastExampleRequest())
    ctx.logger.info(f"Trying to contact {len(status_list)} agents")

@interview_coordinator.on_message(model=BroadcastExampleResponse)
async def handle_response(ctx: Context, sender: str, msg: BroadcastExampleResponse):
    ctx.logger.info(f"Received message from {sender}: {msg.text}")

@interview_coordinator.on_rest_post("/submit", InterviewRequest, InterviewResponse)
async def submit_content(ctx: Context, model: InterviewRequest):
    ctx.logger.info(f"Received content from {model.sender}: {model.content}")
    return InterviewResponse(question="Content received successfully")


