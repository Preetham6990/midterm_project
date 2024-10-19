import json

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        customer = {}
        items = {}

        for order in data:
            customer[order['phone']] = order['name']
            
            for product in order['items']:
                item_name = product['name']
                
                if item_name not in items:
                    items[item_name] = {
                        'price': product['price'],
                        'orders': 1
                    }
                else:
                    items[item_name]['orders'] += 1

    with open('customers.json', 'w') as f1:
        json.dump(customer, f1, indent=4)
        
    with open('items.json', 'w') as f2:
        json.dump(items, f2, indent=4)

read_json('example_orders.json')
