const Discord = require('discord.js');
 const client = new Discord.Client();

client.on('ready', () => {
 console.log(`Logged in as ${client.user.tag}!`);
 });

client.on('message', msg => {
 if (msg.content === 'ping') {
 msg.reply('pong');
 }
 });

client.login('MTAxMzQ0NjAyMTEzNDY4ODM0Nw.GdE7Ss.JUB1hGAFeNID8c71rAP9UFv42wP14oLIoWX1sY');