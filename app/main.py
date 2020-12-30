from fastapi import FastAPI
import os
import random
from shutil import copyfile

CONFIG_DIRECTORY = "/data/config"
INTERFACE_DIRECTORY = "/data/interface"

app = FastAPI()

configs=None
if os.path.isdir(CONFIG_DIRECTORY):
    configs = os.listdir(CONFIG_DIRECTORY)
print(configs)

interface=None
if os.path.isdir(INTERFACE_DIRECTORY):
    interface=os.path.join(INTERFACE_DIRECTORY, "wg0.conf")
print(interface)

@app.get("/")
def root():
    return "Nothing to see here!"

@app.get("/randomize")
def randomize():
    if configs and interface:
        random_config = random.choice(configs)
        src = os.path.join(CONFIG_DIRECTORY, random_config)
        copyfile(os.path.join(CONFIG_DIRECTORY, random_config), interface)
        return "Success! Using config " + random_config
    else:
        return "No configs available"
