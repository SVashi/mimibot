import discord
from discord.ext import commands
from random import randint

client = commands.Bot(command_prefix = '!')

#IMPORTANT: Set channel id to channel bot is running in
c1 = 625914651582136323

#intialize queues
q1 = []
ready1 = False


#host placeholder
host = 'blank'

#randomNum gen
num = randint(1000, 9999)


@client.event
async def on_ready():
	print('Bot is ready')

#User can set up a raid with !setRaid raidName
@client.command()
async def setRaid(ctx, *, raidName):
	global ready1
	global host
	if ctx.message.channel.id == c1:
		if ready1:
			await ctx.send(f'Error: raid already in progress!')
		else:
			ready1 = True
			host = ctx.author
			await ctx.send(f'Creating raid: {raidName} hosted by {ctx.author.mention}!')

#Users will queue for raids by typing !queue, the bot will sort them into the right queue, even across different channels
@client.command()
async def queue(ctx):
	if ctx.message.channel.id == c1:
		if ctx.author in q1:
			await ctx.send(f'User is already in queue!')
		else:
			q1.append(ctx.author)
			await ctx.send(f'User {ctx.author.mention} has been queued!')

#Host can start the raid to select 3 people and the bot generates a code for them from 1000 to 9999
@client.command()
async def startRaid(ctx):
	if ctx.author == host:
		if ctx.message.channel.id == c1:
			if (len(q1) == 0):
				await ctx.send(f'Error: no users in queue!')
			else:
				global num
				num = randint(1000,9999)
				if(len(q1) == 1):
					u1 = q1.pop(0)
					await ctx.send(f'{u1.mention} Check your DMs for the raid code!')
					await u1.send(num)
					await host.send(num)
				if(len(q1) == 2):
					u1 = q1.pop(0)
					u2 = q1.pop(0)
					await ctx.send(f'{u1.mention} {u2.mention} Check your DMs for the raid code!')
					await u1.send(num)
					await u2.send(num)
					await host.send(num)
				if (len(q1) == 3):
					u1 = q1.pop(0)
					u2 = q1.pop(0)
					u3 = q1.pop(0)
					await ctx.send(f'{u1.mention} {u2.mention} {u3.mention} Check your DMs for the raid code!')
					await u1.send(num)
					await u2.send(num)
					await u3.send(num)
					await host.send(num)
#Host can grab an extra player if necessary with same link code
@client.command()
async def extra(ctx):
	global num
	if ctx.message.channel.id == c1:
		if (len(q1) == 0):
			await ctx.send(f'Error: no users in queue!')
		else:
				u1 = q1.pop(0)
				await ctx.send(f'{u1.mention} Check your DMs for the raid code!')
				await u1.send(num)
				await host.send(num)

#Host can end raid
@client.command()
async def endRaid(ctx):
	if ctx.author == host:
		global q1
		global ready1
		q1 = []
		ready1 = False
		await ctx.send(f'Thanks for raiding everyone! Be sure to leave a comment on the host\'s reddit thread if they have one!')




client.run('NjY4MjkxMTU1MTI0ODEzODI1.XiPI_A._vlJMbxfe1J7y_ErBj0ypicKGG0')
# Mimi bot coded by Shivam Vashi
#
#                               ▄#▓▌
#                               ███▀
#                               ███
#                             ▄█████
#                           ▄██████▀
#                          ████████
#                          ███Ñ║║║█
#                         ▄║║║║║║║║
#                        #│║║║║║║║║
#                       å╢║║║║║║▒║█
#                      ┌Ñ▒║║║▒║║║▒▌
#                      █▒║║║║║║║║▒⌐
#                   ▄#▒║║║║║▒▒║║║║▒╔,
#                ▄▒│║║║║║║║║║▒║║║║║║║▒▄
#             ▄#Ñ║║║║║║▒█╪╡║║║║║║║║║║║║▒▄
#            @│║▒▒▒▒║█████▌║║║║║║║║▒║║║║║▒▄▄▄▄╖╖#N▒▒▒▒▒███╗
#           █║▒▒▒▒▒▒██████║║║║║║║║║║▒║║║║║Ñ╡║║║║▒▒║║║▒▒█████▓
#           ╫║▒▒▒▒╠│Ñ│Ñ▀│▒║║║║║║║║║██████║║║║║║║║║▒║║║████████,
#           └╡▒▒▒║█▌║║║║▒▒▒║▒║║║▒║██████╫▒║▒║║║║▒║│╝╜└  -╙▀▓███▓
#            ╙▒║║║██╙ÑÑ╙││││╙╙Ñ╙╙╙███████║║║║║╠╝╜└          ╙▀███▄
#             ╘∩∩│╙▀▀▀███▄∩∩∩∩∩∩∩∩╙▀▀▀▀└╙║║▒▌¬                 ▀█▌
#              └▄∩∩∩∩∩∩∩▀█▄▄▄∩∩∩∩╓#MM#∩∩∩∩│║          ▄▄,
#                ¼/∩∩∩│∩∩Ñ╙▀██[▄▄█▒▒▒▒Ñ∩∩│#       ▄#▓▒▓▒▒▄
#                ╓Ñ╢░⌂∩∩∩∩∩∩∩▀▀██▒▒▒╙∩∩∩∩╜     ▄▓▒▓▓▓▓▓▒▓█
#               #│║║║▒▒╢╢#╓∩∩∩∩Å╙╙╙Ñ∩∩╓╛└   ▄▓▒▓▓▓▒▓▓▓▓█▓╢
#              #│║║║║║▒║║║║▒▒N▓╙╜╜╙º"-    ▄▓▒▓▓▒▓▒▒▓▓▓▓█▒▀
#             ƒ║║║║║▒▒▒▒╢▒▒▒║║║▄        .▓▒▓▒▓▒▒▒▒▓██▒▒╜-
#            ƒ│▒╢║╙╙╙│││∩│││╙╙╚║▒▄      ▀▓▓▓▓▓▓█▒▒▀╩└
#           ╒Ñ╚Ñ∩∩∩∩∩▄∩∩∩∩╓▄∩∩∩∩│╙╖      █▓▓▓█╙¬
#           ▀∩∩∩∩∩∩∩▐█∩∩∩∩▐█∩∩∩∩∩∩∩%   ▄▓▓▓▓▓▓▌
#          å∩∩∩∩∩∩∩∩▐█∩∩∩∩∩█∩∩∩∩∩∩∩∩▌ ╙▒▒▒▒█╩└
#          V∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩b  █▒▒█
#         ╡∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩│∩∩∩║╓▒║▀╙
#  "½R∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩Ñ▀m▄▄
#   ,▄╗▓▓▓▄▄∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩│∩∩┘∩w
# '▀▀▀╙╙╙█▀▀M\N┴º╙██▀┴Ç/∩\▓▓▓▓≥⌂▄∩∩∩▐████▌ -
