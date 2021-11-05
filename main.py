import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import platform


bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive    
)

bot.remove_command(
    "help")  #removes deafult hehlp command to enable custom command
scheduler = AsyncIOScheduler()  # allows scheduler o be called
bot.author_id =   # Change to your discord id!!!


#####################################################################################################################################
#EVENTS
@bot.event
async def on_ready():
  scheduler.add_job(
    automark, CronTrigger(day_of_week='fri', second=1)) #chnage varibles for the future 
  scheduler.add_job(
    pint_message  )  # in theroy could add to mark attendence at certain time/ linked with funtion below
  scheduler.start()
  print("I'm in")  # When the bot is ready
  print(bot.user)  # Prints the bot's username and identifier
  await bot.change_presence(activity=discord.Game(
    name="Type !help for help :)"))

#links to on ready function in bot events for proof of scheuling working
async def pint_message():
  channel = bot.get_channel()
  await channel.send('Scheduler working')

@bot.event
async def on_member_join(member):
    print('Welcome to the server!')


@bot.event
async def on_member_remove(member):
    print('You have been kicked from the server!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'ERROR! MISSING ARGUMENT!\nPlease use !help for more info')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(
            'ERROR! COMMAND NOT FOUND!\nPlease use !help for avalable commands'
        )


#auto mark function can be chnaged/ copied to match the users requirements of discord channel.
#This is called in the on ready function, in which the user can modify for thier select lessons.
async def automark():
    with open('students.txt', "w") as file:
        channel = bot.get_channel() #set what channel you want to mark
        members = channel.members
        user = bot.get_user()#set admin user to send attendence too
        for member in members:
            file.write("⚪")
            file.write(member.display_name)
            file.write("\n")
    with open("students.txt", "rb") as file:
        await user.send("Student attendence:",
                        file=discord.File(file, "students.txt"))


#####################################################################################
#link cogs together to be used within this program
extensions = [
    'cogs.cryptography',
    'cogs.cheat',
    'cogs.help',
    'cogs.passwords',
    'cogs.extras',
      # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        bot.load_extension(extension)  # Loades every extension.


#######################################################################################

#marks the attendence manaualy through ARG of channel ID
@commands.has_permissions(administrator=True)
@bot.command()  # better as can pass a channel arg
async def attend(ctx, arg):
    with open('students.txt', "w") as file:
        channel = bot.get_channel(int(arg))
        members = channel.members
        for member in members:
            file.write("⚪")
            file.write(member.display_name)
            file.write("\n")
    with open("students.txt", "rb") as file:
        await ctx.author.send("Student attendence:",
                              file=discord.File(file, "students.txt"))


@bot.command()
async def stats(ctx):
  pyversion = platform.python_version()
  dpy = discord.__version__
  memcount = len(set(bot.get_all_members()))
  embed = discord.Embed(title=f'{bot.user.name} Stats', description='BeckettBot is a Discord bot designed with the aim of providing student with a tool to aid them with thier work', colour=ctx.author.colour, timestamp=ctx.message.created_at)
  embed.add_field(name='Python Version:', value=pyversion)
  embed.add_field(name='Discord.Py Version:', value=dpy)
  embed.add_field(name='Total Users:', value=memcount)
  embed.add_field(name='Bot Developer:', value="<")
  embed.set_thumbnail(url=bot.user.avatar_url)
  embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
  await ctx.send(embed=embed)


##########################################################
keep_alive()  # Starts a webserver to be pinged.
my_secret = os.environ['DISCORD_BOT_SECRET']
bot.run(my_secret)  # Starts the bot
