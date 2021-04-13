<?php
if(isset($_POST['url_bbb_svg'])) {
    $command = escapeshellcmd("python ../main.py ". $_POST['url_bbb_svg']);
    $output = shell_exec($command);
    echo $output;
}