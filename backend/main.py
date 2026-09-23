from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def home():
    return{
        "message": "welcome to IFSC branch Mapping Tool"
    }

@app.get("/api/health")
def health():
    return{
        "message":"welcome to IFSC branch Mapping Tool"
    }
@app.get("/api/branches")
def get_branches():
    return [
        {
            "id":1,
            "name":"banglore Main",
            "city":"banglore",
            "state": "karnataka"
        },
        {
            "id": 2,
            "name": "Mumbai Central",
            "city": "Mumbai",
            "state": "Maharashtra"
        },
         {
            "id": 3,
            "name": "Delhi North",
            "city": "Delhi",
            "state": "Delhi"
        }
    ]