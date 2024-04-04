import disnake
from disnake.ext import commands
from cogs.view.buttons import SelectGender
class MainVerify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Верефикация Пользователй")
    async def verify(self, interaction: disnake.AppCommandInteraction, member: disnake.Member):
        embed = disnake.Embed(description=f"{member.mention}")
        await interaction.response.send_message(embed=embed, view=SelectGender(interaction.author, member))

def setup(bot):
    bot.add_cog(MainVerify(bot))