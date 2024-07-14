# API Documentation

## Users

### `[POST] /users/` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| username | str         |
| password | str         |
| name     | str         |
| email    | str         |

> Response

| Data        | Description |
| ----------- | ----------- |
| last_login  | str: token  |
| username    | str: token  |
| email       | str: token  |
| date_joined | str: token  |
| name        | str: token  |

### `[POST] /users/username/<str:username>/` [✔]

> Response

**login success** You can receive `HTTP 200 OK`
**login fail** You can receive `HTTP 204 NO CONTENT`

### `[POST] /users/log-in/` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| username | str         |
| password | str         |

> Response

**login success** You can receive `HTTP 200 OK`
**login fail** You can receive `HTTP 401 UNAUTHORIZED`

### `[POST] /users/me/` [✔]

> Request

| Data        | Description |
| ----------- | ----------- |
| last_login  | str         |
| username    | str         |
| email       | str         |
| date_joined | str         |
| name        | str         |

> Response

**login success** You can receive `HTTP 200 OK`
**login fail** You can receive `HTTP 401 UNAUTHORIZED`

### `[POST] /users/token/` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| username | str         |
| password | str         |

> Response

| Data    | Description |
| ------- | ----------- |
| refresh | str: token  |
| access  | str: token  |

### `[POST] /users/token/refresh/` [✔]

> Request

| Data    | Description |
| ------- | ----------- |
| refresh | str: token  |

> Response

| Data   | Description |
| ------ | ----------- |
| access | str: token  |

## Receipts

### `[GET] /receipts/`[✔]

> Response

| Data(Many)  | Description |
| ----------- | ----------- |
| id          | int         |
| total_price | int         |
| purchase_at | str         |

### `[GET] /receipts/1/` [✔]

> Response

| Data           | Description          |
| -------------- | -------------------- |
| purchase_at    | str                  |
| total_price    | int                  |
| past_medicines | **_past_medicines_** |

| **_past_medicines_**(Many)     | Description    |
| ------------------------------ | -------------- |
| quantity                       | int            |
| price_per_medicine_at_purchase | str            |
| medicine                       | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| id             | int         |
| name           | str         |
| company        | str         |
| price          | int         |
| average_rating | float       |
| review_count   | int         |
| remaining      | int         |

## Inventories

### `[GET POST] /inventories/` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| medicine | int: id     |
| quantity | int: >=0    |

> Response

`GET이면 Many O`<br>
`POST면 Many X > 하나만`

| Data(Many) | Description    |
| ---------- | -------------- |
| id         | int            |
| quantity   | int            |
| medicine   | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| id             | int         |
| name           | str         |
| company        | str         |
| price          | int: >=0    |

### `[PUT DELETE] /inventories/1/` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| quantity | int: >=0    |

> Response

| Data     | Description    |
| -------- | -------------- |
| id       | int            |
| quantity | int            |
| medicine | **_medicine_** |

| medicine | Description |
| -------- | ----------- |
| id       | int         |
| name     | str         |
| company  | str         |
| price    | int         |

### `[POST] /inventories/purchase/` [✔]

> Response

**_인벤토리 비어있으면_** You can receive `HTTP 400 BAD REQUEST`<br>
**_재고가 없으면_** You can receive `HTTP 204 NO CONTENT`<br>
**_통과_** You can receive `HTTP 200 OK`

## Medicines

### `[GET] /medicines/` [✔]

> Request

| _Params_ | Description        | Division     |
| -------- | ------------------ | ------------ |
| page     | int >=1(default=1) | **Optional** |
| search   | str                | **Optional** |

> Response

| Data(Many)     | Description           |
| -------------- | --------------------- |
| id             | int                   |
| name           | str                   |
| company        | str                   |
| price          | int                   |
| average_rating | float (소숫점 첫번쨰) |
| review_count   | int                   |
| remaining      | int                   |

### `[GET] /medicines/1/` [✔]

> Response

| Data            | Description |
| --------------- | ----------- |
| id              | int         |
| created_at      | str         |
| updated_at      | str         |
| serial_number   | int         |
| name            | str         |
| main_ingredient | str         |
| efficacy        | str         |
| usage           | str         |
| need_to_know    | str         |
| cautions        | str         |
| beware_food     | str         |
| side_effect     | str         |
| how_to_store    | str         |
| price           | int         |
| average_rating  | float       |
| review_count    | int         |
| is_favorite     | boolean     |

### `[GET POST] /medicines/1/reviews/` [✔]

> request

| Data   | Description |
| ------ | ----------- |
| detail | str         |
| rating | int (1~5)   |

| _Params_ | Description        |
| -------- | ------------------ |
| page     | int >=1(default=1) |

> Response

| Data(Many) | Description        |
| ---------- | ------------------ |
| id         | int                |
| updated_at | str                |
| created_at | str                |
| detail     | str                |
| rating     | float(소수점 첫째) |
| user       | **_user_**         |

| **_user_** | Description |
| ---------- | ----------- |
| id         | int         |
| username   | str         |

## Reviews

### `[GET] /reviews/` (내가 단 리뷰들) [✔]

> Response

| Data(Many) | Description    |
| ---------- | -------------- |
| id         | int            |
| updated_at | str            |
| created_at | str            |
| detail     | str            |
| rating     | int            |
| medicine   | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| id             | int         |
| name           | str         |
| company        | str         |
| price          | int         |
| average_rating | float       |
| review_count   | int         |
| remaining      | int         |

### `[PUT DELETE] /reviews/1/` [✔]

> Request

| Data   | Description |
| ------ | ----------- |
| detail | str         |
| rating | int(1~5)    |

> Response

| Data       | Description    |
| ---------- | -------------- |
| id         | int            |
| updated_at | str            |
| created_at | str            |
| detail     | str            |
| rating     | int            |
| medicine   | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| id             | int         |
| name           | str         |
| company        | str         |
| price          | int         |
| average_rating | float       |
| review_count   | int         |
| remaining      | int         |

## Diagnosis #TODO

### `[POST] /diagnosis/` [✔]

> Request

| Data   | Description |
| ------ | ----------- |
| prompt | str         |

> Response

/diagnosis/1/
아래에 적혀있는 곳으로 redirect 시킴

### `[GET POST] /diagnosis/1/` []

> Request

| Data   | Description |
| ------ | ----------- |
| prompt | str         |

> Response

| Data    | Description   |
| ------- | ------------- |
| id      | int           |
| title   | str           |
| queries | **_queries_** |

| **_queries_** | Description                    |
| ------------- | ------------------------------ |
| prompt        | str (사용자가 입력한 프롬프트) |
| result        | str (gpt가 답한 답변)          |
| created_at    | str                            |

### `[GET] /diagnosis/history/` []

> Request

| _Params_ | Description        |
| -------- | ------------------ |
| page     | int >=1(default=1) |

> Response

| Data(Many) | Description |
| ---------- | ----------- |
| id         | int         |
| title      | str         |
| created_at | str         |

## Favorites

### `[GET] /favorites/` (나의 즐겨찾기) [✔]

> Response

| Data(Many) | Description    |
| ---------- | -------------- |
| medicine   | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| id             | int         |
| name           | str         |
| company        | str         |
| price          | int         |
| average_rating | float       |
| review_count   | int         |
| remaining      | int         |
