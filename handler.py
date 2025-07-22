import runpod
from hello import say_hello

def handler(event):
    name = event.get("input", {}).get("name", "World")
    return {"message": say_hello(name)}

runpod.serverless.start({"handler": handler})
