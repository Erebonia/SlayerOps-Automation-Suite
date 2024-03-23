import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
from dotenv import load_dotenv
from discord.ui import View, Button, Select
import asyncio
import re
from math import ceil

async def send_message(message, user_message, is_private):
    try:
        await message.author.send() if is_private else await message.channel.send()
    
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    intents.members = True

    #Emojis
    FIRE_SLASH = '<:FireSlash:1054837281246163054>'
    ICE_STONE = '<:IceStone:1054837289466986589>'
    LIGHTNING_SLASH = '<:LightningSlash:1054837295062188053>'
    STONE_STRIKE = '<:StoneStrike:1054837307947098162>'
    FIRE_SWORD = '<:FireSword:1054837553951416431>'
    MANAS_BLESSING = '<:ManasBlessing:1054837518668923000>'
    GROUNDS_BLESSING = '<:GroundsBlessing:1054837631726395506>'
    LIGHTNING_STROKE = '<:LightningStroke:1054837501195468851>'
    HOT_BLAST = '<:HotBlast:1054837499027013642>'
    ICE_SHOWER = '<:IceShower:1054837351270060173>'
    AGILE = '<:Agile:1054837638730879106>' 
    POWER_STRIKE = '<:PowerStrike:1054837360354938950>'
    POWER_IMPACT = '<:PowerImpact:1054837502499889262>'
    FLAME_SLASH = '<:FlameSlash:1054837335084236881>'
    WATER_SLASH = '<:WaterSlash:1054837500012671046>'
    THUNDER_SLASH = '<:ThunderSlash:1054837355497922641>'
    BURNING_SWORD = '<:BurningSword:1054837580388126721>'
    FLOWING_BLADE = '<:FlowingBlade:1054837613074321561>'
    SPEED_SWORD = '<:SpeedSword:1054837558133129236>'
    EARTHS_WILL = '<:EarthsWill:1054837582124560485>'
    FLAME_WAVE = '<:Flamewave:1054837524343824444>'
    CURVED_BLADE = '<:CurvedBlade:1054837628563890197>'
    FULGUROUS = '<:Fulgurous:1054837528714293288>'
    IRON_WILL = '<:IronWill:1054837555482341487>'
    DANCING_WAVES = '<:DancingWave:1054837660025360464>'
    WIND_SWORD = '<:WindSword:1054837583382847648>'
    LIFE_MANA = '<:LifeMana:1054837659052285972>'
    HELLFIRE_SLASH = '<:HellfireSlash:1054837443347615796>'
    FIRE_BLAST = '<:FireBlast:1054837514675966034>'
    ICE_TIME = '<:IceTime:1054837455246868560>'
    THUNDERBOLT_SLASH = '<:ThunderboltSlash:1054837459994812426>'
    GIGA_STRIKE = '<:GigaStrike:1054837450415022140>'
    RAGE = '<:Rage:1054837629679575160>'
    MEDITATION = '<:Meditation:1054837527204352010>'
    RED_LIGHTNING = '<:RedLightning:1054837517523882115>'
    GIGA_IMPACT = '<:GigaImpact:1054837516102021211>'
    PILLAR_OF_FIRE = '<:PillarofFire:1054837539896295484>'
    BLIZZARD = '<:Blizzard:1054837537312608287>'
    SUPERSONIC = '<:Supersonic:1054837538793197628>'
    DEMON_HUNT = '<:DemonHunt:1054837525799248034>'
    WARRIOR_BURN = '<:WarriorBurn:1054837661195583558>'
    STRONG_CURRENT = '<:StrongCurrent:1054837556778373120>'
    LIGHTNING_BODY = '<:LightningBody:1054837662445469706>'
    WRATH_OF_GOD = '<:WrathofGoth:1054837540970057778>'
    RAVE = '<:rave:1055598059628789772>'
    MANTRA = '<:Mantra:1054837329367420998>'

    #Spirits
    SALA = '<:sala:1060758775839080598>'
    MUM = '<:mum:1060758787092402237>'
    BO = '<:worrybo:1060758772752056380>'
    ARK = '<:ark:1060758770373886002>'
    TODD = '<:todd:1060758778221436989>'
    LUGA = '<:luga:1060758784106057880>' 
    HERH = '<:herh:1060758774421409792>'
    KART = '<:kart:1060759190672515092>'
    ZAPPY = '<:zappy:1060758779488112701>'
    LOAR = '<:loar:1060758780775764058>'
    RADON = '<:radon:1060758791207002131>'
    NOAH = '<:noah:1060758788237443132>'

    #weapons
    MYTHIC_4 = '<:mythic4:1055585724344320080>'
    MYTHIC_3 = '<:mythic3:1055585725590032436>'
    MYTHIC_2 = '<:mythic2:1055585726802186351>'
    MYTHIC_1 = '<:mythic1:1055585728140148747>'
    IMMORTAL_ORR = '<:immortal:1055585922177040454>'
    AWAKENED_ORR = '<:awakensword:1055585923364048966>'

    #classes
    CLASS_17 = '<:class17:1055586740276052028>'
    CLASS_18 = '<:class18:1055586741010059329>'
    CLASS_19 = '<:class19:1055586742952018001>'
    CLASS_20 = '<:class20:1055586744231272498>' 
    TERA = '<:tera:1055588078254825585>'
    
    #Disclaimer
    buildDisclaimer = "These builds are the **BARE MINIMUM** so you may need to amp up your character depending on your build."

    # Change only the no_category default string
    help_command = commands.DefaultHelpCommand(
        no_category = 'General Commands')

    bot = commands.Bot(intents=intents, command_prefix="!", help_command = help_command)

    load_dotenv()
    TOKEN = os.getenv("Discord_TOKEN")

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now active.')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        ##Redo code to detect user ID instead
        #print(f'{username} said: "{user_message}" ({channel})')
        # guild = message.guild
        # if 'Wangster' in username:
        #     print("GOT IT CHIEF I'M ON HIS ASS")
        #     member = message.author
        #     role = discord.utils.get(message.guild.roles, name="Adamantite")
        #     await member.add_roles(role) 
        #     print('Wangster defeated.')

        if user_message is None:
            return

        if str(user_message) == '!':
            return print('The message is just an exclamation point. Exiting function.')

        if message.content == "!closeticket":
            category = message.channel.category
            if category.name == "Support Tickets" or category.name == "Slayer Master Tickets":
                await message.channel.send("This ticket is now closed. The channel will be deleted in 60 seconds. Type `stop` to cancel deletion.")
                try:
                    msg = await bot.wait_for("message", check=lambda m: m.channel == message.channel and m.author != bot.user, timeout=60)
                    if msg.content.lower() == "stop":
                        await message.channel.send("Deletion canceled.")
                    else:
                        await message.channel.delete()
                except asyncio.TimeoutError:
                    await message.channel.delete()
            else:
                await message.channel.send("This command can only be used in a ticket channel.")

        if user_message[0] == '!':
            user_message = user_message[1:] #user message is everything after the prefix !
            user_message = user_message.lower()

            if str(message.channel) not in ['❓questions','🤖bot-channel', 'test']: #'💬general', 
                return print('Im guh')
        else:
            return 

        await bot.process_commands(message)

    @bot.command(brief='Displays avatar', aliases=['ava', 'avat'] )
    async def avatar(ctx, member : discord.Member = None):
        if member == None:
            member = ctx.author

        memberAvatar = member.avatar

        avaEmbed = discord.Embed(title = f"{member.name}'s Avatar")
        avaEmbed.set_image(url = memberAvatar)

        await ctx.send(embed= avaEmbed)

    @bot.command(brief='Pulls up the guide and recommends you to the #resources channel for access to other documents.')
    async def guide(ctx):
        await ctx.channel.send('<:guide:1055587557976580106> **Slayer Legend Master Guide**: https://docs.google.com/document/d/1ZmuecOLwfVM4pi71nWzjQIAlqLJlu9RE2meRvj9ugtM/edit?usp=sharing For more information check out <#1120946427305152523>')

    @bot.command(brief='Explains the growth tree priority', aliases=['grow'])
    async def growth(ctx):
        await ctx.channel.send('<:dragonatk:1055586248552628274> **Growth Priority**: CRIT > Luck > STR > ACC > Dodge. If you are new try a mix of crit and luck at first if you lack damage. For latent roles using dragon souls: Focus attack and crit as first priority luck secondary then Hp and Vit last. For latent, roll everything completely to start. You’ll want to basic reset working towards 9/10 Crit and 9/10 Atk respectively, until then do not do advanced rolls')
               
    @bot.command(brief='Explains briefly about the Rave skill')
    async def rave(ctx):
        await ctx.channel.send('<:rave:1055598059628789772> https://cdn.discordapp.com/attachments/1098632587699814431/1103794686411415672/image.png')

    @bot.command(brief='What new players should strive for.')
    async def new(ctx):
        await ctx.channel.send('❗ New players generally focus on getting a mythic weapon (M1 preferred) and class grade 16 or above. For Companion and Slayer promo go for just red attack and slowly get them all to blue attack, if you lack mana recovery use some mana regen in comp slots. For a more in depth guide please go to #📚resources')

    @bot.command(brief='miscguides', aliases=['misc','miscguide'])
    async def miscguides(ctx):
        await ctx.channel.send('**How to change Slayer Legends Accounts on Android** \n \
1.  Load up the [Google] Play Games App \n \
2.  Go the Settings (Often found at the top right of the screen) \n \
3.  Scroll down to the "Your Data" section, and go to Change account for games  \n \
4.  Change the account you want to login to here. You can also proceed to change the default account.\n\n \
**IOS Manual Update Guide** \n \
If you are on iOS and the game has a new patch but AppStore does not show the update: \n \
1. Go to your account profile (top right icon in AppStore) \n \
2. Swipe down to force a refresh on all apps \n \
3. Then scroll down to the app and it should have an update')

    @bot.command(brief='Brief description on spirits.', aliases=['spirits', 'spir'])
    async def spirit(ctx):
        embed = discord.Embed(title="<:zappy:1060758779488112701> Spirit Combinations <:kart:1060759190672515092>", description="A brief overview of spirit combinations to use.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1060758788237443132.webp?size=128&quality=lossless")
        embed.add_field(name="<:stageboss:1055593196983439510> Boss Focused", value="Noah, Loar, Sala", inline=False)
        embed.add_field(name="<:guide:1055587557976580106>Stage Farm / Closed Mine", value="Mum, Radon, Zappy and if nothing else  (Luga/Todd)", inline=False)
        embed.add_field(name="🌲 Forest of Circulation", value="Mum, Zappy, Kart", inline=False)
        embed.add_field(name="<:riftboss:1055600337014231152> Dimensional Rift / Dragon Boss", value="Herh & Your two highest level spirits.", inline=False)
        embed.add_field(name= AWAKENED_ORR + " Extreme End Game Farming", value="Todd, Luga, Mum, Herh (Optional) or Highest Level Pet (Due to stat bonuses)", inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Comprehensive Guide:", value = "https://docs.google.com/document/d/1ZmuecOLwfVM4pi71nWzjQIAlqLJlu9RE2meRvj9ugtM/edit?usp=sharing")
        embed.set_footer(text = "Thank you Orbpunk, Sand, and Bee for helping to create these loadouts")
        await ctx.channel.send(embed=embed)
    
    @bot.command(brief='Loadout for the Spirit Dungeon.', aliases=['spiritdung', 'spiritd'])
    async def spiritdungeon(ctx):
        embed = discord.Embed(title="Spirit Dungeon Builds", description="A **minimum** loadout for spirit dungeons.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1060758775839080598.webp?size=128&quality=lossless")
        embed.add_field(name="<:stageboss:1055593196983439510> Early Game", value=LIGHTNING_STROKE + RED_LIGHTNING + SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + '\n' + BURNING_SWORD, inline=False)
        embed.add_field(name="<:guide:1055587557976580106> Mid Game", value=SUPERSONIC + LIGHTNING_STROKE + RED_LIGHTNING + MEDITATION + FIRE_SWORD + '\n' + STRONG_CURRENT + SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + FULGUROUS + '/' + SUPERSONIC + FLAME_SLASH + HELLFIRE_SLASH + MEDITATION + '\n' + 'pick 2-3 atk spd buffs and 2-3 atk power buffs' , inline=False)
        embed.add_field(name= AWAKENED_ORR + " Late Game", value=FULGUROUS + '/' + SUPERSONIC + FLAME_SLASH + HELLFIRE_SLASH + DEMON_HUNT + '/' + ICE_TIME + MEDITATION + '\n' + RAGE + LIGHTNING_BODY + SPEED_SWORD + EARTHS_WILL + BURNING_SWORD, inline=False)
        embed.add_field(name= AWAKENED_ORR + " End Game", value=SUPERSONIC + LIGHTNING_BODY + LIGHTNING_STROKE + RED_LIGHTNING + MEDITATION + '\n' + ICE_TIME + '/' + BLIZZARD + CURVED_BLADE + SPEED_SWORD + EARTHS_WILL + RAGE, inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=MUM + ZAPPY + KART + '/' + RADON, inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Tips", value = "Manual SS, DH, and Med. Use ice time if enhanced for the late game build.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A build specifically for the Training Cave for EXP', aliases=['train', 'trainingcave', 'trainingc'])
    async def training(ctx):
        embed = discord.Embed(title="Training Cave Skill build", description="A **minimum** loadout for training cave EXP dungeon", color=discord.Colour.random())
        embed.add_field(name="Early Game", value=POWER_STRIKE + GIGA_STRIKE + MEDITATION + FLOWING_BLADE + SPEED_SWORD + '\n' + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name="Mid - Early End Game", value=POWER_STRIKE + GIGA_STRIKE + DEMON_HUNT + MEDITATION + FLOWING_BLADE + '/' + LIGHTNING_BODY + '\n' + SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD + STRONG_CURRENT + '/' + WRATH_OF_GOD, inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> Notes", value="If you do not have DH but do have PoF simply replace DH with PoF, Power/Giga Strike with Hellfire Slash and Flowing Blade with Fire Sword then farm Earth stages (5 and 10s). Lastly use farming spirits because training cave mobs are affected by their bonuses. (Zone 1 neutral -> Zone 2 Fire -> Zone 3 Water -> Zone 4 Wind -> Zone 5 Earth -> repeat)", inline=False)
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for stage farming.', aliases=['stage', 'stagef'])
    async def stagefarm(ctx):
        embed = discord.Embed(title="Stage Farm Skill buiild", description="A **minimum** loadout for stage farming.", color=discord.Colour.random())
        embed.add_field(name="Early Game", value=FULGUROUS + THUNDER_SLASH + THUNDERBOLT_SLASH + FLAME_WAVE + IRON_WILL + '/' + '\n' + FIRE_SWORD, inline=True)
        embed.add_field(name="Mid Game", value=FULGUROUS + SUPERSONIC + FLAME_WAVE + RED_LIGHTNING + MEDITATION + '\n' + FLOWING_BLADE + AGILE + IRON_WILL + '/' + FIRE_SWORD, inline=True)
        embed.add_field(name="Late Game", value=FULGUROUS + SUPERSONIC + FLAME_WAVE + RED_LIGHTNING + BLIZZARD + '\n' + MEDITATION + FLOWING_BLADE + AGILE + IRON_WILL + FIRE_SWORD, inline=True)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value='Farming spirits eg:' + MUM + ZAPPY + TODD, inline=False)
        embed.add_field(name="Tips", value="If you run out of mana using fulgurous level Luna’s mana dope", inline=False)
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for adventures', aliases=['adv', 'adventures', 'advent'])
    async def adventure(ctx):
        embed = discord.Embed(title="Adventure Skill buiild", description="A **minimum** loadout for adventures", color=discord.Colour.random())
        embed.add_field(name="<:dragonatk:1055586248552628274> High Volume of Mobs", value=FULGUROUS + THUNDERBOLT_SLASH + HELLFIRE_SLASH + RED_LIGHTNING + SPEED_SWORD + '\n' + EARTHS_WILL + IRON_WILL + 'or' + LIFE_MANA, inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Mostly Boss focused", value=FULGUROUS + HELLFIRE_SLASH + RED_LIGHTNING + SPEED_SWORD + EARTHS_WILL + '\n' + BURNING_SWORD + IRON_WILL + 'or' + LIFE_MANA, inline=False)
        embed.add_field(name= TERA + " End Game", value=FULGUROUS + BLIZZARD + PILLAR_OF_FIRE + DEMON_HUNT + MEDITATION + '\n' + SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD + IRON_WILL + 'or' + FIRE_SWORD, inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value='For primarily mob focused fights use;' + MUM + ZAPPY + KART + '\n' + 'For primarily boss focused fights use;' + NOAH + LOAR + SALA, inline=False)
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for companion fights.', aliases=['comp', 'compani', 'compan', 'companionbuild'])
    async def companion(ctx):
        embed = discord.Embed(title="Companion Boss Builds", description="A **minimum** loadout for companion fights", color=discord.Colour.random())
        embed.add_field(name=":cloud_tornado: Elie", value=POWER_STRIKE + GIGA_STRIKE + LIFE_MANA + FLOWING_BLADE + FIRE_SWORD + '\n' + MEDITATION + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name=":earth_africa: Zeke", value=FULGUROUS + FLAME_SLASH + HELLFIRE_SLASH + HOT_BLAST + MANAS_BLESSING + '\n' + FIRE_SWORD + SPEED_SWORD + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name=":fire: Miho", value=FULGUROUS + WATER_SLASH + ICE_TIME + FLOWING_BLADE + MEDITATION + '\n' + SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + IRON_WILL + '/' + LIFE_MANA, inline=False)
        embed.add_field(name=":bubbles: Luna", value=FULGUROUS + THUNDER_SLASH + THUNDERBOLT_SLASH + RED_LIGHTNING + LIFE_MANA + '\n' + FIRE_SWORD + SPEED_SWORD + EARTHS_WILL + BURNING_SWORD, inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=NOAH + LOAR + SALA, inline=False)
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for closed mines', aliases=['closed', 'mines', 'closedmi', 'closedmine', 'closedminebuild', 'closeminebuild'])
    async def closedmines(ctx):
        embed = discord.Embed(title="Closed Mine Skill Build", description="A **minimum** loadout for closed mine dungeon", color=discord.Colour.random())
        embed.set_thumbnail(url="https://discord.com/assets/6ed16a164f91fc0843c06088529e3a27.svg")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: Any", inline=True)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value="Any", inline=True)
        embed.add_field(name= TERA + " Class", value="Any", inline=True)
        embed.add_field(name="<:skillbook:1055586814481678407> Early Skill Build", value=BURNING_SWORD + AGILE + FIRE_SWORD + FLAME_WAVE + FULGUROUS + '\n' + THUNDERBOLT_SLASH + LIGHTNING_STROKE + IRON_WILL + LIFE_MANA + '/' + MANAS_BLESSING , inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> Mid Game Skill Build", value=BURNING_SWORD + AGILE + FIRE_SWORD + SUPERSONIC + RED_LIGHTNING + '\n' + FLAME_WAVE + MEDITATION + THUNDERBOLT_SLASH + IRON_WILL, inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> End Game Skill Build", value=LIGHTNING_BODY + RAGE + AGILE + BURNING_SWORD + SUPERSONIC + '\n' + EARTHS_WILL + FLAME_WAVE + MEDITATION + BLIZZARD + RED_LIGHTNING, inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Notes:", value = "This is a build dedicated to speedy clears.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for stage farming.', aliases=['rift', 'dimensional', 'dim', 'dimension', 'dimen', 'dimens'])
    async def dimensionalrift(ctx):
        embed = discord.Embed(title="Dimensional Rift Skill Build", description="A **minimum** loadout for dimensional rift", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1055600337014231152.webp?size=128&quality=lossless")
        embed.add_field(name="<:skillbook:1055586814481678407> Early - Mid Game", value=HELLFIRE_SLASH + GIGA_STRIKE + DANCING_WAVES + MEDITATION + SPEED_SWORD + '\n' + FLAME_SLASH + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD, inline=True)
        embed.add_field(name="<:skillbook:1055586814481678407> High mid - Late Game", value=HELLFIRE_SLASH + DEMON_HUNT + DANCING_WAVES + MEDITATION + WRATH_OF_GOD + '\n' + FLAME_SLASH + SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> Late End Game", value=FLAME_SLASH + '/' + RAGE + HELLFIRE_SLASH + DEMON_HUNT + LIGHTNING_BODY + WRATH_OF_GOD + '\n' + MEDITATION + SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value= HERH + '(preferred)' , inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Tips:", value = "The boss has several skills that run on rotation, if using a manual build activate dancing waves when the boss goes to attack to dodge. Can alternate between Flame Slash and Rage in the auto build, flame slash will cause you to run out of mana faster but you may die a few levels earlier using rage. \n These builds can also be used for Shelter of Sleeping Flame.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for stage bosses', aliases=['stageb', 'boss', 'bossing', 'stagebossbuild', 'stagebuild', 'bossbuild'])
    async def stageboss(ctx):
        embed = discord.Embed(title="Stage Boss Skill Build", description="A **minimum** loadout for stage bosses", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1055593196983439510.webp?size=128&quality=lossless")
        embed.add_field(name="Early - Mid Game", value='2-3 ATK SPD buffs, 2 ATK Buffs, 2-3 DPS or Strike Skills', inline=True)
        embed.add_field(name="High mid - Late Game", value=GIGA_STRIKE + HELLFIRE_SLASH + PILLAR_OF_FIRE + FLOWING_BLADE + FIRE_SWORD + '\n' + RAGE + MEDITATION + SPEED_SWORD + EARTHS_WILL, inline=True)
        embed.add_field(name="What are good ATK Speed buffs / Skills?", value=FULGUROUS + FLOWING_BLADE + SPEED_SWORD + CURVED_BLADE, inline=True)
        embed.add_field(name="What are good Attack Buff Skills?", value=FIRE_SWORD + EARTHS_WILL + BURNING_SWORD + IRON_WILL, inline=False)
        embed.add_field(name ="What are good DPS / Strike Skills?", value = POWER_STRIKE + FLAME_SLASH + GIGA_STRIKE + HELLFIRE_SLASH)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=NOAH + LOAR + SALA, inline=False)
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='Response to easy promotion ranks', aliases=['silver', 'gold', 'bronze', 'stone'])
    async def easypromotions(ctx):
        await ctx.channel.send('We do not offer skill builds for these ranks. Try your best to level up and figure things out to the best of your ability. If you are new try the bot command !new for more information.')

    @bot.command(brief='A **minimum** loadout for Mithril Promotion', aliases=['mith', 'mithri', 'mit', 'mi'])
    async def mithril(ctx):
        embed = discord.Embed(title="Mithril Promotion Build (No Supersonic)", description="A **minimum** loadout for the mithril promotion class.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1054852906903425035.webp?size=128&quality=lossless")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: 100 Trillion+, Crit DMG: 4000%+, Deathstrike: 200%+", inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value= MYTHIC_4 + " and above", inline=True)
        embed.add_field(name= TERA + " Class", value="Class Rank 16 and above", inline=True)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=FULGUROUS + FLAME_WAVE + THUNDERBOLT_SLASH + RED_LIGHTNING + SPEED_SWORD + '\n' + CURVED_BLADE + IRON_WILL, inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=ZAPPY + MUM + KART + RADON + '(preferred to use any of these)', inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Tips:", value = "This build is focused on the assumption you have enough damage to one shot the small mobs with Fulgurous. We recommend that you turn off the auto feature for red lightning and thunderbolt slash casting them manually to be efficient. Supersonic makes advancing here extremely easy.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for orichalcum', aliases=['oric', 'ori', 'orichal', 'or', 'orich'])
    async def orichalcum(ctx):
        embed = discord.Embed(title="Orichalcum Promotion Build ", description="A **minimum** loadout for the orichalcum promotion class.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1054853274613862490.webp?size=128&quality=lossless")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: 100 Trillion+, Crit DMG: 7000%+, Deathstrike: 500%+", inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value= MYTHIC_2 + " and above.", inline=True)
        embed.add_field(name= TERA + " Class", value="Class Rank 16 and above", inline=True)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=FULGUROUS + GIGA_STRIKE + HELLFIRE_SLASH + SPEED_SWORD + EARTHS_WILL + '\n'+ BURNING_SWORD + IRON_WILL, inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=NOAH + LOAR + SALA, inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Skill build Guide:", value = "https://docs.google.com/document/d/1RZONQDkVokeafE5tUJBTAI9NqlAYeaeLr8Z6QTQHMZU/edit?usp=sharing")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for Arcanite Promotion', aliases=['arc', 'arcani', 'arca', 'arcan', 'arcanit'])
    async def arcanite(ctx):
        embed = discord.Embed(title="Arcanite Promotion Build ", description="A **minimum** loadout for the arcanite promotion class.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1054853414686834699.webp?size=128&quality=lossless")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: 150 Quadrillion+, Crit DMG: MAX, Deathstrike: 1000%+", inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value= MYTHIC_1 + " +100 and above", inline=True)
        embed.add_field(name=TERA + " Class", value= CLASS_17 + " and above", inline=True)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=FULGUROUS + SUPERSONIC + FLAME_WAVE + HELLFIRE_SLASH + SPEED_SWORD + '\n' + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=ZAPPY + MUM + KART + RADON + '(preferred to use any of these)', inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Tips", value = "N/A")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for Adamantite Promotion', aliases=['ada', 'adamant', 'adamanti', 'adaman', 'adama'])
    async def adamantite(ctx):
        embed = discord.Embed(title="Adamantite Promotion Build ", description="A **minimum** loadout for the adamantite promotion class.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1054852905020170390.webp?size=128&quality=lossless")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: 1.2 Quintillion+, Crit DMG: MAX, Deathstrike: 1700%+", inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value= MYTHIC_1 + " +100 and above", inline=True)
        embed.add_field(name= TERA + " Class", value= CLASS_18 + " and above", inline=True)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=FULGUROUS + SUPERSONIC + LIGHTNING_STROKE + RED_LIGHTNING + RAGE + '\n' + MEDITATION + SPEED_SWORD + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=ZAPPY + MUM + KART + RADON + '(preferred to use any of these)', inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Tips", value = "To maximise the benefit from rage, swap to your worst accessory and class before the start of the battle and then swap back once you’re in the battle.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for Ether Promotion', aliases=['ethe', 'eth'])
    async def ether(ctx):
        embed = discord.Embed(title="Ether Promotion Build ", description="A **minimum** loadout for the ether promotion class.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1060039749336830002.webp?size=128&quality=lossless")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: 60-70 Quintillion+, Crit DMG: MAX, Deathstrike: 2800%+", inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value= MYTHIC_1 + " +200", inline=True)
        embed.add_field(name= TERA + " Class", value= CLASS_18 + " and above", inline=True)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=NOAH + LOAR + SALA + '(preferred)', inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=PILLAR_OF_FIRE + GIGA_STRIKE + RED_LIGHTNING + SPEED_SWORD + EARTHS_WILL + '\n' + FIRE_SWORD + MEDITATION + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Tips", value = "Copy the skill placement shown exactly, If you consistently get the ether boss low, configure the skill placements and re-attempt.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for Companion 3 Page')
    async def comp3(ctx):
        embed = discord.Embed(title="Companion Page 3 ", description="Skill builds for companion page III", color=discord.Colour.random())
        embed.add_field(name=":cloud_tornado: Elie", value=SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD + WRATH_OF_GOD + '\n' + GIGA_STRIKE + FULGUROUS + 'or' + BLIZZARD + '(' + DEMON_HUNT + RAVE + 'or' + POWER_STRIKE + GIGA_IMPACT + ')' , inline=False)
        embed.add_field(name=":earth_africa: Zeke", value=SPEED_SWORD + CURVED_BLADE + BURNING_SWORD + MEDITATION + WRATH_OF_GOD + '\n' + BLIZZARD + HELLFIRE_SLASH + PILLAR_OF_FIRE + '(' + DEMON_HUNT + RAVE + 'or' + FLAME_SLASH + STRONG_CURRENT + ')', inline=False)
        embed.add_field(name=":fire: Miho", value=SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD + MEDITATION + '\n' + WRATH_OF_GOD + GIGA_STRIKE + BLIZZARD + 'or' + DANCING_WAVES + '(' + DEMON_HUNT + RAVE + 'or' + WATER_SLASH + STRONG_CURRENT + ')', inline=False)
        embed.add_field(name=":bubbles: Luna", value=SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD + MEDITATION + '\n' + WRATH_OF_GOD + FULGUROUS + GIGA_STRIKE + 'or' + DANCING_WAVES + '(' + DEMON_HUNT + RAVE + 'or' + THUNDER_SLASH + THUNDERBOLT_SLASH + ')', inline=False)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value = NOAH + LOAR + SALA, inline=False)
        embed.add_field(name ="<:guide:1055587557976580106> Tips", value = "Skills are to be dropped in the reverse order (bottom right to top left) if not enough skill slots.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for Black Mythril', aliases=['bm', 'blackmythri', 'blackmythr', 'blackmyth', 'blackmyt', 'blackmy', 'blackm', 'black'])
    async def blackmythril(ctx):
        embed = discord.Embed(title="Black Mythril Promotion Build ", description="A **minimum** loadout for the black mythril promotion class.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1060039750913888296.webp?size=128&quality=lossless")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: 1.5 Sextillion Attack, 40 Quintillion HP, Max Damage Resist", inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value= IMMORTAL_ORR + " +200", inline=True)
        embed.add_field(name= TERA + " Class", value= CLASS_18 + " and above", inline=True)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=NOAH + LOAR + SALA + '(preferred)', inline=False) 
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=BLIZZARD + PILLAR_OF_FIRE + DEMON_HUNT + RAVE + STRONG_CURRENT + '\n' + WRATH_OF_GOD + MEDITATION + SPEED_SWORD + EARTHS_WILL + BURNING_SWORD, inline=False)
        embed.add_field(name ="Tips", value = "1st Rave = Less than 600x HP, 2nd Wrath of God = Around 300x HP, 2nd Rave = 175-150x HP to kill.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for Demon Metal', aliases=['demonmeta', 'demonmet', 'demonme', 'demonm', 'demon', 'demo'])
    async def demonmetal(ctx):
        embed = discord.Embed(title="Demon Metal Promotion Build ", description="A **minimum** loadout for the demon metal promotion class.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1060039752704864336.webp?size=128&quality=lossless")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: 55+ Sextillion Attack, 500+ Quintillion HP", inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value= IMMORTAL_ORR + " +200 (Preferably Awakened)", inline=True)
        embed.add_field(name= TERA + " Class", value= CLASS_20 + " + 200", inline=True)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=NOAH + LOAR + SALA + '(preferred to be 2-4* awaken)', inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=BURNING_SWORD + CURVED_BLADE + EARTHS_WILL + SPEED_SWORD + MEDITATION + '\n' + FLAME_SLASH + HELLFIRE_SLASH + FLOWING_BLADE + WRATH_OF_GOD + DEMON_HUNT, inline=False)
        embed.add_field(name ="Tips", value = "When popping the first rave, spam rave to get sala in the opening, otherwise I recommend restarting. \n Getting double DH and rave in the very last bit of timing is very hard. I would try to time it where you pop meditation and rave at 23.5 WOG timer left, waiting for noah to pop up, spam double DH, and also spam rave at the very end.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for Dragonos', aliases=['dragono', 'drago'])
    async def dragonos(ctx):
        embed = discord.Embed(title="Dragonos Promotion Build ", description="A **minimum** loadout for the Dragonos promotion class.", color=discord.Colour.random())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1060039754382585856.webp?size=128&quality=lossless")
        embed.add_field(name="<:dragonatk:1055586248552628274> Stats", value="Base ATK: 400+ Sextillion Attack, 3 Sextillion HP, MAX Deathstrike, CRIT, and MAX Miho damage resistance.", inline=False)
        embed.add_field(name="<:equipment:1055587315457732761> Weapon", value= IMMORTAL_ORR + " Immortal Orr (Preferably 6* awakened)", inline=True)
        embed.add_field(name= TERA + " Class", value= CLASS_20 + " + 200 and above", inline=True)
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=NOAH + LOAR + SALA + '(preferred to be 2-4* awaken)', inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=BLIZZARD + DEMON_HUNT + WRATH_OF_GOD + RAVE + MEDITATION + '\n' + FLAME_SLASH + SPEED_SWORD + EARTHS_WILL + CURVED_BLADE + BURNING_SWORD, inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=BURNING_SWORD + CURVED_BLADE + EARTHS_WILL + SPEED_SWORD + MEDITATION + '\n' + FLAME_SLASH + HELLFIRE_SLASH + FLOWING_BLADE + WRATH_OF_GOD + DEMON_HUNT, inline=False)
        embed.add_field(name ="Tips", value = "9 mobs need to be killed before the boss. This boss has two abilities. The first one is Cooldown Resetting. It resets your cooldowns on the first skill row and later on the 2nd skill row. This means the order you put the skill build is highly important. Try to proc meditation right before his ability. \n The second ability is action speed buffs. He increases his attack speed, so use blizzard or have high HP to withstand these attacks.")
        embed.set_footer(text = buildDisclaimer)
        await ctx.channel.send(embed=embed)

    @bot.command(brief='A **minimum** loadout for training diary', aliases=['diar', 'dia', 'di'])
    async def diary(ctx):
        embed = discord.Embed(title="Training Diary Build", description="A **minimum** loadout for the training diary.", color=discord.Colour.random())
        embed.add_field(name="<:noah:1060758788237443132> Pets", value=NOAH + '(preferred)' , inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> Skill Build", value=SPEED_SWORD + EARTHS_WILL + POWER_STRIKE + GIGA_STRIKE + FIRE_SWORD + '\n' + BURNING_SWORD + CURVED_BLADE + FLAME_SLASH + IRON_WILL + FLOWING_BLADE, inline=False)
        embed.add_field(name="<:skillbook:1055586814481678407> End Game Skill Build", value=SPEED_SWORD + DEMON_HUNT + RAVE + MEDITATION + POWER_STRIKE + '\n' + CURVED_BLADE + WRATH_OF_GOD + BURNING_SWORD + '/' + WARRIOR_BURN + EARTHS_WILL + GIGA_STRIKE, inline=False)
        embed.add_field(name ="Tips", value = "If you’re unable to get two dh under wog rave move meditation to replace powerstrike and put in strong current, Manual Demon Hunt and Rave. For no DH/Rave build with 9/8/7 slots take out :FireSword: :IronWill: :FlowingBlade: respectively.")
        embed.add_field(name="Warning", value="You’re able to quit the battle and go back in without penalty. Spirits that do % based damage will not work such as Sala, loar, and radon. It’s best to use Noah. If ark and herh are low level use your two highest level spirits.", inline=False)
        embed.set_footer(text = buildDisclaimer + " Credit to Aurius, Bannibal and Patter.")
        await ctx.channel.send(embed=embed)

    async def ticketcallback(interaction):
        guild = interaction.guild
        role = discord.utils.get(guild.roles, name = "Moderation")
        role2 = discord.utils.get(guild.roles, name = "Trial Moderator")
        role3 = discord.utils.get(guild.roles, name = "Master Slayer")
        role4 = discord.utils.get(guild.roles, name = "Trial Master Slayer")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel = False),
            interaction.user: discord.PermissionOverwrite(view_channel = True),
            role: discord.PermissionOverwrite(view_channel = True),
            role2:discord.PermissionOverwrite(view_channel = True)
        }
        overwriteSlayer = {
            guild.default_role: discord.PermissionOverwrite(view_channel = False),
            interaction.user: discord.PermissionOverwrite(view_channel = True),
            role: discord.PermissionOverwrite(view_channel = True),
            role2:discord.PermissionOverwrite(view_channel = True),
            role3:discord.PermissionOverwrite(view_channel = True),
            role4:discord.PermissionOverwrite(view_channel = True)
        }

        select = Select(options=[
            discord.SelectOption(label = "Support Ticket", value = "01", emoji = "🌐", description = "Talk to a member of staff."),
            discord.SelectOption(label = "Master Slayer Ticket", value = "02", emoji = "‼️", description = "Ask a master slayer for some specific help."),
            # discord.SelectOption(label = "Moderator Application", value = "03", emoji = "<:roeycheck:1058492848279912569>", description = "Apply for the moderator position. If denied, this will remain confidential."),
            # discord.SelectOption(label = "Master Slayer Application", value = "04", emoji = "<:slayer:1060884306056204309>", description = "Apply for the Master Slayer role. If denied, this will remain confidential.")
        ])

        async def my_callback(interaction):
            channels = guild.text_channels
            name = f"{interaction.user.name.lower()}-ticket"
            duplicate = any(name == channel.name for channel in channels)
            message = ""
            masterSlayer = discord.utils.get(guild.roles, name = "Master Slayer")
            moderation = discord.utils.get(guild.roles, name = "Moderation")
            trialMS = discord.utils.get(guild.roles, name = "Trial Master Slayer")
            if duplicate:
                return await interaction.response.send_message("You already have an open ticket. Please resolve the current one.", ephemeral = True)

            if select.values[0] == "01":
                category = discord.utils.get(guild.categories, name = "Support Tickets")
                channel =  await guild.create_text_channel(f"{interaction.user.name}-ticket", category = category, overwrites=overwrites)
                await interaction.response.send_message(f"Created ticket - <#{channel.id}>", ephemeral = True)
                message = await channel.send(f"Hello, how may we help you? {interaction.user.mention}. Staff will be with you shortly. To close this ticket react to the checkmark below.") # {moderation.mention} {trialMod.mention}
                #message = await channel.send(f"Ponch is currently running tests on me, please disregard this ticket.")
            elif select.values[0] == "02":
                category = discord.utils.get(guild.categories, name = "Slayer Master Tickets")
                channel = await guild.create_text_channel(f"{interaction.user.name}-ticket", category = category, overwrites=overwriteSlayer)
                await interaction.response.send_message(f"Created ticket - <#{channel.id}>", ephemeral = True)
                message = await channel.send(f"Please wait a moment and a Master Slayer be with you to assist. Please feel free to ask your questions now while waiting. {interaction.user.mention}  The {masterSlayer.mention} {trialMS.mention} staff will be with you shortly. Please do not ask questions that are easily answerable in #faq or #bot-channel.")
            elif select.values[0] == "03":
                category = discord.utils.get(guild.categories, name = "Applications")
                channel = await guild.create_text_channel(f"{interaction.user.name}-ticket", category = category, overwrites=overwrites)
                await interaction.response.send_message(f"Created ticket - <#{channel.id}>", ephemeral = True)
                message = await channel.send(f"Thanks for your interest in the moderator position. A member of staff will get back to you after review. If the application is denied the result will remain confidential. {interaction.user.mention} To close this ticket react to the checkmark below. The {moderation.mention} staff will be with you shortly. In the meantime please answer these questions.")
                message = await channel.send(f" **Questions** \n \
- What is your time zone? \n \
- What interests you in this position? \n \
- Are you an active member of the community? \n \
- Aside from the game are you willing to help out with staff duties such as assigning roles and enforcing our current #rules")
            elif select.values[0] == "04":
                category = discord.utils.get(guild.categories, name = "Applications")
                channel = await guild.create_text_channel(f"{interaction.user.name}-ticket", category = category, overwrites=overwrites)
                await interaction.response.send_message(f"Created ticket - <#{channel.id}>", ephemeral = True)
                message = await channel.send(f"Thanks for your interest in the Master Slayer role. A member of staff will get back to you after review. If the application is denied the result will remain confidential. {interaction.user.mention} To close this ticket react to the checkmark below. The {moderation.mention} staff will be with you shortly. In the meantime please answer these questions. \n \
- What is your time zone? \n \
- What interests you in this position? \n \
- Are you an active member of the community? \n \
- Do you have deep knowledge about the game? \n \
- Are you okay with being pinged quite often for help?")

        select.callback = my_callback
        view = View(timeout = None)
        view.add_item(select)
        await interaction.response.send_message("Choose an option below", view=view, ephemeral = True)

    @bot.command()
    async def ticket(ctx):
        button = Button(label = "📥 Create Ticket", style = discord.ButtonStyle.green)
        button.callback = ticketcallback
        view = View(timeout = None)
        view.add_item(button)
        await ctx.send("Support System initiated. Please select an option below to open a ticket.", view=view)

    @bot.event
    async def on_message_delete(message):
        if message.author == bot.user:  # ignore messages from the bot itself
            return
        embed = discord.Embed(title="{} deleted a message".format(message.author.name),
                            description="", color=discord.Colour.random())
        embed.set_thumbnail(url=message.author.avatar)
        embed.add_field(name="Message that was deleted",
                        value=message.content, inline=False)
        embed.set_footer(text="In channel: {}".format(message.channel.name))
        channel = bot.get_channel(1054504916732879039)
        await channel.send(embed=embed)

    @bot.event
    async def on_message_edit(message_before, message_after):
        if message_before.author == bot.user:  # ignore messages from the bot itself
            return
        embed = discord.Embed(title="{} edited a message".format(message_before.author.name),
                            description="", color=discord.Colour.random())
        embed.set_thumbnail(url=message_before.author.avatar)
        embed.add_field(name="Before", value=message_before.content, inline=False)
        embed.add_field(name="After", value=message_after.content, inline=False)
        embed.set_footer(text="In channel: {}".format(message_before.channel.name))
        channel = bot.get_channel(1054504916732879039)
        await channel.send(embed=embed)

    def equipment(currentLevel, targetLevel, currentSummons):
        summonLevels = {
            "2": 100,
            "3": 250,
            "4": 100,
            "5": 4800,
            "6": 12000,
            "7": 25000,
            "7.5": 27500,
            "8": 55000
        }

        if currentLevel == "7.5" and currentSummons < summonLevels[currentLevel]: 
            currentSummons = summonLevels[currentLevel]

        flag = False
        residual = 0
        summonsNeeded = 0

        for level in summonLevels.keys():
            if targetLevel == "8" and level == "7.5":
               continue
            if float(level) > float(currentLevel) and float(level) <= float(targetLevel):
                if not flag:
                    tempSummonsNeeded = summonLevels[level] - currentSummons - residual
                    flag = True
                else:
                    tempSummonsNeeded = summonLevels[level] - residual

                residual = (ceil(tempSummonsNeeded / 33) * 33) - tempSummonsNeeded
                summonsNeeded += tempSummonsNeeded

        result = f"{ceil(summonsNeeded / 33 * 1500):,}" #diamond calculation

        return result 

    @bot.command()
    async def equip(ctx, currentLevel: str, targetLevel: str, currentSummons: int):
        if not currentLevel or not targetLevel or currentSummons is None:
            raise ValueError("Missing or invalid arguments")
    
        if currentLevel >= targetLevel:
            await ctx.send("Error: currentLevel must be lower than targetLevel.")

        elif targetLevel < 1 or targetLevel > 8:
            await ctx.send("Error: Max level for targetLevel is 8!")

        elif not isinstance(currentSummons, int) or currentSummons < 0:
            await ctx.send("Error: currentSummons must be a positive integer")

        else:
            result = equipment(currentLevel, targetLevel, currentSummons)
            await ctx.send(result)

    @equip.error
    async def equip_error(ctx, error):
        if(isinstance(error, TypeError)):
            await ctx.send(f"Error: currentLevel and targetLevel must be String and currentSummons must be integer.")
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send(f"Usage: !equip <currentLevel> <targetLevel> <currentSummons>\nExample: !equip 5 7.5 2000")

    bot.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()










