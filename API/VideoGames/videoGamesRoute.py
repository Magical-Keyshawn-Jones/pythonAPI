from fastapi import APIRouter

# Defining our Router
router = APIRouter()

@router.get('/gaming')
def games():
    return {"Message": "Gaming API Here"}
