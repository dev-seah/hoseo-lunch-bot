import os
import time
import sys
from datetime import datetime
from supabase import create_client, Client
from playwright.sync_api import sync_playwright

# GitHub Secrets에서 불러오기
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "captures")

def capture_instagram_post(username: str, screenshot_path: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 2400})
        try:
            page.goto(f"https://www.instagram.com/{username}/", timeout=60000)
            page.wait_for_timeout(5000)
            page.locator('article a').first.click()
            page.wait_for_timeout(4000)
            page.screenshot(path=screenshot_path)
            print(f"✅ 캡쳐 완료: {screenshot_path}")
        except Exception as e:
            print("❌ 캡처 실패:", e)
            sys.exit(1)
        finally:
            browser.close()

def upload_to_supabase(filepath: str, filename: str):
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        with open(filepath, "rb") as f:
            res = supabase.storage().from_(SUPABASE_BUCKET).upload(
                path=f"captures/{filename}",
                file=f,
                file_options={"content-type": "image/png"},
                upsert=True
            )
        print("✅ Supabase 업로드 완료:", res)
    except Exception as e:
        print("❌ Supabase 업로드 실패:", e)
        sys.exit(1)

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%y%m%d_%H%M")
    file_name = f"lunch_{timestamp}.png"
    screenshot_path = f"./{file_name}"

    capture_instagram_post("hoseofood", screenshot_path)
    time.sleep(1)
    upload_to_supabase(screenshot_path, file_name)
