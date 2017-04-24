<?php
$arr1=$_POST["num1"];
$arr2=split(',',$arr1);
$arr3=$_POST["num2"];
$arr4=split(',',$arr3);

for($i=0;$i<count($arr2);$i++)
	$arr2[$i]=int($arr2[$i]);

for($i=0;$i<count($arr4);$i++)
	$arr4[$i]=int($arr4[$i]);

function binary($search,array $arr2)
{
	$low=0;
	$high=count($arr2)-1;
	while($low<=$high)
	{
		$mid=$low+$high/2;
		$mid=int($mid);
			if($arr2[$mid]==$search)
			{
			echo "Element found ";
			echo $search;
			echo " At position ";
			echo $i;
			break;
			}
			else if($arr2[$mid]<$search)
				$low=$mid+1;
			else if($arr2[$mid]>$search)
				$high=$mid-1;
			else
				echo "Number not found";
	}
	if($low>$high)
		echo "Number not found";
}
for($i=0;i<count($arr4);$i++)
	binary($arr4[$i],$arr2);
?>
