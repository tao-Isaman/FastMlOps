# from fastapi import FastAPI
from FastML import FastML



app = FastML()

config = {
    "method" : "POST" ,
    "path" : "/getclass" ,
    "inputModel" : {
        "x" : int,
        "y" : int
    } , 
    "responseModel" : {
        "catagory" : str ,
        "confidence" : float
    },
    "model" : "model1.h5"
}

# print(dir(app))
app.createAPI(config)