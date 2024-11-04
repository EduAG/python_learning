import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items

app = Flask(__name__)


@app.get("/store")
def get_stores():
   try:
      return {"store": list(stores.values())}
   except KeyError:
      abort(404, message = "Store not found.")

@app.get("/store/<string:store_id>")
def get_store(store_id):
   try:
      return stores[store_id]
   except KeyError:
      abort(404, message = "Store not found.")

@app.post("/store")
def create_store():
   try:
      store_data = request.get_json()
      if "name" not in store_data:
         abort(400, message = "Bad Request. Ensure 'name' are included in the JSon play")
      for store in stores.values():
         if store_data["name"] == store["name"]:
            abort(400, "Bad Request. Ensure 'price, 'store_id, and 'name' are included in the JSon play"
                  )
      for store in stores.values():
         if store_data["name"] == store["name"]:
            abort(400, message = f"Store already exist")

      store_id = uuid.uuid4().hex
      new_store = {**store_data, "id": store_id}
      stores[store_id] = new_store
      return new_store, 201
   except KeyError:
      abort(500, message = "Store not created.")

@app.put("/store/<string:store_id>")
def update_store(store_id):
   try:
      store_data = request.get_json()
      if bool(store_data["name"]):
         stores[store_id]["name"] = store_data["name"]
         return stores[store_id]
      abort(400, message = "Bad Request. Ensure 'price, 'store_id, and 'name' are included in the JSon play")
   except KeyError:
      abort(404, message="Store not found.")   

@app.delete("/store/<string:store_id>")
def delete_store(store_id):
   if bool(stores[store_id]):
      del stores[store_id]
      abort(410, message  = "Store deleted." )
   abort(404, message = "Store not found.")

@app.get("/item")
def get_all_items():
   try:
      return {"items": list(items.values())}
   except KeyError:
      abort(404, message = "Items not found.")

@app.get("/item/<string:item_id>")
def get_item(item_id):
      try:
         return items[item_id]
      except KeyError:
         abort(404, message = "Items not found.")
     
@app.post("/item")
def create_item():
   item_data = request.get_json()
   print(item_data)

   if("price" not in item_data
      or "store_id" not in item_data
      or "name" not in item_data):
      abort(400,
            message = "Bad Request. Ensure 'price, 'store_id, and 'name' are included in the JSon play")
   
      # for item in items.value():
      #    if(item_data["name"] == item["name"]
      #       and item_data["store_id"] == item["store_id"]):
      #       abort(400, message=f"Item already exist")

   if item_data["store_id"] not in stores:
      abort(404, message = "Store not found.")

   item_id = uuid.uuid4().hex
   item = {**item_data, "id": item_id}
   items[item_id] = item
   return item, 201

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
   print(items)
   if bool(items[item_id]):
      del items[item_id]
      abort(410, message  = "Item deleted." )
   abort(404, message = "Item not found.")

@app.put("/item/<string:item_id>")
def update_item(item_id):
   try:
      item_data = request.get_json()
      print(item_data)
      print(items)
      if bool(item_data["name"] and item_data["price"]):
         items[item_id]["name"] = item_data["name"]
         items[item_id]["price"] = item_data["price"]
         return items[item_id]
      abort(400, message = "Bad Request. Ensure 'price, 'store_id, and 'name' are included in the JSon play")
   except KeyError:
      abort(404, message="Item not found.") 

if __name__ == '__main__':
   app.run()