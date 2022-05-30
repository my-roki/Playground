from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


from app.models import mongodb
from app.models.book import BookModel
from app.book_scraper import NaverBookScraper

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # book = BookModel(keyword="test book", publisher="록록 출판사", price=19900, image="book.png")
    # print(await mongodb.engine.save(book))
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "Project Collector"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    # 1. 쿼리에서 검색어 추출
    keyword = q

    # (예외처리) 검색어가 없다면 사용자에게 검색을 요구 return
    if not keyword:
        context = {"request": request, "title": "Project Collector"}
        return templates.TemplateResponse("./index.html", context)

    # (예외처리) 해당 검색어에 대해 이미 수집된 데이터가 있으면 해당 데이터를 사용자에게 보여준다. return
    if await mongodb.engine.find_one(BookModel, BookModel.keyword == keyword):
        books = await mongodb.engine.find(BookModel, BookModel.keyword == keyword)
        return templates.TemplateResponse(
            "./index.html", {"request": request, "keyword": keyword, "books": books}
        )

    # 2. 데이터 수집기로 해당 검색어에 대해 데이터를 수집한다.
    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(keyword, 10)

    # 3. 수집된 데이터를 저장한다.
    book_models = list()
    for book in books:
        book_model = BookModel(
            keyword=keyword,
            publisher=book.get("publisher"),
            price=book.get("price"),
            image=book.get("image"),
        )
        book_models.append(book_model)
    await mongodb.engine.save_all(book_models)

    return templates.TemplateResponse(
        "./index.html", {"request": request, "keyword": keyword, "books": books}
    )


# on_event
@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()
    print(".... Database start")


@app.on_event("shutdown")
def on_app_shutdown():
    """after app shutdown"""
    print(".... Database shutdown")
    mongodb.close()
