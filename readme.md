### Medicines

GET pharmacy/medicines

- 약 보기, 가격

GET pharmacy/medicines/1

- 자세한 약 정보, 가격

GET POST pharmacy/medicines/1/reviews

- 리뷰 페이지

GET PUT DELETE pharmacy/medicines/1/reviews/1

- 자기가 쓴 리뷰 수정 또는 삭제

#

### receipts

GET pharmacy/receipts

- 구매내역 간단히

GET pharmacy/receipts/1

- 더 자세한 정보

#

### users

GET POST PUT pharmacy/users

#

### diagnosis

GET POST pharmacy/diagnosis

- 진단하기

GET DELETE pharmacy/diagnosis/1

- 진단내역

#

### inventories

- GET POST pharmacy/inventories [✅]

| Params   | Description | Division      |
| -------- | ----------- | ------------- |
| medicine | int: pk     | **Essential** |
| quantity | int: >=0    | **Essential** |

- PUT DELETE pharmacy/inventories/1 [✅]

| Params   | Description | Division     |
| -------- | ----------- | ------------ |
| quantity | int: >=0    | **Optional** |
