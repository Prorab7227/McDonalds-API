from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

def load_products():
    with open('mcdonalds_project/mcdonalds_products.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Get all products
@app.get("/products", summary="Get all products", tags=["Products"])
def all_products():
    products = load_products()

    return {"items": products}

# Get product info
@app.get("/products/{product_name}", summary="Get product info", tags=["Products"])
def get_product(product_name: str):
    products = load_products()

    for product in products:
        if product['name'].lower() == product_name.lower():
            return product
        
    return {"message": f"Product with name {product_name} not found"}

# Get product by field
@app.get("/products/{product_name}/{product_field}", summary="Get field by product", tags=["Products"])
def get_product_by_parameter(product_name: str, product_field: str):
    products = load_products()

    for product in products:
        if product['name'].lower() == product_name.lower():
            if product_field in product:
                return {product_field: product[product_field]}
            return {"message": f"Field {product_field} not found"}
        
    return {"message": f"Product with name {product_name} not found"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="localhost", port=8000)