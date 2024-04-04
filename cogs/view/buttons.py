import disnake
from cfg import Verify
man = Verify.man
woman = Verify.woman

class SelectGender(disnake.ui.View):
    def __init__(self, author, member: disnake.Member):
        self.author = author
        self.member = member
        super().__init__(timeout=None)

    @disnake.ui.button(label="🚹", custom_id="man")
    async def man(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        manrole = interaction.guild.get_role(man)
        await self.member.add_roles(manrole)
        embed = disnake.Embed(description="Вы успешно верефицировали, спасибо за работу)")
        await interaction.response.edit_message(embed=embed, view=None)

    @disnake.ui.button(label="🚺", custom_id="woman")
    async def woman(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        woman = interaction.guild.get_role(woman)
        await self.member.add_roles(woman)
        embed = disnake.Embed(description="Вы успешно верефицировали, спасибо за работу)")
        await interaction.response.edit_message(embed=embed, view=None)