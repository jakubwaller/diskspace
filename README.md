# diskspace

This tiny Python script checks available disk space on a Raspberry Pi and sends a Telegram message if it is low.

## Deployment

### Setup Environment

- Install packages listed in requirements.txt.
- Create a Telegram Bot using the BotFather
- Create a chat where the bot will send the messages.
- Create a file `env.json` in the `diskspace` directory with the chat_id, the bot_token, and the available_gb_alert.
```json
{
  "chat_id": "<REPLACE WITH DEVELOPER CHAT ID>",
  "bot_token": "<REPLACE WITH BOT TOKEN>",
  "available_gb_alert": "5"
}
```

### Add a line to crontab

E.g. something like this:

```bash
4-59/5 * * * * cd ~/diskspace && flock -n /tmp/diskspace.lockfile python3 diskspace.py
```

This starts at the 4th minute and runs every 5 minutes. 
It also uses flock to prevent accidental parallel runs.

If the disk space is low, the bot sends one message every hour (not every 5 minutes).