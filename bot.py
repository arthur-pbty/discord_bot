import json
import requests
import discord
from discord import app_commands
from discord.ext import tasks, commands


#----------VAR----------
with open('data.json', 'r') as f:
    data = json.load(f)
#----------CODE----------
bot = commands.Bot(intents=discord.Intents.all(),command_prefix=data['prefix'],help_command=None)


@bot.event
async def on_ready():
    print(data['message_de_lancement'])
    #----------STATUT----------
    await bot.change_presence(activity=discord.Game(data['statut']))
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``event``", inline=True)
    embed.add_field(name="Commande :", value="``on_ready``", inline=True)
    await channel_bot_info.send(embed=embed)
    #---------COMMANDE SLASH---------
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    #----------TASK----------
    clear_task.start()
    #---------ROLES---------
    guild = bot.get_guild(991074780105015337)
    role1 = discord.utils.get(guild.roles, id=1067512882541121556)
    role2 = discord.utils.get(guild.roles, id=1067512565040693339)
    role3 = discord.utils.get(guild.roles, id=1067856532517175347)
    for member in guild.members:
        if member.id != 855019362499035147:
            await member.add_roles(role1)
            await member.add_roles(role2)
            await member.add_roles(role3)


@tasks.loop(minutes=1)
async def clear_task():
    channel = discord.utils.get(bot.get_all_channels(), id=1067147389829390426)
    await channel.purge()
    channel = bot.get_channel(1067147389829390426)
    embed = discord.Embed(title="**Dans ce salon vous pouvez spam !**", description="Faite vous plaisir, vous pouvez détruire votre clavier !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-assets/855019362499035147/1067510679134818444.png")
    react_messasge = await channel.send(embed=embed)
    await react_messasge.add_reaction("<:averified:1003029363073228991>")


