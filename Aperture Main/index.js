// Load up the discord.js library
const Discord = require("discord.js");

/*
 DISCORD.JS VERSION 12 CODE
*/


const client = new Discord.Client();

 
const config = require("./config.json");


client.on("ready", () => {
  console.log(`Bot has started, with ${client.users.cache.size} users, in ${client.channels.cache.size} channels of ${client.guilds.cache.size} guilds.`);
  client.user.setActivity(`+ | ${client.guilds.cache.size} Servers`);
});

client.on("guildCreate", guild => {
  console.log(`New guild joined: ${guild.name} (id: ${guild.id}). This guild has ${guild.memberCount} members! :D`);
  client.user.setActivity(`+ | ${client.guilds.cache.size} Servers`);
});

client.on("guildDelete", guild => {
  console.log(`I have been removed from: ${guild.name} (id: ${guild.id}) D:`);
  client.user.setActivity(`+ | ${client.guilds.cache.size} Servers`);
});


client.on("message", async message => {
   
  
  if(!message.content.startsWith(config.prefix)) return;
  
  const args = message.content.slice(config.prefix.length).trim().split(/ +/g);
  const command = args.shift().toLowerCase();
  
  
  if(command === "ping") {
    if(message.author.bot) {
      return message.reply("**ERROR**: Your too nub to do that command!");
      return;
    }
    const m = await message.channel.send("Ping?");
    m.edit(`Pong! Latency is ${m.createdTimestamp - message.createdTimestamp}ms. API Latency is ${Math.round(client.ws.ping)}ms`);
  }
  
  if(command === "say") {
    if(message.author.bot) {
      return message.reply("**ERROR**: Your too nub to do that command!");
      return;
    }
    const sayMessage = args.join(" ");
    message.delete().catch(O_o=>{}); 
    message.channel.send(sayMessage);
  }
  
  if(command === "kick") {
    if(message.author.bot) {
      return message.reply("**ERROR**: Your too nub to do that command!");
      return;
    }
    if(!message.member.roles.cache.some(r=>["Admin", "Mod"].includes(r.name)))
      return message.reply("**ERROR**: Sorry, you don't have permissions to use this!");
    
    let member = message.mentions.members.first() || message.guild.members.get(args[0]);
    if(!member)
      return message.reply("**ERROR**: Please mention a valid member of this server");
    if(!member.kickable) 
      return message.reply("**ERROR**: I cannot kick this user! Do they have a higher role? Do I have kick permissions?");
    
    let reason = args.slice(1).join(' ');
    if(!reason) reason = "**SERVER**: No reason provided";
    
    await member.kick(reason)
      .catch(error => message.reply(`**ERROR**: Sorry ${message.author} I couldn't kick because of : ${error}`));
    message.reply(`${member.user.tag} has been kicked by ${message.author.tag} because: ${reason}`);

  }
  
  if(command === "ban") {
    if(message.author.bot) {
      return message.reply("**ERROR**: Your too nub to do that command!");
      return;
    }
    if(!message.member.roles.cache.some(r=>["Admin"].includes(r.name)))
      return message.reply("**ERROR**: Sorry, you don't have permissions to use this!");
    
    let member = message.mentions.members.first();
    if(!member)
      return message.reply("**ERROR**: Please mention a valid member of this server");
    if(!member.bannable) 
      return message.reply("**ERROR**: I cannot ban this user! Do they have a higher role? Do I have ban permissions?");

    let reason = args.slice(1).join(' ');
    if(!reason) reason = "**SERVER**: No reason provided";
    
    await member.ban(reason)
      .catch(error => message.reply(`**ERROR**: Sorry ${message.author} I couldn't ban because of : ${error}`));
    message.reply(`${member.user.tag} has been banned by ${message.author.tag} because: ${reason}`);
  }
  
  if(command === "purge") {

    if(message.author.bot) {
      return message.reply("**ERROR**: Your too nub to do that command!");
      return;
    }
    if(!message.member.roles.cache.some(r=>["Admin", "Mod"].includes(r.name)))
       return message.reply("**ERROR**: Sorry, you don't have permissions to use this!");
    const deleteCount = parseInt(args[0], 10);
    
    if(!deleteCount || deleteCount < 2 || deleteCount > 100)
      return message.reply("Please provide a number between 2 and 100 for the number of messages to delete");
    
    const fetched = await message.channel.messages.fetch({limit: deleteCount});
    message.reply(`You Have Deleted Messages! This message will stay here if you want you delete it.`);
    message.channel.bulkDelete(fetched)
      .catch(error => message.reply(`Couldn't delete messages because of: ${error}`));
  }
});

client.login(config.token);