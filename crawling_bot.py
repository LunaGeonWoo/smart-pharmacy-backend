import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import random
import time

# 디렉토리 생성
os.makedirs("crawling_imgs", exist_ok=True)

# 엑셀 파일 읽기 및 필터링
df = (
    pd.read_excel("e약은요정보검색.xlsx")
    .dropna(subset=["이 약의 효능은 무엇입니까?"])
    .reset_index(drop=True)
)

# 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("user-agent=facebookexternalhit")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

results = []

# 체크포인트 파일 확인
checkpoint_files = sorted(
    [
        f
        for f in os.listdir("crawling_imgs")
        if f.startswith("image_sources_checkpoint_bot_")
    ]
)
if checkpoint_files:
    latest_checkpoint = checkpoint_files[-1]
    results_df = pd.read_csv(os.path.join("crawling_imgs", latest_checkpoint))
    results = results_df.to_dict("records")
    start_index = results[-1]["index"] + 1
else:
    start_index = 0

# 이미지 크롤링
for i, name in enumerate(df["제품명"][start_index:], start=start_index):
    driver.get("https://www.google.com/imghp?hl=ko")
    search_box = driver.find_element(By.NAME, "q")
    time.sleep(random.random() * 1.2)
    search_box.send_keys(name)

    try:
        search_box.submit()
    except StaleElementReferenceException:
        search_box = driver.find_element(By.NAME, "q")
        search_box.submit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "DS1iW"))
    )

    divs = driver.find_elements(By.CLASS_NAME, "DS1iW")

    if divs:
        img_src = divs[0].get_attribute("src")
        results.append({"index": i, "img_src": img_src})

    if (i + 1) % 50 == 0:
        results_df = pd.DataFrame(results)
        results_df.to_csv(
            f"crawling_imgs/image_sources_checkpoint_bot_{i + 1}.csv", index=False
        )
        # 이전 체크포인트 파일 삭제
        if (i + 1) > 50:
            os.remove(f"crawling_imgs/image_sources_checkpoint_bot_{i + 1 - 50}.csv")
    print(f"{(i + 1) % 50} / 50")
    time.sleep(random.random() * 1.2)

# 결과 저장
results_df = pd.DataFrame(results)
results_df.to_csv("crawling_imgs/image_sources_bot.csv", index=False)

# 드라이버 종료
driver.quit()
