from .rules import Rules

async def setup(bot):
    await bot.add_cog(Rules(bot))
