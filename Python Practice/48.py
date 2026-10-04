orders1 = [{"order_id": 1, "item": "apple"}, {"order_id": 2, "item": "banana"}]
orders2 = [{"order_id": 2, "item": "banana"}, {"order_id": 3, "item": "cherry"}]

order_ids1={order["order_id"] for order in orders1}
order_ids2={order["order_id"] for order in orders2}
common_ids=order_ids1 & order_ids2
common_ids=[order for order in orders1 if order["order_id"] in common_ids]
print(common_ids)