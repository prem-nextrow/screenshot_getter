from datetime import datetime

def highlight(page, el):
    try:
        page.evaluate("""
            (e) => {
                e.style.outline = '4px solid red';
                e.style.zIndex = '9999';
            }
        """, el)
    except:
        pass


def screenshot_path(folder, name):
    ts = datetime.now().strftime("%H%M%S_%f")
    return f"{folder}/{name}_{ts}.png"


def capture_dropdown_menu(page, button, folder, index):
    screenshots = []
    try:
        button.scroll_into_view_if_needed()
        highlight(page, button)

        before = screenshot_path(folder, f"menu_{index}_before")
        page.screenshot(path=before)
        screenshots.append(("before", before))

        try:
            button.click(timeout=2000)
            page.wait_for_timeout(1500)
            clicked = screenshot_path(folder, f"menu_{index}_clicked")
            page.screenshot(path=clicked)
            screenshots.append(("clicked", clicked))
            page.keyboard.press("Escape")
        except:
            button.hover(timeout=2000)
            page.wait_for_timeout(1500)
            hover = screenshot_path(folder, f"menu_{index}_hover")
            page.screenshot(path=hover)
            screenshots.append(("hover", hover))
    except:
        pass

    return screenshots
