from arbiter import ArbiterNode, ArbiterRunner
from fastapi import FastAPI

app = ArbiterNode()

@app.http_task()
async def simple_http_stream(x: int):
    for i in range(5):
        yield {"result": "success_stream + " + str(x + i)}


# if __name__ == '__main__':
#     ArbiterRunner.run(
#         app=app,
#     )
