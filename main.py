from fastapi import FastAPI

# ۱. ساختن یک نمونه از برنامه FastAPI
app = FastAPI()

# ۲. تعریف یک مسیر (Route) ساده روی متد GET
@app.get("/")
def read_root():
    return {"status": "success", "message": "سلام! اولین API من با موفقیت کار می‌کنه!"}

# ۳. یک مسیر دیگر برای نمونه
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "category": "cloud-tools"}