import discord
from discord.ext import commands
from random import randint

client = commands.Bot(command_prefix = '!')

#intialize queues
q1 = []
ready1 = False


#host placeholder
host = 'blank'

#set channel ids
c1 = 625914651582136323


@client.event
async def on_ready():
	print('Bot is ready')

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

@client.command()
async def queue(ctx):
	if ctx.message.channel.id == c1:
		if ctx.author in q1:
			await ctx.send(f'User is already in queue!')
		else:
			q1.append(ctx.author)
			await ctx.send(f'User {ctx.author.mention} has been queued!')


@client.command()
async def startRaid(ctx):
	if ctx.message.channel.id == c1:
		if (len(q1) == 0):
			await ctx.send(f'Error: no users in queue!')
		else:
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

@client.command()
async def extra(ctx):
	if ctx.message.channel.id == c1:
		if (len(q1) == 0):
			await ctx.send(f'Error: no users in queue!')
		else:
				num = randint(1000,9999)
				u1 = q1.pop(0)
				await ctx.send(f'{u1.mention} Check your DMs for the raid code!')
				await u1.send(num)
				await host.send(num)

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
