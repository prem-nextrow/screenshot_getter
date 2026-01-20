import os
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from .download_utils import safe_name, download_media
from .media_utils import gif_to_video
from .screenshot_utils import capture_dropdown_menu
from .report_utils import create_single_pdf

BASE_DIR = "output"

def run_crawler(URL):
    site = safe_name(URL)
    folder = f"{BASE_DIR}/{site}"
    media_folder = f"{folder}/media"
    screenshot_folder = f"{folder}/screenshots"
    pdf_folder = f"{folder}/pdfs"

    os.makedirs(media_folder, exist_ok=True)
    os.makedirs(screenshot_folder, exist_ok=True)
    os.makedirs(pdf_folder, exist_ok=True)

    individual_pdfs = []
    media_items = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, timeout=60000)
        page.wait_for_timeout(3000)

       
        full_img = f"{screenshot_folder}/full_page.png"
        page.screenshot(path=full_img, full_page=True)
        pdf_path = create_single_pdf(pdf_folder, full_img, "Full_Page_Report")
        individual_pdfs.append({"name": "Full Page Report", "path": pdf_path})

       
        elements = page.query_selector_all("img, video")
        for idx, el in enumerate(elements[:10], start=1):
            src = el.get_attribute("src")
            if not src: continue
            
            local_path = download_media(urljoin(URL, src), media_folder, f"media_{idx}")
            if not local_path: continue

            if local_path.endswith(".gif"):
                mp4_path = local_path.replace(".gif", ".mp4")
                if gif_to_video(local_path, mp4_path):
                    media_items.append({"type": "video", "path": mp4_path})
            elif local_path.endswith((".mp4", ".webm")):
                media_items.append({"type": "video", "path": local_path})


        menus = page.query_selector_all("nav a, button")
        for idx, menu in enumerate(menus[:5], start=1):
            shots = capture_dropdown_menu(page, menu, screenshot_folder, idx)
            for label, img_path in shots:
                name = f"Menu_{idx}_{label}"
                p_path = create_single_pdf(pdf_folder, img_path, name)
                individual_pdfs.append({"name": f"Interaction: {name}", "path": p_path})

        browser.close()

    return {
        "pdfs": [{"name": p["name"], "src": p["path"].replace(f"{BASE_DIR}/", "")} for p in individual_pdfs],
        "media": [{"type": m["type"], "src": m["path"].replace(f"{BASE_DIR}/", "")} for m in media_items]
    }