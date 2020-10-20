from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import io
import pandas as pd

app = FastAPI()
data = { "1" : {"item_id":1, "name": "item1"},
        "2" : {"item_id":2, "name": "item2"},
        "3" : {"item_id":3, "name": "item3"},
        "4" : {"item_id":4, "name": "item4"}}

@app.get("/")
def read_root():
    return data

@app.get("/items/{item_id}")
def read_item(item_id):
    return data.get(item_id)

@app.get("/items/layer/{item_id}")
def read_item(item_id):
    return data.get(item_id)

@app.get("/csv/download")
def getcsv():
    df = pd.DataFrame.from_dict(data, orient="index")
    print(df)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]),
                                 media_type="text/csv"
                                 )
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response