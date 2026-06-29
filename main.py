# - Input: List dictionary chứa thông tin sinh viên.
# - Output: Object JSON gồm 2 key là "message" và "data".
# - Điều kiện: Lọc sinh viên có key "status" là "active".
# - Các bước: 
#   1. Khai báo endpoint GET /students/active
#   2. Duyệt mảng lọc data
#   3. Check mảng rỗng để trả về response tương ứng.

from fastapi import FastAPI

app = FastAPI()
students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get("/students/active")
def get_active_students():
    active_students = [s for s in students if s.get("status") == "active"]
    
    if not active_students:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
        }
        
    return {
        "message": "Danh sách sinh viên đang học",
        "data": active_students
    }