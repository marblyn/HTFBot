import discord
from redbot.core import commands

HTF_SERVER = {
    1033567360692523008  # HTF server exclusive command
}

RULES = {
    "a": {
        1: {
            "text": "Disrespect towards other server members",
            "subtext": "We want this server to be enjoyable for everyone. Constructive criticism isn't disrespectful. Please respect the members of the server."
        },
        2: {
            "text": "Excessively using swear words",
            "subtext": "Swearing is 100% allowed. Please don't excessively swear in the chat."
        },
        3: {
            "text": "Use of languages other than English",
            "subtext": "This is to make it easy to moderate messages. We ask you to use English on this server."
        },
        4: {
            "text": "Excessively discussing about banned or problematic people",
            "subtext": "We ask you to not bring up any problematic people, as it causes issues.\n- Discussion about controversial users are not allowed anywhere on the server. Move it to Direct Messages."
        },
        5: {
            "text": "Posting things outside of specific channels",
            "subtext": (
                "Post memes in <#1165650627901272064>, and post art and other things you made in <#1165650489715724288>."
                "\n- This also includes roleplaying outside of <#1350629370322096209> or <#1165650655122309251>."
            )          
        },
        6: {
            "text": "Having an unpingable username/nickname",
            "subtext": "“Fancy” text in your name isn't allowed, we will ask you to change it, or change your nickname so it's easier for users to ping you."
        },
        7: {
            "text": "Voice Chat Misusage",
            "subtext": "Screaming, playing loud music, and screen sharing inappropriate content\n- Do not troll, or constantly skip audio in the Music VC."
        },
        8: {
            "text": "Asking for roles that are not available in <id:browse>",
            "subtext": "We will never release any staff applications. Moderation is handpicked by Senior Administrators."
        },
        9: {
            "text": "Misuse of the ping function",
            "subtext": "Do not mass ping users in the server.\n- Do not ping the HTF crew or Vixa Games without a proper reason. (“Where’s HTF?”)"
        },
        10: {
            "text": "Having member(s) of the staff team blocked",
            "subtext": "If a staff member is being a problem to you or anyone else in the server, or the fandom itself, please DM a Senior Administrator, and we will look into it.\n- We have this rule in place because we need to DM you for important things, like if you have received a warning, etc."
        },
        11: {
            "text": "Minimodding",
            "subtext": "If a user is breaking the rules of the server, ping an online staff member. **More info is in the rules doc.**"
        },
        12: {
            "text": "Posting sensitive attachments without a warning",
            "subtext": "Attachments that are loud, flashing, etc.\n- Please apply a spoiler to the attachment instead, with a warning shown."
        },
        13: {
            "text": "Erotic Roleplaying, inside or outside the #roleplay channel",
            "subtext": "Do that in Direct Messages __with the user’s permission__, not in the server."
        },
        14: {
            "text": "Bypassing AutoMod words",
            "subtext": "We have a set of blacklisted users from the server and we do not want them brought up."
        },
        15: {
            "text": "Venting in the public chat",
            "subtext": "Please don't vent in the public chat. Keep things like this in Direct Messages as it can lead to topics not allowed for the server."
        },
        16: {
            "text": "Spoilers outside of the #spoilers channel",
            "subtext": "For access to the spoilers channel you must select the `@Spoilers` role via <id:customization>"
        },
        17: {
            "text": "Posting AI content",
            "subtext": "Posting AI (mostly images) is not allowed."
        },
        18: {
            "text": "Going off-topic in <#1165649280506269777> or <#1165649355370401832>",
            "subtext": "Please use <#1165649280506269777> for talking about HTF and <#1165649355370401832> for talking about other MondoMedia content (including HTF).\n- This also includes forcibly changing the subject in the other channels."
        }
    },
    "b": {
        1: {
            "text": "Spamming the chat",
            "subtext": "Using bots outside of <#1346712978115792897> are fine (some commands do not work outside of that channel), don't go too overboard with them.\n- Reacting to one or more messages with a bunch of reactions (or putting a reaction on a bunch of messages) also falls under this.\n- Starting message chains or participating in one can cause you to be muted.\n-Fear Mongering/chainmail (messages that are meant to deceive/scare people “You will get ddosed if you accept this person's friend request!”) **will** fall under this rule."
        },
        2: {
            "text": "Not listening to Server Staff",
            "subtext": "Listen to what the server staff tells you to do.\n- Do not abuse loopholes."
        },
        3: {
            "text": "Tampering with the bots or abusing them",
            "subtext": "If there's a bug with a bot, please report them to a staff member instead!"
        },
        4: {
            "text": "Hate speech",
            "subtext": "Do not use the ableist, racist, and homophobic slurs.\n  - Usage of these slurs, even being part of these, are also not allowed.\n   - You will be given a one week timeout by AutoMod if you use these slurs.\n- This also includes discussion about HTF Thin Ice Level 19 (and even posting an image of it)."
        },
        5: {
            "text": "Unsanitary jokes towards people",
            "subtext": "Don’t use these towards people. Since Mondo Media’s shows have unsanitary jokes, we’re gonna allow it on this server but not excessively."
        },
        6: {
            "text": "Serious politician discussion/argument",
            "subtext": "Please keep conversations like these outside of the server."
        },
        7: {
            "text": "Sending offensive memes",
            "subtext": "You will be removed from the <#1165650627901272064> channel for this. Otherwise, it could lead to a ban too."
        },
        8: {
            "text": "Starting any sort of drama in the chat",
            "subtext": "We do not want **any** drama on this server. If you join the server with the purpose of bringing up drama (rather than letting a staff member know first), it will just lead you to a Section C offense (a ban).\n- Ragebaiting other members of the server also applies to this."
        },
        9: {
            "text": "Jokes about mental illnesses",
            "subtext": "The rule speaks for itself."
        },
        10: {
            "text": "Questionable roleplays (as an adult) without confirming anyone’s age, or otherwise, roleplaying around minors.",
            "subtext": "We do not want any incidents with adults roleplaying without not confirming anyone’s age.\n- This includes questionable roleplaying around minors (which could even lead to a ban depending on the situation)."
        }
    },
    "c": {
        1: {
            "text": "Breaking Discord’s Terms of Service or Community Guidelines",
            "subtext": (
                "If you are under the age of 13, you will be banned. You may rejoin when you're 13.\n"
                "  - **If you lie about your age to stay in the server until you turn 13, you will be permanently banned without an appeal. "
                "In order to comply with the law and Discord’s ToS, we have to strictly enforce this rule.**\n"
                "- If you raid the server or organize one, you will be banned along with your Discord account reported.\n"
                "- If you have been known to raid other HTF servers, you will be banned from this server.\n\n"
                "**__Please read Discord's Terms of Service and Community Guidelines:__**\n"
                "https://discord.com/terms\n"
                "https://discord.com/guidelines"
            )
        },
        2: {
            "text": "Incitement or Discussion of illegal activity",
            "subtext": (
                "Which includes:\n"
                "  - Doxxing\n"
                "  - Pirated Content\n"
                "  - Real-life threats\n"
                "  - ETC"
            )
        },
        3: {
            "text": "Posting inappropriate content",
            "subtext": (
                "Not Safe For Work (NSFW) isn't allowed and will never be tolerated ever.\n"
                "  - Posting NSFW art is also not tolerated.\n"
                "- Drawn gore is okay (as Happy Tree Friends is mainly gruesome), **real life gore (including rat abuse videos) leads to a ban.**\n"
                "- This rule also complies to any form of fetish content."
            )
        },
        4: {
            "text": "Discrimination",
            "subtext": "Inappropriate discussions discriminating against anyone based on their race, sexuality, religion, gender, etc, is not tolerated at all.\n- Deadnaming and misgendering others will also result in a ban."
        },
        5: {
            "text": "Impersonation",
            "subtext": "If you are pretending to be someone else, you will be asked to change your appearance. Otherwise, you will be banned.\n- Impersonating staff will lead to an immediate ban and it cannot be appealed."
        },
        6: {
            "text": "Joining the server to troll",
            "subtext": "Just don't. Find something better to do."
        },
        7: {
            "text": "Attempting to circumvent a moderation action",
            "subtext": "This server has autoroles, if you get caught evading a mute your mute will stay permanent and unappealable.\n- Asking a staff member to revoke moderation action also counts\n- We will find out if you attempt to spy on the server."
        },
        8: {
            "text": "Sending malicious attachments/links",
            "subtext": "If your Discord account was hacked, send in an appeal and we will unban you and give you directions on how to secure your account."
        },
        9: {
            "text": "Sending any official paid Mondo products in the chat",
            "subtext": "Continuation to Rule C2. We’re going to strictly enforce this rule and sending attachments, like the Still Alive package or The Crackpet Show will result in a permanent ban."
        },
        10: {
            "text": "Attempting to start any argument with staff after receiving infractions",
            "subtext": "Use common sense. Either take the moderation action or appeal. Do not argue with staff about it."
        },
        11: {
            "text": "Unsolicited Direct Messages",
            "subtext": "Do not DM advertise to users of the server, unless they have asked. There is an ads channel, use it!\n- Do not message the Vixa Games staff team any complaints about the server, use the feedback form instead, and we will do our best to improve the server."
        },
        12: {
            "text": "Leaking Member-Only Content",
            "subtext": "Leaking any previews of MondoMedia’s membership-only features (such as HTF Episode Previews) in the server isn't allowed.\n- Sending MondoMedia’s community posts will only result in a warning with your message being deleted."
        }
    }
}

