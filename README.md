<div align="center">

# Todo API
Python entrance test - Kyanon Digital
  
</div>

---

- [1| Giới thiệu](#1-giới-thiệu)
- [2| Cài đặt](#2-cài-đặt)
- [3| Usage](#3-usage)

---

## 1| Giới thiệu
### a| Project structure
```
entrace_test_to_do_api
│   Pipfile
│   Pipfile.lock
│
├───database
│       entrace_test_to_do_api.sql
│
└───todo_api
    │   db.sqlite3
    │   manage.py
    │   output.txt
    │
    ├───todo_api
    │   │   asgi.py
    │   │   settings.py
    │   │   urls.py
    │   │   wsgi.py
    │   └   __init__.py
    │   
    ├───todo
    │   │   ...
    │
    │
    ├───user
    │   │   ...
    │
    └───user_auth
        │   ...

```


**Trong đó**:
+ Gồm 3 app: 
	+ user_auth: Dùng để thực hiện tính năng signup & signin 

	`API 1`, `API 2`
	+ user: Dùng để thực hiện việc truy xuất thông tin user

	`API 8`
	+ todo: Dùng để thực hiện các tính năng với đối tượng todo

	`API 3`, `API 4`, `API 5`, `API 6`, `API 7`, `API 8`
+ Database file: ```database\entrace_test_to_do_api.sql``` (MySQL)

### b| Các Package sử dụng
+ pipenv
+ django
+ djangorestframework
+ djangorestframework-simplejwt
+ mysqlclient

### c| Tính năng của API
1. **API 1 / SIGN-UP**: API cho phép người dùng mới sign-up vào hệ thống. 
2. **API 2 / SIGN-IN**: API cho phép người dùng (đã có trong hệ thống) sign-in vào hệ thống. Kết quả của API sẽ là một chuỗi JWT dùng để chứng thực cho các API tiếp theo. 
3. **API 3 / ADD-TO-DO**: cho phép người dùng thêm 1 record to-do vào database: thông tin 1 record to-do bao gồm: 
	- Id 
	- Name of the task 
	- Description of the task 
	- User Id: Id của user được assign task này 
	- Date of completion: task phải được hoàn thành trước thời gian này 
	- Status: nhận một trong 2 giá trị : NEW hoặc COMPLETE 
	- Date of creation 
	- Date of modification 
4. **API 4 / UPDATE-TO-DO**: cho phép người dùng cập nhật 1 record to-do nếu trạng thái của nó không phải là COMPLETE 
5. **API 5 / REMOVE-TO-DO**: cho phép người dùng xóa 1 record to-do nếu trạng thái của nó không phải là COMPLETE 
6. **API 6 / GET-ALL-TO-DO**: trả về danh sách tất cả các to-do hiện có
7. **API 7 / GET-TO-DO-BY-ID** : trả về một to-do với đầu vào của API là id của to-do đó 
8. **API 8 / GET-ALL-USER**: trả về danh sách tất cả các user đang có trong hệ thống 
9. **API 9 / ASSIGN-TO-DO**: với đầu vào là id của 1 to-do, thực hiện assign to-do này cho một user hiện có trong hệ thống. User được assign không được trùng với user tạo ra chứng thực JWT đang được dùng

## 2| Cài đặt

**1. Cài đặt pipenv để sử dụng môi trường ảo**
```python
python -m pip install pipenv
```

**2. Cài đặt các package cần thiết**
```python
python -m pipenv install 
```

**3. Sinh một shell trong môi trường ảo**
```python
python -m pipenv shell
```

**4. Cài đặt Database**
Import file ```database\entrace_test_to_do_api.sql``` vào hệ quản trị MySQL (Có thể sử dụng công cụ phpMyAdmin để quản lý MySQL)

**Thông tin database**
+ NAME: 'entrace_test_to_do_api',
+ USER: 'root',
+ PASSWORD': '',
+ HOST: '127.0.0.1',
+ PORT: '3306',

> Nếu có sự khác biệt so với thông tin ở trên thì chỉnh sửa lại thông tin database ở file ```todo_api\todo_api\setting.py```

**5. Khởi chạy server**


+ Kiểm tra mỉgrations
```python
python manage.py makemigrations
python manage.py migrate
```

+ Khởi chạy server
```python
python manage.py runserver
```

> Đảm bảo là database đang chạy

## 3| Usage

### a| Thông tin tài khoản
Database có đã sẵn các dữ liệu sau:

+ 4 tài khoản user
	+ 1 super user
	+ 3 normal user
+ 5 record todo

**User**

| STT | username | password |
|-----|----------|----------|
| 1   | admin    | 12345678 |
| 2   | user1    | 123456   |
| 3   | user2    | 123456   |
| 4   | user3    | 123456   |

### b| API diagrams

```text
/admin					# Admin site
/api/v1/auth/signup			# POST:   [API 1] Sign up for a new user
/api/v1/auth/signin			# POST:   [API 2] Sign in
/api/v1/todo				# GET:    [API 6] Get all todos
/api/v1/todo				# POST:   [API 3] Add a new todo
/api/v1/todo/<pk:int>			# GET:    [API 7] Get a todo
/api/v1/todo/<pk:int>			# POST:   [API 9] Assign a todo to specific user
/api/v1/todo/<pk:int>			# PUT:    [API 4] Update a todo
/api/v1/todo/<pk:int>			# DELETE: [API 5] Delete a todo
/api/v1/user				# GET:    [API 8] Get all user

```

### c| API Document
[API Doc](https://github.com/Merevoli-DatLuu/entrace_test_to_do_api/wiki/API-Documentation-V1)
