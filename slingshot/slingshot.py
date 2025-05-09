import discord
from redbot.core import commands
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

class Screenshot(commands.Cog):
    """A cog for displaying the Deadeye Derby leaderboard."""

    def __init__(self, bot):
        self.bot = bot
        self.width = 540
        self.height = 937
        self.url = "https://htfslingshot.endersfund.com/htf_slingshot/web/sidebar/weekly"

    async def take_screenshot(self, path: str):
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--window-size={self.width},{self.height}")        
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        driver.execute_script("document.body.style.zoom='175%'")  # Zoom in by 175%
        driver.set_window_size(self.width, self.height)  # Resize the page
        driver.execute_script("document.body.style.overflow = 'hidden';")  # Hide scrollbar
        driver.save_screenshot(path)
        driver.quit()

    @commands.command()
    async def slingshot(self, ctx):
        """Display the current Deadeye Derby leaderboard."""
        filename = "screenshot.png"
        await self.take_screenshot(filename)
        await ctx.send(file=discord.File(filename))
        os.remove(filename)

from redbot.core.bot import Red

def setup(bot: Red):  # Remove async from setup
    bot.add_cog(Screenshot(bot))
