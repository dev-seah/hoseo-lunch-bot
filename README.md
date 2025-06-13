# 🥗 hoseo-lunch-bot

> 월~금 오전 11:30에 @hoseofood 인스타그램 계정의 최신 게시물을 자동 캡쳐하고 Supabase에 업로드하는 봇입니다.

---

## ✅ 기능 요약

- `@hoseofood` 계정의 **최신 게시물 캡쳐**
- Supabase Storage에 이미지 자동 업로드
- 파일명에 날짜 및 시간(`예: lunch_250613_1130.png`) 포함
- 매주 **평일 오전 11:30 자동 실행** (Railway cron)

---

## 🚀 사용 방법

### 1. 환경변수 설정 (`.env`)

```env
SUPABASE_URL=YOUR_SUPABASE_URL
SUPABASE_KEY=YOUR_SUPABASE_ANON_KEY
SUPABASE_BUCKET=YOUR_BUCKET_NAME
```

### 2. 필요 패키지 설치

```bash
pip install -r requirements.txt
playwright install
```

### 3. 수동 실행 (테스트용)

```bash
python main.py
```

---

## ☁️ Railway에서 자동 실행하기

1. Railway에서 GitHub 저장소 연결
2. `Deployments > Schedule` 에서 다음과 같이 설정:

- **Command**: `python main.py`
- **Schedule**: `30 2 * * 1-5`  
  (한국 시간 오전 11:30, 월~금)

3. `.env` 항목을 Environment 변수로 등록

---

## 📦 결과 파일 예시

Supabase에 다음 경로로 저장됨:

```
captures/lunch_250613_1130.png
```

---

## 👀 참고 계정

[https://www.instagram.com/hoseofood](https://www.instagram.com/hoseofood)

---

본 봇은 오직 **공개 계정의 콘텐츠**만 수집하며, 비상업적 목적으로만 사용됩니다.