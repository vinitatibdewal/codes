<?php
$num1=(int)$_POST["num1"];
$num2=(int)$_POST["num2"];

function binary($n)
{
$count=3;
$num=$n;
$bin=array(0,0,0,0);
if($num<0)
	$num=16+$n;
while($num!=0)
{
	$bin[$count]=$num%2;
	$num=$num/2;
	$count=$count-1;	
}
return $bin;
}

function add($a,$b)
{
$carry=0;
for($i=8;$i>=0;$i--)
{
	$temp=$a[$i]+$b[$i]+$carry;
	$a[$i]=$temp%2;
	$carry=$temp/2;
}
return $a;
}

function right($c)
{
for($i=8;$i>=1;$i--)
	$c[$i]=$c[$i-1];
return $c;
}

function dec(array $d)
{
$t=1;
$ans=0;
for($i=7;$i>=0;$i--,$t=$t*2)
{
	$ans=$ans+($d[$i]*$t);
	if($ans>64)
	{
		$ans=-(265-$ans);
	}
}
return $ans;
}

function multiply($n1,$n2)
{
$m=binary($n1);
$m1=binary(-$n1);
$r=binary($n2);

$A=array(0,0,0,0,0,0,0,0,0);
$S=array(0,0,0,0,0,0,0,0,0);
$P=array(0,0,0,0,0,0,0,0,0);

for($i=0;$i<9;$i++)
{
	$A[$i]=$m[$i];
	$S[$i]=$m1[$i];
	$P[$i+4]=$r[$i];
}

for($i=0;$i<4;$i++)
{
	if($P[7]==0 && $P[8]==0);
		//do nothing
	else if($P[7]==0 && $P[8]==1)
		$P=add($P,$A);
	else if($P[7]==1 && $P[8]==0)
		$P=add($P,$S);
	else if($P[7]==1 && $P[8]==1);
		//do nothing
	$P=right($P);
}
echo "binary output: ";
for($i=0;$i<9;$i++)
	echo $P[$i];
echo "\n";
echo "decimal output: ";
$ans=dec($P);
echo $ans;
}
multiply($num1,$num2)
?>
