# hoseo-lunch-bot

📸 인스타그램 계정(@hoseofood)의 최신 게시물을 캡처하고 Supabase에 업로드하는 자동 봇입니다.

## 작동 방식

- 매주 월~금 오전 11:30
- `@hoseofood` 인스타그램 계정 접속 → 첫 번째 게시물 클릭 → 전체 화면 캡처
- Supabase Storage에 업로드

## 구성 파일

| 파일 | 설명 |
|------|------|
| `main.py` | 인스타그램 캡처 + Supabase 업로드 |
| `requirements.txt` | 필요한 Python 라이브러리 목록 |
| `.github/workflows/lunch.yml` | GitHub Actions 자동 실행 설정 |
| `README.md` | 이 리포지토리 설명서 |

## GitHub Secrets 설정

Settings → Secrets → Actions 에 아래 키들을 추가하세요:

- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_BUCKET` (예: captures)

