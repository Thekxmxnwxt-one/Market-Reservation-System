from pydantic import BaseModel
#from typing import Optional

class ContractModel(BaseModel):
    ID_card:  str
    Contract_Num: int
    Contract_Date: str
    Finish_Date: str
    Start_Date: str
    Deposit: int