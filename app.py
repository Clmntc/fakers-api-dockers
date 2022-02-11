# 1. Library imports
import pickle
import uvicorn
from fastapi import FastAPI
from model import text_cleaning

# 2. Create the app object and load model
app = FastAPI()
model = pickle.load(open('model_final.pkl', 'rb'))

# 3. Index route, opens automatically on http://127.0.0.1:8000
# 3. get text, preprocessing, news prediction
@app.get("/")
def predict_news(news: str):
    cleaned_review = text_cleaning(news)

    # perform prediction
    prediction = model.predict([cleaned_review])
    output = int(prediction[0])
    return {output}
    # return {'Hello World'}

    # output dictionary
    # sentiments = {0: "Real News", 1: "Fake news"}


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# uvicorn app:app --reload