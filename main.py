from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API de Demonstração Swagger",
    description="API para demonstrar a documentação viva do FastAPI",
    version="1.0.0"
)


class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None


class Product(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    in_stock: bool = True


@app.get("/", tags=["Home"])
def read_root():
    """Rota principal da API"""
    return {"message": "Bem-vindo à API de Demonstração Swagger"}


@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int, q: Optional[str] = None):
    """Busca um item específico por ID"""
    return {"item_id": item_id, "q": q}


@app.get("/users", tags=["Users"])
def list_users():
    """Lista todos os usuários"""
    return {
        "users": [
            {"id": 1, "name": "João Silva", "email": "joao@example.com"},
            {"id": 2, "name": "Maria Santos", "email": "maria@example.com"}
        ]
    }


@app.post("/users", tags=["Users"])
def create_user(user: User):
    """Cria um novo usuário"""
    return {
        "message": "Usuário criado com sucesso",
        "user": user,
        "id": 123
    }


@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int):
    """Busca um usuário específico por ID"""
    return {
        "id": user_id,
        "name": "João Silva",
        "email": "joao@example.com",
        "age": 30
    }


@app.put("/users/{user_id}", tags=["Users"])
def update_user(user_id: int, user: User):
    """Atualiza um usuário existente"""
    return {
        "message": "Usuário atualizado com sucesso",
        "id": user_id,
        "user": user
    }


@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int):
    """Remove um usuário"""
    return {"message": f"Usuário {user_id} removido com sucesso"}


@app.get("/products", tags=["Products"])
def list_products(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    """Lista produtos com filtros opcionais"""
    return {
        "products": [
            {"id": 1, "name": "Notebook", "price": 3500.00, "category": "Eletrônicos"},
            {"id": 2, "name": "Mouse", "price": 50.00, "category": "Acessórios"}
        ],
        "filters": {
            "category": category,
            "min_price": min_price,
            "max_price": max_price
        }
    }


@app.post("/products", tags=["Products"])
def create_product(product: Product):
    """Cria um novo produto"""
    return {
        "message": "Produto criado com sucesso",
        "product": product,
        "id": 456
    }


@app.get("/health", tags=["System"])
def health_check():
    """Verifica o status da API"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": "2025-12-01T00:00:00Z"
    }
