from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name} ' + str(update.message.text))


def str_to_int(a: str) -> int:
    num1, num2 = map(int, a.split())
    sum = num1 + num2
    return sum


async def sumsa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'sum is: {str_to_int(update.message.text.replace("/sum ",""))}')

app = ApplicationBuilder().token("7408234875:AAEC_HLgFFA2MtqoBRPZ-HIRWogtEGTIe-0").build()

#app.add_handler(MessageHandler(filters.TEXT ,hello))
app.add_handler(CommandHandler("sum" ,sumsa))

app.run_polling()


