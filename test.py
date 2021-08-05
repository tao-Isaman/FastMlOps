from FastMlOps import FastMlOps

app = FastMlOps()

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

app.createAPI(config)
