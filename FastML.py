from fastapi import FastAPI
from pydantic import BaseModel, create_model
import numpy as np
from tensorflow.keras.models import load_model
import json

class FastML(FastAPI):


    def helloTao(self):
        print("Hello Tao")

    def createAPI(self, config):
        method, path, inputModel, responseModel, model = (config.get(key) for key in ['method', 'path', 'inputModel', 'responseModel', 'model' ])
        inputModel = self.addDefaultValue(inputModel)
        inputModel = create_model('BaseModel', **inputModel)
        mlModel = load_model(model)
        if method == 'GET' :
            pass
        elif method == 'POST' :
            @FastAPI.post(self, path=path)
            async def createAPI(data: inputModel):
                category, confidence = await self.predict(data.__dict__, mlModel)
                res = {'class': category, 'confidence':confidence}
                return json.dumps(res)
    
    async def predict(self, inputs, model):
        X = np.array([list(inputs.values())])

        pred = model.predict(X)

        res = np.argmax(pred, axis=1)[0]
        confidence = float(pred[0][res])

        return int(res) , float(confidence)

    def addDefaultValue(self, inputModel):
        for key , val in inputModel.items() :
            if val == int:
                inputModel[key] = 0
            elif val == str:
                inputModel[key] = ''
            elif val == float:
                inputModel[key] = 0.0
            # if 
        return inputModel





        


