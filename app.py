from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import pandas as pd
from req_models.models import model,scaler
from schema.user_input import UserInput
from fastapi.staticfiles import StaticFiles

app = FastAPI()


origins = [
    "https://fractal-exportprice-predictor.onrender.com",  # frontend Render URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # specify frontend domain
    allow_credentials=True,
    allow_methods=["*"],          # or restrict to specific methods
    allow_headers=["*"],
)


app = FastAPI()
frontend = Jinja2Templates(directory="frontend")


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return frontend.TemplateResponse("main.html", {"request": request})


@app.get('/about')
def hello():
    return {'message':f'This API is for Fractal Export Price Prediction with XGBOOST Classifier of 78.6% of accuracy'}


@app.post('/predict')
def predict_user_input(data: UserInput):
    input_df = pd.DataFrame([{
        'QTY': int(data.quantity), 
        'DRAWBACK': data.drawback_num, 
        'FOREIGN_COUNTRY': data.foreign_country_num, 
        'Categories': data.categories_num,
        'FOREIGN PORT CONTINENT': data.FOREIGN_PORT_CONTINENT
    }])

    try:
        scaled_input = scaler.transform(input_df)  # fixed typo
        prediction = model.predict(scaled_input)[0]  # call predict on model, not app
        def prediction_str(pred):
            if pred ==0:
                return 'The Per Unit value in USD is b/w $0 to $0.23'
            elif pred==1:
                return 'The Per Unit value in USD is b/w $0.23 to $0.367'
            elif pred==2:
                return 'The Per Unit value in USD is b/w $0.367 to $ 4.76'
            elif pred==3:
                return 'The Per Unit value in USD is b/w $4.76 to and above'
        return JSONResponse(status_code=200, content={'predicted_category': prediction_str(prediction)})
    except Exception as err:
        return JSONResponse(status_code=400, content={'error': str(err)})

    # scaled_input = scaler.
    
