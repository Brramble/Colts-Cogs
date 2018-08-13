import discord
from discord.ext import commands
from redbot.core import checks
from redbot.core import Config
import aiohttp

    payload = { "user_id": userid }
    headers = {'Authorization': 'JJFoWzWeBJVl802f5FR2Z9L9qMSCiPE6tcmvJIs_fjg'}
    url = "https://bans.discord.id/api/check.php"
    isbanned = False
    async with aiohttp.ClientSession() as session:
        resp = await session.post(url, data=payload)
        final = await resp.text()
        resp.close()
        if '"banned": "0"' in final.lower():
            banned = False
        elif '"banned": "1"' in final.lower():
            banned = True
            data= json.loads(final)
            case_id =  data["case_id"] 
            reason = data["reason"]
            proof = data["proof"]