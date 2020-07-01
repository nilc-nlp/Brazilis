<?php
include('tmp.php');

if($_POST){
	$tmp_file = write_tmp_file($_POST['operation'], $_POST['sentence']);
	exec("tokenizer/webtok < ".$tmp_file. " > ".$tmp_file."0");
	#$corrected_sentence = exec("python toolkit.py ".$tmp_file."0");
	exec("python toolkit.py ".$tmp_file."0 > ".$tmp_file."1");

	$file_handle = fopen($tmp_file."1", "r");
	$corrected_sentence = '';
	while (!feof($file_handle)) {
	  $line = fgets($file_handle);
	  $corrected_sentence = $corrected_sentence.$line;
	  }
	fclose($file_handle);
	exec("php call_palavras_flat_nathan.php ".$tmp_file."1"." > ".$tmp_file."2");
	$file_handle = fopen($tmp_file."2", "r");
	$palavras_output = '';
	while (!feof($file_handle)) {
	  $line = fgets($file_handle);
	  $palavras_output = $palavras_output.$line;
	  }
	fclose($file_handle);
	$response['corrected_sentence'] = $corrected_sentence;
	$response['output_palavras'] = $palavras_output;

	exec("rm ".$tmp_file.' '.$tmp_file.'0'.' '.$tmp_file.'1'.' '.$tmp_file.'2');
	echo(json_encode($response));

}	
else echo('Not posting!');
exit();
?>