RULES_DOC_LINK = "https://docs.google.com/document/d/10KYIGh5H1lOHLQkVHPEQb8Z2zHSQcvNVpfQq7GtxNMg/edit"

class RulesCog(commands.Cog):
    """Display the rules for the HTF server."""

    def __init__(self, bot):
        self.bot = bot
        self.custom_prefix = "r."

    async def cog_check(self, ctx):
        return ctx.guild and ctx.guild.id in HTF_SERVER

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or not message.guild:
            return
        if message.guild.id not in HTF_SERVER:
            return

        if not message.content.lower().startswith(self.custom_prefix):
            return

        cmd = message.content[len(self.custom_prefix):].strip()
        if not cmd:
            return

        # Keyword search
        if cmd.lower().startswith("search "):
            keyword = cmd[7:].strip().lower()
            if not keyword:
                return await message.channel.send("❌ Please include a keyword to search.")

            results = []
            for section, rules in RULES.items():
                for num, data in rules.items():
                    combined = (data["text"] + " " + data["subtext"]).lower()
                    if keyword in combined:
                        results.append(f"**Rule {section.upper()}{num}**: {data['text']}")

            if not results:
                return await message.channel.send("❌ No matching rules found.")

            if len(results) > 10:
                results = results[:10]
                results.append("*...and more matches were found.*")

            embed = discord.Embed(
                title=f"🔍 Rules matching: {keyword}",
                description="\n".join(results),
                color=0xc2e0b4
            )
            embed.set_footer(text="📄 For full context, view the rule directly or read the rules document.")
            return await message.channel.send(embed=embed)

        # Rule lookup like r.a1
        if len(cmd) < 2 or not cmd[0] in RULES or not cmd[1:].isdigit():
            return

        section = cmd[0]
        number = int(cmd[1:])

        rule_obj = RULES.get(section, {}).get(number)
        if not rule_obj:
            return

        embed = discord.Embed(
            title=f"Rule {section.upper()}{number}: {rule_obj['text']}",
            description=f"- {rule_obj['subtext']}",
            color=0xc2e0b4
        )
        embed.set_footer(text="📄 Please read the full rules document.")
        embed.url = RULES_DOC_LINK

        await message.channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(RulesCog(bot))
