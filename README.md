# 🍔 McDonald's API

Developed by [@Prorab7227]

## 🕷 Spiders

### mcd_m
Spider for collecting basic McDonald's menu information:
- Product URL
- Product ID
- Product name

### mcd_i
Spider for collecting detailed information about each product:
- Name
- Description
- Portion size
- Calories
- Fats
- Unsaturated fats
- Carbohydrates
- Sugars
- Proteins
- Salt

## 📚 Available Endpoints

### 📋 Get All Products

```
GET /products
```

### 📋 Get Product Info By Name

```
GET /products/{product_name}
```

### 📋 Get Product By Field And Name

```
GET /products/{product_name}/{product_field}
```


