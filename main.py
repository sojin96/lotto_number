import random
import numpy as np
from fastapi import FastAPI
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware  # cross domin

# 입력받은 예상 번호 List 변수
LOTTO_NUMBERS = []

# 지난주 번호 List 변수
LAST_LOTTO_NUMBERS = []

# FastAPI() 실행하여 app이란 변수에 할당
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:8887",
    "http://127.0.0.1",
    "http://127.0.0.1:5000",
    "http://127.0.0.1:8887",
    "http://119.195.78.216"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 지난주 로또번호 가져오기(랜덤)
@app.get("/api/get_last_lotto_numbers")
def get_last_lotto_numbers():

    LAST_LOTTO_NUMBERS.clear()

    while True:
        lotto_number = str(random.randrange(1, 46)).zfill(2)

        if lotto_number not in LAST_LOTTO_NUMBERS:
            LAST_LOTTO_NUMBERS.append(lotto_number)

        if len(LAST_LOTTO_NUMBERS) > 5:
            break

    print(LAST_LOTTO_NUMBERS)
    return json.loads(json.dumps(LAST_LOTTO_NUMBERS))

# 입력받은 예상 번호 문자열을 리스트로 변환
# http://xxxxxxxx/api/insert_lotto_numbers?numbers=11 22 33 44 32 17


@app.get("/api/insert_lotto_numbers")
def insert_lotto_numbers(numbers):

    number_arrary = numbers.split(" ")
    print(100, numbers, number_arrary)

    LOTTO_NUMBERS.clear()
    for lotto_number in number_arrary:
        LOTTO_NUMBERS.append(str(lotto_number).zfill(2))

    print(200, LOTTO_NUMBERS)

    return json.loads(json.dumps(LOTTO_NUMBERS))

# 자동 번호 가져오기


@app.get("/api/get_auto_lotto_numbers")
def get_auto_lotto_numbers():

    LOTTO_NUMBERS.clear()
    while True:
        lotto_number = str(random.randrange(1, 46)).zfill(2)

        if lotto_number not in LOTTO_NUMBERS:
            LOTTO_NUMBERS.append(lotto_number)

        if len(LOTTO_NUMBERS) > 5:
            break

    print(LOTTO_NUMBERS)

    return json.loads(json.dumps(LOTTO_NUMBERS))

# 번호 비교


@app.get("/api/check_lotto_numbers")
def check_lotto_numbers():

    result = False
    print(LOTTO_NUMBERS, LAST_LOTTO_NUMBERS)
    if LOTTO_NUMBERS == LAST_LOTTO_NUMBERS:
        result = True

    return json.loads(json.dumps({"RESULT": result}))


if __name__ == "__main__":

    # 웹서버 실행
    uvicorn.run(app, host="0.0.0.0", port=9003)
