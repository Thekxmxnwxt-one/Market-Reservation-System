from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from contract import ContractModel,get_all_contract,get_contract_by_id,add_contract,update_contract,delete_contract

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Get param
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_all_contract/", response_model=list[ContractModel])
def get_all_contract_api():
    contracts = get_all_contract()
    #print(products)
    return JSONResponse(status_code=200, content=jsonable_encoder(contracts))

@app.get("/get_contract/{ID_card}", response_model=ContractModel)
def get_product_by_id_api(ID_card:str):
    contracts = get_contract_by_id(ID_card)
    print(contracts)
    return JSONResponse(status_code=200, content=jsonable_encoder(contracts))

##CREATE
@app.post('/create_contract/', response_model=ContractModel)
def create_contract_api(contract: ContractModel):
    contract_id = add_contract(contract)
    return JSONResponse(status_code=201, content={'status': 'success', 'contract_ID_card': contract_id})

## UPDATE
@app.put("/update_contract/{ID_card}", response_model=ContractModel)
def update_contract_api(ID_card: str, contract: ContractModel):
    # Check if product exists
    existing_product = get_contract_by_id(ID_card)
    if len(existing_product) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    updated_contract = update_contract(ID_card, contract)
    if updated_contract:
        return JSONResponse(status_code=200, content={'status': 'success', 'contract_data': updated_contract})
    else:
        raise HTTPException(status_code=500, detail="Failed to update data")
    
#Delete
@app.delete("/delete_contract/{ID_card}", response_model=ContractModel)
def delte_contract_api(ID_card: str):
    # Check if product exists
    existing_contract = get_contract_by_id(ID_card) 
    if len(existing_contract) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    is_deleted = delete_contract(ID_card)
    if is_deleted:
        return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
    else:
        raise HTTPException(status_code=500, detail="Failed to delete data")
