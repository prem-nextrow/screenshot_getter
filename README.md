# Website Screenshot & Asset Getter

A powerful, FastAPI-based web crawler that automatically captures full-page screenshots, interacts with navigation menus, and extracts media assets (GIFs/Videos) from any given URL. The tool generates professional PDF reports for screenshot captures and converts dynamic media (GIFs) to optimized video formats.

## 🚀 Key Features

- **Full-Page Capture**: Automated high-resolution screenshots of the entire webpage.
- **Interactive Navigation Crawling**: Automatically identifies and interacts with top navigation links and buttons to capture dropdown menus and overlays.
- **Media Extraction**: Intelligent extraction of images and videos from the target site.
- **GIF to Video Conversion**: Automatically converts `.gif` files to `.mp4` for better performance and compatibility.
- **Automated PDF Reporting**: Wraps captured screenshots into individual PDF reports.
- **Modern Dashboard**: A clean, Tailwind CSS-powered web interface for easy interaction and result viewing.

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Automation**: [Playwright](https://playwright.dev/python/)
- **PDF Generation**: [FPDF](https://pyfpdf.readthedocs.io/en/latest/)
- **Video Processing**: [MoviePy](https://zulko.github.io/moviepy/)
- **Frontend**: HTML5, [Tailwind CSS](https://tailwindcss.com/)
- **Server**: Uvicorn

## 📋 Prerequisites

- Python 3.8+
- Node.js (for Playwright browser installation)

## ⚙️ Installation

1.  **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd screenshot_getter
    ```

2.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Playwright browsers**:
    ```bash
    playwright install chromium
    ```

## 🚀 Running the App

Start the development server:

```bash
python src/main.py
```

The application will be available at `http://localhost:3030`.

## 📂 Project Structure

```text
screenshot_getter/
├── src/
│   ├── main.py            # Application entry point & FastAPI setup
│   ├── routers/           # API route definitions (crawl, static)
│   ├── services/          # Business logic (crawler_service)
│   ├── schemas/           # Pydantic models for API requests/responses
│   └── utils/             # Helper utilities (download, media, report, screenshot)
├── static/                # Static assets (if any)
├── templates/             # HTML templates (index.html)
├── output/                # Generated screenshots, PDFs, and media (created at runtime)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🖥️ Usage

1.  Open your browser and navigate to `http://localhost:3030`.
2.  Enter the URL of the website you want to analyze in the input box.
3.  Click **"Analyze"**.
4.  Wait for the process to complete. You will see:
    - **Screenshot Reports (PDF)**: Downloadable PDF files of the full page and menu interactions.
    - **Media Assets (.mp4)**: Extracted and processed videos/GIFs from the site.

## 📄 License

© 2026 Nextrow Digital. All rights reserved.
