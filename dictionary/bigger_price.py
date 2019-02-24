data = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
        ]


def bigger_price(limit: int, items: list) -> list:
    max_items_list = []
    while limit:
        max_price = 0
        for item in items:
            if item['price'] > max_price:
                max_item = item
                max_price = item['price']
        max_items_list.append(max_item)
        items.remove(max_item)
        limit -= 1
    return max_items_list

print(bigger_price(2, data))
# ===================================================
data = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
        ]


def bigger_price(number, goods):
    result = sorted(goods, key=lambda x: x['price'], reverse=True)
    return result[0: number]

print(bigger_price(2, data))
