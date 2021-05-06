<?php

function bubble_sort(&$mang)
{
	$phan_tu = sizeof($mang);
	for($i = 0; $i < $phan_tu - 1; $i++)
	{
		for ($j = $phan_tu - 1; $j > $i - 1; $j--)
		{
			if ($mang[$j] < $mang[$j-1])
			{
				$tmp = $mang[$j];
				$mang[$j] = $mang[$j-1];
				$mang[$j-1] = $tmp;
			}
		}
	}
}

$mang = array(3, 5, 6, 1, 2, 0, 8, 9, 4, 7);
bubble_sort($mang);
for ($i = 0; $i < sizeof($mang); $i++)
	echo $mang[$i]." ";

?>
