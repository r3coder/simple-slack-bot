
from slackBot import slackBot

import time

# DEMO

slackBot.SetToken("your-oauth-token")

slackBot.SendStartSignal()

time.sleep(6)
slackBot.SendMessage("I'm sending one message")
slackBot.SendMessage("And second hehehehe")

slackBot.DisableLimit()

time.sleep(3)
slackBot.SendProgress(0.15)

slackBot.SendMessage("Let's go on...")
slackBot.SendWarning("I think I can handle on...")
slackBot.SendError("Error! \n I have an error! \n\n Please SOMEBODY HELP!")


slackBot.SendMessage("After some stuffs.. Finally...")
slackBot.SendEndSignal()