import discord
from discord.ext import commands
from discord import SlashCommandGroup


def check(num):
    ans = True
    i = 2
    while i*i <= num:
        if (num % i == 0):
            ans = False
            break
        i += 1
    return ans


def len_control(s):
    s_len = len(s)
    if (s_len < 2000):
        return s
    return s[s_len-2000:]


count = 2
a, b = 1, 1


class Primenumclass(discord.ui.View):
    @discord.ui.button(label="ć°ăă", style=discord.ButtonStyle.primary, emoji="đŽâđ¨")
    async def button_callback(self, button, interaction):
        global count
        text = len_control(interaction.message.content+str(count)+"...")
        await interaction.response.edit_message(content=text)
        while True:
            count += 1
            if check(count):
                break


class Fibonumclass(discord.ui.View):
    @discord.ui.button(label="ć°ăă", style=discord.ButtonStyle.primary, emoji="đŽâđ¨")
    async def button_callback(self, button, interaction):
        global a, b
        text = len_control(interaction.message.content+str(a)+"...")
        await interaction.response.edit_message(content=text)
        a, b = b, a+b


class PNR(commands.Cog):
    def __init__(self, bot):
        print("start PNR init")
        self.bot = bot

    command = SlashCommandGroup("pnr", "ăŞăă")

    @command.command(description="ăăăăŁç´ ć°ăć°ăăŚč˝ăĄçăăă ăŁ!!!")
    async def primenum(self, ctx: discord.ApplicationContext):
        global count
        count = 2
        await ctx.respond("ăăăăăăďźăăăŻăăăăŻçśćă ďźďźă¨ăăăăç´ ć°ăć°ăăŚč˝ăĄçăăďźďźďźďźďźďź", view=Primenumclass())

    @command.command(description="ăľăăľăăľăăăŁăăăăć°ĺăć°ăăŚč˝ăĄçăăă ăŁ!!!")
    async def fibonum(self, ctx: discord.ApplicationContext):
        global a, b
        a, b = 1, 1
        await ctx.respond("ăăăăăăďźăăăŻăăăăŻçśćă ďźďźă¨ăăăăăăŁăăăăć°ĺăć°ăăŚč˝ăĄçăăďźďźďźďźďźďź", view=Fibonumclass())


def setup(bot):
    bot.add_cog(PNR(bot))
