# i0i Bot

Simple [Telegram bot](https://t.me/i0i_bot) to shortening links via [i0i.wtf](https://i0i.wtf) service (instance of [schort](https://github.com/sqozz/schort)).

## Usage

Use `/start` or `/help` option to display available commands.

## Self-hosting

+ Create `environment` file with your bot token.
```
TOKEN=your_token_here
```
+ Start bot with `python3 main.py`.

### With Docker

+ Build image.
```
# docker build -t samedamci/i0i .
```
+ Run bot in container.
```
# docker run --rm -d -e TOKEN='your_token_here' --name i0i samedamci/i0i
```
