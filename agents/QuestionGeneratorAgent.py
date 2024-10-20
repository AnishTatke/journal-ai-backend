from uagents import Agent, Context
from protocols.broadcast_protocol import broadcast_protocol

question_generator = Agent('QuestionGeneratorAgent')


@question_generator.on_event('startup')
async def on_startup(ctx: Context):
    ctx.logger.info('Question Generator Agent started')