@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(991084100532191303)
    embed = discord.Embed(title="**Ho ! Un nouveau membre !**", description=f"🎉 Bienvenue {member.mention} 🎉!", color=discord.Colour.red())
    await channel.send(member.mention)
    await channel.send(embed=embed)
    #---------MEMBER COUNT---------
    voice_channel = bot.get_channel(1026532380061749280)
    await voice_channel.edit(name=f"Membres : {member.guild.member_count}")
    #---------creer un compte au joueur---------
    user_id = str(member.id)
    if user_id not in users:
        users[user_id] = {"balance": 0, "xp": 0, "level": 0}
        with open('users.json', 'w') as f:
            json.dump(users, f)
    #---------ROLES---------
    role1 = discord.utils.get(member.guild.roles, id=1067512882541121556)
    role2 = discord.utils.get(member.guild.roles, id=1067512565040693339)
    role3 = discord.utils.get(member.guild.roles, id=1067856532517175347)
    await member.add_roles(role1)
    await member.add_roles(role2)
    await member.add_roles(role3)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``event``", inline=True)
    embed.add_field(name="Commande :", value="``on_member_join``", inline=True)
    embed.add_field(name="member :", value=f"``{member}``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(991084100532191303)
    embed = discord.Embed(title="**Un membre vient de partir 😢**", description=f"À bientôt {member.mention} 👋", color=discord.Colour.red())
    await channel.send(embed=embed)
    voice_channel = bot.get_channel(1026532380061749280)
    await voice_channel.edit(name=f"Membres : {member.guild.member_count}")
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``event``", inline=True)
    embed.add_field(name="Commande :", value="``on_member_remove``", inline=True)
    embed.add_field(name="member :", value=f"``{member}``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.event
async def on_raw_reaction_add(ctx):
    guild = discord.utils.find(lambda g: g.id == ctx.guild_id, bot.guilds)
    if ctx.message_id == 1062057817214820474:
        role = discord.utils.get(guild.roles, id=991114582275932170)
        if role is not None:
            member = discord.utils.find(lambda m: m.id == ctx.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
    #----------REACT MENTION----------
    message_id = ctx.message_id
    if message_id == 1067855647548387478: # remplacez cette valeur par l'ID du message où vous souhaitez utiliser le système de réaction-rôle
        guild_id = ctx.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        member = discord.utils.find(lambda m : m.id == ctx.user_id, guild.members)
        if str(ctx.emoji) == "<:1_:1067816693105172480>":
            role = discord.utils.get(guild.roles, id=1067788975319830618)
            await member.add_roles(role)
        if str(ctx.emoji) == "<:2_:1067816690039144469>":
            role = discord.utils.get(guild.roles, id=1067796435724157048)
            await member.add_roles(role)
        if str(ctx.emoji) == "<:3_:1067816687480610858>":
            role = discord.utils.get(guild.roles, id=1067796538396512297)
            await member.add_roles(role) 
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``event``", inline=True)
    embed.add_field(name="Commande :", value="``on_raw_reaction_add``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.event
async def on_raw_reaction_remove(ctx):
    guild = discord.utils.find(lambda g: g.id == ctx.guild_id, bot.guilds)
    if ctx.message_id == 1062057817214820474:
        role = discord.utils.get(guild.roles, id=991114582275932170)
        if role is not None:
            member = discord.utils.find(lambda m: m.id == ctx.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
    #----------REACT MENTION----------
    message_id = ctx.message_id
    if message_id == 1067855647548387478: # remplacez cette valeur par l'ID du message où vous souhaitez utiliser le système de réaction-rôle
        guild_id = ctx.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        member = discord.utils.find(lambda m : m.id == ctx.user_id, guild.members)
        if str(ctx.emoji) == "<:1_:1067816693105172480>":
            role = discord.utils.get(guild.roles, id=1067788975319830618)
            await member.remove_roles(role)
        if str(ctx.emoji) == "<:2_:1067816690039144469>":
            role = discord.utils.get(guild.roles, id=1067796435724157048)
            await member.remove_roles(role)
        if str(ctx.emoji) == "<:3_:1067816687480610858>":
            role = discord.utils.get(guild.roles, id=1067796538396512297)
            await member.remove_roles(role)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``event``", inline=True)
    embed.add_field(name="Commande :", value="``on_raw_reaction_remove``", inline=True)
    await channel_bot_info.send(embed=embed)


#@bot.command()
#async def verif_message(ctx):
#    embed = discord.Embed(title="**Hello @everyone !**", description="Tu es sur un serveur chill :\n❌ pas d'insulte\n❌ pas de messages haineux\n❌ pas de politique\n❌ pas de pub sans demande préalable\n❌ pas de spam\n\nLa bise,\nTuturP33")
#    react_messasge = await ctx.send(embed=embed)
#    await react_messasge.add_reaction("<:averified:1003029363073228991>")


@bot.tree.command(name="help", description="C'est une commande d'aide")
@app_commands.describe(commande = "Aide sur une seul commande ?")
async def help(ctx, commande: str = None):
    if commande == None:
        embed = discord.Embed(title="**help - Liste des commandes :**", description="Utilise ``/help <commande>`` pour plus d'info !")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001152938800058409.webp")
        embed.add_field(name="💵 Economie", value="``bal``,``create``,``add``,``withdraw``", inline=False)
        embed.add_field(name="🎲 Fun", value="``joke``", inline=False)
        embed.add_field(name="<:mod:997918695718408344> Utilitaire", value="``suggest``,``ping``,``say``,``weather``,``serverinfo``,``userinfo``,``discordpy``", inline=False)
        embed.add_field(name="<:supmod:997918691838672976> Modération", value="``clear``,``kick``,``ban``,``unban``,``lban``,``rules``", inline=False)
        embed.add_field(name="<:owner:997918694065848370> Créateur", value="``annonce``", inline=False)
    elif commande == "annonce":
        embed = discord.Embed(title="**help - annonce :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/annonce [annonce]``", inline=False)
        embed.add_field(name="Permission :", value="``Bannir des membres``", inline=False)
        embed.add_field(name="Description :", value="Creer une annonce dans le salon <#991074780692250686>.", inline=False)
    elif commande == "clear":
        embed = discord.Embed(title="**help - clear :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/clear [nombre]``", inline=False)
        embed.add_field(name="Permission :", value="``Bannir des membres``", inline=False)
        embed.add_field(name="Description :", value="Supprime un nombre donné de messages.", inline=False)
    elif commande == "ban":
        embed = discord.Embed(title="**help - ban :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/ban [membre] [reason]``", inline=False)
        embed.add_field(name="Permission :", value="``Bannir des membres``", inline=False)
        embed.add_field(name="Description :", value="Ban un membre donné, pour une raison donné.", inline=False)
    elif commande == "unban":
        embed = discord.Embed(title="**help - unban :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/unban [membre] [reason]``", inline=False)
        embed.add_field(name="Permission :", value="``Bannir des membres``", inline=False)
        embed.add_field(name="Description :", value="Déban un membre donné, pour une raison donné.", inline=False)
    elif commande == "kick":
        embed = discord.Embed(title="**help - kick :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/kick [membre] [reason]``", inline=False)
        embed.add_field(name="Permission :", value="``Kick des membres``", inline=False)
        embed.add_field(name="Description :", value="Kick un membre donné, pour une raison donné.", inline=False)
    elif commande == "suggest":
        embed = discord.Embed(title="**help - suggest :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/suggest [suggestion]``", inline=False)
        embed.add_field(name="Permission :", value="``Envoyer des messages``", inline=False)
        embed.add_field(name="Description :", value="Envoie une suggestion dans le salon <#991478556355997808>.", inline=False)
    elif commande == "ping":
        embed = discord.Embed(title="**help - ping :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/ping``", inline=False)
        embed.add_field(name="Permission :", value="``Envoyer des messages``", inline=False)
        embed.add_field(name="Description :", value="Calcul le ping du bot.", inline=False)
    elif commande == "lban":
        embed = discord.Embed(title="**help - lban :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/lban``", inline=False)
        embed.add_field(name="Permission :", value="``Bannir des membres``", inline=False)
        embed.add_field(name="Description :", value="Donne la liste des personnes banni.", inline=False)
    elif commande == "say":
        embed = discord.Embed(title="**help - say :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/say``", inline=False)
        embed.add_field(name="Permission :", value="``aucune``", inline=False)
        embed.add_field(name="Description :", value="Le bote va écrire le message donner.", inline=False)
    elif commande == "bal":
        embed = discord.Embed(title="**help - bal :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/bal``", inline=False)
        embed.add_field(name="Permission :", value="``aucune``", inline=False)
        embed.add_field(name="Description :", value="Permet de voir sont argent", inline=False)
    elif commande == "rules":
        embed = discord.Embed(title="**help - rules :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/rules``", inline=False)
        embed.add_field(name="Permission :", value="``aucune``", inline=False)
        embed.add_field(name="Description :", value="Permet de voir les règles", inline=False)
    elif commande == "weather":
        embed = discord.Embed(title="**help - weather :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/weather``", inline=False)
        embed.add_field(name="Permission :", value="``aucune``", inline=False)
        embed.add_field(name="Description :", value="Permet de voir la météo", inline=False)
    elif commande == "serverinfo":
        embed = discord.Embed(title="**help - serverinfo :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/serverinfo``", inline=False)
        embed.add_field(name="Permission :", value="``aucune``", inline=False)
        embed.add_field(name="Description :", value="Affiche des informations sur le serveur", inline=False)
    elif commande == "userinfo":
        embed = discord.Embed(title="**help - userinfo :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/userinfo``", inline=False)
        embed.add_field(name="Permission :", value="``aucune``", inline=False)
        embed.add_field(name="Description :", value="Afficher des informations sur un utilisateur", inline=False)
    elif commande == "discordpy":
        embed = discord.Embed(title="**help - discordpy :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/discordpy``", inline=False)
        embed.add_field(name="Permission :", value="``aucune``", inline=False)
        embed.add_field(name="Description :", value="Afficher un exemple de script de bot discord en python", inline=False)
    elif commande == "joke":
        embed = discord.Embed(title="**help - joke :**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
        embed.add_field(name="Usage :", value="``/joke``", inline=False)
        embed.add_field(name="Permission :", value="``aucune``", inline=False)
        embed.add_field(name="Description :", value="Afficher une blague", inline=False)
    else:
        embed = discord.Embed(title="**Veuilley écrire ``le nom d'une commande`` en commande**")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``help``", inline=True)
    embed.add_field(name="commande :", value=f"``{commande}``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="suggest", description="C'est une commande pour faire des suggestion")
@app_commands.describe(idee = "Votre idée")
async def suggest(ctx, idee:str):
    channel = bot.get_channel(991478556355997808)
    embed = discord.Embed(title="**Suggestion :**")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001160986713149541.webp")
    embed.add_field(name="Auteur :", value=ctx.user.name, inline=False)
    embed.add_field(name="Proposition :", value=idee, inline=False)
    role_notif = discord.utils.get(ctx.guild.roles, id=1067796435724157048)
    await channel.send(role_notif.mention)
    msg = await channel.send(embed=embed)
    await msg.add_reaction("<a:yes:1067802368072237066>")
    await msg.add_reaction("<a:no:1067802344026292274>")
    embed2 = discord.Embed(title="**Votre suggestion à bien été envoyer.**")
    await ctx.response.send_message(embed=embed2)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``suggest``", inline=True)
    embed.add_field(name="idee :", value=f"``{idee}``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="clear", description="C'est une commande pour effacer un nombre donnais de message")
@app_commands.describe(nombre = "Le nombre de massage que vous voulez effacer")
async def clear(ctx, nombre: int):
    await ctx.channel.purge(limit=nombre)




@bot.tree.command(name="annonce", description="C'est une commande pour faire des annonces")
@app_commands.describe(news = "L'annonce que vous voulez faire")
async def annonce(ctx, news:str):
    channel = bot.get_channel(991074780692250686)
    role = discord.utils.get(ctx.guild.roles, id=1067788975319830618)
    msg = await channel.send(f"<:annonce:1003028582379036753> **Annonce :**\n{news}\n{role.mention}")
    await msg.add_reaction("<:averified:1003029363073228991>")
    embed2 = discord.Embed(title="**Votre annonce à bien été envoyer.**")
    await ctx.response.send_message(embed=embed2)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``annonce``", inline=True)
    embed.add_field(name="news :", value=f"``{news}``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="ban", description="C'est une commande pour ban des gens")
@app_commands.describe(reason = "La raison du ban")
async def ban(ctx, user: discord.User, reason: str = None):
    await ctx.guild.ban(user, reason=reason)
    embed = discord.Embed(title="**Banissement :**", description="Un modérateur a frappé !")
    embed.set_thumbnail(url="https://cdn.mastodon.technology/custom_emojis/images/000/082/789/static/aa073598e886a035.png")
    embed.add_field(name="Membre banni", value=user.name, inline=False)
    embed.add_field(name="Raison", value=reason, inline=False)
    embed.add_field(name="Modérateur qui a banni", value=ctx.user.name, inline=False)
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``ban``", inline=True)
    embed.add_field(name="reason :", value=f"``{reason}``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="ping", description="C'est une commande pour voir ton ping")
async def ping(ctx):
    ping = round(bot.latency* 1000)
    if ping < 101:
        emote = "<a:bot_ping:1065703322390102077>"
    elif ping < 201:
        emote = "<a:bot_ping:1065703322390102077>"
    elif ping < 301:
        emote = "<a:bot_ping:1065703322390102077>"
    elif ping < 401:
        emote = "<a:bot_ping:1065703322390102077>"
    else:
        emote = "<a:bot_ping:1065703322390102077>"
    embed = discord.Embed(title=f"**La latence est de {emote} {ping}ms !**")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``ping``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="say", description="C'est une commande pour faire dire des chose au bot")
@app_commands.describe(message = "Le message que le bot va dire")
async def say(ctx, message: str):
    await ctx.response.send_message(message)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``say``", inline=True)
    embed.add_field(name="message :", value=f"``{message}``", inline=True)
    await channel_bot_info.send(embed=embed)


#@bot.tree.command(name="unban", description="C'est une commande pour unban des gens")
#@app_commands.describe(reason = "La raison de l'unban")
#async def unban(ctx, user: str, reason: str = None):
#    userName, userId = user.split("#")
#    bannedUsers = await ctx.guild.bans()
#    for i in bannedUsers:
#        if i.user.name == userName and i.user.discriminator == userId:
#            await ctx.guild.unban(i.user, reason=reason)
#            embed = discord.Embed(title="**Débanissement :**", description="Un modérateur a frappé !")
#            embed.set_thumbnail(url="https://cdn.mastodon.technology/custom_emojis/images/000/082/789/static/aa073598e886a035.png")
#            embed.add_field(name="Membre débanni", value=i.user, inline=False)
#            embed.add_field(name="Raison", value=reason, inline=False)
#            embed.add_field(name="Modérateur qui a banni", value=ctx.user.name, inline=False)
#            await ctx.response.send_message(embed=embed)
#        else:
#            embed = discord.Embed(title=f"**L'utilisateur {user} n'est pas dans la liste des banni !**")
#            await ctx.response.send_message(embed=embed)


#------SYSTEME DE MONEY/NIVEAU------ vvv
with open('users.json', 'r') as f:
    users = json.load(f)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    user_id = str(message.author.id)
    if user_id in users:
        users[user_id]["balance"] += 10
        with open('users.json', 'w') as f:
            json.dump(users, f)

    # Vérifier si l'utilisateur a un compte
    if user_id in users:
        # Ajouter de l'expérience
        users[user_id]['xp'] += 10
    else:
        # Créer un compte pour l'utilisateur
        users[user_id] = {"xp": 10, "level": 0}

    # Vérifier si l'utilisateur a atteint un nouveau niveau
    if users[user_id]['xp'] >= 1000 * (users[user_id]['level'] + 1):
        # Augmenter le niveau de l'utilisateur
        users[user_id]['level'] += 1

        # Envoyer un message de félicitations dans le salon
        channel = bot.get_channel(991151133206794331)
        await channel.send(f'Félicitations {message.author.mention} ! Vous avez atteint le niveau {users[user_id]["level"]} !')

    # Enregistrer les données utilisateur
    with open('users.json', 'w') as f:
        json.dump(users, f)
    #---------BOT INFO---------
    #channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    #embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    #embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    #embed.add_field(name="Action :", value="``event``", inline=True)
    #embed.add_field(name="Commande :", value="``on_message``", inline=True)
    #embed.add_field(name="message :", value=f"``{message}``", inline=True)
    #await channel_bot_info.send(embed=embed)


# Commande pour afficher le solde de l'utilisateur
@bot.tree.command(name="bal", description="C'est une commande pour voir sont argent")
async def bal(ctx):
    user_id = str(ctx.user.id)
    if user_id in users:
        embed = discord.Embed(title=f'**Votre solde est de ``{users[user_id]["balance"]}$``**')
    else:
        embed = discord.Embed(title="**Vous n'avez pas encore de compte**")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``bal``", inline=True)
    await channel_bot_info.send(embed=embed)


# Commande pour ajouter de l'argent au compte de l'utilisateur
@bot.tree.command(name="add", description="C'est une commande pour ajouter de l'argent")
@app_commands.describe(amount = "La quantiter d'argent")
async def add(ctx, amount: int):
    user_id = str(ctx.user.id)
    if user_id in users:
        users[user_id]["balance"] += amount
        await ctx.response.send_message(f'{amount} a été ajouté à votre compte')
        with open('users.json', 'w') as f:
            json.dump(users, f)
    else:
        await ctx.response.send_message('Vous n\'avez pas encore de compte')
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``add``", inline=True)
    embed.add_field(name="amount :", value=f"``{amount}``", inline=True)
    await channel_bot_info.send(embed=embed)


# Commande pour retirer de l'argent du compte de l'utilisateur
@bot.tree.command(name="withdraw", description="C'est une commande pour retirer de l'argent")
@app_commands.describe(amount = "La quantiter d'argent")
async def withdraw(ctx, amount: int):
    user_id = str(ctx.user.id)
    if user_id in users:
        if users[user_id]["balance"] >= amount:
            users[user_id]["balance"] -= amount
            await ctx.response.send_message(f'{amount} a été retiré de votre compte')
            with open('users.json', 'w') as f:
                json.dump(users, f)
        else:
            await ctx.response.send_message('Vous n\'avez pas suffisamment d\'argent')
    else:
        await ctx.response.send_message('Vous n\'avez pas encore de compte')
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``withdraw``", inline=True)
    embed.add_field(name="amount :", value=f"``{amount}``", inline=True)
    await channel_bot_info.send(embed=embed)


# Commande pour créer un compte utilisateur
@bot.tree.command(name="create", description="C'est une commande pour créer un compte")
async def create(ctx):
    user_id = str(ctx.user.id)
    if user_id in users:
        await ctx.response.send_message('Vous avez déjà un compte')
    else:
        users[user_id] = {"balance": 0, "xp": 0, "level": 0}
        await ctx.response.send_message('Votre compte a été créé avec succès')
        with open('users.json', 'w') as f:
            json.dump(users, f)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``create``", inline=True)
    await channel_bot_info.send(embed=embed)


# Commande pour créer un compte utilisateur pour tout le monde
@bot.tree.command(name="create_all", description="C'est une commande pour créer un compte a tout le monde")
async def create_all(ctx):
    server = ctx.guild
    for member in server.members:
        user_id = str(member.id)
        if user_id not in users:
            users[user_id] = {"balance": 0, "xp": 0, "level": 0}
    with open('users.json', 'w') as f:
        json.dump(users, f)
    await ctx.response.send_message('Les comptes ont été créés avec succès')
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``create_all``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="level", description="C'est une commande pour afficher sont niveau")
async def level(ctx):
    user_id = str(ctx.user.id)
    if user_id in users:
        level = users[user_id]['level']
        xp = users[user_id]['xp']
        max_xp = xp-(1000*level)
        embed = discord.Embed(title=f'**Votre niveau actuel est : ``{level}`` avec ``{max_xp}/1000`` xp !**')
    else:
        embed = discord.Embed(title="**Vous n'avez pas encore de compte**")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``level``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="leveltop", description="C'est une commande pour afficher les personne qui ont le plus de niveau")
async def leveltop(ctx):
    sorted_users = sorted(users.items(), key=lambda x: x[1]['level'], reverse=True)
    top_users = sorted_users[:5]
    message = ''
    for i, user in enumerate(top_users):
        member = ctx.guild.get_member(int(user[0]))
        message += f'{i+1}. {member.name} - Niveau {user[1]["level"]}\n'
    embed = discord.Embed(title="**Voici les 5 personnes ayant le plus haut niveau :**", description=message)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-assets/855019362499035147/1066031618382377010.png")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``leveltop``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="baltop", description="C'est une commande pour afficher les personne qui ont le plus d'argent")
async def baltop(ctx):
    sorted_users = sorted(users.items(), key=lambda x: x[1]['balance'], reverse=True)
    top_users = sorted_users[:5]
    message = ''
    for i, user in enumerate(top_users):
        member = ctx.guild.get_member(int(user[0]))
        message += f'{i+1}. {member.name} - {user[1]["balance"]}$\n'
    embed = discord.Embed(title="**Voici les 5 personnes ayant le plus d'argent :**", description=message)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-assets/855019362499035147/1066031618382377010.png")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``baltop``", inline=True)
    await channel_bot_info.send(embed=embed)
#------SYSTEME DE MONEY------ ^^^


@bot.tree.command(name="rules", description="C'est une commande pour afficher les règles")
async def rules(ctx):
    rules_channel = bot.get_channel(991074780692250685)
    embed = discord.Embed(title="**Voici le lien vers les règles:**", description=rules_channel.mention)
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``rules``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="weather", description="C'est une commande pour afficher la météo")
@app_commands.describe(city = "Le nom d'une ville")
async def weather(ctx, city: str):

    # Requête à l'API OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1985c9953ebeb80c9e188191feb28eb9'
    response = requests.get(url)
    data = json.loads(response.text)

    # Vérification de la réponse de l'API
    if data['cod'] == 200:
        # Récupération des données météo
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Affichage des données météo dans le salon Discord
        embed = discord.Embed(title=f'Météo à {city}', color=0x00ff00)
        embed.add_field(name='Température', value=f'{temp} °C')
        embed.add_field(name='Température minimale', value=f'{temp_min} °C')
        embed.add_field(name='Température maximale', value=f'{temp_max} °C')
        embed.add_field(name='Humidité', value=f'{humidity} %')
        embed.add_field(name='Vitesse du vent', value=f'{wind_speed} m/s')
        embed.add_field(name='Description', value=description)
        await ctx.response.send_message(embed=embed)
    else:
        await ctx.response.send_message('Ville non trouvée')
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``weather``", inline=True)
    embed.add_field(name="city :", value=f"``{city}``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="serverinfo", description="Affiche des informations sur le serveur.")
async def serverinfo(ctx):
    server = ctx.guild
    roles = []
    for role in server.roles:
        if role.name != "@everyone":
            roles.append(role.mention)
        else:
            roles.append(role.name)
    role_list = ", ".join(roles)
    embed = discord.Embed(title=f"Informations sur {server.name}", color=0x00ff00)
    embed.add_field(name="Nom du serveur:", value=server.name)
    embed.add_field(name="ID du serveur:", value=server.id)
    embed.add_field(name="Propriétaire du serveur:", value=server.owner)
    embed.add_field(name="Nombre de membres:", value=server.member_count)
    embed.add_field(name="Rôles:", value=role_list)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-assets/855019362499035147/1066079079511629824.png")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``serverinfo``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="userinfo", description="C'est une commande pour afficher des informations sur un utilisateur")
@app_commands.describe(member = "Le nom d'un membre")
async def userinfo(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.user
    roles = []
    for role in member.roles:
        if role.name != "@everyone":
            roles.append(role.mention)
        else:
            roles.append(role.name)
    embed = discord.Embed(title=f"Informations sur {member}", color=member.color)
#    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="ID :", value=member.id, inline=False)
    embed.add_field(name="Statut :", value=member.status, inline=False)
    embed.add_field(name="Crée le :", value=member.created_at.strftime('%a %#d %B %Y'), inline=False)
    embed.add_field(name="Rejoint le :", value=member.joined_at.strftime('%a %#d %B %Y'), inline=False)
    embed.add_field(name="Roles :", value=', '.join(roles) or 'Aucun role', inline=False)
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``userinfo``", inline=True)
    embed.add_field(name="member :", value=f"``{member}``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="discordpy", description="C'est une commande pour apprendre a faire des bot discord en python")
async def discordpy(ctx):
    embed = discord.Embed(title="**Voici un example de bot discord en python :**", description="```import discord\n\nbot = commands.Bot(command_prefix= '!')\n\n@bot.event\nasync def on_ready():\n    print('Le bot est lancé !')\n\n@bot.command()\nasync def say(ctx, message=None)\n    await ctx.send(message)\n\nbot.run('Votre TOKEN')```")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``discordpy``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="joke", description="C'est une commande pour faire des blagues")
async def joke(ctx):
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    data = json.loads(response.text)
    joke = data['setup'] + ' ' + data['punchline']
    embed = discord.Embed(title="**Voici votre blague :**", description=joke)
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``joke``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="lban", description="C'est une commande pour voir la liste des banni")
async def lban(ctx):
    bannedUsers = bot.guilds.bans()
    print(bannedUsers)
    if bannedUsers == []:
        embed = discord.Embed(title="**Il n'y a personne de banni !**")
        await ctx.response.send_message(embed=embed)
    for i in bannedUsers:
        embed = discord.Embed(title="**Liste banni :**", description=f"{i.user.name}#{i.user.discriminator} ")
        await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``lban``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="statut", description="C'est une commande pour voir le statut du bot")
async def statut(ctx):
    embed = discord.Embed(title="**Le statut du bot est :**", description=f"``{data['statut']}``")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``statut``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="setstatut", description="C'est une commande pour modifier le statut du bot")
@app_commands.describe(new_statut = "Le nouveau statut du bot")
async def setstatut(ctx, new_statut: str):
    data['statut'] = new_statut
    await bot.change_presence(activity=discord.Game(data['statut']))
    embed = discord.Embed(title="**Le nouveau statut du bot est :**", description=f"``{data['statut']}``")
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``setstatut``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="binaire", description="C'est une commande pour convertire en binaire")
@app_commands.describe(phrase = "La phrase a convertire")
async def binaire(ctx, phrase: str):
    newphrase = ' '.join(format(ord(c), 'b') for c in phrase)
    embed = discord.Embed(title="**Voici le binire de votre phrase :**", description=newphrase)
    await ctx.response.send_message(embed=embed)
    #---------BOT INFO---------
    channel_bot_info = bot.get_channel(data['ID_salon_logs'])
    embed = discord.Embed(title="**bot - information**", description="Le bot a effectuer une action !")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
    embed.add_field(name="Action :", value="``tree.command``", inline=True)
    embed.add_field(name="Commande :", value="``binaire``", inline=True)
    await channel_bot_info.send(embed=embed)


@bot.tree.command(name="message_mention", description="C'est une commande pour un message de mention")
async def message_mention(ctx):
    channel = bot.get_channel(1067821068963819540)
    role_notif1 = discord.utils.get(ctx.guild.roles, id=1067788975319830618)
    role_notif2 = discord.utils.get(ctx.guild.roles, id=1067796435724157048)
    role_notif3 = discord.utils.get(ctx.guild.roles, id=1067796538396512297)
    embed = discord.Embed(title="**Voicie les notif de role proposer :**", description="Si vous voulez recevoir une notification quand une certain avec se produira, vous devais mettre la reaction demander.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-assets/855019362499035147/1067820652297457684.png")
    embed.add_field(name="Notification des annonces : <:1_:1067816693105172480>", value=role_notif1.mention, inline=False)
    embed.add_field(name="Notification des suggestions : <:2_:1067816690039144469>", value=role_notif2.mention, inline=False)
    embed.add_field(name="Notification des events : <:3_:1067816687480610858>", value=role_notif3.mention, inline=False)
    msg = await channel.send(embed=embed)
    await msg.add_reaction("<:1_:1067816693105172480>")
    await msg.add_reaction("<:2_:1067816690039144469>")
    await msg.add_reaction("<:3_:1067816687480610858>")


@bot.event
async def on_voice_state_update(member, before, after):
    category = discord.utils.get(member.guild.categories, id=1067780889788022824)
    if after.channel == None:
        if before.channel is not None:
            if before.channel.category.id == 1067780889788022824 and before.channel.id != 1067784582864314388 and before.channel.id != 1067784198217285692 and before.channel.id != 1067865535250964520:
                await before.channel.delete()
    # Vérifie si l'utilisateur vient de rejoindre le salon vocal spécifique
    elif after.channel.id == 1067865535250964520:
        # Créer un salon vocal privé pour l'utilisateur
        private_channel = await member.guild.create_voice_channel(name=f"Salon de {member.name}",category=category)
        # Ajouter l'utilisateur au salon vocal privé
        await member.move_to(private_channel)
#----------ROLE VOCAL----------
    role = discord.utils.get(member.guild.roles, id=1067781951685140530)
    if before.channel is None and after.channel is not None:
        await member.add_roles(role)
    elif before.channel is not None and after.channel is None:
        await member.remove_roles(role)


bot.run(data['TOKEN'])