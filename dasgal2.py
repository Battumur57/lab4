
stores = [
    ["Бамбарууш", 534, 5000, 487, 10000],
    ["Жимсхэн", 764, 4800, 423, 9300],
    ["Fruits", 136, 5000, 228, 10000]
]

total_revenue = 0  

for store in stores:
    name = store[0] 
    annual_sold_kg = store[1]  
    per_kg_price = store[2] 
    daily_sold_kg = store[3]  
    per_day_price = store[4] 

   
    revenue = (annual_sold_kg * per_kg_price) + (daily_sold_kg * per_day_price * 365)

    print(f"{name} дэлгүүрийн орлого: {revenue}")
    total_revenue += revenue 

