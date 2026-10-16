import os
from pathlib import Path

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv(Path(__file__).parent / ".env")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN is missing. Add it to the .env file.")
BANNER = Path(__file__).parent / "banner.jpg"
REGISTER_URL = "https://t.me/SLOTSERVICESWC88"

CAPTION = (
    "សូមស្វាគមន៍មកវេបសាយធំបំផុត ងាយស្រួលលេង📲 "
    "និងគួរឱ្យទុកចិត្តបំផុតនៅកម្ពុជា🔥សេវាកម្ម២៤ម៉ោង"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("ចុះឈ្មោះឥឡូវនេះ", url=REGISTER_URL)]]
    )
    with BANNER.open("rb") as photo:
        await update.message.reply_photo(
            photo=photo, caption=CAPTION, reply_markup=keyboard
        )


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
