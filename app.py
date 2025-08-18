from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import pandas as pd
from req_models.models import model,scaler
from schema.user_input import UserInput
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates (if using templates)
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501"],  # or ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],
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
    return {'message':f'THE RESPONSE HAVE WITH ACCURACY OF 78.6%'}


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
                return 'THE PER UNIT VALUE IN USD IS B/W $0 TO $0.23'
            elif pred==1:
                return 'THE PER UNIT VALUE IN USD IS B/W $0.23 TO $0.367'
            elif pred==2:
                return 'THE PER UNIT VALUE IN USD IS B/W $0.367 TO $4.76'
            elif pred==3:
                return 'THE PER UNIT VALUE IN USD IS B/W $4.76 AND ABOVE'
        return JSONResponse(status_code=200, content={'predicted_category': prediction_str(prediction)})
    except Exception as err:
        return JSONResponse(status_code=400, content={'error': str(err)})

    # scaled_input = scaler.
