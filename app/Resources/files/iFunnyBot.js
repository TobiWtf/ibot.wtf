const WebSocket = require('ws')

var AppId = "AFB3A55B-8275-4C1E-AEA8-309842798187"; // This is the SendBird app ID
var BotId = ""; // This is your iFunny account ID
var MessengerToken = ""; // This is your messenger token for establishing connection
var Prefix = "!";  // This is your bots prefix
var CommandsCaseSensitive = false; // This is a value for determining case sensitivity
                                   // of commands
var url = "wss://ws-us-1.sendbird.com/?p=Android&pv=22&sv=3.0.55&ai=" // This is the base url
var querys = AppId + "&user_id=" + BotId + "&access_token=" + MessengerToken; // this is the queried url
const connection = new WebSocket(url + querys); // this creates a new websocket connection with the api

connection.onopen = () => {
    console.log('Bot is online'); // This listens for the open enviroment and logs that its online to terminal
}

connection.onerror = (error) => {
    console.log('WebSocket error: ' + error); // This listens for Errors in the websocket and logs them
}

connection.onmessage = (e) => {
    var Frame = e.data;
    var FrameType = e.data.substr(0, 4);
    if (Parser[FrameType] != undefined) {
        const parse = new Parser[FrameType](Frame);
    }
}

var Parser = {"MESG": MESG,};

function MESG(Frame) {
    const FrameObject = new MesgParse(Frame);
    return FrameObject;
}

class Channel {
    constructor(FrameData) {
        this.id = FrameData["channel_id"];
        this.type = FrameData["channel_type"];
        this.url = FrameData["channel_url"];
    }

    send(Message) {
      let message_data = {"channel_url": this.url,
                          "message": Message,
                          "type": "MESG",
                          "req_id": "doesnt matter"};
      let to_send = "MESG" + JSON.stringify(message_data) + "\n";
      connection.send(to_send);
    }

}

class Author {
    constructor(FrameData) {
        let raw = FrameData["user"];
        this.id = raw["guest_id"];
        this.pfp = raw["image"];
        this.nick = raw["name"];
        this.metadata = raw["metadata"];
    }
}

class Message {
    constructor(FrameData) {
        this.content = FrameData["message"];
        this.ts = FrameData["ts"];
        this.id = FrameData["msg_id"];
        const authorObj = new Author(FrameData);
        this.author = authorObj;
    }
}

class CtxParse {
    constructor(channel, message) {
        let fullCommand = message.content.substr(1);
        let splitCommand = fullCommand.split(" ");

        if (CommandsCaseSensitive == true) {
            this.primaryCommand = splitCommand[0];
        }

        else {
            this.primaryCommand = splitCommand[0].toLowerCase();
        }

        this.args_list = splitCommand.slice(1);
        this.args = splitCommand[1];
        if (this.args == undefined) {
            this.args = "";
        }
        this.message = message;
        this.channel = channel;
    }
}

class MesgParse {

    constructor(Frame) {
        this.type = Frame.substr(0, 4);
        var unJson = Frame.replace(this.type, "", 1);
        this.data = JSON.parse(unJson);
        const channelObj = new Channel(this.data);
        const messageObj = new Message(this.data);
        this.channel = channelObj;
        this.message = messageObj;
        if (this.message.content.startsWith(Prefix)) {
            const ctx = new CtxParse(this.channel, this.message);
            CommandsRun(ctx);
        }
  }
}

function CommandsRun(ctx) {
    const commands = new Commands();

    if (commands.commands[ctx.primaryCommand] != undefined) {
          console.log(ctx.message.author.nick + ": " + ctx.message.content);
          commands.commands[ctx.primaryCommand](ctx);
    }

    else {
        ctx.channel.send("That is not one of my commands");
    }
}


class Commands {

    constructor() {
        this.commands =  {"help": this.help,
                          "echo": this.echo,
                          "whoami": this.whoami,
                          "clap": this.clap};
    }

    help(ctx) {
        ctx.channel.send("NodeJS Test Success");
    }

    echo(ctx) {
        ctx.channel.send(ctx.args);
    }

    whoami(ctx) {
        ctx.channel.send("You are " + ctx.message.author.nick);
    }

    clap(ctx) {
        var clap = "Clap Emoji";
        var finalClap = clap;

        ctx.args_list.forEach(item => {
            finalClap += item + clap;
        });

        ctx.channel.send(finalClap)

    }


}
