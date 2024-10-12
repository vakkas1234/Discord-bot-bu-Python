import discord
import requests
import random
import wikipediaapi
from discord.ext import commands
API_KEY = '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'
API_URL = 'https://api-inference.huggingface.co/models/gpt2'
class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        # Komut listesini oluştur
        help_message = "**Commands:**\n"
        for cog, commands_list in mapping.items():
            for command in commands_list:
                help_message += f"!{command.name}\n"
        await self.get_destination().send(help_message)

game_data = {}
intents  = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "!",intents = intents,help_command=CustomHelpCommand())
@bot.event
async def on_ready():
    print(f'logged in as {bot.user}' )              
@bot.command()
async def hello(ctx):
   await ctx.send("Hi")
@bot.command()   
async def invite(ctx):
   await ctx.send("https://discord.gg/eHWh54Tj")
@bot.command()   
async def brotherbot(ctx):
  await ctx.send("https://discord.gg/pZqxDQEz")
@bot.command()  
async def creator(ctx):
  await  ctx.send("This bot was created by Vakkas Emre Yıldız")
@bot.command()
async def murphy(ctx):
    murphy = ['Even if you block out the possibilities that something could go wrong, a new possibility immediately appears','The probability of something happening is inversely proportional to the probability of wanting it.', "If you cant understand something, it's instinctive.", 'If something has several possible ways to go wrong, it will always go wrong in the worst possible way.', 'If you play with something too much, you break it.' ] 
    random1 = random.choice(murphy)
    await ctx.send(random1)
@bot.command()
async def randommessage(ctx):
    p =["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.","Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?", "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?","At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio" ," Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ]
    random1  = random.choice(p)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    await ctx.send(random1)
@bot.command()

async def numberpredictiongame(ctx, guess: int = None):
   
    if guess is None:
        if ctx.author.id in game_data:
            await ctx.send(" the game has already started.Please enter a prediction")
        else:
            number = random.randint(1,100)
            game_data[ctx.author.id] = {'number' : number}
            await ctx.send("game started")
    else:
        if ctx.author.id not in game_data:
            await ctx.send("Firstly you need to start a game")
            return

        number = game_data[ctx.author.id]['number']

        
       
     
      
          

    
        if (guess == number):
             await ctx.send("Congratulations"+" game finished")
             del game_data[ctx.author.id]
        elif(guess > number ):
              await ctx.send("please enter a smaller number")
        elif(guess < number ):
             await ctx.send("please enter a bigger number")
@bot.command()
async def quitgame(ctx):
    """Oyunu sonlandırma komutu."""
    if ctx.author.id in game_data:
        del game_data[ctx.author.id]  # Kullanıcının oyun verilerini sil
        await ctx.send("Game quit")
    else:
        await ctx.send("You don't have a game.You can start a game")


   
@bot.command()
async def createdeneyapcart(ctx):
    random1  = random.randint(1,100)
    await ctx.send(str(random1)+" units" + " were created")
@bot.command(help = "!collection number1 number2")
async def collection(ctx, sayi1: int,sayi2: int):
    result = sayi1 + sayi2
    await ctx.send(f"{result}")
@bot.command()
async def multiplying(ctx, sayi1: int,sayi2: int):
    result = sayi1 *sayi2
    await ctx.send(f"{result}")
@bot.command()
async def divide(ctx, sayi1:int , sayi2:int):
    result = sayi1 / sayi2
    await ctx.send(f"{result}")
@bot.command()
async def extraction(ctx, sayi1: int,sayi2:int):
    result = sayi1-sayi2
    await ctx.send(f"{result}")
@bot.command()
async def userid(ctx,member:discord.Member = None):
    if member is None:
        member  = ctx.author
    await ctx.send(f"{member.name}'s id is: {member.id}")
@bot.command()
async def ping(ctx):
    latency = bot.latency *1000
    await ctx.send(f"Ping {latency:.2f}ms")

@bot.command()
async def githublink(ctx):
    link = "https://github.com/vakkas1234"
    await ctx.send(f"{link}")
@bot.command()
async def mycvsite(ctx):
    link = "https://vakkas1234.github.io"
    await ctx.send(f"{link}")
@bot.command()    
async def clear(ctx, amount: int):
    """Silmek için belirtilen sayıda mesajı siler."""
    if ctx.author.guild_permissions.manage_messages:
        # +1 ekleyerek komut mesajını da siler
        deleted = await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{len(deleted) - 1} mesaj silindi.", delete_after=5)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.", delete_after=5)



















    





async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!ask'):
        question = message.content[len('!ask '):]
        try:
            # Hugging Face API'sine istek yap
            response = requests.post(
                "https://api-inference.huggingface.co/models/gpt2",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={"inputs": question},
            )

            # Yanıtı kontrol et ve hata mesajını göster
            if response.status_code == 200:
                answer = response.json()[0]['generated_text'].strip()
                await message.channel.send(answer)
            else:
                # Hata durumunda detaylı yanıtı göster
                await message.channel.send(f"Bir hata oluştu: {response.status_code} - {response.text}")

        except Exception as e:
            await message.channel.send(f'Bir hata oluştu: {e}')






















bot.run("Your Discord Bot Token")






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                


