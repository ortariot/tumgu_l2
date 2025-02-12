import uvicorn
from fastapi import FastAPI

from field import Student

app = FastAPI()

RESULT = 0
OPERATIONS = list()
# LANGUES = {
#     1: "c++",
#     2: "js",
#     3: "python",
# }


# @app.get("/")
# async def root():
#     return {"mes": "hello world"}


# @app.get("/lang/{item_id}")
# async def lang(item_id):
#     return {"lang": LANGUES.get(int(item_id), "unknown")}



#"localhost:port/items/1?limit=100&page=1"
# @app.get("/sum")
# async def sum(a: int = 0, b: int = 0):
#         return {"sum": a+b}
    
# @app.get("/dif")
# async def dif(a: int = 0, b: int = 0):
#         return {"dif": a-b}
    
# @app.get("/mul")
# async def mul(a: int = 0, b: int = 0):
#         return {"mul": a*b}
    
# @app.get("/div")
# async def div(a: int = 0, b: int = 0):
#         return {"div": a/b}


# @app.get("/polish")
# async def div(op: str, a: int = 0):
#     global RESULT
    
#     if op == "+":
#         RESULT += a
#     elif op == "-":
#         RESULT -= a
#     elif op == "*":
#         RESULT *= a
#     elif op == "/" and a > 0:
#         RESULT /= a
#     else:
#         return {"error": f"operation {op} not suported"}
    
#     OPERATIONS.append(f"{op} {a}")
    
#     return {"result": RESULT}
    
@app.get("/student")
async def sum(model: Student):
    print(model.dump_json())
    
    return {}

# @app.get("/polish_op")
# async def div():
    
#     return {"op": OPERATIONS}



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
    
    
"""
Создать FastAPI приложение реализующее работу простого калькулятора:
    - методы сложения, вычитания, умножения, деления
    *- метод создания выражения, возможность добавления слодных выражения типа: (а+b)*c + (d - e)/(f-g) ...
     - метод просмотра текущего выражения
     - метод выполнения выражения
"""