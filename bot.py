import os
import pyrogram
from pyrogram import filters
import random
from time import sleep
#import keep_alive

#keep_alive.keep_alive()
token = os.environ['BOT_TOKEN']
api_hash = os.environ['API_HASK']
api_id = os.environ['API_ID']

# Inicializar o cliente do Pyrogram
app = pyrogram.Client(
    "suporte_bot",
    bot_token=token,
    api_id=api_id,
    api_hash=api_hash)
print("iniciado")

lista = [1, 2, 3, 4, 5]
print(lista[:4])
	
@app.on_message(filters.command("cor"))
def comando_cor(client, message):
 cores = ["<b>Vermelho</b> ", "<b>Rosa</b>",
"<b>Laranja</b>","<b>Amarelo</b>",
 "<b> Verde</b> ", "<b>Azul </b>",
 "<b>Roxo </b>", "<b>Preto </b>",
 "<b>Branco </b>", "<b>Marrom </b>",
 "<b>Ciano</b>", "<b>Cinza </b>"]
 cor = cores[random.randint(0, 11)]
 message.reply(cor)
 
@app.on_message(filters.command("time"))
def comando_time(client, message):
	time = ["<b>Equipe 1</b>", "<b>Equipe 2</b>"]
	i = random.randint(0,1)
	message.reply(f"{time[i]}")

@app.on_message(filters.command("sorteio"))
def comando_sorteio(client, message):
	sorteado = random.randint(1,75)
	message.reply(f"{sorteado}")

@app.on_message(filters.command("numeros"))
def comando_numeros(client, message):
	sorteado = random.randint(0,99)
	message.reply(f"{sorteado}")
 
@app.on_message(filters.command("letras"))
def comando_letras(client, message):
	# Gera um número aleatório de 65 a 90
	letra_num = random.randint(65, 90)
	# Converte o número em seu caractere correspondente
	letra = chr(letra_num)
	message.reply(f"{letra}")
 
 
@app.on_message(filters.command("joquempo"))
def comando_joquempo(client, message):
 ppt = ["🪨", "📃", "✂️"]
 i = random.randint(0,2)
 message.reply(f"{ppt[i]}")
 

@app.on_message(filters.command("comandos"))
def comando_commands(client, message):
 comandos = """❯ <b>Comandos disponíveis:</b>

↳ /cor
↳ /joquempo

⏳ Mais atualizações em breve."""
 message.reply(comandos)
 
