from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt',"w", encoding='utf-8')
for href in soup_list_href:
    f.write(f"{href['href']}\n")
f.close()

links_list = []
with open('link.txt', 'r') as file:
    links_list = file.readlines()

f = open('info.txt', 'w', encoding='utf-8')
list_name = []
list_desc = []
for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text, features="html.parser")
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    if len(soup_list_name_film)> 0:
        f.write(f'{soup_list_name_film[0].text}\n')
        list_name.append(soup_list_name_film[0].text)
    soup_list_ul = soup1.find_all('ul',{"class":"short-list fx-1"})
    for item in soup_list_ul:
        f.write(f"{item.text}\n")
        list_desc.append(item.text)
f.close()

command = """/help - Список всіх команд бота.
/hello - Привітання.
/film - Список найновіщих фільмів.
/easycomedy - Список легких комедійних фільмів, які піднімуть настрій.
/feelgood - Фільми для гарного настрою, легкі та надихаючі.
/popular - Фільми які популярні на данний час.
/horror - Фільми ужастіки.
/romantic - Романтичні фільми з легким сюжетом для затишного вечора."""

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f"{list_name[i]}\n{list_desc[i]}\n{links_list[i]}"
        await update.message.reply_text(text)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)

async def easycomedy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_name = "Дім шкереберть"
    found = False
    for i in range(len(list_name)):
        if target_name.lower() in list_name[i].lower():
            text = f"Title: {list_name[i]}\nDescription: {list_desc[i]}\nLink: {links_list[i]}"
            await update.message.reply_text(text)
            found = True
            break
    if not found:
        await update.message.reply_text(f"Movie '{target_name}' not found.")

async def feelgood(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_name = "Їжак Сонік 3"
    found = False
    for i in range(len(list_name)):
        if target_name.lower() in list_name[i].lower():
            text = f"Title: {list_name[i]}\nDescription: {list_desc[i]}\nLink: {links_list[i]}"
            await update.message.reply_text(text)
            found = True
            break
    if not found:
        await update.message.reply_text(f"Movie '{target_name}' not found.")

async def popular(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_name = "Майнкрафт в кіно"
    found = False
    for i in range(len(list_name)):
        if target_name.lower() in list_name[i].lower():
            text = f"Title: {list_name[i]}\nDescription: {list_desc[i]}\nLink: {links_list[i]}"
            await update.message.reply_text(text)
            found = True
            break
    if not found:
        await update.message.reply_text(f"Movie '{target_name}' not found.")

async def horror(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_name = "Кімната страху"
    found = False
    for i in range(len(list_name)):
        if target_name.lower() in list_name[i].lower():
            text = f"Title: {list_name[i]}\nDescription: {list_desc[i]}\nLink: {links_list[i]}"
            await update.message.reply_text(text)
            found = True
            break
    if not found:
        await update.message.reply_text(f"Movie '{target_name}' not found.")

async def romantic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_name = "Побачення всліпу"
    found = False
    for i in range(len(list_name)):
        if target_name.lower() in list_name[i].lower():
            text = f"Title: {list_name[i]}\nDescription: {list_desc[i]}\nLink: {links_list[i]}"
            await update.message.reply_text(text)
            found = True
            break
    if not found:
        await update.message.reply_text(f"Movie '{target_name}' not found.")

app = ApplicationBuilder().token("8054099247:AAHhMePpgBk6QwAsR7J22rq_-mu3af5SJQo").build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))
app.add_handler(CommandHandler("easycomedy", easycomedy))
app.add_handler(CommandHandler("feelgood", feelgood))
app.add_handler(CommandHandler("popular", popular))
app.add_handler(CommandHandler("horror", horror))
app.add_handler(CommandHandler("romantic", romantic))

app.run_polling()
