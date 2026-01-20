from datetime import datetime

async def highlight(page, el):
    try:
        await page.evaluate("""
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


async def capture_dropdown_menu(page, button, folder, index):
    screenshots = []
    try:
        await button.scroll_into_view_if_needed()
        await highlight(page, button)

        before = screenshot_path(folder, f"menu_{index}_before")
        await page.screenshot(path=before)
        screenshots.append(("before", before))

        try:
            await button.click(timeout=2000)
            await page.wait_for_timeout(1500)
            clicked = screenshot_path(folder, f"menu_{index}_clicked")
            await page.screenshot(path=clicked)
            screenshots.append(("clicked", clicked))
            await page.keyboard.press("Escape")
        except:
            await button.hover(timeout=2000)
            await page.wait_for_timeout(1500)
            hover = screenshot_path(folder, f"menu_{index}_hover")
            await page.screenshot(path=hover)
            screenshots.append(("hover", hover))
    except:
        pass

    return screenshots