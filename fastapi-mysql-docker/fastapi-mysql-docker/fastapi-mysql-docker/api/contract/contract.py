from fastapi import HTTPException,APIRouter
from database.query import query_get, query_create, query_update
from .models import ContractModel

def get_all_contract():
    contracts = query_get("""
        SELECT  
            *
        FROM contract
        """, ())
    return contracts

def get_contract_by_id(ID_card: str):
    contract = query_get("""
        SELECT 
            *
        FROM contract 
        WHERE ID_card = %s
        """, (ID_card))
    return contract

def add_contract(contract: ContractModel):
    last_row_id = query_create("""
                INSERT INTO contract (
                    ID_card, 
                    Contract_Num, 
                    Contract_Date, 
                    Finish_Date,
                    Start_Date,
                    Deposit
                ) VALUES (%s, %s, %s, %s, %s, %s)
                """,
              (
                  contract.ID_card,
                  contract.Contract_Num,
                  contract.Contract_Date,
                  contract.Finish_Date,
                  contract.Start_Date,
                  contract.Deposit
              )
              )
    return last_row_id

def update_contract(ID_card: str,contract: ContractModel):
    is_update = query_update("""
            UPDATE contract 
                SET Contract_Num = %s, 
                    Contract_Date = %s, 
                    Finish_Date = %s,
                    Start_Date = %s,
                    Deposit = %s
                WHERE ID_card = %s;
            """,
              (
                contract.Contract_Num,
                contract.Contract_Date,
                contract.Finish_Date,
                contract.Start_Date,
                contract.Deposit,
                ID_card
              )
            )
    if is_update:
        contract_update_data = contract.dict()
        contract_update_data.update({"ID_card": ID_card})
        return contract_update_data
    else:
        return None
    
def delete_contract(ID_card: str):
    is_deleted = query_update("""
            DELETE FROM contract 
                WHERE ID_card = %s;
            """,
            (ID_card)
    )
    return is_deleted