feiticos = [
"""‌‎              𝘼𝙣𝙩𝙞‌𝙙𝙤𝙩𝙤 💊

sᴇ ᴄᴜʀᴇ ᴅᴀ ᴘᴏᴄ‌ᴀ‌ᴏ ᴠᴇɴᴇɴᴏsᴀ""",
"""𝙑𝙤𝙘𝙚̂ 𝙘𝙤𝙣𝙟𝙪𝙧𝙤𝙪 𝙪𝙢 𝙧𝙖𝙞𝙤 ⚡️

       💥 2 ᴅᴇ ᴅᴀɴᴏ 💥""",
"""𝙑𝙤𝙘𝙚̂ 𝙘𝙤𝙣𝙟𝙪𝙧𝙤𝙪 𝙪𝙢 𝙛𝙚𝙞𝙩𝙞𝙘̧𝙤 𝙦𝙪𝙚 𝙚𝙭𝙥𝙚𝙡𝙚 𝙜𝙖́𝙨 𝙩𝙤́𝙭𝙞𝙘𝙤 ☢

             💥 3 ᴅᴇ ᴅᴀɴᴏ 💥""",
"""𝙑𝙤𝙘𝙚̂ 𝙘𝙤𝙣𝙟𝙪𝙧𝙤𝙪 𝙪𝙢 𝙩𝙤𝙧𝙣𝙖𝙙𝙤 🌪

            💥 4 ᴅᴇ ᴅᴀɴᴏ 💥""",
"""𝙑𝙤𝙘𝙚̂ 𝙡𝙖𝙣𝙘̧𝙤𝙪 𝙪𝙢𝙖 𝙗𝙤𝙡𝙖 𝙙𝙚 𝙛𝙤𝙜𝙤 🔥

               💥 5 ᴅᴇ ᴅᴀɴᴏ 💥""",

"""𝙑𝙤𝙘𝙚̂ 𝙞𝙣𝙫𝙤𝙘𝙤𝙪 𝙪𝙢 𝙢𝙤𝙣𝙨𝙩𝙧𝙤 🧟‍♂

           💥 6 ᴅᴇ ᴅᴀɴᴏ 💥""",

"""𝙑𝙤𝙘𝙚̂ 𝙛𝙖𝙡𝙝𝙤𝙪 𝙖𝙤 𝙘𝙤𝙣𝙟𝙪𝙧𝙖𝙧 𝙪𝙢 𝙛𝙚𝙞𝙩𝙞𝙘̧𝙤 𝙚 𝙨𝙤𝙛𝙧𝙚𝙪 𝟱 𝙙𝙚 𝙙𝙖𝙣𝙤 ⚡️""",

"""𝙑𝙤𝙘𝙚̂ 𝙘𝙤𝙣𝙜𝙚𝙡𝙤𝙪 𝙨𝙚𝙪 𝙞𝙣𝙞𝙢𝙞𝙜𝙤 ❄️""",

"""𝙑𝙤𝙘𝙚̂ 𝙡𝙖𝙣𝙘̧𝙤𝙪 𝙪𝙢 𝙛𝙚𝙞𝙩𝙞𝙘̧𝙤 𝙙𝙚 𝙘𝙪𝙧𝙖 🌱

               🩸 +2 ᴅᴇ ᴠɪᴅᴀ 🩸""",

"""‌‎‌‎          ‎𝙈𝙖𝙜𝙞𝙖 𝙙𝙚 𝙨𝙖𝙣𝙜𝙪𝙚 🩸

ʀᴏᴜʙᴇ 3 ᴅᴇ ᴠɪᴅᴀ ᴅᴇ ᴜᴍ ɪɴɪᴍɪɢᴏ""",

"""‎𝙑𝙤𝙘𝙚̂ 𝙘𝙤𝙣𝙟𝙪𝙧𝙤𝙪 𝙪𝙢𝙖 𝙥𝙤𝙘̧𝙖̃𝙤 𝙫𝙚𝙣𝙚𝙣𝙤𝙨𝙖 🧪

sᴇᴜ ɪɴɪᴍɪɢᴏ sᴏғʀᴇʀᴀ́ 2 ᴅᴇ ᴅᴀɴᴏ ᴀᴏ ɪɴɪ́ᴄɪᴏ ᴅᴇ ᴛʀᴇ̂s ʀᴏᴅᴀᴅᴀs""",

"""‎        ‎𝘾𝙖𝙥𝙖 𝙙𝙖 𝙞𝙣𝙫𝙞𝙨𝙞𝙗𝙞𝙡𝙞𝙙𝙖𝙙𝙚 

 ғɪǫᴜᴇ ᴘʀᴏᴛᴇɢɪᴅᴏ ᴘᴏʀ ᴜᴍᴀ ʀᴏᴅᴀᴅᴀ""",

"""‌‌‎   ‎  ⚔ 𝘿𝙪𝙚𝙡𝙤 𝙙𝙚 𝙗𝙧𝙪𝙭𝙤𝙨 ⚔

ᴇsᴄᴏʟʜᴀ ᴜᴍ ᴀᴅᴠᴇʀsᴀ́ʀɪᴏ ᴘᴀʀᴀ ᴅᴜᴇʟᴀʀ ᴄᴏɴᴛʀᴀ ᴠᴏᴄᴇ̂""",

"""‌‎    𝙑𝙤𝙘𝙚̂ 𝙘𝙤𝙣𝙟𝙪𝙧𝙤𝙪 𝙪𝙢𝙖 𝙚𝙭𝙥𝙡𝙤𝙨𝙖̃𝙤 💥

ᴄᴀᴜsᴇ 2 ᴅᴇ ᴅᴀɴᴏ ᴇᴍ ᴛᴏᴅᴏs ᴏᴘᴏɴᴇɴᴛᴇs""",

"""‎                 ‌‎𝘼𝙧𝙢𝙖 𝙢𝙖́𝙜𝙞𝙘𝙖 🪄

ᴠᴏᴄᴇ̂ ᴄᴀᴜsᴀʀᴀ́ +1 ᴅᴇ ᴅᴀɴᴏ ᴀᴛᴇ́ ᴏ ғɪᴍ ᴅᴏ ᴊᴏɢᴏ""",

"""‌‌‎                    𝘼𝙧𝙢𝙖𝙙𝙪𝙧𝙖 🪖

ʀᴇᴄᴇʙᴀ -1 ᴅᴇ ᴅᴀɴᴏ ᴀᴛᴇ́ ᴏ ғɪᴍ ᴅᴏ ᴊᴏɢᴏ""",

"""‎     ‌‎    𝙑𝙤𝙘𝙚̂ 𝙜𝙖𝙣𝙝𝙤𝙪 𝙪𝙢 𝙥𝙚𝙩 🦊

ᴠᴏᴄᴇ̂ ᴄᴀᴜsᴀʀᴀ́ +2 ᴅᴇ ᴅᴀɴᴏ ᴀᴛᴇ́ ᴏ ғɪᴍ ᴅᴏ ᴊᴏɢᴏ""",

"""𝙑𝙤𝙘𝙚̂ 𝙡𝙖𝙣𝙘̧𝙤𝙪 𝙪𝙢 𝙛𝙚𝙞𝙩𝙞𝙘̧𝙤 𝙙𝙚 𝙘𝙪𝙧𝙖 🌱

 🩸 +4 ᴅᴇ ᴠɪᴅᴀ ᴘᴀʀᴀ ᴜᴍ ᴀʟɪᴀᴅᴏ 🩸""",
"""‎              𝘼𝙣𝙩𝙞́𝙙𝙤𝙩𝙤 💊

ᴄᴜʀᴇ ᴠᴏᴄᴇ̂ ᴍᴇsᴍᴏ ᴏᴜ ᴜᴍ ᴀʟɪᴀᴅᴏ ᴅᴀ ᴘᴏᴄ̧ᴀ̃ᴏ ᴠᴇɴᴇɴᴏsᴀ"""
	]
pesos = [2, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2]

@app.on_message(filters.command("encantamento"))
def comando_encantamento(client, message):

	frase_sorteada = random.choices(feiticos[1:19], pesos[1:19])[0]
	print(frase_sorteada)
	message.reply(frase_sorteada)
	
@app.on_message(filters.command("feitico"))
def comando_feitico(client, message):

	frase_sorteada = random.choices(feiticos[:17], pesos[:17])[0]
	print(frase_sorteada)
	message.reply(frase_sorteada)
	
	
app.run()