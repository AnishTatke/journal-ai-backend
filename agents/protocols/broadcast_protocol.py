from uagents import Protocol, Context
from classes.BroadcastExample import BroadcastExampleRequest, BroadcastExampleResponse

broadcast_protocol = Protocol('broadcast_example')

@broadcast_protocol.on_message(model=BroadcastExampleRequest, replies=BroadcastExampleResponse)
async def handle_request(ctx: Context, sender: str, _msg: BroadcastExampleRequest):
    await ctx.send(
        sender, BroadcastExampleResponse(text=f"Hello from {ctx.agent.name}")
    )