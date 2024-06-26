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

| Data    | Description |
| ------- | ----------- |
| refresh | str: token  |
| access  | str: token  |

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

### `[POST] /users/token/verify/` [✔]

> Request

| Data  | Description |
| ----- | ----------- |
| token | str         |

> Response

**If is valid** You can receive `HTTP 200 OK`

### `[POST] /users/token/refresh/` [✔]

> Request

| Data    | Description |
| ------- | ----------- |
| refresh | str: token  |

> Response

| Data        | Description |
| ----------- | ----------- |
| username    | str         |
| email       | str         |
| date_joined | str         |

## Receipts

### `[GET] /receipts/`[✔]

> Response

| Data(Many)  | Description |
| ----------- | ----------- |
| id          | int         |
| medicine    | str: name   |
| quantity    | int         |
| purchase_at | str         |

### `[GET] /receipts/1/` [✔]

> Response

| Data                           | Description    |
| ------------------------------ | -------------- |
| id                             | int            |
| purchase_at                    | str            |
| quantity                       | int            |
| price_per_medicine_at_purchase | int            |
| medicine                       | **_medicine_** |

| **_medicine_**  | Description |
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

## Inventories

### `[GET POST] /inventories/` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| medicine | int: id     |
| quantity | int: >=0    |

> Response

| Data(Many) | Description    |
| ---------- | -------------- |
| id         | int            |
| quantity   | str            |
| medicine   | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| name           | str         |
| company        | str         |
| price          | int: >=0    |

### `[PUT DELETE] /inventories/1/` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| quantity | int: >=0    |

## Medicines

### `[GET] /medicines/` [✔]

> Request

| _Params_ | Description        | Division     |
| -------- | ------------------ | ------------ |
| page     | int >=1(default=1) | **Optional** |
| search   | str                | **Optional** |

> Response

| Data(Many) | Description |
| ---------- | ----------- |
| id         | int         |
| name       | str         |
| company    | str         |
| price      | int         |

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

### `[GET POST] /medicines/1/reviews/` [✔]

> request

| Data   | Description |
| ------ | ----------- |
| detail | str         |

| _Params_ | Description        |
| -------- | ------------------ |
| page     | int >=1(default=1) |

> Response

| Data(Many) | Description |
| ---------- | ----------- |
| id         | int         |
| updated_at | str         |
| created_at | str         |
| detail     | str         |
| user       | **_user_**  |

| **_user_** | Description |
| ---------- | ----------- |
| id         | int         |
| username   | str         |

## Reviews

### `[GET] /reviews/` [✔]

> Response

| Data(Many) | Description  |
| ---------- | ------------ |
| review     | **_review_** |

| **_review_** | Description    |
| ------------ | -------------- |
| id           | int            |
| updated_at   | str            |
| created_at   | str            |
| detail       | str            |
| medicine     | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| id             | int         |
| name           | str         |
| company        | str         |
| price          | int         |

### `[PUT DELETE] /reviews/1/` [✔]

> Request

| Data   | Description |
| ------ | ----------- |
| detail | str         |

> Response

| Data       | Description    |
| ---------- | -------------- |
| id         | int            |
| updated_at | str            |
| created_at | str            |
| detail     | str            |
| medicine   | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| id             | int         |
| name           | str         |
| company        | str         |
| price          | int         |

## Diagnosis #TODO

### `[POST] /diagnosis/` []

> Request

| Data   | Description |
| ------ | ----------- |
| prompt | str         |

> Response

/diagnosis/1/

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
