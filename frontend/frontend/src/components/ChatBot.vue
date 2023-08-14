<script>
import axios from 'axios';

export default {
    name: "ChatBot",
    methods: {
        getBotResponse(message) {
            const path = "http://localhost:5000/bot";
            axios.post(path, message)
            .then((res) => {
                var botHTML = '<p class="botText"><span> ' + res.data + ' </span></p>';
                document.getElementById("chatbox").innerHTML = document.getElementById("chatbox").innerHTML + botHTML;
                document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
            })
            .catch((err) =>{
                console.error(err);
            })
        },
        submitted() {
            var rawText = document.getElementById("textInput").value;
            var userHTML = '<p class="userText"><span> ' + rawText + ' </span></p>';
            document.getElementById("textInput").value = "";
            document.getElementById("chatbox").innerHTML = document.getElementById("chatbox").innerHTML + userHTML;
            document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
            this.getBotResponse({ message: rawText })
        }   
    }
}
</script>

<template> 
    <div>
        <h1> Customer Service ChatBot </h1>
        <div>
            <div id="chatbox">
                <p class="botText"> <span> How can I help you? </span></p>
            </div>
            <div id="userInput">
                <input id="textInput" type="text" name="msg" placeholder="Type here" v-on:keyup.enter="submitted">
                <input id="buttonInput" type="submit" @click="submitted">
            </div>
        </div>
    </div>
</template>


<style>
body {
    font-family: Garamond;
    background-color: black;
}

h1 {
    color: white;
    margin-bottom: 0;
    margin-top: 0;
    text-align: center;
    font-size: 40px;
}

h3 {
    color: black;
    font-size: 20px;
    margin-top: 3px;
    text-align: center;
}

#chatbox {
    background-color: black;
    margin-left: auto;
    margin-right: auto;
    width: 60%;
    margin-top: 60px;
}

#userInput {
    margin-left: auto;
    margin-right: auto;
    width: 40%;
    margin-top: 60px;
}

#textInput {
    width: 87%;
    border: none;
    border-bottom: 3px solid #009688;
    font-family: monospace;
    font-size: 17px;
}

#buttonInput {
    padding: 3px;
    font-family: monospace;
    font-size: 17px;
}

.userText {
    color: white;
    font-family: monospace;
    font-size: 17px;
    text-align: right;
    line-height: 30px;
}

.userText span {
    background-color: #009688;
    padding: 10px;
    border-radius: 2px;
}

.botText {
    color: white;
    font-family: monospace;
    font-size: 17px;
    text-align: left;
    line-height: 30px;
}

.botText span {
    background-color: #3353A0;
    padding: 10px;
    border-radius: 2px;
}

#tidbit {
    position:absolute;
    bottom:0;
    right:0;
    width: 300px;
}
</style>