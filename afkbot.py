const mineflayer = require('mineflayer');

const bot = mineflayer.createBot({
  host: '9.205.27.223',
  port: 12404,
  username: 'AFKBOT',
  version: '1.21.11'
});

bot.once('spawn', () => {
  console.log('✅ AFKBOT has joined the server.');
});

bot.on('message', (message) => {
  // message.toString() returns chat like: <AFKBOT> hello
  console.log('[Server]', message.toString());
});

bot.on('end', () => {
  console.log('Bot disconnected, reconnecting in 5 seconds...');
  setTimeout(() => bot.connect(), 5000);
});

// Console input for chat
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', line => {
  if (bot.player) {
    bot.chat(line);
  } else {
    console.log('Bot not connected yet.');
  }
});
