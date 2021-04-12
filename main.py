import os

from discord.ext import commands


def main():
    bot = commands.Bot(command_prefix="exec")
    bot.remove_command("help")

    env = os.getenv("EXECBOT_ENV_TYPE")
    if env.upper() == "MASTER":
        from help import Help
        from status import Status
        from playground import Playground
        from ticker import Ticker

        bot.add_cog(Help(bot))
        bot.add_cog(Status(bot))
        bot.add_cog(Playground(bot))
        bot.add_cog(Ticker(bot))

    else:
        print("Unknown environment ({})".format(env))
        return

    print("Starting with env {}".format(env))
    bot.run(os.getenv("EXECBOT_DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
