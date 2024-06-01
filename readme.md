# API Documentation

## Users

### `[POST] /users/token` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| username | str         |
| password | str         |

> Response

| Dat     | Description |
| ------- | ----------- |
| refresh | str: token  |
| access  | str: token  |

### `[POST] /users/token/verify` [✔]

> Request

| Data  | Description |
| ----- | ----------- |
| token | str         |

> Response

**If is valid** You can receive `HTTP 200 OK`

### `[POST] /users/token/refresh` [✔]

> Request

| Data    | Description |
| ------- | ----------- |
| refresh | str: token  |

> Response

| Data    | Description |
| ------- | ----------- |
| refresh | str: token  |
| access  | str: token  |

## Receipts

### `[GET] /receipts`[✔]

> Response

| Data(Many)  | Description |
| ----------- | ----------- |
| id          | int         |
| medicine    | str: name   |
| quantity    | int         |
| purchase_at | str         |

### `[GET] /receipts/1` [✔]

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

### `[GET POST] /inventories` [✔]

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

### `[PUT DELETE] /inventories/1` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| quantity | int: >=0    |

## Medicines

### `[GET] /medicines` [✔]

> Request

| _Params_ | Description |
| -------- | ----------- |
| page     | int >=1     |

> Response

| Data(Many) | Description    |
| ---------- | -------------- |
| medicine   | **_medicine_** |

| **_medicine_** | Description |
| -------------- | ----------- |
| name           | str         |
| company        | str         |
| price          | int         |

### `[GET] /medicines/1` []

- 자세한 약 정보, 가격

### `[GET/POST] /medicines/1/reviews` []

- 리뷰 페이지

### `[GET/PUT/DELETE] /medicines/1/reviews/1` []

- 자기가 쓴 리뷰 수정 또는 삭제

---

## Diagnosis

### `[GET POST] /diagnosis` []

- 진단하기

### `[GET DELETE] /diagnosis/1` []

- 진단내역
