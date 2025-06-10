from redbot.core import commands
import discord

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def rules(self, ctx):
        """Send server rules embeds. Only the bot owner can use this."""

        # Embed 1 - Welcome
        embed1 = discord.Embed(
            title="Welcome to the server!",
            description=(
                "Hello! Welcome to the Happy Tree Friends Discord server! "
                "Read the rules and enjoy chatting!\n"
                "Got any questions? Please let the <@&1040291339914457138> know!"
            ),
            color=0xC2B280
        )
        embed1.add_field(
            name="Server Rules",
            value="https://docs.google.com/document/d/10KYIGh5H1lOHLQkVHPEQb8Z2zHSQcvNVpfQq7GtxNMg/edit"
        )

        # Embed 2 - Channel Setup
        embed2 = discord.Embed(
            title="Channel Setup",
            description="This server has specific channels that are available for you to chat in.",
            color=0x7278C9
        )
        embed2.add_field(
            name="Discussion Channels",
            value=(
                "<#1165649280506269777> - The most active channel of the server, the main topic is HTF.\n"
                "<#1165649298445316106> - Just chatting.\n"
                "<#1165649318141775872> - Used incase the other two main chats are too active or has a specific topic being talked about.\n"
                "<#1165649355370401832> - For discussion about other Mondo Media shows. HTF can still be talked about there.\n"
                "<#1165785921690546246> - Main server VC.\n"
                "<#1189036953920876545> - Extra VC incase the other one is full."
            )
        )
        embed2.add_field(
            name="Miscellaneous Channels",
            value=(
                "<#1165650489715724288> - Here to show off your works? This board is for you!\n"
                "<#1165650627901272064> - For memes and what-not.\n"
                "<#1350629370322096209> - For HTF specific roleplaying only.\n"
                "<#1165650655122309251> - Other Tupperbox roleplaying (or just general roleplaying).\n"
                "<#1165657360157651076> - For advertising servers, projects, or other stuff you're working on.\n"
                "<#1165782608479785000> - For playing music with the bot."
            )
        )

        # Embed 3 - Other Info
        embed3 = discord.Embed(
            title="Other Information",
            color=0x8BBF94
        )
        embed3.add_field(
            name="Please follow Discord's Terms of Service!",
            value=(
                "When using this server, please keep in mind of Discord's Terms of Service and Community Guidelines!\n"
                "https://discord.com/terms\n"
                "https://discord.com/guidelines"
            )
        )
        embed3.add_field(
            name="Invite Links",
            value=(
                "https://discord.gg/happytreefriends\n"
                "https://discord.gg/qj67XZvAFc"
            )
        )
        embed3.add_field(
            name="Appeals",
            value=(
                "Have you been given a warning or muted and believe it's unfair? "
                "Friend of yours has been banned? Join the appeals server and create a ticket!\n"
                "https://discord.gg/e6MPyeNJbE"
            )
        )

        for embed in [embed1, embed2, embed3]:
            await ctx.send(embed=embed)
