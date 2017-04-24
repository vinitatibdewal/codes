<?php
$parameters=$_POST["num1"];
$path="/var/www/html/a.out $parameters";
exec($path,$output);
for($i=0;$i<count($output);$i++)
	echo $output[$i];
?>
