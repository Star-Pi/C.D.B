import discord
from discord.ext import commands
import os
import random

# --- Constants ---
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')  # Get the token from an environment variable
FACTS = [
    "The Earth's average temperature has risen by over 1 degree Celsius since the late 1800s.",
    "Deforestation contributes to climate change by releasing stored carbon and reducing the planet's ability to absorb CO2.",
    "Renewable energy sources like solar and wind power are becoming increasingly cost-competitive with fossil fuels.",
    "Reducing meat consumption can significantly lower your carbon footprint, as livestock farming has a high environmental impact.",
    "Climate change is already causing more frequent and intense extreme weather events like hurricanes and heatwaves.",
    "The Paris Agreement aims to limit global warming to well below 2 degrees Celsius above pre-industrial levels.",
    "Planting trees helps absorb carbon dioxide from the atmosphere, mitigating climate change.",
    "Electric vehicles produce zero tailpipe emissions, reducing air pollution and greenhouse gas emissions.",
    "Investing in energy efficiency can save money and reduce your carbon footprint at the same time.",
    "Ocean acidification, caused by increased CO2 absorption, threatens marine ecosystems and shellfish."
]
# --- Intents and Bot Setup ---
intents = discord.Intents.default()
intents.message_content = True  # Required for bot to read message content
intents.guilds = True # Required for bot to access server info
bot = commands.Bot(command_prefix='!', intents=intents)

# --- Events ---
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('Ready to educate on climate change!')

# --- Commands ---

@bot.command(name='climatehelp', help='Provides a general overview of climate change solutions.')
async def climate_help(ctx):
    embed = discord.Embed(title="Climate Change Solutions", color=0x2ecc71)
    embed.add_field(name="Reduce Your Carbon Footprint", value="- Use public transport, cycle, or walk more. \n- Eat less meat and dairy. \n- Reduce energy consumption at home. \n- Choose sustainable products.", inline=False)
    embed.add_field(name="Advocate for Change", value="- Vote for climate-conscious leaders. \n- Support organizations working on climate solutions. \n- Talk to friends and family about climate change.", inline=False)
    embed.add_field(name="Support Sustainable Businesses", value="- Buy from companies committed to reducing their emissions. \n- Invest in renewable energy companies.", inline=False)
    embed.set_footer(text="Let's work together to protect our planet! 💚")
    await ctx.send(embed=embed)

@bot.command(name='fact', help='Provides a random fact about climate change.')
async def fact(ctx):
    random_fact = random.choice(FACTS)
    embed = discord.Embed(title="Climate Change Fact", description=random_fact, color=0x3498db)
    await ctx.send(embed=embed)

@bot.command(name='solutions', help='Lists some key solutions to climate change.')
async def solutions(ctx):
    embed = discord.Embed(title="Key Solutions to Climate Change", color=0x9b59b6)
    embed.add_field(name="Renewable Energy", value="Transition to solar, wind, and other renewable sources.", inline=False)
    embed.add_field(name="Energy Efficiency", value="Improve building insulation, use efficient appliances, and reduce overall energy consumption.", inline=False)
    embed.add_field(name="Sustainable Transportation", value="Promote walking, cycling, public transport, and electric vehicles.", inline=False)
    embed.add_field(name="Reforestation", value="Plant trees to absorb CO2 from the atmosphere.", inline=False)
    embed.add_field(name="Policy and Advocacy", value="Support climate-friendly policies and invest in green technologies.", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='resources', help='Provides links to useful resources.')
async def resources(ctx):
    embed = discord.Embed(title="Climate Change Resources", color=0xe74c3c)
    embed.add_field(name="UN Climate Change", value="[Link to UN Climate Change](Replace with actual link)", inline=False)
    embed.add_field(name="EPA - Climate Change", value="[Link to EPA Climate Change](Replace with actual link)", inline=False)
    embed.add_field(name="IPCC Reports", value="[Link to IPCC Reports](Replace with actual link)", inline=False)
    await ctx.send(embed=embed)

# --- Run the Bot ---
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Error: Please set the DISCORD_BOT_TOKEN environment variable.")
