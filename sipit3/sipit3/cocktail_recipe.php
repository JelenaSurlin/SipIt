<?php 
    header("Content-type: application/json");
    $command = escapeshellcmd('python3 cocktail_recipe.py ' .   base64_encode($_POST["postVar"]) );
    $commanderr = $command . " "  . " 2>&1";
    $output = shell_exec($command .  ' 2>&1');
    $myfile = fopen("test.txt", "w") or die("Unable to open file!");
		fwrite ( $myfile, $output);
    echo $output; 
?>