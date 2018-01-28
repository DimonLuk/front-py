import os
import sys
import json
import importlib
PATH = "application"
if __name__ == "__main__":
    if sys.argv[1] == "start" and len(sys.argv) == 2:
        framework = os.path.join(os.getcwd(),PATH)
        sys.path.append(framework)
        for dirs,subdirs,files in os.walk(framework):
            if not "__pycache__" in dirs:
                sys.path.append(dirs)
        params = {}
        with open(os.path.join(PATH,"config.json"),"r") as file:
            params = json.load(file)
        app = importlib.import_module(params["source_file"])
        app.run_app(address=params["address"],port=params["port"])
    elif sys.argv[1] == "config" and len(sys.argv) == 2:
        params = {}
        source_file = input("Enter the filename where you application is (for example sample): ")
        if not source_file:
            raise ValueError("Please enter the filename it's required")
        address = input("Enter the addres you want to host (localhost is default): ")
        if not address:
            address = "localhost"
        port = input("Enter the port you want to host (8000 is default): ")
        if port:
            port = int(port)
        elif not port:
            port = 8000
        with open(os.path.join(PATH,"config.json"),"w") as file:
            json.dump({"source_file":source_file,"address":address,"port":port},file)
    else:
        print("""
Avaliable commands:
    start - to start app
    config - to setup configuration of application
        """)
