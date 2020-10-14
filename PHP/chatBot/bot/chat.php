<?php
include "Bot.php";
$bot = new Bot;
$questions = [
    "what is php" => "PHP is a server side language",
    "what is your name" => "My name is " . $bot->getName(),
    "what is your gender" => "I am a " . $bot->getGender()
];

if (isset($_GET['msg'])) {
    $msg = strtolower($_GET['msg']);
    $bot->hears($msg, function (Bot $botty) {
        global $msg;
        global $questions;
        if ($msg == 'hi' || $msg == "hello") {
            $botty->reply('Hello there!');
        } elseif ($botty->ask($msg, $questions) == "") {
            $botty->reply("Can't respond to that");
        } else {
            $botty->reply($botty->ask($msg, $questions));
        }
    });
}
